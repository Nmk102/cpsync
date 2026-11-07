"""Вход в ManageBac и сбор всех заданий с оценками со страниц классов."""
from __future__ import annotations

import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


class LoginError(Exception):
    pass


class ManageBacError(Exception):
    pass


def _clean(s: str | None) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def _num(s: str):
    s = _clean(s)
    try:
        v = float(s)
        return int(v) if v.is_integer() else v
    except ValueError:
        return None


# ---------------------------------------------------------------- парсинг HTML

def parse_classes(html: str) -> list[dict]:
    """Список классов из меню (на любой странице /student/...)."""
    soup = BeautifulSoup(html, "html.parser")
    seen, out = set(), []
    for a in soup.select("a[href]"):
        m = re.fullmatch(r"/student/classes/(\d+)", a["href"])
        if not m or m.group(1) in seen:
            continue
        name = _clean(a.get_text())
        if not name:
            continue
        seen.add(m.group(1))
        out.append({"id": m.group(1), "name": name, "short": short_name(name)})
    return out


def short_name(name: str) -> str:
    s = re.sub(r"\s*\((MYP|DP|Grade|Year)[^)]*\)\s*$", "", name, flags=re.I)
    s = re.sub(r"\s*\(Class [A-Z]\)", "", s)
    s = re.sub(r"\s+Class [A-Z]\b", "", s)
    s = re.sub(r"^IB (MYP|DP) ", "", s)
    return _clean(s) or name


def parse_terms(soup: BeautifulSoup) -> dict:
    """Триместры из выпадающего списка: [{id, name, current, year_label}], выбранный."""
    sel = soup.select_one("select#term")
    terms, selected = [], None
    if not sel:
        return {"terms": terms, "selected": None}
    for opt in sel.select("option"):
        group = opt.find_parent("optgroup")
        t = {
            "id": opt.get("value", ""),
            "name": _clean(opt.get_text()).replace(" (current)", ""),
            "current": "(current)" in opt.get_text(),
            "year_label": _clean(group.get("label")) if group else "",
        }
        terms.append(t)
        if opt.has_attr("selected"):
            selected = t["id"]
    return {"terms": terms, "selected": selected}


def _year_for(month: int, year_label: str, today: datetime) -> int:
    years = [int(y) for y in re.findall(r"(20\d\d)", year_label)]
    if len(years) >= 2:
        return years[0] if month >= 8 else years[-1]
    start = today.year if today.month >= 8 else today.year - 1
    return start if month >= 8 else start + 1


def _parse_time(due: str):
    m = re.search(r"(\d{1,2}):(\d{2})\s*([AP]M)", due, re.I)
    if not m:
        return None
    h, mi = int(m.group(1)) % 12, int(m.group(2))
    if m.group(3).upper() == "PM":
        h += 12
    return h, mi


def parse_tasks(html: str, class_info: dict, base_url: str, today: datetime | None = None) -> dict:
    """Задания одной страницы /student/classes/<id>/core_tasks."""
    today = today or datetime.now()
    soup = BeautifulSoup(html, "html.parser")
    terms = parse_terms(soup)
    year_label = next((t["year_label"] for t in terms["terms"] if t["id"] == terms["selected"]), "")
    term_name = next((t["name"] for t in terms["terms"] if t["id"] == terms["selected"]), "")

    tasks = []
    for row in soup.select(".short-assignment"):
        link = row.select_one(".title a[href]")
        if not link:
            continue
        href = link["href"]
        m = re.search(r"/(core_tasks|assignments|tasks)/(\d+)", href)
        task_id = m.group(2) if m else href

        # дата
        date_iso = None
        badge = row.select_one(".date-badge")
        due_el = row.select_one(".due-date")
        due_text = _clean(due_el.get_text()) if due_el else ""
        if badge:
            mon = MONTHS.get(_clean((badge.select_one(".month") or badge).get_text())[:3].lower())
            day = _num((badge.select_one(".day") or badge).get_text())
            if mon and isinstance(day, int):
                y = _year_for(mon, year_label, today)
                hm = _parse_time(due_text) or (0, 0)
                try:
                    date_iso = datetime(y, mon, day, *hm).isoformat(timespec="minutes")
                except ValueError:
                    pass

        labels = [_clean(l.get_text()) for l in row.select(".labels-set > .label")]
        labels = [l for l in labels if l]
        status_el = row.select_one(".badge .badge-label")
        status = _clean(status_el.get_text()) if status_el else ""
        late_info = ""
        if status_el:
            b = status_el.find_parent(class_="badge")
            late_info = b.get("data-bs-title", "") if b else ""

        kind = "other"
        low = [l.lower() for l in labels]
        if "summative" in low:
            kind = "summative"
        elif "formative" in low:
            kind = "formative"

        grade = parse_grade(row)
        comment_el = row.select_one(".assessment-comments")
        comment = ""
        if comment_el:
            for br in comment_el.find_all("br"):
                br.replace_with("\n")
            for p in comment_el.find_all(["p", "li", "div"]):
                p.insert_after("\n")
            comment = re.sub(r"\n\s*\n+", "\n", comment_el.get_text()).strip()
            comment = "\n".join(_clean(x) for x in comment.split("\n") if _clean(x))

        tasks.append({
            "id": task_id,
            "class_id": class_info["id"],
            "subject": class_info.get("short") or class_info.get("name"),
            "class_name": class_info.get("name"),
            "title": _clean(link.get_text()),
            "url": urljoin(base_url, href),
            "date": date_iso,
            "due_text": due_text,
            "labels": labels,
            "kind": kind,
            "status": status,
            "status_hint": late_info,
            "term": term_name,
            "grade": grade,
            "comment": comment,
        })
    return {"tasks": tasks, "terms": terms}


def parse_grade(row) -> dict:
    cell = row.select_one(".assessment-cell")
    if not cell:
        return {"type": "none", "text": ""}

    # названия критериев (A: Knowing and understanding) — в всплывающей подсказке
    names = {}
    pop = cell.select_one("[data-bs-content]")
    if pop:
        inner = BeautifulSoup(pop.get("data-bs-content", ""), "html.parser")
        for item in inner.select(".criteria-item"):
            b = item.select_one(".title b")
            if b:
                t = _clean(b.get_text())
                mm = re.match(r"([A-Z])\s*:\s*(.*)", t)
                if mm:
                    names[mm.group(1)] = mm.group(2)

    criteria = []
    for c in cell.select(".criterion-grade"):
        letter_txt = _clean("".join(t for t in c.find_all(string=True, recursive=False)))
        mm = re.match(r"([A-Z])", letter_txt)
        score = c.select_one(".label-score")
        mx = c.select_one(".label-points")
        if not mm:
            continue
        criteria.append({
            "letter": mm.group(1),
            "name": names.get(mm.group(1), ""),
            "score": _num(score.get_text()) if score else None,
            "max": _num(mx.get_text()) if mx else None,
        })

    points = None
    for c in cell.select(".cell"):
        if "point" in c.get_text().lower() and not c.select(".label-group"):
            grp = c.find_next(class_="label-group")
            if grp:
                s, m = grp.select_one(".label-score"), grp.select_one(".label-points")
                points = {
                    "label": _clean(c.get_text()).rstrip(":"),
                    "score": _num(s.get_text()) if s else None,
                    "max": _num(m.get_text()) if m else None,
                }
            break

    # прочие оценки (буква, процент) — label-score вне критериев и баллов
    other = None
    if not criteria and not points:
        s = cell.select_one(".label-score")
        if s:
            m = cell.select_one(".label-points")
            other = {"score": _clean(s.get_text()), "max": _clean(m.get_text()) if m else ""}

    text = ""
    for sp in cell.select("span.cell, .cell.not-assessed, .cell.submitted"):
        text = _clean(sp.get_text())
        if text:
            break
    if not text and not criteria and not points and not other:
        text = _clean(cell.get_text())

    if criteria or points or other:
        return {"type": "graded", "criteria": criteria, "points": points, "other": other, "text": text}
    return {"type": "none", "text": text}


# ---------------------------------------------------------------- сетевой клиент

class ManageBac:
    def __init__(self, school: str, login: str, password: str):
        self.base = f"https://{school}.managebac.com"
        self.login_name = login
        self.password = password
        self.s = self._new_session()

    def _new_session(self, cookies=None):
        s = requests.Session()
        s.headers.update({"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.9"})
        if cookies is not None:
            s.cookies.update(cookies)
        return s

    def login(self):
        r = self.s.get(self.base + "/login", timeout=30)
        soup = BeautifulSoup(r.text, "html.parser")
        tok = soup.select_one("input[name=authenticity_token]")
        if tok is None:
            if "/login" not in r.url:
                return  # уже вошли
            raise ManageBacError("не нашёл форму входа ManageBac")
        r = self.s.post(self.base + "/sessions", data={
            "authenticity_token": tok.get("value", ""),
            "login": self.login_name,
            "password": self.password,
            "remember_me": "1",
            "commit": "Sign in",
        }, timeout=30)
        if "/login" in r.url or "/sessions" in r.url or not self._is_logged_in(r.text):
            raise LoginError("ManageBac не принял логин или пароль")

    @staticmethod
    def _is_logged_in(html: str) -> bool:
        return "/student/" in html and 'name="password"' not in html

    def get(self, path: str, session=None) -> str:
        s = session or self.s
        for attempt in range(3):
            try:
                r = s.get(self.base + path, timeout=40)
            except requests.RequestException:
                if attempt == 2:
                    raise
                time.sleep(2)
                continue
            if "/login" in r.url:
                if session is not None:
                    raise ManageBacError("сессия ManageBac закончилась")
                self.login()
                continue
            if r.status_code >= 500 and attempt < 2:
                time.sleep(2)
                continue
            r.raise_for_status()
            return r.text
        raise ManageBacError(f"не удалось открыть {path}")

    def fetch_all(self) -> dict:
        """Все классы и все задания текущего учебного года (до текущего триместра включительно)."""
        home = self.get("/student/home")
        classes = parse_classes(home)
        if not classes:
            raise ManageBacError("на странице ManageBac не нашлось ни одного класса")
        student = ""
        m = re.search(r"Welcome,\s*([^!<]+)!", home)
        if m:
            student = _clean(m.group(1))

        cookies = self.s.cookies.copy()

        def first_page(c):
            s = self._new_session(cookies)
            return c, parse_tasks(self.get(f"/student/classes/{c['id']}/core_tasks", s), c, self.base)

        with ThreadPoolExecutor(max_workers=5) as ex:
            firsts = list(ex.map(first_page, classes))

        # предыдущие триместры того же учебного года
        jobs = []
        for c, res in firsts:
            terms, sel = res["terms"]["terms"], res["terms"]["selected"]
            idx = next((i for i, t in enumerate(terms) if t["id"] == sel), None)
            if idx is None:
                continue
            ylabel = terms[idx]["year_label"]
            for t in terms[:idx]:
                if t["year_label"] == ylabel and t["id"]:
                    jobs.append((c, t["id"]))

        def term_page(job):
            c, tid = job
            s = self._new_session(cookies)
            return parse_tasks(self.get(f"/student/classes/{c['id']}/core_tasks?term={tid}", s), c, self.base)

        with ThreadPoolExecutor(max_workers=5) as ex:
            extra = list(ex.map(term_page, jobs))

        tasks, seen = [], set()
        for res in [r for _, r in firsts] + extra:
            for t in res["tasks"]:
                key = (t["class_id"], t["id"])
                if key in seen:
                    continue
                seen.add(key)
                tasks.append(t)

        terms_out = []
        if firsts:
            terms_out = max((r["terms"]["terms"] for _, r in firsts), key=len)
        return {"student": student, "classes": classes, "tasks": tasks, "terms": terms_out}

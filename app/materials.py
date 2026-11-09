"""Материалы предметов из ManageBac: юниты (что проходим), описания заданий, файлы и ссылки."""
from __future__ import annotations

import base64
import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag

ALLOWED = {"p", "br", "ul", "ol", "li", "b", "strong", "i", "em", "u", "a", "table", "thead", "tbody",
           "tr", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "sub", "sup", "hr"}
DROP = {"script", "style", "svg", "img", "iframe", "button", "form", "input", "select", "noscript"}


def _clean(s: str | None) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


# ---------------------------------------------------------------- юниты

def parse_units(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    out, seen = [], set()
    for u in soup.select(".unit-component"):
        a = u.select_one(".h4 a[href], .title-and-badge a[href]")
        if not a:
            continue
        m = re.search(r"/units/(\d+)", a["href"])
        if not m or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        start = u.select_one(".label-start")
        dur = u.select_one(".unit-duration")
        out.append({
            "id": m.group(1),
            "title": _clean(a.get_text()),
            "start": _clean(start.get_text()).replace("Starts", "").strip() if start else "",
            "duration": _clean(dur.get_text()) if dur else "",
            "current": "current" in (u.get("class") or []) or bool(u.select_one(".label-unit-current")),
        })
    return out


UNIT_FIELDS = ["Global Context", "Key Concepts", "Related Concept(s)", "Statement of Inquiry",
               "Inquiry Questions", "Objectives", "ATL Skills", "Content", "Skills", "Subjects"]


def parse_unit_popup(html: str) -> dict:
    """Описание юнита: Statement of Inquiry, вопросы, понятия. Возвращает {поле: текст}."""
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(list(DROP)):
        t.decompose()
    lines = [l.strip() for l in soup.get_text("\n").split("\n")]
    lines = [l for l in lines if l]
    info: dict[str, list[str]] = {}
    cur = None
    for l in lines:
        key = next((f for f in UNIT_FIELDS if l.rstrip(":") == f or l.startswith(f + ":")), None)
        if key:
            cur = key
            rest = l[len(key):].lstrip(":").strip()
            info.setdefault(cur, [])
            if rest:
                info[cur].append(rest)
            continue
        if re.match(r"^(Last updated|Unit Template|Grade:|Start date|Duration)", l):
            cur = None
            continue
        if cur:
            info[cur].append(l)
    # «Factual / Conceptual / Debatable» — метки вопросов
    qs = info.get("Inquiry Questions")
    if qs:
        merged, label = [], ""
        for l in qs:
            if l in ("Factual", "Conceptual", "Debatable"):
                label = l
            else:
                merged.append(f"{label}: {l}" if label else l)
        info["Inquiry Questions"] = merged
    return {k: v for k, v in info.items() if v and k != "Subjects"}


# ---------------------------------------------------------------- страница задания

def asset_id_from_attachment(href: str) -> str | None:
    """/attachments/<base64 gid://managebac/Asset/123?...>--sig → '123'."""
    m = re.match(r"/attachments/([^/?#-]+)", href)
    if not m:
        return None
    raw = m.group(1)
    try:
        txt = base64.urlsafe_b64decode(raw + "=" * (-len(raw) % 4)).decode("utf-8", "ignore")
    except Exception:
        return None
    m2 = re.search(r"Asset/(\d+)", txt)
    return m2.group(1) if m2 else None


def link_kind(url: str, name: str = "") -> str:
    host = urlparse(url).netloc
    low = (name or url).lower()
    if "docs.google.com/document" in url:
        return "gdoc"
    if "docs.google.com/spreadsheets" in url:
        return "gsheet"
    if "docs.google.com/presentation" in url:
        return "gslides"
    if "docs.google.com/forms" in url:
        return "gform"
    if "drive.google.com" in url:
        return "gdrive"
    if "youtube.com" in host or "youtu.be" in host:
        return "video"
    if url.startswith("/attachments/") or "managebac.com/uploads" in url:
        ext = re.search(r"\.([a-z0-9]{2,5})(?:$|\?)", low)
        return (ext.group(1) if ext else "file")
    return "link"


def sanitize(node: Tag, base: str) -> str:
    """Безопасный HTML описания: только простые теги, ссылки наружу."""
    soup = BeautifulSoup(str(node), "html.parser")
    for t in soup(list(DROP)):
        t.decompose()
    for t in list(soup.find_all(True)):
        if t.name not in ALLOWED:
            t.unwrap()
            continue
        href = t.get("href") if t.name == "a" else None
        t.attrs = {}
        if t.name == "a":
            if href and (href.startswith("http") or href.startswith("/attachments/")):
                t["href"] = href if href.startswith("http") else urljoin(base, href)
                t["target"] = "_blank"
                t["rel"] = "noopener"
            else:
                t.unwrap()
    html = str(soup)
    html = re.sub(r"(<p>\s*(<br/?>)?\s*</p>\s*)+", "", html)
    return html.strip()


def parse_task_detail(html: str, base: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    out = {"description_html": "", "description_text": "", "files": [], "links": [], "unit_id": "", "unit_title": ""}

    unit = soup.select_one(".core-task-show a[href*='/units/'], main a[href*='/units/']")
    if unit:
        m = re.search(r"/units/(\d+)", unit["href"])
        out["unit_id"] = m.group(1) if m else ""
        out["unit_title"] = _clean(unit.get_text())

    desc = soup.select_one(".core-task-details .fr-view") or soup.select_one(".core-task-details")
    files, links, seen = [], [], set()

    def add_file(name, url, asset, size=""):
        key = asset or url
        if key in seen:
            return
        seen.add(key)
        ext = re.search(r"\.([A-Za-z0-9]{2,5})$", name or "") or re.search(r"\.([A-Za-z0-9]{2,5})(?:\?|$)", url)
        files.append({"name": name, "url": url, "asset": asset or "", "size": size,
                      "kind": ext.group(1).lower() if ext else "file"})

    if desc:
        for a in desc.select("a[href]"):
            href = a["href"]
            name = a.get("data-name") or _clean(a.get_text())
            if href.startswith("/attachments/"):
                size = a.select_one(".fr-file-size")
                nm = a.select_one(".fr-inner")
                add_file(_clean(nm.get_text()) if nm else name, href, asset_id_from_attachment(href),
                         _clean(size.get_text()) if size else "")
            elif "managebac.com/uploads" in href:
                m = re.search(r"/uploads/asset/file/(\d+)/", href)
                add_file(name, href, m.group(1) if m else None)
            elif href.startswith("http") and href not in seen:
                seen.add(href)
                links.append({"name": name if name and not name.startswith("http") else "", "url": href,
                              "kind": link_kind(href)})
        # убираем подписи файлов из текста описания (они показываются отдельно)
        for a in desc.select("a.fr-file"):
            a.decompose()
        out["description_html"] = sanitize(desc, base)
        txt = desc.get_text("\n")
        out["description_text"] = "\n".join(_clean(l) for l in txt.split("\n") if _clean(l))

    for a in soup.select(".resource.fileslibrary .file a.file-name[href]"):
        href = a["href"]
        m = re.search(r"/uploads/asset/file/(\d+)/", href)
        add_file(_clean(a.get_text()), href, m.group(1) if m else None)
    for a in soup.select(".resource-container a[href^='http']"):
        href = a["href"]
        if "managebac.com" in href or href in seen:
            continue
        seen.add(href)
        links.append({"name": _clean(a.get_text()), "url": href, "kind": link_kind(href)})

    out["files"], out["links"] = files, links
    return out


def parse_files_page(html: str) -> list[dict]:
    """Раздел «Files» класса: файлы и ссылки учителя."""
    soup = BeautifulSoup(html, "html.parser")
    out, seen = [], set()
    for a in soup.select("main a[href]"):
        href = a["href"]
        name = _clean(a.get_text())
        if "managebac.com/uploads" in href:
            m = re.search(r"/uploads/asset/file/(\d+)/([^?]+)", href)
            key = m.group(1) if m else href
            if key in seen or not name:
                continue
            seen.add(key)
            out.append({"name": name, "url": href, "asset": m.group(1) if m else "", "kind": link_kind(href, name)})
        elif re.search(r"(docs|drive)\.google\.com", href) and href not in seen:
            seen.add(href)
            out.append({"name": name or "Google Drive", "url": href, "asset": "", "kind": link_kind(href)})
    return out

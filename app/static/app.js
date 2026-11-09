"use strict";
const $ = (s, el = document) => el.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

const store = {
  get(k, d) { try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
};

const S = {
  data: null,
  view: store.get("view", "list"),
  f: { subject: "", kind: "", graded: store.get("graded", true), q: "", term: "" },
  sort: { key: "date", dir: -1 },
  prevVisit: store.get("lastVisit", ""),
  open: new Set(),
  poll: null,
};

async function api(path, opts = {}) {
  const r = await fetch(path, {
    ...opts,
    headers: { "Content-Type": "application/json", "X-Requested-With": "grades", ...(opts.headers || {}) },
  });
  let body = {};
  try { body = await r.json(); } catch {}
  return { status: r.status, body };
}

// ------------------------------------------------------------ оценки

function level(score, max) {
  if (score == null || !max) return 0;
  const r = score / max;
  return r >= 0.875 ? 4 : r >= 0.625 ? 3 : r >= 0.375 ? 2 : 1;
}
const fmt = (n) => (Number.isInteger(n) ? String(n) : n.toFixed(1).replace(/\.0$/, ""));

function gradePct(g) {
  if (!g || g.type !== "graded") return null;
  const parts = [];
  for (const c of g.criteria || []) if (c.score != null && c.max) parts.push(c.score / c.max);
  if (g.points && g.points.score != null && g.points.max) parts.push(g.points.score / g.points.max);
  if (!parts.length) return null;
  return parts.reduce((a, b) => a + b, 0) / parts.length;
}

function chip(label, score, max, title = "") {
  const lv = level(score, max);
  return `<span class="chip lv${lv}"${title ? ` title="${esc(title)}"` : ""}>${label ? `<span class="l">${esc(label)}</span>` : ""}<b>${esc(fmt(score))}</b>${max ? `<small>/${esc(fmt(max))}</small>` : ""}</span>`;
}

function gradeHtml(t) {
  const g = t.grade || {};
  if (g.type !== "graded") {
    const missing = /not submitted/i.test(g.text || "");
    return `<span class="status${missing ? " missing" : ""}">${esc(missing ? "Не сдано" : g.text || "—")}</span>`;
  }
  const out = [];
  for (const c of g.criteria || []) {
    if (c.score == null) out.push(`<span class="chip" title="${esc(c.name)}"><span class="l">${esc(c.letter)}</span>—</span>`);
    else out.push(chip(c.letter, c.score, c.max, c.name ? `${c.letter}: ${c.name}` : ""));
  }
  if (g.points && g.points.score != null) {
    const pct = g.points.max ? ` · ${Math.round((g.points.score / g.points.max) * 100)}%` : "";
    out.push(chip("", g.points.score, g.points.max, (g.points.label || "Баллы") + pct));
  }
  if (g.other) out.push(`<span class="chip"><b>${esc(g.other.score)}</b>${g.other.max ? `<small>/${esc(g.other.max)}</small>` : ""}</span>`);
  return `<div class="grades">${out.join("")}</div>`;
}

function isNew(t) {
  if (!t.graded_at) return false;
  const at = new Date(t.graded_at).getTime();
  const threeDays = Date.now() - 3 * 864e5;
  return (S.prevVisit && at > new Date(S.prevVisit).getTime()) || at > threeDays;
}

// ------------------------------------------------------------ фильтры

function filtered({ ignoreSubject = false } = {}) {
  const q = S.f.q.trim().toLowerCase();
  return (S.data.tasks || []).filter((t) => {
    if (!ignoreSubject && S.f.subject && t.class_id !== S.f.subject) return false;
    if (S.f.kind && t.kind !== S.f.kind) return false;
    if (S.f.term && (t.term || "").toLowerCase() !== S.f.term.toLowerCase()) return false;
    if (S.f.graded && t.grade?.type !== "graded") return false;
    if (q && !(`${t.title} ${t.subject} ${t.comment}`.toLowerCase().includes(q))) return false;
    return true;
  });
}

function sortTasks(list) {
  const { key, dir } = S.sort;
  const val = (t) => key === "date" ? (t.date || "") : key === "subject" ? t.subject : key === "title" ? t.title.toLowerCase() : (gradePct(t.grade) ?? -1);
  return [...list].sort((a, b) => {
    const x = val(a), y = val(b);
    if (x < y) return -dir;
    if (x > y) return dir;
    return (b.date || "").localeCompare(a.date || "");
  });
}

function fmtDate(iso) {
  if (!iso) return "";
  const d = new Date(iso);
  return d.toLocaleDateString("ru-RU", { day: "numeric", month: "short" }).replace(".", "");
}

// ------------------------------------------------------------ отрисовка

function renderHeader() {
  const d = S.data;
  $("#student").textContent = d.student || "";
  $("#mb-link").href = (d.school_url || "") + "/student";
  if (d.fetched_at) {
    const mins = Math.round((Date.now() - new Date(d.fetched_at).getTime()) / 60000);
    $("#updated").textContent = mins < 1 ? "обновлено только что" : mins < 60 ? `обновлено ${mins} мин назад` :
      "обновлено " + new Date(d.fetched_at).toLocaleString("ru-RU", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
  } else $("#updated").textContent = "";
  $("#sync-dot").hidden = !d.syncing;
  $("#refresh").disabled = !!d.syncing;

  const b = $("#banner");
  if (d.error) {
    b.hidden = false;
    b.textContent = d.error;
  } else b.hidden = true;
}

function renderFilters() {
  const d = S.data;
  const sel = $("#f-subject");
  const used = new Set((d.tasks || []).map((t) => t.class_id));
  const classes = (d.classes || []).filter((c) => used.has(c.id));
  sel.innerHTML = `<option value="">Все предметы</option>` + classes.map((c) => `<option value="${esc(c.id)}">${esc(c.short)}</option>`).join("");
  sel.value = S.f.subject;

  const terms = [...new Map((d.tasks || []).filter((t) => t.term).map((t) => [t.term.toLowerCase(), t.term])).values()];
  const tsel = $("#f-term");
  tsel.hidden = terms.length < 2;
  tsel.innerHTML = `<option value="">Весь год</option>` + terms.map((t) => `<option>${esc(t)}</option>`).join("");
  if (!terms.includes(S.f.term)) S.f.term = "";
  tsel.value = S.f.term;

  $("#f-graded").checked = S.f.graded;
  for (const b of $("#kind-seg").children) b.classList.toggle("on", b.dataset.kind === S.f.kind);
  for (const b of $("#view-seg").children) b.classList.toggle("on", b.dataset.view === S.view);
}

function subjectSummary(tasks) {
  const graded = tasks.filter((t) => t.grade?.type === "graded");
  const summ = graded.filter((t) => t.kind === "summative" && t.grade.criteria?.length);
  const critSrc = summ.length ? summ : graded;
  const crit = {};
  for (const t of critSrc) for (const c of t.grade.criteria || []) {
    if (c.score == null || !c.max) continue;
    (crit[c.letter] ||= { sum: 0, n: 0, max: c.max, name: c.name });
    crit[c.letter].sum += c.score; crit[c.letter].n++;
  }
  const pts = graded.filter((t) => t.grade.points?.max);
  const ptsPct = pts.length ? pts.reduce((a, t) => a + t.grade.points.score / t.grade.points.max, 0) / pts.length : null;
  return { graded, summative: summ.length > 0, crit, ptsPct, ptsN: pts.length };
}

function renderSubjects() {
  const d = S.data;
  const box = $("#subjects");
  const all = filtered({ ignoreSubject: true });
  const by = new Map();
  for (const t of all) { if (!by.has(t.class_id)) by.set(t.class_id, []); by.get(t.class_id).push(t); }
  const nowIso = new Date().toISOString().slice(0, 16);
  const missingOf = (cid) => (d.tasks || []).filter((t) => t.class_id === cid && /not submitted/i.test(t.grade?.text || "") && (t.date || "") < nowIso).length;
  const cards = (d.classes || []).filter((c) => by.has(c.id) || missingOf(c.id)).map((c) => {
    const ts = by.get(c.id) || [];
    const s = subjectSummary(ts);
    const letters = Object.keys(s.crit).sort();
    const critHtml = letters.length ? `<div class="crit">${letters.map((l) => {
      const x = s.crit[l];
      return chip(l, Math.round((x.sum / x.n) * 10) / 10, x.max, `${l}${x.name ? ": " + x.name : ""} — среднее по ${x.n} ${s.summative ? "summative" : "заданиям"}`);
    }).join("")}</div>` : "";
    const ptsHtml = s.ptsPct != null ? `<div class="pts">баллы: <b>${Math.round(s.ptsPct * 100)}%</b> в среднем (${s.ptsN})</div>` : "";
    const newN = ts.filter(isNew).length;
    const missing = missingOf(c.id);
    return `<button class="subj${S.f.subject === c.id ? " on" : ""}" data-id="${esc(c.id)}">
      <div class="name"><span>${newN ? '<span class="newdot" title="Новые оценки"></span>' : ""}${esc(c.short)}</span><span class="count">${s.graded.length} оц.</span></div>
      ${critHtml}${ptsHtml}${!critHtml && !ptsHtml ? '<div class="none">пока без оценок</div>' : ""}
      ${missing ? `<div class="missing-n" title="Срок прошёл, а работа не сдана">не сдано: ${missing}</div>` : ""}
    </button>`;
  });
  box.innerHTML = cards.join("");
  box.hidden = !cards.length;
}

function th(key, label, cls = "") {
  const on = S.sort.key === key;
  return `<th data-sort="${key}" class="${cls}">${label}${on ? ` <span class="arrow">${S.sort.dir < 0 ? "↓" : "↑"}</span>` : ""}</th>`;
}

function taskTags(t) {
  const tags = [];
  if (t.kind === "summative") tags.push('<span class="tag summative">Summative</span>');
  else if (t.kind === "formative") tags.push('<span class="tag formative">Formative</span>');
  for (const l of t.labels || []) if (!/^(summative|formative)$/i.test(l)) tags.push(`<span class="tag">${esc(l)}</span>`);
  if (/late/i.test(t.status_hint || "") || /late|overdue/i.test(t.status || "")) tags.push(`<span class="tag late">${esc(t.status_hint || t.status)}</span>`);
  else if (t.status && t.status !== "Submitted") tags.push(`<span class="tag">${esc(t.status)}</span>`);
  return tags.join("");
}

function renderList(list) {
  const rows = sortTasks(list).map((t) => {
    const key = `${t.class_id}:${t.id}`;
    return `<tr class="task${S.open.has(key) ? " open" : ""}" data-key="${esc(key)}">
      <td class="c-date">${esc(fmtDate(t.date))}</td>
      <td class="c-subj">${esc(t.subject)}</td>
      <td class="c-title">${isNew(t) ? '<span class="newdot" title="Новая оценка"></span>' : ""}<a href="${esc(t.url)}" target="_blank" rel="noopener">${esc(t.title)}</a>
        <div class="meta">${taskTags(t)}</div></td>
      <td class="c-grade">${gradeHtml(t)}</td>
      <td class="c-comment">${t.comment ? `<div class="clip">${esc(t.comment)}</div>` : ""}</td>
    </tr>`;
  });
  return `<div class="list"><table class="tbl"><thead><tr>
    ${th("date", "Дата")}${th("subject", "Предмет")}${th("title", "Задание")}${th("grade", "Оценка")}<th class="nosort">Комментарий учителя</th>
  </tr></thead><tbody>${rows.join("")}</tbody></table></div>`;
}

function renderBySubject(list) {
  const d = S.data;
  const by = new Map();
  for (const t of list) { if (!by.has(t.class_id)) by.set(t.class_id, []); by.get(t.class_id).push(t); }
  const blocks = (d.classes || []).filter((c) => by.has(c.id)).map((c) => {
    const ts = by.get(c.id).sort((a, b) => (a.date || "").localeCompare(b.date || ""));
    const letters = [...new Set(ts.flatMap((t) => (t.grade?.criteria || []).map((x) => x.letter)))].sort();
    const names = {};
    for (const t of ts) for (const x of t.grade?.criteria || []) if (x.name) names[x.letter] = x.name;
    const hasPts = ts.some((t) => t.grade?.points);
    const agg = {};
    const rows = ts.map((t) => {
      const cells = letters.map((l) => {
        const x = (t.grade?.criteria || []).find((y) => y.letter === l);
        if (!x || x.score == null) return `<td class="num"></td>`;
        (agg[l] ||= { s: 0, n: 0, max: x.max }); agg[l].s += x.score; agg[l].n++;
        return `<td class="num">${chip("", x.score, x.max)}</td>`;
      });
      let ptsCell = "";
      if (hasPts) {
        const p = t.grade?.points;
        if (p && p.score != null) { (agg._p ||= { s: 0, n: 0 }); agg._p.s += p.max ? p.score / p.max : 0; agg._p.n++; }
        ptsCell = `<td class="num">${p && p.score != null ? chip("", p.score, p.max) : ""}</td>`;
      }
      const status = t.grade?.type !== "graded" ? `<span class="status"> · ${esc(t.grade?.text || "")}</span>` : "";
      return `<tr><td class="c-date">${esc(fmtDate(t.date))}</td>
        <td class="c-title">${isNew(t) ? '<span class="newdot"></span>' : ""}<a href="${esc(t.url)}" target="_blank" rel="noopener">${esc(t.title)}</a>${status}
          <div class="meta">${taskTags(t)}</div></td>${cells.join("")}${ptsCell}</tr>`;
    });
    const foot = letters.map((l) => agg[l] ? `<td class="num">${chip("", Math.round((agg[l].s / agg[l].n) * 10) / 10, agg[l].max)}</td>` : `<td class="num"></td>`);
    const footPts = hasPts ? `<td class="num">${agg._p ? Math.round((agg._p.s / agg._p.n) * 100) + "%" : ""}</td>` : "";
    return `<section class="subj-block"><h2>${esc(c.short)} <small>${esc(c.name)}</small></h2>
      <table class="tbl mtx"><thead><tr><th class="nosort">Дата</th><th class="nosort">Задание</th>
      ${letters.map((l) => `<th class="nosort num"${names[l] ? ` title="${esc(names[l])}"` : ""}>${esc(l)}</th>`).join("")}
      ${hasPts ? '<th class="nosort num">Баллы</th>' : ""}</tr></thead>
      <tbody>${rows.join("")}</tbody>
      ${letters.length || hasPts ? `<tfoot><tr><td></td><td>Среднее</td>${foot.join("")}${footPts}</tr></tfoot>` : ""}</table></section>`;
  });
  return blocks.join("");
}

function render() {
  const d = S.data;
  renderHeader();
  renderFilters();
  renderSubjects();
  const list = filtered();
  const view = $("#view");
  const empty = $("#empty");
  if (!d.tasks) {
    view.innerHTML = "";
    empty.hidden = false;
    empty.textContent = d.syncing ? "Собираю задания и оценки из ManageBac… Обычно это 10–30 секунд." : (d.error ? "" : "Данных пока нет.");
    return;
  }
  if (!list.length) {
    view.innerHTML = "";
    empty.hidden = false;
    empty.textContent = S.f.graded ? "Здесь нет заданий с оценками. Снимите галочку «только с оценкой», чтобы увидеть все задания." : "Ничего не найдено.";
    return;
  }
  empty.hidden = true;
  view.innerHTML = S.view === "list" ? renderList(list) : renderBySubject(list);
}

// ------------------------------------------------------------ данные

async function load() {
  const { status, body } = await api("/api/data");
  $("#loading").hidden = true;
  if (status === 401) return showLogin();
  if (status !== 200) { setTimeout(load, 5000); return; }
  const first = !S.data;
  S.data = body;
  $("#login").hidden = true;
  $("#app").hidden = false;
  render();
  if (first) route();
  clearTimeout(S.poll);
  if (body.syncing) S.poll = setTimeout(load, 2500);
  else if (body.fetched_at) store.set("lastVisit", body.fetched_at);
}

function showLogin() {
  $("#app").hidden = true;
  $("#login").hidden = false;
  $("#login-form [name=login]").focus();
}

$("#login-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const f = e.target, btn = f.querySelector("button"), err = $("#login-error");
  err.hidden = true;
  btn.disabled = true; btn.textContent = "Проверяю в ManageBac…";
  const { status, body } = await api("/api/login", {
    method: "POST",
    body: JSON.stringify({ login: f.login.value, password: f.password.value }),
  });
  btn.disabled = false; btn.textContent = "Войти";
  if (status === 200) { f.password.value = ""; load(); }
  else { err.hidden = false; err.textContent = body.error || "Не получилось войти."; }
});

$("#refresh").addEventListener("click", async () => {
  await api("/api/refresh", { method: "POST" });
  S.data.syncing = true;
  renderHeader();
  clearTimeout(S.poll);
  S.poll = setTimeout(load, 1500);
});
$("#logout").addEventListener("click", async () => {
  await api("/api/logout", { method: "POST" });
  location.reload();
});

$("#f-subject").addEventListener("change", (e) => { S.f.subject = e.target.value; render(); });
$("#f-term").addEventListener("change", (e) => { S.f.term = e.target.value; render(); });
$("#f-graded").addEventListener("change", (e) => { S.f.graded = e.target.checked; store.set("graded", S.f.graded); render(); });
$("#f-search").addEventListener("input", (e) => { S.f.q = e.target.value; render(); });
$("#kind-seg").addEventListener("click", (e) => {
  const b = e.target.closest("button"); if (!b) return;
  S.f.kind = b.dataset.kind; render();
});
$("#view-seg").addEventListener("click", (e) => {
  const b = e.target.closest("button"); if (!b) return;
  S.view = b.dataset.view; store.set("view", S.view); render();
});
$("#subjects").addEventListener("click", (e) => {
  const b = e.target.closest(".subj"); if (!b) return;
  S.f.subject = S.f.subject === b.dataset.id ? "" : b.dataset.id; render();
});
$("#view").addEventListener("click", (e) => {
  if (e.target.closest("a")) return;
  const h = e.target.closest("th[data-sort]");
  if (h) {
    const k = h.dataset.sort;
    S.sort = S.sort.key === k ? { key: k, dir: -S.sort.dir } : { key: k, dir: k === "date" || k === "grade" ? -1 : 1 };
    return render();
  }
  const tr = e.target.closest("tr.task");
  if (tr) {
    const k = tr.dataset.key;
    S.open.has(k) ? S.open.delete(k) : S.open.add(k);
    tr.classList.toggle("open");
  }
});
document.addEventListener("visibilitychange", () => { if (!document.hidden && S.data) load(); });

// ------------------------------------------------------------ вкладки: оценки / предметы

function route() {
  const h = location.hash || "#/";
  const study = h.startsWith("#/subjects") || h.startsWith("#/s/");
  $("#page-grades").hidden = study;
  $("#page-study").hidden = !study;
  for (const a of $("#tabs").children) a.classList.toggle("on", a.dataset.tab === (study ? "study" : "grades"));
  if (study && window.Study) window.Study.show(h);
  if (!study) document.title = "Оценки ManageBac";
}
window.addEventListener("hashchange", route);
window.App = { api, esc, gradeHtml, fmtDate, chip, level, store, reload: () => load() };

// убрать service worker прежнего сайта, если он ещё остался
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.getRegistrations().then((regs) => regs.forEach((r) => r.unregister())).catch(() => {});
}

load();

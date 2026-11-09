/* Раздел «Предметы»: что проходим (из ManageBac), задания с материалами, конспекты и разборы. */
(() => {
  "use strict";
  const { api, esc, gradeHtml } = window.App;
  const root = document.getElementById("page-study");
  const mem = { subjects: null, subject: {}, note: {} };

  const KIND = {
    notes: "Конспект", solutions: "Решения", guide: "Как выполнить", review: "Повторение", cheatsheet: "Шпаргалка",
  };
  const FILE_ICON = {
    pdf: "PDF", doc: "DOC", docx: "DOC", ppt: "PPT", pptx: "PPT", xls: "XLS", xlsx: "XLS", jpg: "IMG", jpeg: "IMG",
    png: "IMG", gdoc: "Docs", gsheet: "Sheets", gslides: "Slides", gform: "Form", gdrive: "Drive", video: "Video", link: "Link",
  };
  const MONTHS = ["янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"];

  const day = (iso) => {
    if (!iso) return "";
    const d = new Date(iso);
    return `${d.getDate()} ${MONTHS[d.getMonth()]}`;
  };
  const daysLeft = (iso) => {
    const ms = new Date(iso).setHours(0, 0, 0, 0) - new Date().setHours(0, 0, 0, 0);
    const n = Math.round(ms / 864e5);
    if (n === 0) return "сегодня";
    if (n === 1) return "завтра";
    if (n < 0) return "";
    const w = n % 10 === 1 && n % 100 !== 11 ? "день" : [2, 3, 4].includes(n % 10) && ![12, 13, 14].includes(n % 100) ? "дня" : "дней";
    return `через ${n} ${w}`;
  };
  const isFuture = (t) => t.date && new Date(t.date) >= new Date(new Date().setHours(0, 0, 0, 0));

  function setTitle(t) { document.title = t ? `${t} · Предметы` : "Предметы"; }

  async function get(path, key, store) {
    if (store && store[key]) return store[key];
    const { status, body } = await api(path);
    if (status === 401) { window.App.reload(); throw new Error("auth"); }
    if (status !== 200) throw new Error(body.error || "Ошибка " + status);
    if (store) store[key] = body;
    return body;
  }

  function loading(msg = "Загрузка…") { root.innerHTML = `<p class="st-empty">${esc(msg)}</p>`; }
  function fail(e) {
    if (e.message === "auth") return;
    root.innerHTML = `<p class="st-empty">Не получилось загрузить: ${esc(e.message)}. <a href="javascript:location.reload()">Обновить страницу</a></p>`;
  }

  // ------------------------------------------------------------------ роутер

  async function show(hash) {
    const p = hash.replace(/^#\/?/, "").split("/").map(decodeURIComponent);
    window.scrollTo(0, 0);
    try {
      if (p[0] === "subjects") return await showSubjects();
      if (p[0] === "s" && p[1]) {
        if (p[2] === "n" && p[3]) return await showNote(p[1], p[3]);
        if (p[2] === "t" && p[3]) return await showTask(p[1], p[3]);
        return await showSubject(p[1]);
      }
      return await showSubjects();
    } catch (e) { fail(e); }
  }

  // ------------------------------------------------------------------ список предметов

  let pollTimer = null;
  async function showSubjects() {
    setTitle("");
    if (!mem.subjects) loading();
    const d = await get("/api/subjects", "x", null);
    mem.subjects = d;
    const subs = d.subjects || [];
    const study = subs.filter((s) => s.notes || (s.units || []).length || s.tasks);
    const cards = study.map((s) => {
      const next = s.upcoming[0];
      return `<a class="st-card" href="#/s/${esc(s.id)}">
        <div class="st-card-top"><h3>${esc(s.short)}</h3>${s.notes ? `<span class="st-badge">${s.notes} ${plural(s.notes, "материал", "материала", "материалов")}</span>` : ""}</div>
        ${(s.pending || []).length ? `<div class="st-pending" title="${esc(s.pending.map((p) => p.title).join("\n"))}"><span class="dot"></span>${s.pending.length} ${plural(s.pending.length, "новое задание", "новых задания", "новых заданий")} с файлами без разбора</div>` : ""}
        ${nowUnits(s.units || []).length ? `<div class="st-now"><span class="st-label">Сейчас</span>${nowUnits(s.units).slice(0, 4).map((u) => `<span>${esc(u.title)}</span>`).join("")}</div>` : ""}
        ${next ? `<div class="st-next ${next.kind === "summative" ? "sum" : ""}"><b>${esc(day(next.date))}</b> ${esc(next.title)} <span class="muted">${esc(daysLeft(next.date))}</span></div>` : ""}
      </a>`;
    });
    const waiting = !d.materials_at;
    root.innerHTML = `
      <div class="st-head"><h1>Предметы</h1>
        <p class="muted">Что сейчас проходите, задания с файлами из ManageBac, конспекты и разборы.</p></div>
      ${subs.some((x) => (x.pending || []).length) ? `<div class="st-note warn"><b>Есть новые файлы без разбора</b> (отмечены красной точкой). Напишите Claude «обнови конспекты» — он заберёт файлы и напишет разборы.</div>` : ""}
      ${waiting ? `<div class="st-note">Сервер собирает материалы из ManageBac (темы, описания заданий, файлы). Это занимает минуту-две — страница обновится сама.</div>` : ""}
      <div class="st-grid">${cards.join("") || '<p class="st-empty">Пока пусто.</p>'}</div>`;
    setBadge(subs);
    clearTimeout(pollTimer);
    if (waiting || d.syncing) pollTimer = setTimeout(() => { if (location.hash.startsWith("#/subjects")) showSubjects(); }, 5000);
  }

  function setBadge(subs) {
    const n = subs.reduce((k, x) => k + (x.pending || []).length, 0);
    const tab = document.querySelector('#tabs [data-tab="study"]');
    if (!tab) return;
    let b = tab.querySelector(".tab-dot");
    if (!n) { if (b) b.remove(); return; }
    if (!b) { b = document.createElement("span"); b.className = "tab-dot"; tab.appendChild(b); }
    b.textContent = n;
    b.title = "Новые задания с файлами без разбора";
  }
  async function refreshBadge() {
    try { const { status, body } = await api("/api/subjects"); if (status === 200) setBadge(body.subjects || []); } catch {}
  }

  function plural(n, a, b, c) {
    const m10 = n % 10, m100 = n % 100;
    if (m10 === 1 && m100 !== 11) return a;
    if (m10 >= 2 && m10 <= 4 && (m100 < 12 || m100 > 14)) return b;
    return c;
  }

  // ------------------------------------------------------------------ страница предмета

  async function loadSubject(cid, fresh = false) {
    if (fresh) delete mem.subject[cid];
    return get(`/api/subject/${encodeURIComponent(cid)}`, cid, mem.subject);
  }

  function noteCard(cid, n) {
    return `<a class="st-notecard k-${esc(n.kind)}" href="#/s/${esc(cid)}/n/${esc(n.slug)}">
      <span class="st-kind">${esc(KIND[n.kind] || "Материал")}</span>
      <b>${esc(n.title)}</b>${n.summary ? `<span class="muted">${esc(n.summary)}</span>` : ""}</a>`;
  }

  function unitBlock(cid, u, notes) {
    const info = u.info || {};
    const soi = (info["Statement of Inquiry"] || []).join(" ");
    const qs = info["Inquiry Questions"] || [];
    const kc = (info["Key Concepts"] || []).map((x) => x.split(/ is | are /)[0]).filter((x) => x.length < 40);
    const rc = (info["Related Concept(s)"] || []).join(", ");
    const gc = (info["Global Context"] || []).join(", ");
    const un = notes.filter((n) => n.units.includes(u.id));
    return `<article class="st-unit">
      <div class="st-unit-meta">${u.start ? `с ${esc(u.start)}` : ""}${u.duration ? ` · ${esc(u.duration)}` : ""}</div>
      <h3>${esc(u.title)}</h3>
      ${soi ? `<blockquote class="st-soi"><span>Statement of Inquiry</span>${esc(soi)}</blockquote>` : ""}
      ${kc.length || rc || gc ? `<div class="st-concepts">${kc.map((k) => `<span class="pill">${esc(k)}</span>`).join("")}${rc ? `<span class="pill soft">${esc(rc)}</span>` : ""}${gc ? `<span class="pill soft">${esc(gc)}</span>` : ""}</div>` : ""}
      ${qs.length ? `<details class="st-qs"><summary>Вопросы темы (${qs.length})</summary><ul>${qs.map((q) => {
        const [lab, ...rest] = q.split(": ");
        return rest.length && ["Factual", "Conceptual", "Debatable"].includes(lab) ? `<li><span class="qk">${esc(lab)}</span> ${esc(rest.join(": "))}</li>` : `<li>${esc(q)}</li>`;
      }).join("")}</ul></details>` : ""}
      ${un.length ? `<div class="st-unit-notes">${un.map((n) => noteCard(cid, n)).join("")}</div>` : ""}
    </article>`;
  }

  // «Сейчас проходим»: отметке Current Unit в ManageBac верим, только если юнит начался недавно;
  // иначе — юниты, к которым привязаны свежие задания.
  const MON = { Jan: 0, Feb: 1, Mar: 2, Apr: 3, May: 4, Jun: 5, Jul: 6, Aug: 7, Sep: 8, Oct: 9, Nov: 10, Dec: 11 };
  function unitStart(u) {
    const m = /W(\d)\s*([A-Z][a-z]{2})/.exec(u.start || "");
    if (!m || !(m[2] in MON)) return null;
    const now = new Date(), mon = MON[m[2]];
    const yStart = now.getMonth() >= 7 ? now.getFullYear() : now.getFullYear() - 1;
    return new Date(mon >= 7 ? yStart : yStart + 1, mon, 1 + (m[1] - 1) * 7);
  }
  function recentTaskUnits(units) {
    const now = Date.now(), W = 7 * 864e5;
    return units.filter((u) => u.last_task && new Date(u.last_task).getTime() > now - 3 * W)
      .sort((a, b) => b.last_task.localeCompare(a.last_task));
  }
  const JUNK = /^(example|test|template|copy of .*)$/i;   // учебные заготовки учителей
  function nowUnits(allUnits) {
    const units = allUnits.filter((u) => !JUNK.test((u.title || "").trim()));
    const now = Date.now(), W = 7 * 864e5;
    const fresh = units.filter((u) => {
      if (!u.current) return false;
      const s = unitStart(u);
      return s && s.getTime() > now - 6 * W && s.getTime() < now + W;
    });
    if (fresh.length >= 1 && fresh.length <= 4) return fresh;   // план ManageBac правдоподобен
    const byTasks = recentTaskUnits(units);
    if (byTasks.length) return byTasks;                          // иначе — по свежим заданиям
    if (fresh.length) return fresh.slice(0, 3);
    return units.filter((u) => u.current).slice(0, 3);
  }

  function taskRow(cid, t) {
    const files = (t.files || []).length + (t.links || []).length;
    const sum = t.kind === "summative";
    return `<a class="st-task ${sum ? "sum" : ""}" href="#/s/${esc(cid)}/t/${esc(t.id)}">
      <span class="st-task-date">${esc(day(t.date))}</span>
      <span class="st-task-main"><b>${esc(t.title)}</b>
        <span class="st-task-meta">${sum ? '<span class="tag summative">Summative</span>' : t.kind === "formative" ? '<span class="tag formative">Formative</span>' : ""}
        ${files ? `<span class="tag">${files} ${plural(files, "файл", "файла", "файлов")}</span>` : ""}
        ${t.notes && t.notes.length ? '<span class="tag sol">есть разбор</span>' : ""}
        ${t.needs_notes ? '<span class="tag nonote"><span class="dot"></span>нет разбора</span>' : ""}
        ${isFuture(t) ? `<span class="tag due">${esc(daysLeft(t.date))}</span>` : ""}</span></span>
      <span class="st-task-grade">${t.grade && t.grade.type === "graded" ? gradeHtml(t) : ""}</span>
    </a>`;
  }

  async function showSubject(cid) {
    if (!mem.subject[cid]) loading();
    const d = await loadSubject(cid);
    const c = d.class;
    setTitle(c.short);
    const cur = nowUnits(d.units);
    const extraUnits = recentTaskUnits(d.units).filter((u) => !cur.includes(u));
    const notes = d.notes || [];
    const tasks = [...d.tasks].sort((a, b) => (b.date || "").localeCompare(a.date || ""));
    const upcoming = tasks.filter(isFuture).reverse();
    const past = tasks.filter((t) => !isFuture(t));
    const unitNotes = new Set(cur.flatMap((u) => notes.filter((n) => n.units.includes(u.id)).map((n) => n.slug)));
    const otherNotes = notes.filter((n) => !unitNotes.has(n.slug));
    const groups = {};
    for (const n of otherNotes) (groups[n.kind] ||= []).push(n);
    const order = ["review", "notes", "solutions", "guide", "cheatsheet"];

    root.innerHTML = `
      <nav class="st-crumbs"><a href="#/subjects">← Все предметы</a></nav>
      <div class="st-head"><h1>${esc(c.short)}</h1>
        <p class="muted">${esc(c.name)} · <a href="${esc(d.school_url)}/student/classes/${esc(cid)}" target="_blank" rel="noopener">открыть в ManageBac ↗</a></p></div>
      ${!d.materials_at ? `<div class="st-note">Материалы из ManageBac ещё собираются — обновите страницу через минуту.</div>` : ""}
      <div class="st-layout">
        <div class="st-main">
          ${cur.length ? `<section><h2>Сейчас проходим</h2>${cur.map((u) => unitBlock(cid, u, notes)).join("")}
            ${extraUnits.length ? `<p class="st-extra">Свежие задания в ManageBac привязаны также к: ${extraUnits.map((u) => `<span class="pill soft">${esc(u.title)}</span>`).join(" ")}</p>` : ""}</section>` : ""}
          ${otherNotes.length ? `<section><h2>Конспекты и разборы</h2>${order.filter((k) => groups[k]).map((k) =>
            `<div class="st-notes">${groups[k].map((n) => noteCard(cid, n)).join("")}</div>`).join("")}
            ${Object.keys(groups).filter((k) => !order.includes(k)).map((k) => `<div class="st-notes">${groups[k].map((n) => noteCard(cid, n)).join("")}</div>`).join("")}</section>` : ""}
          ${upcoming.length ? `<section><h2>Впереди</h2><div class="st-tasks">${upcoming.map((t) => taskRow(cid, t)).join("")}</div></section>` : ""}
          <section><h2>Задания ${past.length ? `<small>${past.length}</small>` : ""}</h2>
            <div class="st-tasks">${past.map((t) => taskRow(cid, t)).join("") || '<p class="muted">Заданий нет.</p>'}</div></section>
        </div>
        <aside class="st-side">
          ${d.files && d.files.length ? `<section><h4>Файлы предмета</h4>${d.files.map(fileLink).join("")}</section>` : ""}
          ${d.units.some((u) => !u.extra) ? `<section><h4>Темы года</h4><ol class="st-units-all">${d.units.filter((u) => !u.extra).map((u) =>
            `<li class="${cur.includes(u) ? "cur" : ""}"><span>${esc(u.title)}</span><small>${esc(u.start || "")}</small></li>`).join("")}</ol></section>` : ""}
        </aside>
      </div>`;
  }

  function fileLink(f) {
    const k = (f.kind || "").toLowerCase();
    return `<a class="st-file" href="${esc(f.url)}" target="_blank" rel="noopener">
      <span class="st-ficon k-${esc(k)}">${esc(FILE_ICON[k] || k.toUpperCase().slice(0, 4) || "FILE")}</span>
      <span class="st-fname">${esc(f.name || prettyUrl(f.url))}${f.size ? `<small>${esc(f.size)}</small>` : ""}</span></a>`;
  }
  function prettyUrl(u) {
    try { const x = new URL(u); return x.hostname.replace(/^www\./, "") + (x.pathname.length > 1 ? x.pathname.slice(0, 30) + "…" : ""); } catch { return u; }
  }

  // ------------------------------------------------------------------ страница задания

  async function showTask(cid, tid) {
    if (!mem.subject[cid]) loading();
    const d = await loadSubject(cid);
    const t = d.tasks.find((x) => String(x.id) === String(tid));
    if (!t) { root.innerHTML = `<nav class="st-crumbs"><a href="#/s/${esc(cid)}">← ${esc(d.class.short)}</a></nav><p class="st-empty">Задание не найдено.</p>`; return; }
    setTitle(t.title);
    const notes = (d.notes || []).filter((n) => n.tasks.includes(String(t.id)));
    const unit = d.units.find((u) => u.id === t.unit_id);
    const graded = t.grade && t.grade.type === "graded";
    root.innerHTML = `
      <nav class="st-crumbs"><a href="#/subjects">Предметы</a> / <a href="#/s/${esc(cid)}">${esc(d.class.short)}</a></nav>
      <article class="st-taskpage">
        <div class="st-task-head">
          <div class="st-task-when">${esc(day(t.date))}${t.due_text ? ` · ${esc(t.due_text.replace(/^\w+ at\s*/, ""))}` : ""}${isFuture(t) ? ` · <b>${esc(daysLeft(t.date))}</b>` : ""}</div>
          <h1>${esc(t.title)}</h1>
          <div class="st-task-meta">${(t.labels || []).map((l) => `<span class="tag ${/summative/i.test(l) ? "summative" : /formative/i.test(l) ? "formative" : ""}">${esc(l)}</span>`).join("")}
            ${t.status ? `<span class="tag">${esc(t.status)}${t.status_hint ? " · " + esc(t.status_hint) : ""}</span>` : ""}
            ${unit ? `<span class="tag soft">${esc(unit.title)}</span>` : t.unit_title ? `<span class="tag soft">${esc(t.unit_title)}</span>` : ""}</div>
        </div>
        ${notes.length ? `<section class="st-sol-links"><h2>Разбор и подготовка</h2><div class="st-notes">${notes.map((n) => noteCard(cid, n)).join("")}</div></section>` : ""}
        ${graded || t.comment ? `<section class="st-grade-box"><h2>Оценка</h2>${graded ? gradeHtml(t) : `<span class="muted">${esc((t.grade && t.grade.text) || "")}</span>`}
          ${t.comment ? `<p class="st-comment">${esc(t.comment)}</p>` : ""}</section>` : ""}
        <section><h2>Задание в ManageBac</h2>
          ${t.description_html ? `<div class="st-desc">${t.description_html}</div>` : `<p class="muted">${d.materials_at ? "Учитель не добавил описания." : "Описание ещё загружается."}</p>`}
          ${(t.files || []).length || (t.links || []).length ? `<div class="st-files">${(t.files || []).map(fileLink).join("")}${(t.links || []).map((l) => fileLink({ ...l, name: l.name })).join("")}</div>` : ""}
          <p><a class="btn ghost" href="${esc(t.url)}" target="_blank" rel="noopener">Открыть в ManageBac ↗</a></p>
        </section>
      </article>`;
  }

  // ------------------------------------------------------------------ конспект

  async function showNote(cid, slug) {
    const key = cid + "/" + slug;
    if (!mem.note[key]) loading();
    const [d, n] = await Promise.all([loadSubject(cid), get(`/api/note/${encodeURIComponent(cid)}/${encodeURIComponent(slug)}`, key, mem.note)]);
    const meta = n.meta || {};
    setTitle(meta.title || slug);
    const list = d.notes || [];
    const i = list.findIndex((x) => x.slug === slug);
    const me = list[i] || { tasks: [], units: [] };
    const tasks = me.tasks.map((id) => d.tasks.find((t) => String(t.id) === String(id))).filter(Boolean);
    const units = me.units.map((id) => d.units.find((u) => u.id === id)).filter(Boolean);
    const prev = list[i - 1], next = list[i + 1];
    root.innerHTML = `
      <nav class="st-crumbs"><a href="#/subjects">Предметы</a> / <a href="#/s/${esc(cid)}">${esc(d.class.short)}</a></nav>
      <div class="st-reader">
        <article class="md" id="md">
          <div class="md-kind">${esc(KIND[meta.kind] || "Материал")}</div>
          <h1>${esc(meta.title || slug)}</h1>
          ${units.length || tasks.length ? `<div class="md-for">${units.map((u) => `<span class="pill soft">${esc(u.title)}</span>`).join("")}
            ${tasks.map((t) => `<a class="pill" href="#/s/${esc(cid)}/t/${esc(t.id)}">${esc(t.title)}${t.date ? " · " + esc(day(t.date)) : ""}</a>`).join("")}</div>` : ""}
          <div class="md-body">${renderMarkdown(n.markdown)}</div>
          <nav class="md-pager">${prev ? `<a href="#/s/${esc(cid)}/n/${esc(prev.slug)}">← ${esc(prev.title)}</a>` : "<span></span>"}
            ${next ? `<a href="#/s/${esc(cid)}/n/${esc(next.slug)}">${esc(next.title)} →</a>` : ""}</nav>
        </article>
        <aside class="md-toc" id="toc"></aside>
      </div>`;
    enhance(root.querySelector(".md-body"));
    buildToc(root.querySelector(".md-body"), root.querySelector("#toc"));
  }

  // ------------------------------------------------------------------ Markdown + формулы

  const PH = "";
  const BOXES = { solution: "Решение", hint: "Подсказка", answer: "Ответ", proof: "Доказательство", more: "Подробнее" };

  function renderMarkdown(src) {
    if (!window.marked) return `<pre>${esc(src)}</pre>`;
    const codes = [], maths = [];
    let md = src.replace(/^```[^\n]*\n[\s\S]*?^```\s*$/gm, (m) => { codes.push(m); return `${PH}C${codes.length - 1}${PH}`; });
    md = md.replace(/`[^`\n]+`/g, (m) => { codes.push(m); return `${PH}C${codes.length - 1}${PH}`; });
    md = md.replace(/\$\$([\s\S]+?)\$\$/g, (m, tex) => { maths.push([tex, true]); return `${PH}M${maths.length - 1}${PH}`; });
    md = md.replace(/(^|[^\\$])\$(?=\S)([^$\n]*?\S)\$(?!\d)/g, (m, pre, tex) => { maths.push([tex, false]); return `${pre}${PH}M${maths.length - 1}${PH}`; });
    md = md.replace(/\\\$/g, "$");
    md = containers(md);
    md = md.replace(new RegExp(`${PH}C(\\d+)${PH}`, "g"), (m, k) => codes[k]);
    let html = window.marked.parse(md, { gfm: true });
    html = html.replace(new RegExp(`${PH}M(\\d+)${PH}`, "g"), (m, k) => {
      const [tex, display] = maths[k];
      try { return window.katex.renderToString(tex, { displayMode: display, throwOnError: false, strict: false, trust: false }); }
      catch { return esc(tex); }
    });
    return html;
  }

  function containers(md) {
    const out = [], stack = [];
    for (const line of md.split("\n")) {
      const m = line.match(/^:::\s*([a-z]+)?\s*(.*?)\s*$/);
      if (m && m[1]) {
        const type = m[1], title = m[2];
        if (type === "plot") { stack.push({ type, buf: [] }); continue; }
        stack.push({ type });
        const t = title ? window.marked.parseInline(title) : "";
        if (BOXES[type]) out.push("", `<details class="box ${type}"><summary>${t || BOXES[type]}</summary><div class="box-body">`, "");
        else out.push("", `<div class="box ${type}">${t ? `<div class="box-title">${t}</div>` : ""}`, "");
        continue;
      }
      if (m && !m[1] && stack.length) {
        const top = stack.pop();
        if (top.type === "plot") out.push("", `<div class="plot" data-cfg="${esc(top.buf.join("\n"))}"></div>`, "");
        else out.push("", BOXES[top.type] ? "</div></details>" : "</div>", "");
        continue;
      }
      const top = stack[stack.length - 1];
      if (top && top.type === "plot") top.buf.push(line); else out.push(line);
    }
    return out.join("\n");
  }

  function enhance(el) {
    for (const p of el.querySelectorAll(".plot")) {
      try { mountPlot(p, JSON.parse(p.dataset.cfg)); } catch (e) { p.textContent = "Ошибка графика: " + e.message; }
    }
    for (const t of el.querySelectorAll("table")) {
      const w = document.createElement("div"); w.className = "md-table";
      t.replaceWith(w); w.appendChild(t);
    }
    for (const a of el.querySelectorAll("a[href^='http']")) { a.target = "_blank"; a.rel = "noopener"; }
  }

  function plainText(el) {
    const c = el.cloneNode(true);
    for (const k of c.querySelectorAll(".katex")) {
      const tex = k.querySelector("annotation");
      k.replaceWith(document.createTextNode(tex ? tex.textContent : k.textContent));
    }
    return c.textContent.trim();
  }

  function buildToc(body, toc) {
    const hs = [...body.querySelectorAll("h2, h3")];
    if (hs.length < 3) { toc.remove(); return; }
    hs.forEach((h, i) => { h.id = "sec-" + i; });
    toc.innerHTML = `<div class="toc-title">Содержание</div>` + hs.map((h) =>
      `<a href="#" data-to="${h.id}" class="${h.tagName === "H3" ? "sub" : ""}">${esc(plainText(h))}</a>`).join("");
    toc.addEventListener("click", (e) => {
      const a = e.target.closest("a[data-to]"); if (!a) return;
      e.preventDefault();
      document.getElementById(a.dataset.to).scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  // ------------------------------------------------------------------ интерактивный график

  function compile(expr, names) {
    const js = String(expr).replace(/\^/g, "**");
    // eslint-disable-next-line no-new-func
    return new Function(...names, `const ln=Math.log, sgn=Math.sign, lg=Math.log10; with (Math) { return (${js}); }`);
  }

  function mountPlot(el, cfg) {
    const params = cfg.params || {};
    const names = ["x", ...Object.keys(params)];
    const vals = Object.fromEntries(Object.entries(params).map(([k, p]) => [k, p.value ?? p.min ?? 0]));
    const tnames = ["t", ...Object.keys(params)];
    const fns = (cfg.fns || []).map((f) => (typeof f === "string" ? { f } : f)).map((f, i) => ({ ...f,
      fn: f.f != null ? compile(f.f, names) : null,
      fx: f.xt != null ? compile(f.xt, tnames) : null, fy: f.yt != null ? compile(f.yt, tnames) : null,
      c: f.color || i + 1 }));
    const pnames = Object.keys(params);
    const ev = (e) => compile(e, pnames)(...pnames.map((k) => vals[k]));
    const W = 640, H = Math.round(W * (cfg.aspect || 0.62));
    const [x0, x1] = cfg.x || [-5, 5], [y0, y1] = cfg.y || [-5, 5];
    const X = (x) => ((x - x0) / (x1 - x0)) * W, Y = (y) => H - ((y - y0) / (y1 - y0)) * H;

    el.innerHTML = `${cfg.title ? `<div class="plot-title">${esc(cfg.title)}</div>` : ""}<svg viewBox="0 0 ${W} ${H}" role="img"></svg>
      ${pnames.length ? `<div class="plot-ctrl">${pnames.map((k) => {
        const p = params[k];
        return `<label><span>${esc(p.label || k)} = <b data-v="${k}"></b></span><input type="range" data-k="${k}" min="${p.min}" max="${p.max}" step="${p.step || 0.1}" value="${vals[k]}"></label>`;
      }).join("")}</div>` : ""}
      ${cfg.legend !== false && fns.some((f) => f.label) ? `<div class="plot-legend">${fns.filter((f) => f.label).map((f) => `<span class="c${f.c}">${esc(f.label)}</span>`).join("")}</div>` : ""}
      <div class="plot-out"></div>${cfg.note ? `<div class="plot-note">${esc(cfg.note)}</div>` : ""}`;
    const svg = el.querySelector("svg"), out = el.querySelector(".plot-out");

    const step = (span) => { const raw = span / 10, p = 10 ** Math.floor(Math.log10(raw)), m = raw / p; return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p; };
    function draw() {
      const parts = [];
      const sx = cfg.xstep || step(x1 - x0), sy = cfg.ystep || step(y1 - y0);
      for (let x = Math.ceil(x0 / sx) * sx; x <= x1 + 1e-9; x += sx) parts.push(`<line class="g" x1="${X(x)}" x2="${X(x)}" y1="0" y2="${H}"/>`);
      for (let y = Math.ceil(y0 / sy) * sy; y <= y1 + 1e-9; y += sy) parts.push(`<line class="g" y1="${Y(y)}" y2="${Y(y)}" x1="0" x2="${W}"/>`);
      if (y0 < 0 && y1 > 0) parts.push(`<line class="ax" x1="0" x2="${W}" y1="${Y(0)}" y2="${Y(0)}"/>`);
      if (x0 < 0 && x1 > 0) parts.push(`<line class="ax" y1="0" y2="${H}" x1="${X(0)}" x2="${X(0)}"/>`);
      const ty = y0 < 0 && y1 > 0 ? Y(0) : H, tx = x0 < 0 && x1 > 0 ? X(0) : 0;
      const edgeX = (x1 - x0) * 0.025, edgeY = (y1 - y0) * 0.04;
      for (let x = Math.ceil(x0 / sx) * sx; x <= x1 + 1e-9; x += sx) if (Math.abs(x) > 1e-9 && x - x0 > edgeX && x1 - x > edgeX) parts.push(`<text class="t" x="${X(x)}" y="${Math.min(ty + 14, H - 3)}" text-anchor="middle">${+x.toFixed(4)}</text>`);
      for (let y = Math.ceil(y0 / sy) * sy; y <= y1 + 1e-9; y += sy) if (Math.abs(y) > 1e-9 && y - y0 > edgeY && y1 - y > edgeY) parts.push(`<text class="t" x="${Math.max(tx - 5, 18)}" y="${Y(y) + 4}" text-anchor="end">${+y.toFixed(4)}</text>`);
      const args = (x) => [x, ...pnames.map((k) => vals[k])];
      for (const s of cfg.shade || []) {
        // закрасить область между f (снизу) и g (сверху) там, где выполнено условие
        const lo = compile(s.below ?? String(y0), names), hi = compile(s.above ?? String(y1), names);
        const n = 300, top = [], bot = [];
        for (let i = 0; i <= n; i++) {
          const x = x0 + ((x1 - x0) * i) / n;
          let a = lo(...args(x)), b = hi(...args(x));
          if (!isFinite(a)) a = y0; if (!isFinite(b)) b = y1;
          a = Math.max(y0, Math.min(y1, a)); b = Math.max(y0, Math.min(y1, b));
          if (b < a) b = a;
          bot.push(`${X(x).toFixed(1)},${Y(a).toFixed(1)}`); top.push(`${X(x).toFixed(1)},${Y(b).toFixed(1)}`);
        }
        parts.push(`<polygon class="sh c${s.color || 1}" points="${bot.join(" ")} ${top.reverse().join(" ")}"/>`);
      }
      for (const f of fns) {
        if (f.fx) {
          // параметрическая кривая x(t), y(t)
          if (f.show && !ev(f.show)) continue;
          const [ta, tb] = (f.t || [0, 1]).map((v) => (typeof v === "string" ? ev(v) : v));
          const n = f.n || 800; let d = "", pen = false;
          for (let i = 0; i <= n; i++) {
            const t = ta + ((tb - ta) * i) / n, a = [t, ...pnames.map((k) => vals[k])];
            let x, y; try { x = f.fx(...a); y = f.fy(...a); } catch { x = NaN; }
            if (isFinite(x) && isFinite(y)) { d += `${pen ? "L" : "M"}${X(x).toFixed(1)},${Y(y).toFixed(1)}`; pen = true; } else pen = false;
          }
          parts.push(`<path class="fn c${f.c}${f.dash ? " dash" : ""}${f.thin ? " thin" : ""}" d="${d}"/>`);
          continue;
        }
        const n = 600; let d = "", pen = false, prev = null;
        const [a, b] = f.domain ? f.domain.map((v) => (typeof v === "string" ? ev(v) : v)) : [x0, x1];
        for (let i = 0; i <= n; i++) {
          const x = a + ((b - a) * i) / n;
          let y; try { y = f.fn(...args(x)); } catch { y = NaN; }
          const ok = isFinite(y) && y > y0 - (y1 - y0) * 3 && y < y1 + (y1 - y0) * 3;
          if (ok && prev !== null && Math.abs(y - prev) > (y1 - y0) * 1.5) pen = false;
          if (ok) { d += `${pen ? "L" : "M"}${X(x).toFixed(1)},${Y(y).toFixed(1)}`; pen = true; prev = y; } else { pen = false; prev = null; }
        }
        parts.push(`<path class="fn c${f.c}${f.dash ? " dash" : ""}" d="${d}"/>`);
      }
      for (const v of cfg.vlines || []) { const o = typeof v === "object" ? v : { x: v }; const x = ev(o.x); parts.push(`<line class="vl c${o.color || 4}" x1="${X(x)}" x2="${X(x)}" y1="0" y2="${H}"/>`); if (o.label) parts.push(`<text class="lbl c${o.color || 4}" x="${X(x) + 4}" y="14">${esc(o.label)}</text>`); }
      for (const v of cfg.hlines || []) { const o = typeof v === "object" ? v : { y: v }; const y = ev(o.y); parts.push(`<line class="vl c${o.color || 4}" y1="${Y(y)}" y2="${Y(y)}" x1="0" x2="${W}"/>`); if (o.label) parts.push(`<text class="lbl c${o.color || 4}" x="${W - 4}" y="${Y(y) - 5}" text-anchor="end">${esc(o.label)}</text>`); }
      for (const c of cfg.circles || []) {
        if (c.show && !ev(c.show)) continue;
        const cx = ev(c.x), cy = ev(c.y), r = ev(c.r);
        parts.push(`<ellipse class="circ c${c.color || 4}${c.dash ? " dash" : ""}"${c.fill ? ` style="fill: var(--c${c.color || 4}s)"` : ""} cx="${X(cx)}" cy="${Y(cy)}" rx="${Math.abs(X(cx + r) - X(cx))}" ry="${Math.abs(Y(cy + r) - Y(cy))}"/>`);
      }
      for (const g of cfg.segs || []) {
        if (g.show && !ev(g.show)) continue;
        parts.push(`<line class="seg c${g.color || 4}${g.dash ? " dash" : ""}" x1="${X(ev(g.x1))}" y1="${Y(ev(g.y1))}" x2="${X(ev(g.x2))}" y2="${Y(ev(g.y2))}"/>`);
      }
      for (const a of cfg.arrows || []) {
        // стрелка-вектор из (x, y) длины (dx, dy) в единицах графика
        if (a.show && !ev(a.show)) continue;
        let xa, ya, dx, dy; try { xa = ev(a.x); ya = ev(a.y); dx = ev(a.dx); dy = ev(a.dy); } catch { continue; }
        const px = X(xa), py = Y(ya), qx = X(xa + dx), qy = Y(ya + dy), L = Math.hypot(qx - px, qy - py);
        if (!isFinite(L)) continue;
        const cls = `c${a.color || 2}`;
        if (L > 2) {
          const ang = Math.atan2(qy - py, qx - px), h = Math.min(11, L * 0.5);
          const bx = qx - h * 0.8 * Math.cos(ang), by = qy - h * 0.8 * Math.sin(ang);
          const h1 = [qx - h * Math.cos(ang - 0.4), qy - h * Math.sin(ang - 0.4)], h2 = [qx - h * Math.cos(ang + 0.4), qy - h * Math.sin(ang + 0.4)];
          parts.push(`<line class="vec ${cls}" x1="${px}" y1="${py}" x2="${bx}" y2="${by}"/><polygon class="head ${cls}" points="${qx},${qy} ${h1[0]},${h1[1]} ${h2[0]},${h2[1]}"/>`);
        }
        if (a.label) parts.push(`<text class="lbl ${cls}" x="${qx + (a.lx || 6)}" y="${qy + (a.ly || -6)}">${esc(a.label.replace(/\{(\w+)\}/g, (m, k) => (k in vals ? fmtNum(vals[k]) : m)))}</text>`);
      }
      for (const p of cfg.points || []) {
        let x, y; try { x = ev(p.x); y = ev(p.y); } catch { continue; }
        if (!isFinite(x) || !isFinite(y)) continue;
        if (p.show && !ev(p.show)) continue;
        parts.push(`<circle class="pt c${p.color || 2}${p.open ? " open" : ""}" cx="${X(x)}" cy="${Y(y)}" r="4.5"/>`);
        if (p.label) parts.push(`<text class="lbl c${p.color || 2}" x="${X(x) + 7}" y="${Y(y) - 7}">${esc(p.label.replace(/\{(\w+)\}/g, (m, k) => (k in vals ? fmtNum(vals[k]) : m)))}</text>`);
      }
      svg.innerHTML = parts.join("");
      for (const k of pnames) { const b = el.querySelector(`[data-v="${k}"]`); if (b) b.textContent = fmtNum(vals[k]); }
      if (cfg.out) {
        try { out.innerHTML = cfg.out.map((o) => `<span>${esc(o.label)}: <b>${esc(fmtOut(ev(o.expr), o))}</b></span>`).join(""); } catch { out.textContent = ""; }
      }
    }
    el.addEventListener("input", (e) => { const k = e.target.dataset.k; if (k) { vals[k] = +e.target.value; draw(); } });
    draw();
  }
  const fmtNum = (v) => (Math.abs(v - Math.round(v)) < 1e-9 ? String(Math.round(v)) : (+v.toFixed(2)).toString());
  function fmtOut(v, o) {
    if (o.map) return o.map[String(v)] ?? String(v);
    if (typeof v === "number") return isFinite(v) ? fmtNum(v) : "—";
    return String(v);
  }

  window.Study = { show, renderMarkdown, enhance, refreshBadge };
})();

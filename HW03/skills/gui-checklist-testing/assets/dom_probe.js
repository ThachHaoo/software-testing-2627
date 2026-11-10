// dom_probe.js — dán vào DevTools Console của từng trang (P3: chrome://inspect trên PC).
// Chỉ ĐỌC DOM, không sửa gì. In JSON dữ kiện cho người chạy checklist chấm; không tự kết luận Pass/Fail.
// Bước 3 của skill gui-checklist-testing: chép file này vào thư mục checklist, thêm probe riêng của phạm vi nếu cần.
(() => {
  const txt = (el) => (el?.innerText || el?.value || "").trim().replace(/\s+/g, " ").slice(0, 80);
  const box = (el) => { const r = el.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }; };
  const labelOf = (el) => {
    if (el.id) { const l = document.querySelector(`label[for="${CSS.escape(el.id)}"]`); if (l) return { text: txt(l), linked: true }; }
    const wrap = el.closest("label"); if (wrap) return { text: txt(wrap), linked: true };
    const prev = el.parentElement?.querySelector("label"); return prev ? { text: txt(prev), linked: false } : null;
  };
  const focusables = [...document.querySelectorAll("a[href], button, input, select, textarea, [tabindex]")]
    .filter((e) => !e.disabled && e.tabIndex >= 0 && e.offsetParent !== null);
  // thứ tự Tab theo quy tắc trình duyệt: tabindex > 0 tăng dần trước, sau đó tabindex = 0 theo thứ tự DOM
  const tabOrder = [...focusables.filter((e) => e.tabIndex > 0).sort((a, b) => a.tabIndex - b.tabIndex),
                    ...focusables.filter((e) => e.tabIndex === 0)]
    .map((e) => ({ tag: e.tagName.toLowerCase(), text: txt(e) || e.getAttribute("placeholder") || e.type, tabindex: e.tabIndex, y: box(e).y }));
  const fields = [...document.querySelectorAll("input, textarea, select")].map((e) => {
    const l = labelOf(e);
    return { tag: e.tagName.toLowerCase(), type: e.type, required: e.required, disabled: e.disabled,
             label: l?.text ?? null, label_linked: l?.linked ?? false, label_has_asterisk: !!l?.text?.includes("*"),
             placeholder: e.getAttribute("placeholder") };
  });
  const buttons = [...document.querySelectorAll("button, input[type=submit]")].map((b) => {
    const cs = getComputedStyle(b);
    return { text: txt(b), type: b.type, bg: cs.backgroundColor, color: cs.color, font: `${cs.fontFamily} ${cs.fontSize}`, ...box(b) };
  });
  const submit = document.querySelector("form button[type=submit], form input[type=submit]");
  const alerts = [...document.querySelectorAll('[role=alert], [class*="red-"], [class*="error"]')]
    .filter((e) => e.offsetParent !== null && txt(e))
    .map((e) => ({ text: txt(e), y: box(e).y, above_submit: submit ? box(e).y < box(submit).y : null }));
  const out = {
    url: location.href, ua: navigator.userAgent, viewport: `${innerWidth}x${innerHeight}`,
    title: document.title, lang: document.documentElement.lang,
    h1: [...document.querySelectorAll("h1")].map(txt), headings: [...document.querySelectorAll("h1,h2,h3")].map((h) => `${h.tagName}: ${txt(h)}`),
    horizontal_scroll: document.documentElement.scrollWidth > innerWidth,
    fields, buttons, tab_order: tabOrder, messages: alerts,
    nav_links: [...document.querySelectorAll("header a, nav a, header button")].map((a) => ({ text: txt(a), href: a.getAttribute("href"), aria_current: a.getAttribute("aria-current"), cls: a.className })),
    innerhtml_risk: [...document.querySelectorAll("header *")].filter((e) => e.children.length && /<[a-z]/i.test(e.textContent)).map(txt),
  };
  console.log(JSON.stringify(out, null, 2));
  return out;
})();

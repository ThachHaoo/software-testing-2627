#!/usr/bin/env python3
"""
Sinh bảng dữ kiện cấp bài (không theo feature) cho report chính HW02. Không dùng AI, không viết lời đánh giá.

Thay nội dung giữa marker <!-- REPORT:HW02:<khối>:START --> ... <!-- REPORT:HW02:<khối>:END -->:
  summary   : bảng của tools/summary.py
  allbugs   : mọi bugs/BUG-xx.md (chép nguyên văn ID, Tiêu đề, Severity, Priority, dòng "Fail", link issue)
  artifacts : danh mục artifact AI tạo cho AI Audit — cột (1) tool/thời gian/commit, (2) output, (5) commit sửa sau đó
  aiforms   : file trong ai-forms/ và trạng thái

In một lần (không có marker, để SV điền — chạy lại sẽ không ghi đè report):
  --print auditsv : khung bảng Verdict/Lý do cho từng artifact (`<SV viết>`)
  --print tceval  : bảng đánh giá từng TC origin AI/Both (trạng thái sửa theo freeze + git; cột Verdict `<SV viết>`)

Cách dùng (từ gốc repo):
  python tools/audit_tables.py HW02 --report HW02/23120255_HW02_Report.md
  python tools/audit_tables.py HW02 --print tceval
"""
import argparse
import datetime as dt
import glob
import json
import re
import subprocess
import sys
from pathlib import Path

FEATS = {"FR01": "A_FR01", "FR07": "B_FR07", "FR15": "C_FR15", "FR20": "D_FR20"}
DESIGN = ["title", "inputs", "expected_result", "covers", "ec_target", "bva_point", "rationale", "steps"]
TBD = "[#n: chờ chốt transcript]"
LOG = "appendix/A_prompt_log.md"
FEAT_NUM = {"A_FR01": 3, "B_FR07": 4, "C_FR15": 5, "D_FR20": 6}  # mục của feature trong report = tiền tố section trong notes


def turns_of(hw):
    """Lượt trong prompt log: [(n, giờ, model, section)] theo thứ tự xuất hiện (bỏ tiêu đề nằm trong khối output)."""
    out, fence = [], None
    for l in (hw / LOG).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(`{3,})", l)
        if m:
            fence = None if fence and m.group(1).startswith(fence) and l.strip() == m.group(1) else (fence or m.group(1))
            continue
        if fence:
            continue
        m = re.match(r"## #(\d+) \| (\d\d:\d\d \d\d/\d\d/\d{4}) \| ([^|]+) \| (.*)$", l)
        if m:
            out.append((int(m.group(1)), dt.datetime.strptime(m.group(2), "%H:%M %d/%m/%Y"), m.group(3).strip(), m.group(4).strip()))
    return out


def seckey(sec):
    """Khoá so section: mã "n.k" ở đầu nếu có (vd "4.1 B_FR07 Bước 1" và "4.1 B_FR07 Bước 1 – …" cùng khoá), không thì cả chuỗi."""
    m = re.match(r"\d+\.\d+", sec)
    return m.group(0) if m else sec


def nref(hw, h, want=None):
    """#n cho artifact tạo ở commit h: khối lượt liên tiếp cùng section (theo notes) có giờ ≤ giờ commit.
    want = mã section bắt buộc ("n.k") với bản đóng băng bước k; không có thì lấy section của lượt cuối trước commit."""
    if not h:
        return "[#n: không khớp – chưa có commit]"
    ts = dt.datetime.fromisoformat(git("log", "-1", "--format=%aI", h).strip()).replace(tzinfo=None, second=0)
    tl = [x for x in turns_of(hw) if x[1] <= ts]
    if not tl:
        return "[#n: không khớp – không có lượt nào trước commit]"
    if want:
        cand = [i for i, x in enumerate(tl) if seckey(x[3]) == want]
        if not cand:
            return f"[#n: không khớp – notes không có lượt section {want} trước commit (lượt #{tl[-1][0]} ngay trước commit thuộc \"{tl[-1][3]}\")]"
        end = cand[-1]
    else:
        end = len(tl) - 1
    key = seckey(tl[end][3])
    if key in ("", "[...]"):
        return f"[#n: không khớp – lượt #{tl[end][0]} trước commit chưa có section trong notes]"
    i = end
    while i > 0 and seckey(tl[i - 1][3]) == key:
        i -= 1
    blk = tl[i:end + 1]
    models = sorted({m for x in blk for m in x[2].split(" + ")})
    a, b = blk[0], blk[-1]
    return f"#{a[0]}–#{b[0]} ({a[1]:%H:%M %d/%m} – {b[1]:%H:%M %d/%m}; {', '.join(models)}; section \"{a[3]}\")"


# Danh mục artifact ngoài bản đóng băng: (mã, tên, đường dẫn trong repo, ghi chú). Bản đóng băng bước 1–4 sinh tự động.
EXTRA = [
    ("H1", "Harness: CLAUDE.md", ["CLAUDE.md"], ""),
    ("H2", "Agent Skill `domain-bva-testing` (SKILL.md, references, scripts freeze/check_domain/render_md/merge_results…)", [".claude/skills/domain-bva-testing"], ""),
    ("H3", "Hook Stop + script trích prompt log", [".claude/settings.json", "tools/hooks/on_stop.py", "tools/extract_prompt_log.py", "tools/hw.toml"], ""),
    ("H4", "Script tổng hợp số liệu `summary.py`", ["tools/summary.py"], ""),
    ("H5", "Script xuất commit log", ["tools/export_commit_log.ps1"], ""),
    ("H6", "Script nén ảnh chạy tay", ["tools/compress_manual.py"], ""),
    ("H7", "Script sinh bảng report `report_tables.py`, `audit_tables.py`", ["tools/report_tables.py", "tools/audit_tables.py"], ""),
    ("T1", "Playwright: cấu hình chung, global-setup, README", ["HW02/tests/playwright.config.ts", "HW02/tests/global-setup.ts", "HW02/tests/README.md"], ""),
    ("T2", "Playwright A_FR01", ["HW02/tests/A_FR01"], ""),
    ("T3", "Playwright B_FR07", ["HW02/tests/B_FR07"], ""),
    ("T4", "Playwright C_FR15", ["HW02/tests/C_FR15"], ""),
    ("R1", "RUN.md B_FR07", ["HW02/B_FR07/RUN.md"], ""),
    ("R2", "RUN.md C_FR15", ["HW02/C_FR15/RUN.md"], ""),
    ("R3", "RUN.md D_FR20 (chạy tay) + mẫu file lượt", ["HW02/D_FR20/RUN.md", "HW02/D_FR20/results/D_FR20_manual_TEMPLATE.json"], ""),
    ("N1", "Ghi chú bước 1 B_FR07", ["HW02/B_FR07/notes_step1.md"], ""),
    ("N2", "Ghi chú bước 1 D_FR20", ["HW02/D_FR20/step1_notes.md"], ""),
    ("G1", "Câu trả lời gap analysis của AI – A_FR01", ["HW02/A_FR01/ai_gap_answer.md"], ""),
    ("G2", "Câu trả lời gap analysis của AI – B_FR07", ["HW02/B_FR07/ai_gap_answer.md"], ""),
    ("G3", "Câu trả lời gap analysis của AI – C_FR15", ["HW02/C_FR15/ai_gap_answer.md"], ""),
    ("G4", "Câu trả lời gap analysis của AI – D_FR20", ["HW02/D_FR20/ai_gap_answer.md"], ""),
    ("G5", "Khung trống `sv_cases.md` (AI tạo khung, nội dung SV viết; commit chung với nội dung SV)", ["HW02/C_FR15/sv_cases.md"], "Feature khác: [...]"),
    ("Q1", "Câu hỏi/trả lời bước 5 (`sv_questions.md`) B_FR07", ["HW02/B_FR07/sv_questions.md"], ""),
    ("Q2", "Câu hỏi/trả lời bước 5 (`sv_questions.md`) C_FR15", ["HW02/C_FR15/sv_questions.md"], ""),
    ("BG1", "Dữ kiện bug `_groups` A_FR01", ["HW02/bugs/_groups_A_FR01.md"], ""),
    ("BG2", "Dữ kiện bug `_groups` B_FR07", ["HW02/bugs/_groups_B_FR07.md"], ""),
    ("BG3", "Dữ kiện bug `_groups` C_FR15 + script tái hiện", ["HW02/bugs/_groups_C_FR15.md", "HW02/bugs/_repro_C_FR15"], ""),
    ("BG4", "Dữ kiện bug `_groups` D_FR20 + bảng web ↔ mobile", ["HW02/bugs/_groups_D_FR20.md", "HW02/D_FR20/compare_web_mobile.md"], ""),
    ("BG5", "Quy ước bug (`bugs/README.md`), nhật ký đính chính A", ["HW02/bugs/README.md", "HW02/bugs/_edit_log_A.md"], ""),
    ("BG6", "Khung BUG-xx (trống, chỉ dữ kiện) và sửa dữ kiện theo evidence (7/7a, 7/7c)", [], "commits:7/7a|7/7c|7/7d3"),
    ("BG7", "Bản che ảnh để đăng issue", ["HW02/bugs/_issue_redacted"], ""),
    ("BG8", "Tạo GitHub Issues bằng `gh issue create` (nội dung SV viết) + ảnh trang Issues", [], "commits:Issues|issue"),
    ("E1", "Môi trường + patch API_URL mobile", ["HW02/env/environment.md", "HW02/env/mobile_api_url.patch"], ""),
    ("P1", "Kế hoạch nộp bài `report_plan.md`", ["HW02/report_plan.md"], ""),
    ("P2", "Khung report + bảng dữ kiện + 21 khối giải thích từng bước do AI nháp (§2, x.1–x.4, x.6) + các mục chung", ["HW02/23120255_HW02_Report.md"], ""),
    ("P3", "README HW02 (bảng tự đánh giá trống, khối SUMMARY)", ["HW02/README.md"], ""),
    ("P4", "File lượt chạy tay D (AI chép nguyên văn từ `Check.md` của SV)", ["HW02/D_FR20/results/D_FR20_manual_20261021-001500.json"], ""),
    ("F1", "Biểu mẫu AI-02/03/05 (.md)", ["HW02/ai-forms"], "chưa làm"),
]


def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout if r.returncode == 0 else ""


def cell(s):
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def table(head, rows):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] +
                     ["| " + " | ".join(cell(x) for x in r) + " |" for r in rows])


def model_of(h):
    m = re.search(r"Co-Authored-By: (Claude [^<]+?)\s*<", git("log", "-1", "--format=%B", h))
    return m.group(1).strip() if m else "(commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3)"


def commits(paths):
    out = git("log", "--reverse", "--format=%h|%ad|%s", "--date=format:%d/%m/%Y %H:%M", "--", *paths)
    return [l.split("|", 2) for l in out.splitlines() if l]


def excerpt(path):
    p = Path(path)
    if p.is_dir():
        files = sorted(x.as_posix() for x in p.rglob("*") if x.is_file() and "node_modules" not in x.parts)
        return f"{len(files)} file: " + ", ".join(Path(f).name for f in files[:6]) + (" …" if len(files) > 6 else "")
    if not p.exists():
        return "(không có file)"
    if p.suffix == ".json":
        return f"JSON {p.stat().st_size // 1024} KB"
    for l in p.read_text(encoding="utf-8", errors="replace").splitlines():
        s = l.strip().lstrip("#").strip()
        if s and not s.startswith(("```", "<!--", "import", "\"\"\"", "!", "//")):
            return s[:90] + ("…" if len(s) > 90 else "")
    return ""


# ---------- khối ----------

def b_summary(hw):
    return subprocess.run([sys.executable, "tools/summary.py", str(hw)], capture_output=True, text=True,
                          encoding="utf-8").stdout.strip() + f"\n\n*Nguồn: `python tools/summary.py {hw.name}`.*"


def parse_bug(t):
    f = lambda k: (re.search(rf"\*\*{k}:\*\*\s*(.+)", t) or [None, ""])[1].strip()
    tc = re.search(r"## TC liên quan\s*\n(.*?)(?:\n## |\Z)", t, re.S)
    lines = tc.group(1).splitlines() if tc else []
    fail = next((l[2:].strip() for l in lines if l.startswith("- Fail")), "")
    sec = re.search(r"## Link GitHub Issue\s*\n+(.*)", t)
    link = re.search(r"https?://[^\s)\]]+", sec.group(1)) if sec else None
    tcs = re.findall(r"TC-(FR\d\d)-\d+", tc.group(1) if tc else "")
    return f("ID"), fail, f("Tiêu đề"), f("Severity"), f("Priority"), link.group(0) if link else "", tcs


def b_allbugs(hw):
    rows = []
    for p in sorted((hw / "bugs").glob("BUG-*.md"), key=lambda x: int(x.stem[4:])):
        bid, fail, title, sev, pri, link, tcs = parse_bug(p.read_text(encoding="utf-8"))
        feat = ", ".join(dict.fromkeys(FEATS.get(x, x) for x in tcs))
        num = re.search(r"/issues/(\d+)", link)
        rows.append((f"[{bid}](bugs/{p.name})", feat, fail, title, sev, pri, f"[#{num.group(1)}]({link})" if num else link))
    return table(["Bug ID", "Feature", "TC liên quan (dòng \"Fail\")", "Tiêu đề", "Severity", "Priority", "GitHub Issue"], rows) + \
        f"\n\n*(AI chép) nguyên văn từ {len(rows)} file `bugs/BUG-xx.md`; Feature suy từ mã TC trong mục \"TC liên quan\". Mô tả bug do em viết.*"


def diff_summary(fz, hd, st):
    """Đếm phần tử khác giữa bản AI đóng băng và bản HEAD (chỉ phần mà bước đó tạo ra)."""
    key = lambda l: {x["id"]: x for x in l}
    items = [("biến", key(fz.get("domain", {}).get("variables", [])), key(hd["domain"]["variables"]))]
    if st >= 2:
        items.append(("lớp", key(fz.get("domain", {}).get("partitions", [])), key(hd["domain"]["partitions"])))
    if st >= 3:
        pick = lambda c: {f: c.get(f) for f in DESIGN}
        items.append(("TC (trường thiết kế)", {c["id"]: pick(c) for s in fz.get("suites", []) for c in s["cases"]},
                      {c["id"]: pick(c) for s in hd["suites"] for c in s["cases"]}))
    out = []
    for name, a, b in items:
        ch = sum(1 for k in a if k in b and a[k] != b[k])
        rm = sum(1 for k in a if k not in b)
        add = sum(1 for k in b if k not in a)
        out.append(f"{name}: {ch} đổi, {rm} bỏ" + (f", {add} thêm" if not name.startswith("TC") else ""))
    return "; ".join(out) + "."


def all_commits():
    """[(hash, giờ địa phương không tz, theo phút, subject)] theo thời gian tăng dần."""
    out = []
    for l in git("log", "--reverse", "--format=%h|%aI|%s").splitlines():
        h, ts, s = l.split("|", 2)
        out.append((h, dt.datetime.fromisoformat(ts).replace(tzinfo=None, second=0), s))
    return out


def fmt_turns(blk, extra=""):
    models = sorted({m for x in blk for m in x[2].split(" + ")})
    secs = list(dict.fromkeys(x[3] for x in blk))
    a, b = blk[0], blk[-1]
    return (f"#{a[0]}–#{b[0]} ({a[1]:%H:%M %d/%m} – {b[1]:%H:%M %d/%m}; {', '.join(models)}; "
            f"section trong notes: {' / '.join(f'“{s}”' for s in secs)}{extra})")


_SRC = None


def turn_sources(hw):
    """#n → (nguồn, prompt): dựng lại danh sách lượt y như tools/extract_prompt_log.py (cùng thứ tự, cùng cách bỏ trùng),
    nguồn = 'code' (transcript Claude Code), 'claude-ai' (file claude-ai_session_*), 'extra' (prompt_log_extra.toml).
    Cần thư mục transcript cục bộ (gitignore); không khớp số lượt/giờ với prompt log → trả {}."""
    global _SRC
    if _SRC is not None:
        return _SRC
    import importlib.util, tomllib
    cfg = tomllib.loads(Path("tools/hw.toml").read_text(encoding="utf-8"))
    spec = importlib.util.spec_from_file_location("epl", "tools/extract_prompt_log.py")
    epl = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(epl)
    turns = []
    for p in sorted(Path(cfg["transcripts"]).glob("*.jsonl")):
        for t in epl.load_session(p):
            t["src"] = "claude-ai" if p.name.startswith("claude-ai_session") else "code"
            turns.append(t)
    for e in epl.load_toml(cfg.get("extra")).get("entry", []):
        turns.append({"time": dt.datetime.fromisoformat(e["time"]).replace(tzinfo=epl.LOCAL_TZ), "prompt": e["prompt"].strip(),
                      "output": [e["output"].strip()], "src": "extra"})
    uniq = {}
    for t in turns:
        k = (t["time"], t["prompt"])
        if k not in uniq or len("".join(t["output"])) > len("".join(uniq[k]["output"])):
            uniq[k] = t
    turns = sorted(uniq.values(), key=lambda t: t["time"])
    if cfg.get("since"):
        turns = [t for t in turns if t["time"].date() >= dt.date.fromisoformat(cfg["since"])]
    log = turns_of(hw)
    if len(turns) != len(log) or any(t["time"].replace(tzinfo=None, second=0, microsecond=0) != x[1] for t, x in zip(turns, log)):
        _SRC = {}
    else:
        _SRC = {x[0]: (t["src"], t["prompt"]) for t, x in zip(turns, log)}
    return _SRC


STEP_WORDS = re.compile(r"bước|Bước|\d/7|step", re.I)


def step_excerpt(prompt, n=15):
    """≤ n từ nguyên văn: dòng đầu tiên của prompt có nhắc bước (bước / k/7 / step), không có thì dòng đầu."""
    lines = [l.strip() for l in prompt.splitlines() if l.strip()]
    line = next((l for l in lines if STEP_WORDS.search(l)), lines[0] if lines else "")
    w = line.split()
    return " ".join(w[:n]) + (" …" if len(w) > n else "")


def turns_between(hw, t0, t1):
    """Lượt có giờ > t0 và ≤ t1 (t0 None = từ đầu); rỗng thì nới thành ≥ t0 (lượt cùng phút với commit trước).
    Vẫn rỗng (một lượt AI tạo nhiều commit liên tiếp) → lượt Claude Code đang chạy lúc commit: lượt cuối có giờ ≤ commit
    lấy từ transcript Claude Code (commit chỉ do Claude Code tạo), kèm trích prompt ≤ 15 từ."""
    tl = turns_of(hw)
    blk = [x for x in tl if (t0 is None or x[1] > t0) and x[1] <= t1]
    blk = blk or [x for x in tl if (t0 is None or x[1] >= t0) and x[1] <= t1]
    if not blk:
        src = turn_sources(hw)
        before = [x for x in tl if x[1] <= t1 and src.get(x[0], ("?",))[0] == "code"]
        if before:
            x = before[-1]
            steps = list(dict.fromkeys(re.findall(r"[Bb]ước \d|\b\d/7[a-z]?\d?\b", src[x[0]][1])))
            blk = [(*x[:3], x[3] + f" [lượt Claude Code đang chạy lúc commit; prompt: “{step_excerpt(src[x[0]][1])}”; "
                                   f"bước nhắc trong prompt: {', '.join(steps) or 'không có'}]")]
    return blk


def nref_git(hw, feat, st, h):
    """Bản đóng băng bước k của feature: lượt sau commit cuối của bước k−1 (hoặc commit trước đó trong repo) tới commit bước k."""
    cs = all_commits()
    idx = next((i for i, c in enumerate(cs) if c[0] == h), None)
    if idx is None:
        return "[#n: không khớp – không thấy commit]"
    tag = f"HW02[{feat[0]}-{feat[2:]}]"
    prev = [c for c in cs[:idx] if c[2].startswith(f"{tag} {st - 1}/7")] if st > 1 else []
    t0 = prev[-1][1] if prev else (cs[idx - 1][1] if idx else None)
    blk = turns_between(hw, t0, cs[idx][1])
    return fmt_turns(blk, "; khớp theo: git") if blk else "[#n: không khớp – không có lượt giữa hai commit]"


def nref_multi(hw, hashes):
    """Artifact gồm nhiều commit: mỗi commit lấy lượt giữa commit trước đó trong repo và commit này; gộp theo feature."""
    cs = all_commits()
    pos = {c[0]: i for i, c in enumerate(cs)}
    by = {}
    for h in hashes:
        i = pos.get(h)
        if i is None:
            continue
        m = re.match(r"HW02\[([A-D])-FR(\d\d)\]", cs[i][2])
        key = f"{m.group(1)}_FR{m.group(2)}" if m else "chung"
        by.setdefault(key, []).extend(turns_between(hw, cs[i - 1][1] if i else None, cs[i][1]))
    parts = []
    for k, blk in by.items():
        blk = sorted(dict.fromkeys(blk), key=lambda x: (x[1], x[0]))
        parts.append(f"{k}: " + (fmt_turns(blk, "; khớp theo: git") if blk else "(không có lượt nào giữa các commit này và commit trước)"))
    return " · ".join(parts) or "[#n: không khớp – không có lượt]"


def freeze_rows(hw):
    final = {f: json.load(open(hw / f / "testcases.json", encoding="utf-8")) for f in FEATS.values()}
    groups = {}
    for f in sorted(glob.glob(str(hw / "appendix" / "ai-outputs" / "*_step*_*"))):
        m = re.search(r"([A-D]_FR\d\d)_step(\d+)_(\d{8})-(\d{4,6})", f)
        if m:
            groups.setdefault((m.group(1), int(m.group(2))), []).append(Path(f).name)
    rows = []
    for (feat, st), files in sorted(groups.items()):
        code = feat[0]
        subj = f"HW02[{code}-{feat[2:]}] {st}/7"
        cs = [c for c in commits([f"{hw.name}/{feat}/testcases.json"]) if c[2].startswith(subj)]
        first = cs[0] if cs else None
        js = sorted(x for x in files if x.endswith(".json"))
        d = json.load(open(hw / "appendix" / "ai-outputs" / js[-1], encoding="utf-8")) if js else {}
        dom = d.get("domain", {})
        parts = [f"{len(dom.get('variables', []))} biến"] + ([f"{len(dom['partitions'])} lớp"] if dom.get("partitions") else []) + \
                [f"{s['id']} {len(s['cases'])}" for s in d.get("suites", [])]
        out = ", ".join(parts) + f" · `appendix/ai-outputs/{feat}_step{st}_*` ({len(js)} lần đóng băng)"
        later = ("Commit cùng bước sau commit đầu: " + "; ".join(f"`{c[0]}` {c[2]}" for c in cs[1:]) + ". ") if cs[1:] else ""
        later += "Bản cuối (HEAD) so với bản đóng băng cuối của bước — " + diff_summary(d, final[feat], st)
        rows.append((f"{code}{st}", f"{feat} – bước {st} ({['', 'biến vào/ra', 'lớp tương đương', 'TC Domain', 'TC BVA', '', '', ''][st] or 'thủ tục chạy'})",
                     f"{model_of(first[0]) if first else '?'} · {first[1] if first else '?'} · `{first[0] if first else '?'}` · {nref_git(hw, feat, st, first[0]) if first else '[#n: không khớp – không có commit của bước]'}",
                     out, later))
    return rows


def extra_rows(hw):
    rows = []
    for code, name, paths, note in EXTRA:
        if note.startswith("commits:"):
            pat = re.compile(note.split(":", 1)[1])
            cs = [l.split("|", 2) for l in git("log", "--reverse", "--format=%h|%ad|%s", "--date=format:%d/%m/%Y %H:%M").splitlines()
                  if l and pat.search(l.split("|", 2)[2]) and "HW02[" in l]
            first = cs[0] if cs else None
            out = f"{len(cs)} commit: " + ", ".join(f"`{c[0]}`" for c in cs[:8]) + (" …" if len(cs) > 8 else "")
            rows.append((code, name, f"{model_of(first[0]) if first else '?'} · {first[1] if first else '?'} · `{first[0] if first else '?'}` · {nref_multi(hw, [c[0] for c in cs])}",
                         out, "—"))
            continue
        existing = [p for p in paths if Path(p).exists()]
        cs = commits(existing) if existing else []
        if not cs:
            rows.append((code, name, "— · [#n: không khớp – chưa có file/commit]", note or "(chưa có)", "—"))
            continue
        first = cs[0]
        if note == "chưa làm":
            rows.append((code, name, "— · [#n: form chưa làm]", note, "—"))
            continue
        out = "; ".join(f"`{p}`" + (f" — “{excerpt(p)}”" if excerpt(p) else "") for p in existing) + (f" · {note}" if note else "")
        sv = [c for c in cs[1:] if re.search(r"\bSV\b", c[2])]
        later = (f"{len(cs) - 1} commit sau; có chữ \"SV\": " + ("; ".join(f"`{c[0]}` {c[2]}" for c in sv) if sv else "không")) if len(cs) > 1 else "không có commit sau"
        rows.append((code, name, f"{model_of(first[0])} · {first[1]} · `{first[0]}` · {nref(hw, first[0])}", out, later))
    return rows


def b_artifacts(hw):
    rows = freeze_rows(hw) + extra_rows(hw)
    tl = turns_of(hw)
    when = dt.datetime.fromtimestamp((hw / LOG).stat().st_mtime)
    head = (f"*#n theo bản trích {when:%H:%M %d/%m/%Y} ({len(tl)} lượt trong `{LOG}`); số có thể đổi ở lần trích cuối trước khi nộp. "
            "Cách khớp: khối lượt liên tiếp cùng section trong `prompt_log_notes.toml`, giờ ≤ giờ commit tạo artifact; "
            "riêng bản đóng băng bước k và artifact nhiều commit khớp theo git (ghi \"khớp theo: git\"): lượt sau commit cuối của bước k−1 "
            "(hoặc commit trước đó) tới commit bước k — không có lượt nào trong khoảng đó (một lượt tạo nhiều commit) thì lấy lượt đang chạy lúc commit; "
            "section hiện nhãn đang có trong notes.*\n\n")
    return head + table(["Mã", "Artifact", "(1) Tool · thời gian · commit tạo · #n", "(2) Output (trích + đường dẫn)",
                  "(5) Commit sửa sau đó (git log)"], rows) + \
        f"\n\n*{len(rows)} artifact. Sinh bằng `tools/audit_tables.py` từ `appendix/ai-outputs/`, `git log` (trailer Co-Authored-By cho tool), danh mục ở đầu script. " \
        "Cột (5) chỉ liệt kê commit, không diễn giải lý do. Cột (3) Verdict, (4) Lý do ở bảng ngay dưới (em viết).*"


def b_auditsv(hw):
    rows = [(r[0], r[1], "`<SV viết>`", "`<SV viết>`") for r in freeze_rows(hw) + extra_rows(hw)]
    return table(["Mã", "Artifact", "(3) Verdict (VALID / INVALID / INCOMPLETE)", "(4) Lý do (dẫn ISTQB/slide)"], rows)


def b_aiforms(hw):
    want = ["AI-02_Audit_Report_23120255", "AI-03_Disclosure_Form_23120255", "AI-05_Privacy_Checklist_23120255"]
    rows = []
    for w in want:
        for ext in (".md", ".pdf"):
            p = hw / "ai-forms" / f"{w}{ext}"
            rows.append((w[:5], f"`ai-forms/{w}{ext}`", "ĐÃ CÓ" if p.exists() else "THIẾU"))
    other = [p.name for p in (hw / "ai-forms").glob("*") if not any(p.name.startswith(w) for w in want)]
    return table(["Mã", "File", "Trạng thái"], rows) + \
        f"\n\n*Kiểm bằng script lúc sinh report. File khác trong `ai-forms/`: {', '.join(other) or 'không có'}.*"


REPORT = "23120255_HW02_Report.md"
# Quyết định SV 21/10 (V1, V2) cho 10.3 — chép nguyên văn câu lý do SV chốt
V1 = ("VALID", "đã đủ tốt ở các case AI tìm ra")
V2 = ("INCOMPLETE", "hiểu nhầm context nên phải chỉnh sửa")


def tc_states(hw):
    """[(TC, suite, origin, trạng thái sửa, giữ nguyên?)] cho mọi TC origin AI/Both."""
    return [(r[0], r[1], r[2], r[3], r[3].startswith("giữ nguyên")) for r in _tceval_rows(hw)]


def b_tc103(hw):
    st = tc_states(hw)
    by = {}
    for tc, suite, og, state, keep in st:
        if keep:
            key = (FEATS[re.search(r"FR\d\d", tc).group(0)], suite)
            by[key] = by.get(key, 0) + 1
    a = table(["Feature", "Suite", "Số TC giữ nguyên bản AI", "Verdict", "Lý do"], [(f, s, n, V1[0], V1[1]) for (f, s), n in by.items()])
    ch = [(tc, state, V2[0], V2[1]) for tc, suite, og, state, keep in st if not keep]
    b = table(["TC", "Thay đổi (git)", "Verdict", "Lý do"], ch)
    return (f"**Bảng A – TC giữ nguyên bản AI (gộp theo suite)**\n\n{a}\n\n"
            f"**Bảng B – TC khác bản AI hoặc không có trong bản đóng băng**\n\n{b}\n\n"
            f"*{len(st)} TC có `origin` AI/Both: {sum(x[4] for x in st)} giữ nguyên, {sum(not x[4] for x in st)} khác/không có trong bản đóng băng. "
            "Verdict và lý do theo quyết định của em (V1, V2, 21/10), áp theo trạng thái sửa trong git. "
            "Bản đánh giá từng TC trước đó: `appendix/audit_103_sv_old.md`.*")


def verdicts_102(hw):
    """[(mã, artifact, verdict)] từ bảng 10.2 trong report (em viết), theo thứ tự hàng."""
    t = (hw / REPORT).read_text(encoding="utf-8")
    s = t[t.index("### 10.2"):t.index("### 10.3")]
    out = []
    for l in s.splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 4 and re.match(r"[A-Z]\d+$", c[0]):
            out.append((c[0], c[1], c[2], c[3]))
    return out


def b_audit104(hw):
    v = [x for x in verdicts_102(hw) if x[0] != "F1"]
    st = tc_states(hw)
    tcv = [V1[0] if x[4] else V2[0] for x in st]
    def row(name, vs):
        n = len(vs)
        cnt = {k: sum(1 for x in vs if x.upper().startswith(k)) for k in ("VALID", "INVALID", "INCOMPLETE")}
        other = n - sum(cnt.values())
        pct = lambda k: f"{cnt[k]} ({cnt[k] / n:.1%})" if n else "0"
        return (name, pct("VALID"), pct("INVALID"), pct("INCOMPLETE"), f"{n}" + (f" (khác: {other})" if other else ""))
    return table(["", "VALID", "INVALID", "INCOMPLETE", "Tổng"],
                 [row("Artifact (cột (3) ở 10.2, không tính F1)", [x[2] for x in v]),
                  row("TC do AI sinh (theo số TC ở 10.3)", tcv)]) + \
        "\n\n*Tỉ lệ = số verdict loại đó / tổng hàng (hoặc tổng TC). Đếm bằng script từ cột Verdict ở 10.2 và trạng thái TC ở 10.3.*"


def b_auditcheck(hw):
    """Hàng 10.2 có Lý do có thể mâu thuẫn với dữ kiện ở 10.1 (chỉ liệt kê, không kết luận)."""
    arts = freeze_rows(hw) + extra_rows(hw)
    v = verdicts_102(hw)
    feats = {f: json.load(open(hw / f / "testcases.json", encoding="utf-8")) for f in FEATS.values()}
    ids = {}
    for f, d in feats.items():
        s = {x["id"] for x in d["domain"]["variables"]} | {x["id"] for x in d["domain"]["partitions"]}
        s |= {re.match(r"([A-Z]\d+[a-z]?)", a).group(1) for a in d["meta"]["assumptions"] if re.match(r"[A-Z]\d", a)}
        s |= {c["id"] for x in d["suites"] for c in x["cases"]} | {c["id"].split("-")[-1] for x in d["suites"] for c in x["cases"]}
        ids[f] = s
    out = ["# Đối chiếu Lý do ở 10.2 với dữ kiện ở 10.1 (chỉ liệt kê)", "",
           "> AI sinh bằng `python tools/audit_tables.py HW02 --print auditcheck`. Hàng 10.2 và 10.1 ghép theo thứ tự hàng. Không sửa Lý do của em.", ""]
    rows = []
    for i, (code, name, verdict, why) in enumerate(v):
        if i >= len(arts):
            break
        a = arts[i]
        data = f"{a[3]} {a[4]}"
        issues = []
        why_n = re.sub(r"(?i)bước\s*\d+", "", why)  # số bước (vd "bước 5") không phải số liệu
        nums = [n for n in re.findall(r"(?<![\w.#/-])(\d+)(?![\w.:/])", why_n) if n not in re.findall(r"\d+", data)]
        if nums:
            issues.append(f"số trong Lý do không có ở cột (2)/(5): {', '.join(dict.fromkeys(nums))}")
        if re.search(r"\bSV\b", why) and not re.search(r"\bSV\b", a[4]) and "Commit cùng bước" not in a[4]:
            issues.append("Lý do nói SV làm/sửa nhưng cột (5) không có commit ghi \"SV\"")
        feat = next((f for f in FEATS.values() if a[1].startswith(f)), None)
        if feat:
            toks = re.findall(r"\b(?:EC\d+|V\d+|[A-D]\d+[a-z]?|TC-\d+)\b", why)
            miss = [x for x in toks if x.replace("TC-", "") not in ids[feat] and x not in ids[feat]]
            if miss:
                issues.append(f"mã không có trong `{feat}/testcases.json`: {', '.join(dict.fromkeys(miss))}")
        if issues:
            rows.append((code, name, why, a[4], "; ".join(issues)))
    out.append(table(["Mã", "Artifact", "Lý do (10.2, nguyên văn)", "Cột (5) ở 10.1", "Điểm cần xem"], rows) if rows else "Không có hàng nào.")
    out.append("")
    out.append(f"*{len(rows)} hàng.*")
    return "\n".join(out)


def b_tceval(hw):
    rows = _tceval_rows(hw)
    return table(["TC", "Suite", "Nguồn", "Trạng thái sửa (so bản AI đóng băng cuối chứa TC; git)", "Verdict"], rows) + \
        f"\n\n*{len(rows)} TC có `origin` AI hoặc Both. Bản AI đóng băng cuối của một bước có thể đã gồm các vòng AI sửa theo review (B, C, D có nhiều lần đóng băng mỗi bước). Sinh một lần bằng `python tools/audit_tables.py {hw.name} --print tceval`; không chạy lại sau khi em điền cột Verdict.*"


def _tceval_rows(hw):
    rows = []
    for feat in FEATS.values():
        d = json.load(open(hw / feat / "testcases.json", encoding="utf-8"))
        frz = []
        for f in sorted(glob.glob(str(hw / "appendix" / "ai-outputs" / f"{feat}_step*.json"))):
            m = re.search(r"_step(\d+)_(\d{8})-(\d{4})(\d{2})?", f)
            when = dt.datetime.strptime(m.group(2) + m.group(3) + (m.group(4) or "00"), "%Y%m%d%H%M%S")
            o = json.load(open(f, encoding="utf-8"))
            frz.append((when, Path(f).name, {c["id"]: c for s in o.get("suites", []) for c in s["cases"]}))
        path = f"{hw.name}/{feat}/testcases.json"
        hist = []
        for h, ts in (l.split("|") for l in git("log", "--reverse", "--format=%h|%cI", "--", path).splitlines()):
            try:
                hist.append((dt.datetime.fromisoformat(ts).replace(tzinfo=None), h,
                             {c["id"]: c for s in json.loads(git("show", f"{h}:{path}"))["suites"] for c in s["cases"]}))
            except Exception:
                pass
        for s in d["suites"]:
            for c in s["cases"]:
                if c.get("origin") not in ("AI", "Both"):
                    continue
                last = [(w, n, cs[c["id"]]) for w, n, cs in frz if c["id"] in cs]
                if not last:
                    state = "không có trong bản AI đóng băng"
                else:
                    w, n, base = last[-1]
                    diff = [k for k in DESIGN if base.get(k) != c.get(k)]
                    if not diff:
                        state = f"giữ nguyên bản AI `{n}`"
                    else:
                        ch = next((h for t, h, cs in hist if t > w and c["id"] in cs and any(cs[c["id"]].get(k) != base.get(k) for k in DESIGN)), "?")
                        state = f"khác bản AI `{n}` ở {', '.join(diff)}; commit đầu tiên khác: `{ch}`"
                rows.append((c["id"], s["id"], c.get("origin"), state, "`<SV viết>`"))
    return rows


def b_tree(hw):
    """Cây thư mục của HW02 theo `git ls-files` (= nội dung `git archive HEAD HW02`), gộp thư mục sâu, đếm file."""
    files = [f for f in git("ls-files", hw.name).splitlines() if f]
    tree = {}
    for f in files:
        parts = f.split("/")[1:]
        key = tuple(parts[:2]) if len(parts) > 2 else tuple(parts)
        tree.setdefault(key[0], {}).setdefault("/".join(key[1:]) if len(key) > 1 else "", []).append(f)
    lines = [f"{hw.name}/"]
    tops = sorted(tree, key=lambda k: (bool(tree[k].get("") and len(tree[k]) == 1), k))
    for i, top in enumerate(tops):
        last = i == len(tops) - 1
        subs = tree[top]
        if list(subs) == [""]:
            lines.append(("└── " if last else "├── ") + top)
            continue
        n = sum(len(v) for v in subs.values())
        lines.append(("└── " if last else "├── ") + f"{top}/  ({n} file)")
        names = sorted(k for k in subs if k)
        shown = [k for k in names if len(subs[k]) > 1 or "/" not in k]
        for j, k in enumerate(shown[:12]):
            cnt = len(subs[k])
            lines.append(("    " if last else "│   ") + ("└── " if j == min(len(shown), 12) - 1 else "├── ") +
                         (f"{k}/  ({cnt} file)" if cnt > 1 or k.count("/") else k))
        if len(shown) > 12:
            lines.append(("    " if last else "│   ") + f"    … (+{len(shown) - 12})")
    return "```\n" + "\n".join(lines) + "\n```\n\n" + \
        f"*{len(files)} file đang commit trong `{hw.name}/` (sinh từ `git ls-files {hw.name}`, đúng nội dung `git archive HEAD {hw.name}`).*"


BLOCKS = {"summary": b_summary, "allbugs": b_allbugs, "artifacts": b_artifacts, "aiforms": b_aiforms, "tree": b_tree,
          "tc103": b_tc103, "audit104": b_audit104}
ONCE = {"auditsv": b_auditsv, "tceval": b_tceval, "auditcheck": b_auditcheck}


def main():
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser()
    ap.add_argument("hw")
    ap.add_argument("--report")
    ap.add_argument("--print", dest="show", choices=list(BLOCKS) + list(ONCE))
    a = ap.parse_args()
    hw = Path(a.hw)
    if a.show:
        print({**BLOCKS, **ONCE}[a.show](hw))
        return
    if not a.report:
        sys.exit("Cần --report hoặc --print")
    p = Path(a.report)
    txt, n = p.read_text(encoding="utf-8"), 0
    for name, fn in BLOCKS.items():
        pat = re.compile(rf"(<!-- REPORT:{hw.name}:{name}:START -->\n)(?:.*?\n)?(<!-- REPORT:{hw.name}:{name}:END -->)", re.S)
        if pat.search(txt):
            body = fn(hw)
            txt = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), txt)
            n += 1
    p.write_text(txt, encoding="utf-8")
    print(f"Đã cập nhật {n} khối cấp bài trong {p}")


if __name__ == "__main__":
    main()

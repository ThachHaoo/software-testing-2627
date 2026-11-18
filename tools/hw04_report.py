"""Điền các khối <!-- REPORT:<khoá>:BEGIN/END --> trong HW04/23120255_HW04_Report.md từ file đã commit (không gõ tay).

Khối theo feature (A_FR01, B_FR07, C_FR15):
- selection / assertions / results / review / not_automated: chép nguyên văn file tương ứng trong HW04/<X>/
  (bỏ dòng tiêu đề H1, hạ mọi tiêu đề 2 cấp để nằm dưới mục 3.x/4.x/5.x của report).
- data: số TC, cột inputs, giả định ngoài expected – đọc từ HW04/data/<X>.json.
Khối chung:
- bugs: bảng "(AI chép)" từ HW04/bugs/BUG-*.md (tiêu đề, severity, priority, TC, issue).
- summary: chép khối SUMMARY của HW04/README.md.
- audit: mỗi commit có "HW04" trong message (git log, cũ → mới) là một artifact; GIỮ verdict/lý do đã có (theo hash);
  commit mới của SV (message có "SV viết/sửa/chốt/hoàn thiện/duyệt" hoặc "HW04: Sửa lại") → "— (SV làm…)"; commit mới của AI → <SV viết>.

Chạy: python tools/hw04_report.py
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "HW04/23120255_HW04_Report.md"
FEATS = ["A_FR01", "B_FR07", "C_FR15"]


def copy_md(path: Path) -> str:
    if not path.exists():
        return f"_(chưa có file `{path.relative_to(ROOT / 'HW04').as_posix()}`)_"
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    out, fence = [], False
    for l in lines:
        if l.lstrip().startswith("```"):
            fence = not fence
        if not fence and re.match(r"^#{1,4} ", l):
            l = "##" + l
        out.append(l)
    src = f"_Chép nguyên văn từ `{path.relative_to(ROOT / 'HW04').as_posix()}`._"
    return src + "\n" + "\n".join(out).strip("\n")


def data_block(feat: str) -> str:
    d = json.loads((ROOT / f"HW04/data/{feat}.json").read_text(encoding="utf-8"))
    tcs = d["testcases"]
    cols = list(dict.fromkeys(k for t in tcs for k in t.get("inputs", {})))
    types = {}
    for t in tcs:
        types[t.get("type", "?")] = types.get(t.get("type", "?"), 0) + 1
    rows = [f"- File: `data/{feat}.json` – {len(tcs)} TC; spec `tests/{feat}.spec.ts` lặp theo file này (không có mảng dữ liệu inline).",
            f"- Cột `inputs`: {', '.join(f'`{c}`' for c in cols)}.",
            f"- Loại TC: {', '.join(f'{k} {v}' for k, v in types.items())}.",
            "- `expected` chép nguyên văn từ HW02 kèm sha1; `loadData` và `check_data.py` từ chối file nếu sha1 lệch."]
    a = d.get("assumptions") or {}
    if a:
        rows.append("- Giả định ngoài expected (trường `assumptions`, không tính sha1):")
        rows += [f"  - `{k}` = `{v['value'][:80]}` — {v['note']}" for k, v in a.items()]
    return "\n".join(rows)


def bugs_block() -> str:
    rows = ["_(AI chép từ `bugs/BUG-xx.md`; nội dung bug do em viết.)_", "",
            "| BUG | Tiêu đề | Severity | Priority | TC liên quan | Issue |", "|---|---|---|---|---|---|"]
    files = sorted((ROOT / "HW04/bugs").glob("BUG-*.md"), key=lambda p: int(p.stem.split("-")[1]))
    for f in files:
        md = f.read_text(encoding="utf-8")
        g = lambda pat: (re.search(pat, md, re.M).group(1).strip() if re.search(pat, md, re.M) else "?")
        title = g(r"\*\*Tiêu đề[^*]*:\*\* `(.+)`")
        sev = g(r"^- \*\*Severity:\*\* (.+)$")
        pri = g(r"^- \*\*Priority:\*\* (.+)$")
        tc = g(r"^- Fail \([^)]*\): (.+)$")
        url = g(r"^## Link GitHub Issue\s*\n\s*\n(\S+)")
        num = url.rsplit("/", 1)[-1]
        rows.append(f"| {f.stem} | {title.replace('|', '\\|')} | {sev} | {pri} | {tc} | [#{num}]({url}) |")
    rows.append("")
    rows.append(f"Tổng: {len(files)} bug.")
    return "\n".join(rows)


SV_MSG = re.compile(r"SV (viết|sửa|chốt|hoàn thiện|duyệt)|^HW04: Sửa lại", re.I)
SV_DONE = "— (SV làm, không thuộc phạm vi audit AI)"
ESC = "\\|"                                   # | trong ô bảng markdown


def split_row(line: str) -> list[str]:
    """Tách ô bảng markdown, bỏ qua ký tự | đã escape (backslash + |) trong ô."""
    return [c.strip().replace(ESC, "|") for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def kept_audit() -> dict:
    """Verdict + lý do đã có trong bảng §9 (giữ khi sinh lại), theo hash commit."""
    t = REPORT.read_text(encoding="utf-8")
    b, e = "<!-- REPORT:audit:BEGIN -->", "<!-- REPORT:audit:END -->"
    out = {}
    if b in t and e in t:
        for line in t[t.index(b):t.index(e)].splitlines():
            c = split_row(line) if line.startswith("|") else []
            if len(c) >= 7 and re.fullmatch(r"`[0-9a-f]{7,}`", c[2]):
                out[c[2].strip("`")] = (c[-2], c[-1])
    return out


def audit_block() -> str:
    log = subprocess.run(["git", "log", "--reverse", "--date=format:%Y-%m-%d %H:%M", "--format=%h%x09%ad%x09%s"],
                         cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=True).stdout.splitlines()
    rows = ["| # | Thời điểm | Commit | Artifact (message) | Sửa `.spec.ts` | Verdict | Lý do |", "|---|---|---|---|---|---|---|"]
    keep = kept_audit()
    i = 0
    for line in log:
        h, ad, s = line.split("\t", 2)
        if "HW04" not in s:
            continue
        i += 1
        files = subprocess.run(["git", "show", "--name-only", "--format=", h], cwd=ROOT, capture_output=True, text=True,
                               encoding="utf-8", check=True).stdout.split()
        spec = "Có" if any(re.match(r"HW04/tests/[^/]+\.spec\.ts$", f) for f in files) else ""
        v, why = keep.get(h) or ((SV_DONE, "—") if SV_MSG.search(s) else ("`<SV viết>`", "`<SV viết>`"))
        rows.append(f"| {i} | {ad} | `{h}` | {s.replace('|', ESC)} | {spec} | {v.replace('|', ESC)} | {why.replace('|', ESC)} |")
    return "\n".join(rows)


def summary_block() -> str:
    """Bảng test summary: chép khối SUMMARY của HW04/README.md (sinh bởi tools/hw04_summary.py)."""
    t = (ROOT / "HW04/README.md").read_text(encoding="utf-8")
    b, e = "<!-- SUMMARY:BEGIN -->", "<!-- SUMMARY:END -->"
    if b not in t or e not in t:
        return "_(README chưa có khối SUMMARY – chạy python tools/hw04_summary.py)_"
    return "_Chép từ khối SUMMARY của `README.md` (`tools/hw04_summary.py`)._\n" + t[t.index(b) + len(b):t.index(e)].strip("\n")


def main():
    blocks = {"bugs": bugs_block(), "audit": audit_block(), "summary": summary_block()}
    for f in FEATS:
        d = ROOT / "HW04" / f
        blocks[f"{f}:selection"] = copy_md(d / "selection.md")
        blocks[f"{f}:data"] = data_block(f)
        blocks[f"{f}:assertions"] = copy_md(d / "assertions.md")
        blocks[f"{f}:results"] = copy_md(d / "results.md")
        blocks[f"{f}:review"] = copy_md(d / "review_sv.md")
        blocks[f"{f}:not_automated"] = copy_md(d / "not_automated.md")
    text = REPORT.read_text(encoding="utf-8")
    for k, v in blocks.items():
        b, e = f"<!-- REPORT:{k}:BEGIN -->", f"<!-- REPORT:{k}:END -->"
        if b not in text or e not in text:
            raise SystemExit(f"thiếu marker {k}")
        text = text[:text.index(b) + len(b)] + "\n" + v + "\n" + text[text.index(e):]
    REPORT.write_text(text, encoding="utf-8", newline="\n")
    print(f"Đã điền {len(blocks)} khối vào {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

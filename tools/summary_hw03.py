"""Test summary HW03 cho README (giữa <!-- SUMMARY:START --> … END -->) và report §8 (cùng marker).

    python tools/summary_hw03.py [--print]

Nguồn: HW03/checklist/checklist.json (kết quả P1/P2/P3), HW03/bugs/failed_list.md (trùng / một phần / MỚI),
HW03/bugs/BUG-*.md (khung bug, link GitHub Issue nếu SV đã điền). Không viết lời đánh giá.
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1] / "HW03"
START, END = "<!-- SUMMARY:START -->", "<!-- SUMMARY:END -->"
VALS = ["Passed", "Failed", "N/A", "Blocked"]
SCREENS = 5   # M1 Đăng nhập, M2 Quên mật khẩu (2 bước), M3 Hồ sơ, M4 Lịch sử đơn, M5 Navbar khi đã đăng nhập
NGUON = {"AI": "AI", "Both": "AI + SV sửa", "SV": "SV bổ sung"}


def res(it, P):
    return "N/A" if P not in it.get("nen_tang", []) else it.get("ket_qua", {}).get(P, "")


def usability_line():
    """Số liệu U1 từ usability/sessions/S*.json (pilot không tính), cùng công thức với sus_score.py."""
    ss = [json.loads(f.read_text(encoding="utf-8")) for f in sorted((ROOT / "usability" / "sessions").glob("S*.json"))]
    main = [d for d in ss if not d.get("pilot")]
    if not main:
        return "- Usability (Task 2): chưa có phiếu phiên (`usability/sessions/`)."
    sus = [2.5 * sum((v - 1) if i % 2 == 0 else (5 - v) for i, v in enumerate(d["sus"])) for d in main]
    seq = [d["seq"] for d in main]
    done = sum(1 for d in main if d["nhiem_vu"]["hoan_thanh"] != "khong_hoan_thanh")
    f = lambda x: f"{x:.1f}".replace(".", ",")
    return (f"- Usability (Task 2, U1): {len(main)} phiên chính S01–S{len(main):02d} + 1 pilot S00; hoàn thành {done}/{len(main)}; "
            f"**SUS TB {f(sum(sus) / len(sus))}**, **SEQ TB {f(sum(seq) / len(seq))}** (report §5.6–5.7, `usability/sessions/`).")


def block():
    doc = json.loads((ROOT / "checklist" / "checklist.json").read_text(encoding="utf-8"))
    items, plats = doc["items"], list(doc["meta"]["platforms"])
    c = {P: Counter(res(i, P) for i in items) for P in plats}
    head = re.search(r"\*\*trùng (\d+)\*\*, \*\*trùng một phần (\d+)\*\*.*?\*\*MỚI (\d+)\*\*",
                     (ROOT / "bugs" / "failed_list.md").read_text(encoding="utf-8"))
    dup, part, new = head.groups() if head else ("?", "?", "?")
    bugs = sorted((ROOT / "bugs").glob("BUG-*.md"))
    linked = [b for b in bugs if re.search(r"## Link GitHub Issue\s+\S*https://github\.com/\S+/issues/\d+", b.read_text(encoding="utf-8"))]
    out = ["| Chỉ số | " + " | ".join(f"{P} – {doc['meta']['platforms'][P]}" for P in plats) + " | Tổng |", "|---|" + "---|" * (len(plats) + 1)]
    out.append(f"| Màn hình kiểm (M1–M5) | " + " | ".join(str(SCREENS) for _ in plats) + f" | {SCREENS} |")
    out.append(f"| Item checklist thiết kế | " + " | ".join(str(len(items)) for _ in plats) + f" | {len(items)} |")
    ran = {P: len(items) - c[P]["N/A"] for P in plats}
    out.append("| Item đã chạy (trừ N/A) | " + " | ".join(str(ran[P]) for P in plats) + f" | {sum(ran.values())} ô |")
    for v in VALS:
        out.append(f"| {v} | " + " | ".join(str(c[P][v]) for P in plats) + f" | {sum(c[P][v] for P in plats)} ô |")
    n = Counter(NGUON.get(i["nguon"], i["nguon"]) for i in items)
    out += ["", f"- Bug: item Failed đối chiếu issue nhóm → **trùng {dup}**, **trùng một phần {part}**, **MỚI {new}** (`bugs/failed_list.md`, `bugs/dup_check.md`); "
            f"MỚI + phần mới gom thành **{len(bugs)} bug** `BUG-{bugs[0].stem.split('-')[1]}…{bugs[-1].stem.split('-')[1]}` (`bugs/bug_groups.md`); đã có link GitHub Issue: {len(linked)}/{len(bugs)}.",
            "- Nguồn item checklist: " + " · ".join(f"{k} {v}" for k, v in n.items()) + ".",
            usability_line(),
            "- Video Agent Skill: `skills/VideoLinks.md`.",
            "- Sinh bằng `tools/summary_hw03.py` từ `checklist/checklist.json`, `bugs/`."]
    return "\n".join(out) + "\n"


def put(path, body):
    t = path.read_text(encoding="utf-8")
    pat = re.compile(re.escape(START) + r"\n.*?" + re.escape(END), re.S)
    if not pat.search(t):
        return False
    path.write_text(pat.sub(lambda m: START + "\n" + body + END, t, count=1), encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--print", action="store_true")
    a = ap.parse_args()
    b = block()
    if a.print:
        print(b)
        return
    for f in [ROOT / "README.md", ROOT / "23120255_HW03_Report.md"]:
        print(f"{f.name}: {'đã ghi' if put(f, b) else 'CHƯA CÓ MARKER'}")


if __name__ == "__main__":
    main()

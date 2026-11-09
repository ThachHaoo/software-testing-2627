#!/usr/bin/env python3
"""Kiểm plan.md (9 phần, slide The 9-part test plan) và participant_kit.md (bước 0–1 của skill).

Usage: python check_kit.py [--plan plan.md] [--kit participant_kit.md] [--max-lines 70]
ERROR → mã thoát 1; WARN chỉ in. Script chỉ kiểm cấu trúc, không đánh giá nội dung thay người review.
"""
import argparse, re, sys, unicodedata
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# từ khoá (bỏ dấu, chữ thường) nhận ra tiêu đề từng phần; chấp nhận tiếng Việt hoặc tiếng Anh
PARTS = [
    ("Purpose", ["muc dich", "purpose"]),
    ("Problem statement", ["cau hoi", "problem"]),
    ("Test objectives & tasks", ["nhiem vu", "objective", "task"]),
    ("User profile", ["ho so nguoi dung", "nguoi dung", "user profile", "profile"]),
    ("Method & test design", ["phuong phap", "method"]),
    ("Environment / equipment", ["moi truong", "environment", "equipment"]),
    ("Test-monitor role", ["dieu phoi", "monitor", "moderator"]),
    ("Evaluation measures & data", ["do luong", "du lieu", "measure", "data"]),
    ("Report contents", ["bao cao", "report"]),
]
# nhiệm vụ không nêu bước: các cụm chỉ dẫn thao tác/tên control hay gặp
STEP_WORDS = ["bấm", "nhấn", "click", "nút", "menu", "chọn mục", "vào trang", "gõ vào", "ô tìm kiếm", "bước 1", "→"]


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn").replace("đ", "d")


def sections(text, level="## "):
    out, cur = [], None
    for line in text.splitlines():
        if line.startswith(level):
            cur = [line[len(level):].strip(), []]
            out.append(cur)
        elif cur:
            cur[1].append(line)
    return [(h, "\n".join(b).strip()) for h, b in out]


def check_plan(p, err, warn):
    secs = sections(p.read_text(encoding="utf-8"))
    nums = [(int(m.group(1)), h, b) for h, b in secs if (m := re.match(r"(\d+)\.\s*(.*)", h))]
    if [n for n, _, _ in nums] != list(range(1, 10)):
        err.append(f"plan: cần đúng 9 tiêu đề '## 1.' … '## 9.' theo thứ tự, đang có {[n for n, _, _ in nums]}")
    for (n, h, b), (name, keys) in zip(nums, PARTS):
        if not any(k in norm(h) for k in keys):
            warn.append(f"plan ## {n}. '{h}' — không nhận ra là phần '{name}' của slide")
        if len(re.sub(r"\s", "", b)) < 40:
            err.append(f"plan ## {n}. '{h}' gần như trống")
    t = norm(p.read_text(encoding="utf-8"))
    for k, msg in [("thanh cong", "tiêu chí thành công"), ("benchmark", "benchmark thời gian"), ("pilot", "pilot"), ("sus", "SUS"), ("seq", "SEQ")]:
        if k not in t:
            warn.append(f"plan: không thấy {msg}")


def check_kit(p, err, warn, max_lines):
    text = p.read_text(encoding="utf-8")
    t = norm(text)
    for k, msg in [("dong y", "phần xin đồng ý (quay/ghi âm/liên hệ)"), ("noi to", "lời nhắc think-aloud ('nói to')"),
                   ("khong kiem tra ban", "câu 'kiểm tra sản phẩm, không kiểm tra bạn'")]:
        if k not in t:
            warn.append(f"kit: thiếu {msg}")
    task = re.search(r"##[^\n]*Nhiệm vụ[^\n]*\n(.*?)(?=\n## )", text, re.S)
    if not task:
        err.append("kit: không có mục '## Nhiệm vụ'")
    else:
        quote = " ".join(l.lstrip("> ").strip() for l in task.group(1).splitlines() if l.startswith(">"))
        if not quote:
            warn.append("kit: nhiệm vụ nên đặt trong khối trích dẫn '>' để đọc nguyên văn")
        hits = [w for w in STEP_WORDS if w in quote.lower()]
        if hits:
            warn.append(f"kit: nhiệm vụ có cụm giống chỉ dẫn bước/tên control {hits} — nhiệm vụ phải dạng mục tiêu")
    if not re.search(r"1\s*[–-]\s*2\s*[–-]\s*3\s*[–-]\s*4\s*[–-]\s*5\s*[–-]\s*6\s*[–-]\s*7", text) or "seq" not in t:
        err.append("kit: thiếu SEQ thang 1–7")
    sus_sec = re.search(r"##[^\n]*SUS[^\n]*\n(.*?)(?=\n## |\Z)", text, re.S)
    rows = re.findall(r"^\|\s*(\d+)\s*\|", sus_sec.group(1), re.M) if sus_sec else []
    if [int(r) for r in rows] != list(range(1, 11)):
        err.append(f"kit: SUS phải có đúng 10 câu đánh số 1–10, đang có {rows}")
    else:
        cols = re.search(r"^\|\s*#\s*\|[^\n]*\|\s*1\s*\|\s*2\s*\|\s*3\s*\|\s*4\s*\|\s*5\s*\|", sus_sec.group(1), re.M)
        if not cols:
            warn.append("kit: bảng SUS không có 5 cột 1–5")
    open_sec = re.search(r"##[^\n]*(hỏi mở|open)[^\n]*\n(.*?)(?=\n## |\Z)", text, re.S | re.I)
    qs = re.findall(r"^\s*\d+\.\s", open_sec.group(2), re.M) if open_sec else []
    if len(qs) != 4:
        err.append(f"kit: cần 4 câu hỏi mở (rõ ràng · khôi phục lỗi · tốc độ · tin cậy), đang có {len(qs)}")
    else:
        for k in ["ro rang", "khoi phuc loi", "toc do", "tin cay"]:
            if k not in norm(open_sec.group(2)):
                warn.append(f"kit: câu hỏi mở không thấy chủ đề '{k}'")
    n = len([l for l in text.splitlines() if l.strip()])
    if n > max_lines:
        warn.append(f"kit: {n} dòng có chữ (> {max_lines}) — có thể quá 1 trang khi in")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=Path)
    ap.add_argument("--kit", type=Path)
    ap.add_argument("--max-lines", type=int, default=70)
    a = ap.parse_args()
    if not (a.plan or a.kit):
        ap.error("cần --plan và/hoặc --kit")
    err, warn = [], []
    if a.plan:
        check_plan(a.plan, err, warn)
    if a.kit:
        check_kit(a.kit, err, warn, a.max_lines)
    for e in err:
        print("ERROR", e)
    for w in warn:
        print("WARN ", w)
    print(f"{len(err)} lỗi, {len(warn)} cảnh báo")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()

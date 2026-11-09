#!/usr/bin/env python3
"""Danh sách Failed (item × nền tảng) từ checklist.json + đối chiếu trùng với issue đã có → failed_list.md.

Usage: python failed_list.py --config failed.json   (hoặc run(cfg) từ wrapper của bài – ví dụ tools/failed_list_hw03.py)

- Ô Failed có lap_bug=false (quyết định người dùng, xem merge_runs.py override) → dòng "loại khỏi lập bug", không đếm.
- Ô auto Failed chỉ vì lỗi harness (TimeoutError, không có assertion "Lỗi: Error:") → cảnh báo "chờ chạy lại".
- dup: đối chiếu trùng do AI làm theo tiêu đề issue + màn hình + notes; NGƯỜI DÙNG xác nhận. Chỉ ghi mã issue, không mô tả bug.

Config:
  checklist      đường dẫn checklist.json
  issues         issues.json (`gh issue list --state all --limit 500 --json number,title,state,labels,author`)
  out            đường dẫn failed_list.md
  dup            {"CL-03": ["TRÙNG"|"MỘT PHẦN"|"LIÊN QUAN", [9], "ghi chú"], ...}   (LIÊN QUAN = khác màn → vẫn tính MỚI)
  issue_alias    {"166": "BUG-20", ...}  (tuỳ chọn: issue là bug cũ của chính người dùng)
  title          dòng tiêu đề (# …)
  compare_label  mô tả nguồn đối chiếu thêm, vd "BUG-01…57 HW02 của em"
  exclude_note   nhãn quyết định loại khỏi lập bug, vd "5/6a" (dòng tổng ghi "quyết định 5/6a")
  extra_lines    [các dòng thêm sau dòng tổng]
  source_note    câu giải thích cột "kết quả từ"
"""
import argparse, json
from pathlib import Path


def run(cfg):
    doc = json.loads(Path(cfg["checklist"]).read_text(encoding="utf-8"))
    issues = {i["number"]: i for i in json.loads(Path(cfg["issues"]).read_text(encoding="utf-8"))}
    dup = {k: tuple(v) for k, v in cfg.get("dup", {}).items()}
    alias = {int(k): v for k, v in cfg.get("issue_alias", {}).items()}
    excl_note = cfg.get("exclude_note", "quyết định")
    plats = list(doc["meta"]["platforms"])
    rows, n, harness, pend, excl = [], {"TRÙNG": 0, "MỘT PHẦN": 0, "MỚI": 0}, [], 0, []
    cells = {P: 0 for P in plats}
    for it in doc["items"]:
        f = [P for P in plats if it.get("ket_qua", {}).get(P) == "Failed"]
        if not f:
            continue
        for P in f:
            cells[P] += 1
        kind, nums, note = dup.get(it["id"], ("MỚI", [], ""))
        bad = [x for x in nums if x not in issues]
        if bad:
            raise SystemExit(f"{it['id']}: issue {bad} không có trong issues.json")
        nobug = [P for P in f if it.get("lap_bug", {}).get(P) is False]
        if nobug == f:   # mọi ô Failed đều bị quyết định loại khỏi lập bug
            excl.append(it["id"])
            rows.append(f"| {len(rows) + 1} | {it['id']} | {it['man_hinh']} | {it['muc_kiem_tra'].replace('|', '/')} | {', '.join(f)} | "
                        f"{'/'.join(sorted({it.get('nguon_kq', {}).get(P, '?') for P in f}))} | loại khỏi lập bug ({excl_note}) | {note or 'xem notes'} |")
            continue
        refs = ", ".join(f"#{x}" + (f" ({alias[x]})" if x in alias else "") for x in nums)
        col = {"TRÙNG": f"trùng {refs}", "MỘT PHẦN": f"trùng một phần {refs} + MỚI", "LIÊN QUAN": f"**MỚI** (liên quan {refs})"}.get(kind, "**MỚI**")
        n["MỚI" if kind == "LIÊN QUAN" else kind] += 1
        src = "/".join(sorted({it.get("nguon_kq", {}).get(P, "?") for P in f}))
        # ô auto Failed chỉ vì lỗi harness (Timeout, không có assertion nào fail) → chưa cô lập nguyên nhân, cần chạy lại
        hx = [P for P in f if it.get("nguon_kq", {}).get(P) == "auto" and "TimeoutError" in it.get("notes_nt", {}).get(P, "")
              and "Lỗi: Error:" not in it.get("notes_nt", {}).get(P, "")]
        if hx:
            harness.append(f"{it['id']} {'/'.join(hx)}")
            note = (note + "; " if note else "") + f"⚠ {'/'.join(hx)}: Failed do TimeoutError của Playwright, chưa có assertion fail → chạy lại trước khi coi là lỗi"
            if hx == f:
                col += " ⚠ chờ chạy lại"
                pend += 1
        rows.append(f"| {len(rows) + 1} | {it['id']} | {it['man_hinh']} | {it['muc_kiem_tra'].replace('|', '/')} | {', '.join(f)} | {src} | {col} | {note} |")
    cmp_label = cfg.get("compare_label")
    out = [
        cfg.get("title", "# Danh sách Failed (sinh bằng `failed_list.py` từ `checklist.json`)"),
        "",
        f"{len(rows)} item Failed · ô Failed theo nền tảng: " + ", ".join(f"{P} {cells[P]}" for P in plats) + f" (tổng {sum(cells.values())}).",
        f"Đối chiếu `{cfg.get('issues_label', Path(cfg['issues']).name)}` ({len(issues)} issue nhóm, tới #{max(issues)})" + (f" và {cmp_label}" if cmp_label else "") + ": "
        f"**trùng {n['TRÙNG']}**, **trùng một phần {n['MỘT PHẦN']}** (màn còn lại là MỚI), **MỚI {n['MỚI']}**; loại khỏi lập bug: {', '.join(excl) or 'không'} (quyết định {excl_note}).",
        *cfg.get("extra_lines", []),
        "",
        cfg.get("source_note", "Cột *kết quả từ*: `tay` = lượt chạy tay; `auto` = lượt Playwright. Đối chiếu trùng do AI làm; người dùng xác nhận trước khi viết bug."),
        "",
        "| # | Item | Màn hình | Mục kiểm tra | Failed trên | Kết quả từ | Issue trùng / MỚI | Ghi chú đối chiếu |",
        "|---|---|---|---|---|---|---|---|",
        *rows,
        "",
    ]
    Path(cfg["out"]).write_text("\n".join(out), encoding="utf-8")
    print(f"{len(rows)} item, ô {cells}, {n}, loại: {excl}, timeout harness: {harness}")
    return {"rows": len(rows), "counts": n, "excluded": excl}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    run(json.loads(Path(ap.parse_args().config).read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()

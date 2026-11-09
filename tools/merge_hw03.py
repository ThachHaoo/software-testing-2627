"""Gộp kết quả T1 bước 4 của HW03 vào checklist.json (quyết định V1, Q1, Q2 trong report_plan mục e).

    python tools/merge_hw03.py [--dry-run]

1. runs/P*_manual_<ts>.md (SV viết, KHÔNG sửa) → runs/P*_manual_<ts>.csv (id,status,notes,evidence). Tên ảnh ánh xạ sang
   tên chuẩn đã nén `evidence/<Px_dir>/P<n>_<ID>_<k>.png`; ảnh không còn (đã đổi tên ở 4/6a2) → bỏ, in cảnh báo.
2. merge_platform.py: lượt auto mới nhất → auto_status; lượt tay → ket_qua.
3. Item không có trong lượt tay (item auto) → ket_qua = auto_status, nguon_kq[Px] = "auto".
4. Item có cả hai mà khác nhau → giữ kết quả tay (V1), ghi lech_auto_tay[Px] = "auto X ≠ tay Y: <nguyên nhân>".
"""
import argparse, csv, json, re, subprocess, sys
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO = Path(__file__).resolve().parents[1]
CL = REPO / "HW03" / "checklist"
MERGE = REPO / ".claude" / "skills" / "gui-checklist-testing" / "scripts" / "merge_platform.py"
DIRS = {"P1": "P1_chrome", "P2": "P2_firefox", "P3": "P3_android"}
AUTO = {"P1": "P1_auto_20261109-2236.json", "P2": "P2_auto_20261109-2240.json", "P3": "P3_auto_20261109-2244.json"}
MANUAL = {"P1": "P1_manual_20261109-2257", "P2": "P2_manual_20261110-0010", "P3": "P3_manual_20261110-0046"}
AUTO_ENV = {"P1": "Chrome 157 qua Playwright (Q1: P1 chính thức là Cốc Cốc 160, cùng nhân Chromium)",
            "P2": "Firefox 131 bản build của Playwright", "P3": "Chrome Android 156 thật trên POCO F5 (Playwright _android)"}
LOCALE = "auto ép locale vi-VN (playwright.config) nên hiện \"6.000.000 ₫\"; trình duyệt thật của SV theo locale máy hiện \"6,000,000 ₫\""
CAUSE = {  # nguyên nhân lệch, dữ kiện từ run_check.md mục 1c (L1–L8)
    ("CL-08", "P2"): LOCALE, ("CL-08", "P3"): LOCALE,
    ("CL-09", "P1"): "cả hai cùng thấy \"9/11/2026\" (ảnh P1_CL-09_1); khác ở cách chấm ngưỡng dd/mm/yyyy (run_check R11)",
    ("CL-11", "P1"): "auto so toạ độ, bố cục 2 cột nên 'Cập nhật' → 'Hủy đơn' bị tính là nhảy ngược; SV đọc chuỗi Tab theo cột/hàng",
    ("CL-11", "P2"): "auto so toạ độ, bố cục 2 cột nên 'Cập nhật' → 'Hủy đơn' bị tính là nhảy ngược; SV đọc chuỗi Tab theo cột/hàng",
    ("CL-15", "P1"): "auto đo ở viewport 375 px: scrollWidth 381 > 375; lượt tay không đo ở đúng 375 px (ảnh chụp cửa sổ hẹp, không thấy thanh cuộn)",
    ("CL-15", "P2"): "auto đo ở viewport 375 px: scrollWidth 382 > 375; lượt tay không đo ở đúng 375 px (ảnh chụp cửa sổ hẹp, không thấy thanh cuộn)",
    ("SV-02", "P1"): "auto chỉ kiểm vế dán (Ctrl+V); vế autofill kiểm tay",
}
# Quyết định 5/6a (report_plan mục e: T-P3, CL-34, CL-52 P3). Áp sau cùng → chạy lại script vẫn giữ.
# ket_qua: đổi kết quả; them: nối vào notes (không sửa chữ SV); lap_bug False: loại khỏi danh sách lập bug.
OVERRIDE = {
    ("CL-30", "P3"): {"ket_qua": "Blocked", "them": "Blocked (T-P3): Playwright TimeoutError, không có assertion fail – không lập bug", "lap_bug": False},
    ("CL-48", "P3"): {"ket_qua": "Blocked", "them": "Blocked (T-P3): Playwright TimeoutError, không có assertion fail – không lập bug", "lap_bug": False},
    ("CL-34", "P2"): {"them": "chỉ Firefox Playwright, chưa xác nhận trên trình duyệt thật – không lập bug (5/6a)", "lap_bug": False},
    ("CL-52", "P3"): {"them": "thiếu ảnh (ảnh P3_CL-52_1 chỉ thấy \"Đăng nhập thất bại\", không thấy trạng thái khoá) – 5/6a"},
}
RX = re.compile(r"(P[123])_((?:CL|SV)-?\d{2}|M\d)[-_](\d+)", re.I)


def std(name):
    m = RX.search(name)
    if not m:
        return None
    iid = m[2].upper()
    if iid[:2] in ("CL", "SV") and "-" not in iid:
        iid = iid[:2] + "-" + iid[2:]
    return f"{m[1].upper()}_{iid}_{int(m[3])}.png"


def to_csv(P):
    src = CL / "runs" / f"{MANUAL[P]}.md"
    rows, warn = [], []
    for line in src.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*((?:CL|SV)-\d{2})\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m[2].split("|")]
        status, notes, imgs = cells[0], " | ".join(cells[1:-1]), cells[-1]
        ev = []
        for x in re.split(r"[,;]\s*", imgs):
            if not x:
                continue
            n = std(x)
            path = CL / "evidence" / DIRS[P] / n if n else None
            if path and path.exists():
                ev.append(f"evidence/{DIRS[P]}/{n}")
            else:
                warn.append(f"{P} {m[1]}: ảnh '{x}' không có trong evidence/ – bỏ")
        rows.append({"id": m[1], "status": status, "notes": notes, "evidence": ";".join(ev)})
    out = CL / "runs" / f"{MANUAL[P]}.csv"
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, ["id", "status", "notes", "evidence"])
        w.writeheader()
        w.writerows(rows)
    return out, warn


def merge(run, P, dry):
    cmd = [sys.executable, str(MERGE), str(CL / "checklist.json"), str(run), "--platform", P] + (["--dry-run"] if dry else [])
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr)
    for l in r.stdout.splitlines():
        if l.startswith("WARN"):
            print("  ", l)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    for P in DIRS:
        merge(CL / "runs" / AUTO[P], P, a.dry_run)
        csvp, warn = to_csv(P)
        for w in warn:
            print("WARN ", w)
        merge(csvp, P, a.dry_run)
    if a.dry_run:
        return
    jp = CL / "checklist.json"
    doc = json.loads(jp.read_text(encoding="utf-8"))
    filled, lech = 0, []
    for it in doc["items"]:
        for P in it.get("nen_tang", []):
            au, tay = it.get("auto_status", {}).get(P), it.get("ket_qua", {}).get(P)
            if tay and it.get("run", {}).get(P, "").endswith(".csv"):
                it.setdefault("nguon_kq", {})[P] = "tay"
                if au and au != tay:
                    c = CAUSE.get((it["id"], P), "CHƯA RÕ – SV ghi nguyên nhân")
                    it.setdefault("lech_auto_tay", {})[P] = f"auto {au} ≠ tay {tay} → lấy tay (V1): {c}"
                    lech.append(f"{it['id']} {P}")
            elif au:
                it.setdefault("ket_qua", {})[P] = au
                it.setdefault("notes_nt", {})[P] = f"[auto – {AUTO_ENV[P]}] " + it.get("auto_notes", {}).get(P, "")
                it.setdefault("evidence", {})[P] = it.get("auto_evidence", {}).get(P, [])
                it.setdefault("run", {})[P] = it.get("auto_run", {}).get(P, "")
                it.setdefault("nguon_kq", {})[P] = "auto"
                filled += 1
    items = {i["id"]: i for i in doc["items"]}
    for (iid, P), o in OVERRIDE.items():
        it = items[iid]
        if "ket_qua" in o:
            it["ket_qua"][P] = o["ket_qua"]
        if o.get("them") and o["them"] not in it.get("notes_nt", {}).get(P, ""):
            old = it.setdefault("notes_nt", {}).get(P, "")
            it["notes_nt"][P] = (old + " · " if old else "") + "[" + o["them"] + "]"
        if "lap_bug" in o:
            it.setdefault("lap_bug", {})[P] = o["lap_bug"]
    jp.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    miss = [f"{i['id']} {P}" for i in doc["items"] for P in i.get("nen_tang", []) if not i.get("ket_qua", {}).get(P)]
    print(f"ket_qua từ auto: {filled} ô; lệch auto↔tay: {len(lech)} ({', '.join(lech)}); thiếu kết quả: {len(miss)} {miss}")


if __name__ == "__main__":
    main()

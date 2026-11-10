"""HW03 T2 – điền phiếu phiên usability/sessions/S00…S07.json (khung từ new_session.py) bằng dữ kiện SV đưa.

    python tools/usability_fill_hw03.py [--session S03]

Nguồn (AI chép, SV duyệt):
- `HW03/usability/evidence_raw/responses.csv` (Google Form, gitignore – có họ tên/SĐT): CHỈ đọc cột Timestamp (lấy ngày),
  Mã phiên, 3 câu đồng ý, SEQ, 10 câu SUS, 4 câu hỏi mở. Không đọc/ghi cột họ tên, SĐT, "Bạn là".
- `HW03/usability/sessions/notes/S0x.txt` (SV ghi tay): mỗi dòng → su_kien loại N (câu nói/ghi chú nguyên văn).
- Nghề nghiệp: SV cung cấp trong lệnh 10–11/11 (không lấy từ form).
Thời gian, kết quả hoàn thành, trợ giúp, nền tảng, reset dữ liệu: để `<SV điền>`. Mã phiên "SO1" (chữ O) = S01.
"""
import argparse, csv, json, re, sys
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

U = Path(__file__).resolve().parents[1] / "HW03" / "usability"
SV = "<SV điền>"
NGHE = {"S00": "DA", "S01": "SWE", "S02": "DE", "S03": "Vật lý học", "S04": "Tự động hoá", "S05": "Dược", "S06": "Thực phẩm", "S07": "IT"}
COL = {"ts": "Timestamp", "ma": "Mã phiên", "quay": "Đồng ý quay màn hình", "am": "Đồng ý ghi âm",
       "lh": "Đồng ý để trợ giảng liên hệ xác nhận", "seq": "Nhìn chung, nhiệm vụ vừa rồi khó hay dễ?"}
OPEN = {"ro_rang": "Rõ ràng:", "khoi_phuc_loi": "Khôi phục lỗi:", "toc_do": "Tốc độ:", "tin_cay": "Tin cậy:"}


def num(s):
    m = re.match(r"\s*(\d)", s or "")
    if not m:
        raise SystemExit(f"ô không có số: {s!r}")
    return int(m.group(1))


def yes(s):
    return {"Có": True, "Không": False}[s.strip()]


def rows():
    r = list(csv.DictReader(open(U / "evidence_raw" / "responses.csv", encoding="utf-8-sig")))
    head = list(r[0].keys())
    sus_cols = [h for h in head if h.startswith("Đánh giá trang web EShop [")]
    open_cols = {k: next(h for h in head if h.startswith(p)) for k, p in OPEN.items()}
    out, seen = {}, []
    for x in r:
        raw = x[COL["ma"]].strip()
        code = "S01" if raw == "SO1" else raw
        if not re.fullmatch(r"S0\d", code):
            raise SystemExit(f"mã phiên lạ: {raw!r}")
        if code in out:
            raise SystemExit(f"trùng mã phiên {code}")
        out[code] = {"raw": raw, "ngay": "-".join(x[COL["ts"]].split()[0].split("/")),
                     "dong_y": {"quay_man_hinh": yes(x[COL["quay"]]), "ghi_am": yes(x[COL["am"]]), "lien_he_xac_nhan": yes(x[COL["lh"]])},
                     "seq": num(x[COL["seq"]]), "sus": [num(x[c]) for c in sus_cols],
                     "cau_hoi_mo": {k: x[c].strip() for k, c in open_cols.items()}}
        assert len(out[code]["sus"]) == 10
    miss = [s for s in NGHE if s not in out]
    if miss:
        raise SystemExit(f"thiếu mã phiên trong CSV: {miss}")
    return out


def notes(s):
    lines = (U / "sessions" / "notes" / f"{s}.txt").read_text(encoding="utf-8").splitlines()
    ev = []
    for k, line in enumerate(lines, 1):
        t = re.sub(rf"^{s}:\s*", "", line).strip() if k == 1 else line.strip()
        if t:
            ev.append({"t": SV, "man_hinh": None, "loai": "N", "mo_ta": t, "bug": None, "nguon": f"notes/{s}.txt:{k}"})
    return ev


def fill(s, c):
    p = U / "sessions" / f"{s}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    ghi = []
    if s == "S00":
        ghi.append("PILOT – không tính vào thống kê. Sau pilot giữ nguyên kịch bản; từ S01 bổ sung \"hỏi lại ngay khi nhận xét mơ hồ\" (SV chốt 11/11).")
    if c["raw"] != s:
        ghi.append(f"Người tham gia gõ nhầm mã phiên trong form (\"{c['raw']}\", chữ O) – AI ghép vào {s}.")
    if not c["dong_y"]["lien_he_xac_nhan"]:
        ghi.append("KHÔNG đồng ý để trợ giảng liên hệ xác nhận.")
    d.update({
        "_nguon": "AI chép, SV duyệt: ngày/đồng ý/SEQ/SUS/câu hỏi mở từ responses.csv (cột Mã phiên); su_kien từ notes; nghề nghiệp SV cung cấp. "
                  "Các ô <SV điền> do SV nhập.",
        "ngay": c["ngay"], "nguoi_tham_gia": "P" + s[1:], "nghe_nghiep": NGHE[s], "nghe_nghiep_nguon": "SV cung cấp",
        "nen_tang": SV, "reset_du_lieu": SV, "dong_y": c["dong_y"],
        "nhiem_vu": {"moc": {}, "ket_thuc": SV, "hoan_thanh": SV, "noi_dung_trang_thai": None, "cau_tra_loi_trang_thai": None},
        "su_kien": notes(s), "tro_giup": SV, "seq": c["seq"], "sus": c["sus"], "cau_hoi_mo": c["cau_hoi_mo"],
        "ghi_chu": " ".join(ghi),
    })
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sus = 2.5 * sum((v - 1) if i % 2 == 0 else (5 - v) for i, v in enumerate(c["sus"]))
    print(f"{s}: SEQ {c['seq']} · SUS {sus:g} · {len(d['su_kien'])} dòng notes")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--session")
    a = ap.parse_args()
    data = rows()
    for s in ([a.session] if a.session else sorted(NGHE)):
        fill(s, data[s])


if __name__ == "__main__":
    main()

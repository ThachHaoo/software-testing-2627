# Schema phiếu phiên `sessions/S0x.json`

Một file / phiên. `S00` = pilot (`"pilot": true`, không tính số liệu). Khung trống: `scripts/new_session.py`. **SV nhập toàn bộ giá trị; AI không điền.**

```json
{
  "phien": "S01",
  "pilot": false,
  "ngay": "2026-11-10",
  "nguoi_tham_gia": "P01",
  "nhom": "non-IT",
  "nen_tang": "P1",
  "reset_du_lieu": true,
  "dong_y": { "quay_man_hinh": true, "ghi_am": true, "lien_he_xac_nhan": true },
  "video": "S01.mp4",
  "nhiem_vu": {
    "moc": { "dang_nhap": "00:40", "thay_san_pham": "01:10", "them_gio": "01:30", "ap_ma": "02:50", "dat_hang": "03:20", "thay_don": "04:05" },
    "ket_thuc": "04:20",
    "hoan_thanh": "khong_tro_giup",
    "noi_dung_trang_thai": true,
    "cau_tra_loi_trang_thai": "…"
  },
  "su_kien": [
    { "t": "02:10", "man_hinh": "Thanh toán", "loai": "D", "mo_ta": "…", "bug": false }
  ],
  "tro_giup": [
    { "t": "03:00", "ly_do": "…", "cau_noi": "…" }
  ],
  "seq": 5,
  "sus": [4, 2, 4, 1, 4, 2, 5, 2, 4, 1],
  "cau_hoi_mo": { "ro_rang": "…", "khoi_phuc_loi": "…", "toc_do": "…", "tin_cay": "…" },
  "ghi_chu": ""
}
```

| Trường | Bắt buộc | Quy tắc |
|---|---|---|
| `phien` | ✔ | `S00`…`S99`, trùng tên file |
| `pilot` | ✔ | `true` chỉ cho pilot |
| `nguoi_tham_gia` | ✔ | **mã ẩn danh** `P\d+`; không tên, SĐT, email |
| `nhom` | | nhóm người dùng để so sánh (vd `IT` / `non-IT`) |
| `nhiem_vu.moc` | | `mm:ss` tính từ lúc bắt đầu nhiệm vụ; tên mốc theo plan |
| `nhiem_vu.ket_thuc` | ✔ | `mm:ss` lúc nói "Xong" / bỏ cuộc |
| `nhiem_vu.hoan_thanh` | ✔ | `khong_tro_giup` · `co_tro_giup` · `khong_hoan_thanh` |
| `su_kien[].loai` | | `L` lỗi/chọn sai · `D` do dự · `N` câu nói nguyên văn · `T` trợ giúp |
| `su_kien[].bug` | | `true` = SV cho là lỗi chức năng (bước 6 gom) |
| `tro_giup` | | mỗi lần can thiệp; ≥ 1 lần mà `hoan_thanh = khong_tro_giup` → lỗi check |
| `seq` | ✔ | số nguyên 1–7 |
| `sus` | ✔ | đúng 10 số nguyên 1–5, theo thứ tự câu 1…10 của kit |
| `cau_hoi_mo` | ✔ | 4 khoá; câu trả lời ghi nguyên văn hoặc tóm tắt của SV |

Số lỗi / do dự / trợ giúp = số `su_kien` loại `L` / `D` / (`T` hoặc mục `tro_giup`, lấy số lớn hơn).

Script từ chối file có chuỗi ≥ 9 chữ số liền nhau hoặc địa chỉ email (dữ liệu cá nhân).

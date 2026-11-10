# Schema `checklist.json`

Một file cho một phạm vi (nhóm màn hình). UTF-8, `ensure_ascii=False`, thụt 2.

```jsonc
{
  "meta": {
    "hw": "HW03",
    "task": "T1 – GUI Checklist",
    "scope": "C2 – Tài khoản (…)",
    "sut_version": "tkob-team/eshop-sut @ de0f48f",
    "test_basis": "README.md (SRS v2.0) FR-21…24 …; slide …",
    "platforms": {"P1": "Chrome trên Windows", "P2": "Firefox trên Windows", "P3": "Chrome Android"},
    "result_values": ["Passed", "Failed", "N/A", "Blocked"],
    "inventory": "HW03/checklist/c2_inventory.md",
    "version": "v1 – AI nháp (T1 1/6)",
    "step": 1                       // tuỳ chọn: bước đã xong
  },
  "assumptions": {                  // mã → nội dung; GAx = quyết định Expected, NAx = nền tảng không áp dụng
    "GA1": "…", "NA1": "…"
  },
  "items": [ { …item… } ]
}
```

## Item

| Trường | Bắt buộc | Kiểu | Ghi chú |
|---|---|---|---|
| `id` | ✔ | `CL-01`… | duy nhất, không đánh lại số khi xoá |
| `ia` | ✔ | `IA-01`…`IA-04` | IA-01 chuẩn chung · IA-02 form · IA-03 điều hướng · IA-04 phản hồi/trạng thái |
| `man_hinh` | ✔ | chuỗi | màn hình / vùng |
| `muc_kiem_tra` | ✔ | chuỗi | ngắn, một ý |
| `can_cu` | ✔ | chuỗi | mã điều khoản + `file:dòng`, hoặc tên heuristic/checklist |
| `loai_nguon` | ✔ | `SRS` / `Control` / `Heuristic` | 3 nguồn của slide |
| `expected` | ✔ | chuỗi | thao tác + điểm quan sát + "Fail nếu …" |
| `uu_tien` | ✔ | `Mandatory` / `Optional` | slide: *Mandatory vs Optional* |
| `nen_tang` | ✔ | mảng mã nền tảng | nền tảng áp dụng |
| `na` | khi thiếu nền tảng | `{Px: "Giả định NAx: …"}` | mỗi nền tảng bị bỏ một lý do |
| `nguon` | ✔ | `AI` / `SV` / `Both` | |
| `tien_dieu_kien` | | chuỗi | dữ liệu cần dựng, công cụ (DevTools, chrome://inspect) |
| `gia_dinh` | | chuỗi chứa mã `GAx` | khi Expected dựa vào giả định |
| `ly_do_ai_bo_sot` | item `SV` | chuỗi | SV viết 🔒 |
| `ket_qua` | sau bước 4 | `{Px: "Passed"/"Failed"/"N/A"/"Blocked"}` | |
| `notes_nt` | Failed/Blocked | `{Px: "…"}` | Actual nguyên văn + lý do; Blocked ghi item gốc |
| `evidence` | Failed | `{Px: ["checklist/evidence/P1_chrome/CL-05_failed.png"]}` | ảnh có overlay |
| `run` | sau bước 4 | `{Px: "runs/P1_20261105-0930.csv"}` | lượt đã gộp |
| `notes` | | chuỗi | ghi chú chung |
| `che_do` | bước 3 | `auto` / `manual` / `mixed` | cách chạy (chế độ Playwright) |
| `che_do_ghi_chu` | mixed/manual | chuỗi | phần chạy tay / lý do cần mắt người |
| `auto_nen_tang` | | mảng mã nền tảng | nền tảng chạy auto được (thiếu = mọi nền tảng) |
| `auto_status`, `auto_notes`, `auto_evidence`, `auto_run` | sau lượt auto | `{Px: …}` | kết quả Playwright, không phải verdict |
| `nguon_kq` | sau gộp | `{Px: "tay"/"auto"}` | `ket_qua` lấy từ lượt nào |
| `lech_auto_tay` | khi lệch | `{Px: "auto X ≠ tay Y → lấy tay (V1): nguyên nhân"}` | |
| `lap_bug` | quyết định | `{Px: false}` | ô Failed không lập bug (vd chỉ trên trình duyệt Playwright) |

## File lượt chạy (đầu vào `merge_platform.py`)

CSV UTF-8, có header: `id,status,notes,evidence` (evidence nhiều ảnh cách nhau bởi `;`). Hoặc JSON:

```json
{"platform": "P1", "run_at": "2026-11-05 09:30", "env": "Chrome 142 / Windows 11",
 "results": {"CL-01": {"status": "Failed", "notes": "…", "evidence": ["…png"]}}}
```

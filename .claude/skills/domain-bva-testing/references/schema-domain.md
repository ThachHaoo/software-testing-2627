# Phần mở rộng `domain` cho testcases.json

File vẫn hợp lệ với schema của skill `test-case-writing` (meta, requirements, suites, cases), nên linter và script build Word/Excel của giảng viên vẫn chạy. Skill này thêm:

```jsonc
{
  "meta": { "...": "như test-case-writing", "feature_code": "A_FR01", "bva_model": "9 điểm theo slide (LB-1, LB, LB+1, NOM, UB-1, UB, UB+1, MIN_UI, MAX_UI)" },
  "requirements": [ {"id": "FR-01.1", "text": "..."} ],

  "domain": {
    "variables": [
      {"id": "V1", "name": "Mật khẩu", "io": "input",  "source": "ô 'Mật khẩu' (Register.jsx) / body.password", "type": "string", "constraint": "trích đặc tả"},
      {"id": "V9", "name": "Kết quả đăng ký", "io": "output", "source": "thông báo / chuyển trang / bản ghi DB", "type": "enum", "constraint": "..."}
    ],
    "partitions": [
      {"id": "EC1", "variable": "V1", "class": "mô tả lớp, ví dụ 1 ≤ x ≤ 999", "valid": true,  "guideline": "range", "note": ""},
      {"id": "EC2", "variable": "V1", "class": "x < 1",                        "valid": false, "guideline": "range", "note": ""}
      // tuỳ chọn: "requirements": ["FR-01.6"] trên mỗi EC → render_md.py sinh bảng truy vết từ ánh xạ EC → yêu cầu
    ]
  },

  "suites": [
    {
      "id": "TS-DOM", "name": "Domain — minimum set", "format": "matrix",
      "procedure": [ {"action": "...", "expected": "..."} ],
      "columns": ["Tên cột = tên biến đầu vào"],
      "cases": [
        {
          "id": "TC-FR01-01", "title": "Kiểm tra … khi …",
          "inputs": {"...": "..."},
          "expected_result": "oracle kiểm chứng được",
          "requirements": ["FR-01.1"],
          "covers": ["EC1", "EC5"],          // mảng mã EC (chuỗi "EC1, EC5" cũng được)
          "technique": "EP",                // EP | BVA | EG (error guessing) | ST (state transition)
          "bva_point": "",                  // LB-1 | LB | LB+1 | NOM | UB-1 | UB | UB+1 | MIN_UI | MAX_UI
          "rationale": "vì sao chọn giá trị này",
          "layer": "UI",                    // UI | API | Mobile
          "origin": "AI",                   // AI | Human | Both
          "priority": "High",
          "status": "Not run",              // Not run | Pass | Fail | Blocked | Skipped
          "actual_result": "", "evidence": "", "bug_id": "", "notes": ""
        }
      ]
    },
    { "id": "TS-BVA", "name": "Boundary values", "format": "matrix", "...": "..." },
    { "id": "TS-SV",  "name": "Bổ sung của sinh viên", "format": "matrix", "...": "..." }
  ]
}
```

## Quy tắc `check_domain.py` kiểm

| Mức | Kiểm tra |
|---|---|
| ERROR | `covers` trỏ tới EC không tồn tại; EC trỏ tới biến không tồn tại; trùng mã TC/EC |
| ERROR | Một case phủ **từ 2 lớp không hợp lệ trở lên** (vi phạm quy tắc chọn case không hợp lệ) |
| WARN | EC chưa được case nào phủ |
| WARN | Biến đầu vào không có lớp không hợp lệ nào; biến đầu ra chưa phân lớp |
| WARN | Case BVA thiếu `bva_point`; lớp `range` chưa có đủ LB/UB và hai láng giềng |
| WARN | Case thiếu `rationale`, `origin`, `technique` |
| INFO | Thống kê: số EC (hợp lệ/không), số case theo suite, theo origin, theo status |

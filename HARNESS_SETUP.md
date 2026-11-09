# Cài harness vào repo `software-testing-2627` (làm một lần)

## 1. Chuẩn bị

- **Claude Code** đăng nhập bằng **tài khoản claude.ai** (không dùng API key) để các skill của tài khoản (`cs423-ai-first-homework`, `test-design-istqb`, `hw-submission-audit`, `qa-evidence-review`) tự đồng bộ về máy.
- **Python ≥ 3.11** gọi được bằng lệnh `python` (`python --version`). Hook và script chỉ dùng thư viện chuẩn.
- **Node 22** (đã có khi dựng SUT).
- Repo bài nộp nên **Private**. Nếu không đổi được (không phải chủ repo), **chỉ commit cục bộ và push sau hạn nộp**.
- Fork nhóm `tkob-team/eshop-sut` → Settings → Features → bật **Issues**.

## 2. Chép gói vào repo

Giải nén gói **vào gốc repo** `software-testing-2627` (cùng cấp với `HW01/`). Sau khi chép:

```
software-testing-2627/
├── CLAUDE.md               ← context cho Claude Code
├── HARNESS_SETUP.md        ← file này
├── .gitignore              ← chặn .transcripts/, context/private/, node_modules…
├── .claude/settings.json   ← hook prompt log, quyền, giữ transcript 365 ngày
├── .claude/skills/domain-bva-testing/   ← Agent Skill (bài nộp 10đ)
├── .claude/skills/test-case-writing/    ← skill của thầy, giữ nguyên
├── tools/                  ← extract_prompt_log.py, hooks/on_stop.py, summary.py, export_commit_log.ps1, hw.toml
├── context/                ← đề HW02, bài học HW01; slide PDF bỏ vào context/private/
├── HW01/                   ← giữ nguyên
└── HW02/                   ← khung thư mục bài làm
```

Bỏ 3 file slide (`S04_Domain_Testing.pdf`, `EN.DOMAIN_TESTING.pdf`, `EN.DOMAIN_TESTING_-_UC_Analysis.pdf`) vào `context/private/`.

## 3. Lấy transcript của session cloud

Các lượt AI từ 12/10 đến nay nằm ở session claude.ai, máy em không có transcript. Khi xong việc ở session đó, nhắn "xuất transcript" để nhận file `.jsonl`, rồi đặt vào `.transcripts/` (thư mục này bị gitignore — **không push, không nộp**, vì có thông tin hệ thống/cá nhân). Hook sẽ gộp nó với các session Claude Code trên máy.

## 4. Mở Claude Code lần đầu

```powershell
cd D:\HK7\Testing\Exercise\HW\software-testing-2627    # chỉnh theo đường dẫn thật
claude
```

Trong Claude Code:
1. `/add-dir ..\eshop-sut` — cho phép đọc mã nguồn SUT (nếu SUT nằm cạnh repo).
2. `/skills` — phải thấy `domain-bva-testing`, `test-case-writing` (project) và nhóm **claude.ai sync** có `cs423-ai-first-homework`… Thiếu nhóm sync → kiểm tra đăng nhập/phiên bản Claude Code.
3. `/hooks` — phải thấy hook **Stop** chạy `tools/hooks/on_stop.py`. Lần đầu Claude Code có thể hỏi xác nhận tin cậy thư mục/hook.
4. Kiểm tra nhanh: `python tools/hooks/on_stop.py --manual` → in "Đã ghi N lượt…".

Commit đầu tiên: `HW02: thêm harness (CLAUDE.md, skill domain-bva-testing, tools)`.

## 5. Bắt đầu làm

Prompt mẫu (gõ trong Claude Code, mỗi bước một lượt để log và commit tách bạch):

```
/domain-bva-testing HW02/A_FR01 0
/domain-bva-testing HW02/A_FR01 1
...
```

Sau mỗi bước: đọc `HW02/A_FR01/testcases.md`, sửa nếu cần, rồi bảo Claude commit theo quy ước trong CLAUDE.md. Bước 5 và 7 là phần em tự làm (🔒).

Ghi chú prompt log: mở `HW02/appendix/prompt_log_notes.toml`, xem số lượt bằng
`python tools/extract_prompt_log.py .transcripts/*.jsonl --since 2026-10-12 --list`, ghi Section/Mục đích/Xử lý. Log tự cập nhật sau mỗi lượt.

## 6. Bắt đầu bài mới (HWxx) – checklist

Làm trong commit đầu của bài (`HWxx: khung bài …`), trước lượt AI đầu tiên của bài.

1. **`tools/hw.toml`**: `hw = "HWxx"`, `title`, `log`/`notes`/`extra` → `HWxx/appendix/…`; cấu hình bài cũ giữ dạng comment.
   - `since` **theo giờ** (`"YYYY-MM-DD HH:MM"`, giờ Asia/Saigon) = lượt đầu của bài mới, không theo ngày (cùng ngày có thể còn lượt kết thúc bài cũ).
   - Lượt bài cũ vẫn lọt sau mốc → thêm vào `exclude` (khoá giờ như notes: `"YYYY-MM-DD HH:MM"`, `"…#k"`, khoảng `"A .. B"`).
   - Kiểm: `python tools/extract_prompt_log.py ".transcripts/*.jsonl" --since "<mốc>" --list`; chạy lại cho bài cũ với `--since/--until` cũ → số lượt không đổi.
   - Tạo `HWxx/appendix/prompt_log_notes.toml` và `prompt_log_extra.toml` (chỉ phần hướng dẫn).
2. **`.claude/settings.json`**: thêm 4 luật deny `Edit`/`Write` cho `/HWxx/appendix/ai-outputs/**` và `/HWxx/appendix/A_prompt_log.md`; kiểm hook **Stop** còn bật (`/hooks`).
3. **`HWxx/CLAUDE.md`** (≤ 120 dòng): đề, rubric, phạm vi, môi trường riêng, quyết định (hoặc trỏ tới `report_plan.md`), giới hạn riêng của bài, quy trình + mẫu commit. Cập nhật bảng bài ở đầu `CLAUDE.md` gốc. Phần chung chỉ sửa ở `CLAUDE.md` gốc.
4. **Đề + slide**: `context/HWxx_assignment.md` (pdftotext từ PDF đề); slide → `context/private/` (gitignore, không commit).
5. **`HWxx/.gitattributes`**: file không nộp (vd `report_plan.md`) → `export-ignore`; thử `git archive --format=zip -o <tmp>.zip HEAD HWxx` rồi liệt kê để chắc file đó không có trong zip.
6. **Transcript phiên thảo luận claude.ai** của bài: tải về, đặt `.transcripts/claude-ai_session_<HW>_p1.jsonl` (phần tiếp theo `_p2`, `_p3`…); không push, không nộp.
7. **Hỏi SV ngay từ đầu** (ghi vào `HWxx/CLAUDE.md`): **deadline thật** (giờ + ngày, đối chiếu Moodle, không chỉ đề) và **trình duyệt/thiết bị SV dùng thật** (phiên bản) – nền tảng kế hoạch phải là thứ SV chạy tay được.
8. **Quy tắc ảnh chốt trước lượt chạy tay** (ghi vào RUN/hướng dẫn): nội dung overlay theo đề, chụp gì (item Failed, ảnh tổng quan…), tên file theo item `P<n>_<id>_<k>.png`, thư mục gốc gitignore (`evidence_raw/`) + thư mục nộp.
9. **Khung cho SV điền** (file kết quả chạy, item SV bổ sung, phiếu phiên…) sinh từ schema/check script của skill, không viết tay – để check script bắt được trường trống/sai giá trị.
10. `python tools/hooks/on_stop.py --manual` → commit prompt log; nhắc SV push.

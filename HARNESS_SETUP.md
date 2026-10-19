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

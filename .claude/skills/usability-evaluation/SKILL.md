---
name: usability-evaluation
description: Lập và chạy một đợt usability test moderated theo bài giảng (Rubin & Chisnell – kế hoạch 9 phần, nhiệm vụ dạng mục tiêu, think-aloud, SEQ + SUS, câu hỏi mở), từ kế hoạch → participant kit → pilot → phiếu quan sát từng phiên (JSON) → tính SUS/SEQ/tỉ lệ hoàn thành/thời gian vào report → khung findings (severity × probability) → gom dữ kiện bug. Mỗi lần gọi một bước rồi dừng. Dùng khi người dùng nói "usability test", "kiểm thử khả dụng", "SUS", "SEQ", "think-aloud", "participant kit", "phiếu quan sát", "pilot usability", "findings usability", hoặc gọi /usability-evaluation kèm thư mục usability và số bước.
---

# Usability evaluation theo từng bước

Skill dẫn AI qua một đợt **usability test moderated** theo bài giảng (*The 9-part test plan*, *Summarizing the results*, *Analysis – from data to recommendations*; Rubin & Chisnell, *Handbook of Usability Testing*). **Mỗi lần gọi làm một bước rồi dừng** để người dùng (SV, người điều phối) review và commit.

Thư mục của một đợt (`<dir>`, vd `HW03/usability`):

| File | Bước | Ai viết |
|---|---|---|
| `plan.md` | 0 | AI nháp → SV chốt |
| `participant_kit.md` (1 trang) + `observation_sheet.md` (giấy, tuỳ chọn) | 1 | AI nháp → SV chốt |
| `pilot_changes.md` | 2 | script sinh diff, **SV ghi lý do** |
| `sessions/S0x.json` (S00 = pilot) | 3 | **SV nhập** (khung trống do script tạo) |
| bảng số liệu giữa marker trong report | 4 | `scripts/sus_score.py` |
| `findings.md` | 5 | **SV viết** (khung trống từ `assets/`) |
| `<bugs>/_groups_usability.md` | 6 | script gom dữ kiện; **SV viết bug** |

Schema phiếu phiên: `references/schema-session.md`. Danh mục kiểm kế hoạch 9 phần: `references/plan-9-parts.md`.

## Giới hạn của AI (bắt buộc)

1. **Không tạo danh sách người tham gia** (tên, tuổi, nghề, SĐT, Zalo…), không bịa hồ sơ. Bảng người tham gia do SV lập.
2. **Không viết ghi chú quan sát**, câu nói nguyên văn, mốc thời gian, kết quả hoàn thành của phiên nào. AI chỉ tạo khung trống.
3. **Không tạo/điền/ước lượng câu trả lời SUS, SEQ, câu hỏi mở**, kể cả khi thiếu một câu: script báo lỗi, SV hỏi lại người tham gia hoặc ghi phiên đó thiếu.
4. **Không viết phần tổng hợp/findings** (gom điểm đau, tách bug lẻ / vấn đề thiết kế, severity, probability, khuyến nghị) và không viết mô tả bug. AI chỉ dựng khung, tính số, gom dữ kiện có sẵn.
5. **Không đưa dữ liệu cá nhân của người tham gia cho AI.** Phiếu JSON chỉ có **mã ẩn danh** (`P01`…); SĐT nếu buộc phải ghi ở chỗ khác thì **che 4 số giữa** (vd `090****567`). Script từ chối phiếu có chuỗi ≥ 9 chữ số liền nhau hoặc email.
6. **Video/ghi âm** chứa giọng, màn hình người tham gia: AI không xử lý nội dung, không đăng công khai.
7. **Đóng băng output AI** (plan, kit, phiếu giấy) bằng `scripts/freeze.py` trước khi SV sửa; không sửa file đã đóng băng.
8. Quy định khoá học / `CLAUDE.md` hạn chế AI → quy định đó thắng skill này.

## Các bước

Gọi: `/usability-evaluation <dir> <bước>` — vd `HW03/usability 4`. Thiếu số bước → xem file nào đã có trong `<dir>` để đoán bước kế và hỏi lại.

### Bước 0 — Kế hoạch 9 phần
- Đọc phạm vi đã chốt (flow, nền tảng, số người tham gia, thang đo) và test basis (SRS, giao diện thật: tên nút, route) — không bịa nhãn.
- Viết `plan.md` đủ **9 phần theo slide**, đúng thứ tự: 1 Purpose · 2 Problem statement · 3 Test objectives & tasks · 4 User profile · 5 Method & test design · 6 Environment / equipment · 7 Test-monitor role · 8 Evaluation measures & data to collect · 9 Report contents. Nội dung từng phần: `references/plan-9-parts.md`.
- Nhiệm vụ lấy từ **mô hình người dùng, không từ code**: nêu mục tiêu + trạng thái đầu + tiêu chí thành công đo được + benchmark thời gian (giả định, chỉnh sau pilot). Chỗ SV phải chốt đánh 📝.
- **Hình thức (phần 5–6), SV chọn:**
  - *Trực tiếp (in-person moderated)*: người tham gia dùng máy của người điều phối, SUT chạy local.
  - *Từ xa đồng bộ (remote synchronous moderated)*: gọi video (vd Google Meet), người tham gia dùng máy của mình, **chia sẻ màn hình** và think-aloud; người điều phối quan sát, ghi phiếu. SUT chạy trên máy người điều phối, công khai tạm thời qua tunnel (vd Cloudflare quick tunnel; SUT gọi API bằng URL tuyệt đối `localhost` thì cần một nhánh local chỉ đổi sang đường dẫn tương đối + proxy, không đổi giao diện/logic). Mỗi phiên: **reset dữ liệu SUT + mở tunnel mới → link mới**, gửi ngay trước phiên, đóng tunnel sau phiên; **mỗi lần 1 người**; quay (vd Xbox Game Bar/OBS) **chỉ khi được đồng ý**. Ghi vào plan khác biệt môi trường so với kiểm thử chức năng (trình duyệt/OS của người tham gia, độ trễ Internet, nhánh tunnel). Người điều phối tự đi hết nhiệm vụ qua link (vd điện thoại 4G) trước pilot. Ví dụ script một phiên: `tools/usability_session.ps1` (restart backend → Vite → `cloudflared tunnel --url` → in link; Ctrl+C tắt) và `tools/sut_main.ps1` (đưa SUT về nhánh chính) trong repo HW03.
- `scripts/check_kit.py --plan <dir>/plan.md` → `freeze.py`. Dừng.

### Bước 1 — Participant kit (1 trang) + freeze
- `participant_kit.md` từ `assets/participant_kit_template.md`: lời mở đầu (kiểm tra web, không kiểm tra người; think-aloud; quyền dừng; xin đồng ý quay/ghi âm/liên hệ xác nhận), **nhiệm vụ dạng mục tiêu** (không nêu bước, không gọi tên nút/menu), **SEQ** 1–7, **SUS 10 câu tiếng Việt** (câu lẻ tích cực, câu chẵn tiêu cực, thang 1–5), **4 câu hỏi mở** (rõ ràng · khôi phục lỗi · tốc độ · tin cậy).
- Tuỳ chọn `observation_sheet.md` (bản giấy cho người điều phối) khớp các trường của `references/schema-session.md`.
- `scripts/check_kit.py --kit <dir>/participant_kit.md` → `freeze.py`. Dừng.

### Bước 2 — Pilot → sửa kit
- SV chạy pilot (không tính vào số phiên chính), ghi phiếu `sessions/S00.json` (`"pilot": true`).
- SV sửa kit/plan. AI chạy `scripts/kit_diff.py <bản-đóng-băng> <dir>/participant_kit.md -o <dir>/pilot_changes.md`: bảng từng thay đổi + cột **Lý do (SV)** = "(SV chưa ghi)". **SV tự ghi lý do**; AI không suy diễn lý do.
- `check_kit.py` lại. Dừng.

### Bước 3 — Phiếu quan sát từng phiên
- Trước mỗi phiên: `scripts/new_session.py <dir>/sessions S01` tạo khung trống (mọi giá trị `null`). Reset dữ liệu SUT theo plan (vd restart backend).
- SV ghi trong phiên (giấy hoặc trực tiếp) rồi nhập vào JSON: mốc thời gian, kết quả hoàn thành, sự kiện (L lỗi/chọn sai · D do dự · N câu nói nguyên văn · T trợ giúp), SEQ, 10 câu SUS, 4 câu hỏi mở. **AI không điền.**
- `scripts/sus_score.py <dir>/sessions --check` sau mỗi phiên: báo trường thiếu, SUS ≠ 10 câu hoặc ngoài 1–5, dữ liệu cá nhân. Dừng.

### Bước 4 — Tính số liệu → report
- `scripts/sus_score.py <dir>/sessions --report <report.md> --scope <mã> [--benchmark mm:ss] [--expect 7]`.
- SUS chuẩn: câu lẻ (x − 1), câu chẵn (5 − x), tổng × 2,5 → 0–100; trung bình, SD (mẫu, n − 1), median, min/max. SEQ: trung bình, median, min/max. Tỉ lệ hoàn thành (không trợ giúp / có trợ giúp / không hoàn thành; trong benchmark). Thời gian (phiên hoàn thành): trung bình, median, khoảng, SD. Lỗi/do dự/trợ giúp trung bình mỗi phiên. Pilot (`pilot: true`) không tính.
- Ghi đè nội dung giữa `<!-- REPORT:<scope>:usability_sessions:START/END -->` và `<!-- REPORT:<scope>:usability_summary:START/END -->`; marker chưa có → script in bảng và báo, không tự chèn. Không thêm nhận xét/diễn giải vào bảng. Dừng.

### Bước 5 — Khung findings (SV viết)
- AI chép `assets/findings_template.md` → `<dir>/findings.md` (trống), kèm số liệu bước 4 để SV tham chiếu.
- **SV viết**: gom điểm đau giống nhau (theo dữ kiện phiên), tách **bug lẻ** (lỗi chức năng tái hiện được) với **vấn đề thiết kế**, chấm **severity × probability = criticality** (thang trong template), khuyến nghị ưu tiên. AI chỉ được: đếm số phiên gặp một sự kiện SV đã nêu, kiểm trường thiếu, chỉ chỗ khẳng định quá dữ kiện. Dừng.

### Bước 6 — Gom dữ kiện bug (SV viết mô tả)
- SV đánh dấu sự kiện là bug trong phiếu (`"bug": true`). `scripts/bug_facts.py <dir>/sessions -o <bugs>/_groups_usability.md`: liệt kê phiên, mốc, màn hình, câu ghi nguyên văn của SV.
- Kiểm trùng bug đã biết / issue nhóm (`gh issue list`) → ghi "đã biết – #xx", không lập trùng.
- **Không** viết mô tả bug. SV viết bug; AI chạy bước tái hiện SV viết để cô lập nguyên nhân, tạo issue bằng `--body-file` của SV. Dừng.

## Script

| Script | Việc |
|---|---|
| `scripts/freeze.py <file>... --step k --out <hw>/appendix/ai-outputs --prefix T2 [--note "#n"]` | Đóng băng bất kỳ file nào, có timestamp + sha256, không ghi đè, ghi `INDEX.md` |
| `scripts/check_kit.py [--plan plan.md] [--kit participant_kit.md]` | Plan đủ 9 phần đúng thứ tự; kit có lời đồng ý, nhiệm vụ không nêu bước, SEQ 1–7, đúng 10 câu SUS, 4 câu hỏi mở, ≤ ~1 trang |
| `scripts/kit_diff.py <cũ> <mới> -o pilot_changes.md` | Bảng thay đổi sau pilot, cột lý do để SV ghi |
| `scripts/new_session.py <sessions-dir> S01 [--pilot]` | Khung phiếu trống từ `assets/session_template.json` |
| `scripts/sus_score.py <sessions-dir> [--check] [--report r.md --scope U1] [--benchmark mm:ss] [--expect 7]` | Kiểm phiếu + tính SUS/SEQ/hoàn thành/thời gian, ghi bảng giữa marker |
| `scripts/bug_facts.py <sessions-dir> -o _groups_usability.md` | Gom sự kiện SV đánh dấu bug |

## Quy ước

- Phiên chính thức = 1 người tham gia, 1 lượt nhiệm vụ, dữ liệu SUT đã reset. Phiên hỏng (lỗi môi trường) → ghi `ghi_chu`, không tính, chạy bù.
- Hoàn thành: `khong_tro_giup` / `co_tro_giup` (có ≥ 1 lần can thiệp) / `khong_hoan_thanh` (bỏ cuộc hoặc quá giới hạn thời gian của plan).
- Finding trùng bug đã biết → "đã biết – #xx". Số SUS chỉ mô tả mẫu nhỏ (n = 7), không suy rộng.

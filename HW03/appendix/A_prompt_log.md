# Prompt Log – HW03
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude (không rõ model), Claude Opus 5.5, Claude Sonnet 4.6

> Prompt và output được trích tự động, nguyên văn, từ transcript của công cụ AI bằng script `tools/extract_prompt_log.py` (không qua AI). Section, Mục đích và Xử lý do em tự ghi.

---

## #1 | 12:26 04/11/2026 | Claude Sonnet 4.6 | [...]
**Mục đích:** [...]

**Prompt:**
```
Giờ tôi sẽ bắt đầu thực hiện HW03 nhé /cs423-ai-first-homework . Đầu tiên đọc đề giúp tôi nhé
```
*Đính kèm:* `2026.HW03.GUI Usability_En.pdf`

**Output:**
```
Em sẽ nạp skill CS423 và đọc ghi chú môn học trước, rồi tóm tắt đề HW03.

# HW03 – GUI & Usability: tóm tắt đề

**Cấp độ AI:** Cấp 4 (AI hỗ trợ sản xuất; bạn thiết kế, audit, tích hợp). **Bloom-AI:** G9.3 Analyse + G9.4 Collaborate (theo §3 và §8). Bảng đầu đề ghi "G9.1 → G9.6 tuỳ bài", nên report ghi rõ là theo §3/§8, giống cách đã làm ở HW02. Agent Skill thuộc G9.5.

**Thời lượng đề ghi 10 giờ.** Deadline xem trên Moodle — bạn cho mình ngày cụ thể để lên lịch.

## Rubric

| # | Mục | Điểm | Nội dung chấm |
|---|---|---|---|
| 1 | Task 1 – GUI Checklist | 30 | Thiết kế > 40 item, chạy, bug report |
| 2 | Task 2 – Usability | **40** | Kịch bản, 7 phiên, phân tích |
| 3 | Task 3 – Cross-platform | 20 | Chạy Task 1 trên ≥ 3 nền tảng |
| 4 | Agent Skills | 10 | Đề ghi "encouraged" nhưng có 10 điểm, kèm video YouTube |

Task 2 nặng nhất và phụ thuộc vào người thật, nên cần **tuyển người sớm**.

## Từng task

**Task 1 – GUI Checklist**
- Cần **≥ 41 item** (đề ghi "more than 40") phủ đủ 4 khía cạnh: IA-01 chuẩn UI chung, IA-02 form, IA-03 điều hướng, IA-04 phản hồi/trạng thái. Nên chọn nhiều màn hình.
- AI sinh bộ đầu → đóng băng vào `ai-outputs/` → bạn review → **bạn tự thêm item AI bỏ sót và giải thích vì sao AI bỏ sót**. Đây là phần G9.3: mình sẽ không gợi ý các item này.
- Chạy checklist, chỉ đánh **Passed/Failed**. Cột Notes ghi lý do cho mỗi item Failed. Chỉ chụp ảnh item Failed.
- Bug ghi trong .md và trên GitHub Issues, kèm ảnh. Bug report do bạn viết 100%.

**Task 2 – Usability (7 người thật + 1 pilot)**
- *Pha 1:* viết mục tiêu, kịch bản dạng mục tiêu (không đưa từng bước), chọn thang SUS hoặc UEQ-S, soạn câu hỏi mở (tối thiểu về: rõ ràng, khôi phục lỗi, tốc độ, tin cậy). Tuyển 7 người **ngoài lớp HW03**, có liên hệ kiểm chứng được (che 4 số giữa). Chạy 1 phiên pilot.
- *Pha 2:* mỗi phiên cho người tham gia nói to suy nghĩ (think-aloud), bạn quan sát trung lập. Quay màn hình (kèm audio nếu được đồng ý), ghi chú có cấu trúc, rồi cho điền SUS và hỏi câu hỏi mở.
- *Pha 3:* tính điểm SUS, gom các điểm đau, tách bug lẻ khỏi vấn đề thiết kế hệ thống, xếp theo mức nghiêm trọng. Bug thật lên GitHub Issues.
- **TA có thể gọi ngẫu nhiên 2 người. Mạo danh = 0 điểm Task 2.**

**Task 3 – Cross-platform**
- Chạy Task 1 trên ≥ 3 nền tảng: Chrome, Firefox, Safari (hoặc Android Chrome).
- **Expo Go được thay 1 nền tảng.** Bạn đã có POCO F5 + Expo Go từ HW02D, nên dùng được.
- Đề ưu tiên BrowserStack/LambdaTest. SUT chạy localhost nên cần tunnel (BrowserStack Local). Thiết bị thật cũng chấp nhận.
- Ảnh chụp phải thấy tên browser/OS/thiết bị + URL localhost + thông tin của bạn.

## Chỗ mâu thuẫn / dễ sót

| Mã | Vấn đề | Đề xuất |
|---|---|---|
| M1 | Overlay trên ảnh: §6 ghi "username dạng **email SV**", §11 ghi "**MSSV + họ tên**" | Overlay đủ cả 3 (email, MSSV, họ tên) trên mọi ảnh cross-platform |
| M2 | "Perform Task 1 across ≥ 3 platforms": chạy **toàn bộ** checklist × 3 hay một phần? | Cần bạn quyết, vì ảnh hưởng thời gian lớn (41+ item × 3) |
| M3 | Checklist chỉ có Passed/Failed, nhưng một số item có thể không áp dụng trên một nền tảng (ví dụ Expo Go) | Quyết trước có dùng N/A hay không, và ghi giả định |
| M4 | **Không trùng với thành viên nhóm**: màn hình chính của checklist và flow usability | Cần chốt với nhóm tkob-team trước khi bắt đầu |
| M5 | Bảng Bloom đầu đề ↔ §3/§8 | Ghi G9.3 + G9.4 như HW02 |
| M6 | Excel bắt buộc ("Excel checklist + test summary"); Homework Policies yêu cầu chép bảng tổng hợp sang .md | Làm Excel 3 sheet + chép bảng sang report |
| M7 | Video quay màn hình phiên usability có giọng và dữ liệu của người tham gia; giới hạn 20 MB/file | Cần form đồng ý; không đăng công khai; ưu tiên link Drive giới hạn quyền; che thông tin cá nhân trước khi đưa cho AI (AI-05) |
| M8 | Commit cho **mỗi bước**, kể cả **mỗi phiên usability** | Khoảng 7–8 commit chỉ riêng Task 2 |
| M9 | Bug HW02 đã biết có thể làm flow usability không đi hết được (ví dụ giỏ web là state React, không lưu khi tải lại trang) | Phiên pilot sẽ lộ ra; đề cũng yêu cầu tách "blocker" khỏi lỗi nhỏ |

## Phần AI không được làm (danh mục cấm của bài này)

- Danh sách 7 người tham gia
- Ghi chú quan sát, câu trả lời SUS
- Ảnh cross-platform có overlay
- Item "AI bỏ sót" + lý do
- Bug report
- Critique
- Verdict + lý do Audit
- Điểm tự chấm
- Giọng thuyết minh video

**Cần bạn quyết:** phần tổng hợp usability (gom điểm đau, xếp mức nghiêm trọng) là phần phân tích được chấm. Mình đề xuất bạn tự làm; AI chỉ tính điểm SUS và dựng bảng.

## Biểu mẫu AI (§0)

| Form | Bắt buộc? | Ghi chú |
|---|---|---|
| AI-02 Audit | ✅ | .md + PDF (đề ghi "AI Critique and AI Audit Report (Markdown + PDF)") |
| AI-03 Disclosure | ✅ | .md + PDF |
| AI-04 Reflective | ❌ | HW thường, đề không yêu cầu |
| AI-05 Privacy | ✅ | Làm cuối. Bài này có **dữ liệu cá nhân người tham gia** nên cần chú ý hơn HW02 |
| AI-06 | Đã nộp tuần 1 | Bạn xác nhận lại giúp |

Câu tuyên bố nguyên văn: *"I use AI tools for the following tasks,"*. Tên zip: `23120255_HW03_AI_GUIUsability_<ggg>.zip`.

## Bạn cho mình biết để lập `HW03/report_plan.md` + dàn ý

1. Deadline?
2. Các thành viên nhóm đã chọn màn hình/flow nào (để tránh trùng)?
3. Có slide bài giảng GUI checklist và usability không? Đề yêu cầu checklist bám theo bài giảng, bạn đính kèm giúp.
4. Quyết M2 và M3 theo mẫu `M2=…, M3=…`.
5. Tài khoản BrowserStack/LambdaTest: còn trial không, hay dùng thiết bị thật? Có máy Mac/iPhone để test Safari không?
```

**Xử lý:** [...]

---

## #2 | 12:31 04/11/2026 | Claude Sonnet 4.6 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. 07/11/2026
2. Chưa chọn, vậy bạn có thể đọc repo để đề xuất tôi nên chọn màn hình/flơ nào không?
3. Mình nghĩ là các list youtube thầy đã tạo và đăng trên youtube: https://www.youtube.com/watch?v=aXYxOUiB_zE&list=PLZJXFppLOLwY (GUI Testing); https://www.youtube.com/watch?v=taPQaxYm8Aw&list=PLYH1dAAH7CDo (Usabiity Testing); https://www.youtube.com/watch?v=taPQaxYm8Aw&list=PLYH1dAAH7CDo (Compability Testing)
4. M2=Toàn bộ; M3= dùng thêm N/A và ghi giả định
5. Mấy tài khoản này là gì mình không biết?
```

**Output:**
```
Mình sẽ clone SUT để đọc các màn hình và flow, đồng thời tra thông tin trial BrowserStack/LambdaTest.

No response requested.
```

**Xử lý:** [...]

---

## #3 | 12:31 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Continue with the task described in the conversation above. Your most recent mcp__claude-code-remote__add_repo call has not run yet; nothing is wrong with the tool or its input. Run it now from the beginning with the tools you have, without assuming any result, file or state from it, and use the working directory and file locations you have now rather than ones earlier steps assumed.

The files from earlier in this conversation are available at these paths:
/mnt/user-data/uploads/2026_HW03_GUI_Usability_En.pdf
Read them there (those copies are read-only — copy a file elsewhere to modify it). Each is also attached, at an @-mentioned path, to this message or the file-delivery messages just before it; if a listed path is missing, use that @-mentioned copy instead.

The user's timezone is Asia/Saigon (UTC+07:00).
```
*Đính kèm:* `2026.HW03.GUI_Usability_En.pdf`

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #4 | 12:32 04/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
[Request interrupted by user]
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #5 | 12:33 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. 07/11/2026
2. Chưa chọn, vậy bạn có thể đọc repo để đề xuất tôi nên chọn màn hình/flơ nào không?
3. Mình nghĩ là các list youtube thầy đã tạo và đăng trên youtube: https://www.youtube.com/watch?v=aXYxOUiB_zE&list=PLZJXFppLOLwY (GUI Testing); https://www.youtube.com/watch?v=taPQaxYm8Aw&list=PLYH1dAAH7CDo (Usabiity Testing); https://www.youtube.com/watch?v=taPQaxYm8Aw&list=PLYH1dAAH7CDo (Compability Testing). À cùng với các slide mình cũng đang gửi cho bạn nhé
4. M2=Toàn bộ; M3= dùng thêm N/A và ghi giả định
5. Mấy tài khoản này là gì mình không biết?
```
*Đính kèm:* `EN.GUI__Usability__Compatibility_Testing_AI-First_Combined.pdf`, `GUI-VulqUpdated.UsabilityTesting.pdf`, `S13_GUI_Testing__Usability_Testing.pdf`, `EN.UsabilityTesting.pdf`

**Output:**
```
Mình sẽ trích chữ từ các slide để đọc nhanh, đồng thời kiểm xem hai file "Combined" có trùng nhau không.

## 1. Phát hiện quan trọng khi đọc repo

Đề ghi *"specification does not assign FR codes to the UI concerns"*, nhưng `README.md` §8 của SUT (dòng 240–272) **có sẵn** FR-21 → FR-24, khớp đúng 4 khía cạnh của đề:

| IA trong đề | SRS | Nội dung (tóm tắt) |
|---|---|---|
| IA-01 | FR-21 | Tiếng Việt, màu nút xanh/đỏ, `₫` phân cách hàng nghìn, 1 `<h1>`/trang, thứ tự Tab |
| IA-02 | FR-22 | `*` cho trường bắt buộc, `type="email"`/`password`, lỗi **trên** nút submit, Step Indicator |
| IA-03 | FR-23 | Navbar highlight trang hiện tại, badge giỏ hàng, nhãn "Đăng xuất", breadcrumb |
| IA-04 | FR-24 | Phản hồi khi thêm giỏ, hộp thoại xác nhận xoá, empty state, `alt` ảnh |

FR-05 → FR-08 cũng có yêu cầu UI (loading, empty state, nút +/-, nhãn "Tổng cộng"…). Nghĩa là checklist có **căn cứ đặc tả** cho Expected, giống cách làm ở HW02. Mình ghi đây là mâu thuẫn M10 trong kế hoạch: report nêu ánh xạ IA ↔ FR một lần.

## 2. Đề xuất phạm vi

**Task 1 – Checklist:** chọn cụm **cửa hàng web** (`:5173`): Trang chủ, Chi tiết SP, Giỏ hàng, Thanh toán, cộng thêm navbar và 2 form Đăng nhập/Đăng ký. Màn hình chính khai với nhóm: **Giỏ hàng**.
- Hầu hết điều khoản FR-21…24 nhắm vào đúng các màn này (badge, breadcrumb, hộp thoại xoá, empty state…), nên đủ 41+ item mà không lặp.
- Cùng một frontend nên chạy giống hệt trên 3 trình duyệt (M2 = toàn bộ), ít N/A.
- Phương án dự phòng nếu bạn cùng nhóm đã lấy cụm này: **Admin** (`:5174`, 6 tab Dashboard/Danh mục/Sản phẩm/Coupon/Đơn hàng/Người dùng). Nhiều form/bảng nên rất giàu item cho IA-02, nhưng chỉ có bản desktop.

**Task 2 – Flow usability** (chọn 1, tuỳ nhóm đã lấy gì):

| Mã | Flow | Ưu | Nhược |
|---|---|---|---|
| U1 | Đăng nhập (tài khoản cho sẵn) → tìm SP → thêm giỏ → thanh toán với mã giảm giá → xem đơn trong Hồ sơ | Trùng màn với Task 1 nên hai phần bổ trợ nhau; người không làm IT hiểu ngay | Là ví dụ trong đề nên **dễ trùng nhóm** |
| U2 | Quên mật khẩu (2 bước) → đăng nhập → xem lịch sử đơn → huỷ đơn | Ngắn, có form 2 bước và trạng thái đơn; ít ai chọn | Cần dựng sẵn đơn hàng trước mỗi phiên |
| U3 | U1 nhưng trên **Expo Go** (điện thoại của bạn) | Gần thực tế mua sắm của người Việt | Mỗi phiên phụ thuộc Wi-Fi ký túc xá + IP LAN |

Mình nghiêng về **U1 nếu nhóm chưa ai lấy**, không thì U2. Lưu ý: `node server.js` xoá và seed lại CSDL, nên restart backend trước mỗi phiên sẽ đưa mã giảm giá về trạng thái chưa dùng (ví dụ `SAVE10` chỉ 1 lượt/người). Mỗi người tham gia bắt đầu từ cùng trạng thái.

## 3. BrowserStack / LambdaTest là gì

Đây là các dịch vụ "thuê máy từ xa": bạn mở trang web của họ và điều khiển một trình duyệt/điện thoại thật (Safari trên Mac, iPhone…) đặt ở trung tâm dữ liệu của họ. Muốn test `localhost` thì cài thêm tunnel (BrowserStack Local) để máy từ xa vào được máy bạn.

Trial **quá ít** cho M2 = toàn bộ:
- **BrowserStack:** gói Live chỉ có 30 phút, mỗi thiết bị 1 phút, kèm 100 ảnh chụp.
- **LambdaTest** (nay đổi tên là TestMu AI): gói miễn phí chỉ cho phiên tương tác 2 phút mỗi tháng.

Chạy 41+ item trên Safari không thể xong trong 1 phút. Đề cho phép dùng thiết bị thật, nên mình đề xuất:

| Nền tảng | Cách chạy |
|---|---|
| P1 | Chrome trên Windows (PC của bạn) |
| P2 | Firefox trên Windows |
| P3 | **Chrome Android trên POCO F5**, dùng `adb reverse tcp:5173 tcp:5173` và `adb reverse tcp:3000 tcp:3000` |

Với P3, URL vẫn là `localhost:5173`, đúng yêu cầu ảnh chụp. Cách này còn **bắt buộc** vì web gọi cứng `http://localhost:3000` ở 14 chỗ (`Checkout.jsx`, `AuthContext.jsx`…), nên mở bằng IP LAN sẽ hỏng.

Expo Go chỉ nên làm nền tảng thứ 3 nếu checklist có màn mobile: các item web như `<h1>` hay `type="email"` sẽ thành N/A hàng loạt trên app native. Tuỳ chọn thêm: đăng ký trial BrowserStack chụp vài ảnh Safari làm bằng chứng phụ ("strongly preferred"), không dùng để chạy chính.

## 4. Slide và YouTube

Mình không xem được video, nhưng 5 file slide đã đủ. Hai file "Combined" giống hệt nhau. Điểm liên quan trực tiếp:
- Checklist chấm **Yes / No / N/A** kèm priority & severity. Slide này là căn cứ cho M3 (dùng N/A), report trích được.
- Nguồn tạo checklist: đặc tả, Nielsen 10, Norman 6, Shneiderman 8, WCAG, checklist theo từng control (Waghmare).
- Usability theo Rubin & Chisnell: kế hoạch 9 phần; xếp ưu tiên theo **criticality = severity × probability**.

## 5. Rủi ro lịch

Deadline **thứ Bảy 07/11**, hôm nay trưa thứ Tư, tức còn khoảng 2,5 ngày. Đường găng là **pilot + 7 phiên với người thật**, nên **hôm nay phải tuyển người**. Lịch gợi ý:

| Ngày | Việc |
|---|---|
| T4 | Kế hoạch, tuyển người, AI nháp checklist + kịch bản |
| T5 | Review checklist, chạy P1, pilot, phiên 1–4 |
| T6 | Chạy P2 và P3, phiên 5–7 |
| T7 | Phân tích, bug, form, zip |

Skill + video (10 điểm) nên làm gọn, dùng lại khung skill HW02.

## Bạn chốt giúp

- **S1** = cụm cửa hàng web / Admin. **U** = U1 / U2 / U3. Cả hai sau khi hỏi nhóm.
- **P3** = Android Chrome (đề xuất) / Expo Go.
- Giờ nộp cụ thể ngày 07/11?

Chốt xong mình sẽ lập `HW03/report_plan.md` và đưa lệnh đầu tiên cho Claude Code.

Sources:
- [BrowserStack – What do I get with a free trial](https://www.browserstack.com/support/faq/plans-pricing/plans/what-do-i-get-with-a-free-trial)
- [TestMu AI (ex-LambdaTest) – Pricing](https://www.testmuai.com/pricing/?fp_ref=nick92)
- [BrowserStack – Test localhost với Local Testing](https://www.browserstack.com:443/docs/live/local-testing/test-using-local-testing)
```

**Xử lý:** [...]

---

## #6 | 17:02 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Máy mình không có Firefox. Hiện tại mình đang sử dụng Cốc Cốc để làm. Và máy mình có thêm Chrome và Microsoft Edge thôi nhé.
HW02 mình đã làm Domain Testing, thầy có bảo HW04 thì có thể lấy các test case bên đó để sử dụng. Vậy theo bạn HW này bạn có cần xem Domain Testing trước đó không?
Mà bạn cũng đọc cả repo SUT rồi nhỉ
Task 1: Bạn cứ giúp mình chia 3 ra để đủ cho 3 người rồi chọn nhé. Tránh trường hợp mình chọn nhiều quá thì người khác không làm việc được.
Task 2: Bạn thấy phần nào dễ làm và dễ viết nhất thì chọn nhé, vì nhóm mình chưa ai chọn cả.
Vậy phần BrowserStack / LambdaTest mình nên làm gì nhỉ
===
Rủi ro lịch, mình sẽ cố hoàn thành tất cả T4,T5,T6 trong hôm nay
P3 cứ theo bạn đề xuất nhé, nhưng hãy đảm bảo, kiểm chứng trước mình có thể làm nhé
```

**Output:**
````
Mình sẽ kiểm vài chỗ trong SUT (cấu hình Vite cho `adb reverse`, luồng thanh toán) và mở repo bài nộp để xem danh sách bug HW02.

## 1. Có cần xem HW02 không?

**Không cần test case HW02, nhưng cần danh sách bug HW02.** HW02 phần B đã báo khá nhiều bug GUI ở trang chủ và giỏ hàng:

| Bug HW02 | Nội dung |
|---|---|
| BUG-16 | Không có phản hồi khi thêm giỏ |
| BUG-19 | Xoá không có hộp thoại xác nhận |
| BUG-20 | Thiếu badge giỏ hàng |
| BUG-21 | Empty state thiếu hình minh hoạ |
| BUG-22 | Thiếu breadcrumb |
| BUG-23 | Navbar không highlight trang hiện tại |
| BUG-24 | Hiển thị "VND" thay vì "₫" |
| BUG-25 | `alt` rỗng |
| BUG-26…29 | Sai nhãn |

Ngoài ra còn BUG-12/13 (form Đăng ký) và BUG-49/50 (form/bảng Admin sản phẩm).

Ở HW03, item checklist chạm lại các chỗ này vẫn đánh **Failed**, nhưng Notes ghi "trùng BUG-xx (#…)" thay vì tạo issue mới (luật kiểm trùng). Hệ quả: **chọn màn ít bị HW02 phủ thì tìm được nhiều bug mới hơn**, mà số bug là căn cứ phân hoá điểm.

Mình đã đọc SUT (`tkob-team/eshop-sut @de0f48f`) và repo bài nộp. Repo **chưa có thư mục HW03**.

## 2. Task 1: chia 3 cụm cho nhóm

| Cụm | Màn hình | Đã bị HW02 phủ |
|---|---|---|
| **C1 – Mua hàng (web)** | Trang chủ, Chi tiết SP, Giỏ hàng, Thanh toán, navbar | Nhiều (khoảng 15 bug ở HW02-B) |
| **C2 – Tài khoản (web)** | Đăng nhập, Đăng ký, Quên mật khẩu (2 bước), Hồ sơ + Lịch sử đơn | Ít (chỉ 3 bug form Đăng ký) |
| **C3 – Admin (web)** | Đăng nhập admin, Dashboard, Danh mục, Sản phẩm, Coupon, Đơn hàng, Người dùng | Ít (chỉ tab Sản phẩm) |

**Bạn lấy C2.** Lý do:
- Nhiều form, kể cả form 2 bước có Step Indicator (FR-03, FR-22), nên dễ phủ đủ IA-02.
- Ít trùng HW02.
- Chạy được y hệt trên 3 trình duyệt.

C1 và C3 để cho 2 bạn còn lại. Nhóm có người thứ 4 thì thêm C4 = app mobile.

## 3. Task 2: flow dễ làm và dễ viết nhất

Chọn **U1 – mua hàng có mã giảm giá**:
- **Kịch bản dạng mục tiêu:** đăng nhập bằng tài khoản cho sẵn → tìm một sản phẩm → thêm vào giỏ → thanh toán với mã giảm giá → kiểm tra đơn trong Hồ sơ.
- **Dễ chạy:** người không làm IT hiểu ngay, khoảng 5–8 phút/phiên, tiêu chí thành công rõ (đặt được đơn đã giảm giá).
- **Không trùng với C2 của bạn**, nên report có thêm góc nhìn.
- **Restart backend trước mỗi phiên** (`node server.js` seed lại CSDL) để mọi người bắt đầu cùng trạng thái, mã `SAVE10` dùng lại được.

Lưu ý: người tham gia sẽ vấp vào các bug HW02 đã biết trên flow này (ví dụ BUG-15: lần bấm "Thêm vào giỏ" đầu tiên bị nuốt). Phần phân tích ghi chúng là "bug đã biết", tách khỏi vấn đề thiết kế. Phiên pilot sẽ cho biết flow có đi hết được không.

## 4. Trình duyệt và BrowserStack

**Chrome, Edge và Cốc Cốc đều là Chromium** (cùng engine Blink), nên chạy cả ba gần như là chạy một. Đề đòi Chrome + Firefox + Safari (hoặc Android Chrome). Đề xuất:

| | Nền tảng | Engine |
|---|---|---|
| P1 | Chrome trên Windows | Blink |
| P2 | **Firefox trên Windows** — cài miễn phí, khoảng 5 phút | Gecko |
| P3 | Chrome Android trên POCO F5, qua `adb reverse` | Blink trên mobile |

**BrowserStack/LambdaTest: bỏ qua.** Đề cho phép dùng thiết bị thật. Trial quá ít (30 phút, mỗi thiết bị 1 phút) để chạy toàn bộ 41+ item. Report ghi một câu lý do này. Còn dư giờ cuối bài thì mới tính chuyện chụp thêm vài ảnh Safari.

## 5. Kiểm chứng P3 trước

**Phần mình đã kiểm trên code:**
- Backend `app.listen(3000)` nghe mọi interface, `cors()` mở.
- Web gọi cứng `http://localhost:3000`, nên `adb reverse` cả 3000 lẫn 5173 là cách đúng.

**Một rủi ro mình chưa kiểm được từ đây:** Vite 8 trên Windows có thể chỉ nghe ở IPv6 `::1`, trong khi `adb reverse` nối tới 127.0.0.1. Vì vậy lệnh dưới ép Vite chạy `--host 127.0.0.1`.

Phần trên điện thoại chỉ bạn làm được:

**Trên POCO** (làm trước, khoảng 2 phút):
1. Cài đặt → Giới thiệu điện thoại → bấm 7 lần vào **Phiên bản OS**.
2. Cài đặt bổ sung → Tùy chọn nhà phát triển → bật **Gỡ lỗi USB**.
3. Cắm cáp vào PC, chọn "Truyền tệp", bấm **Cho phép** khi hiện hộp thoại khoá RSA.

**Lệnh cho Claude Code:**
```
HW03 – kiểm chứng P3 (chỉ kiểm, chưa commit gì)
1. gh issue list -R tkob-team/eshop-sut --state all -L 500 --json number,title,author > $env:TEMP\issues.json; in số issue theo author.
2. adb version; nếu thiếu: hỏi tôi trước khi tải platform-tools (dl.google.com), giải nén vào D:\Tools\platform-tools.
3. adb devices (phải thấy 1 thiết bị "device").
4. Chạy ..\eshop-sut\backend: node server.js (nền); ..\eshop-sut\frontend-web: npx vite --host 127.0.0.1 --port 5173 (nền).
5. adb reverse tcp:5173 tcp:5173; adb reverse tcp:3000 tcp:3000; adb reverse --list.
6. Dừng, chờ tôi mở Chrome trên điện thoại vào http://localhost:5173 và đăng nhập test@eshop.com/Test1234!.
Báo cáo ≤ 10 dòng: kết quả từng bước + lỗi nguyên văn nếu có.
```

Thành công khi trên điện thoại thấy **danh sách sản phẩm** (nghĩa là gọi được :3000) và **đăng nhập được**. Nếu bước 3 hoặc 5 lỗi, phương án dự phòng là Expo Go (đã chạy được ở HW02D), nhưng checklist web sẽ có nhiều N/A hơn.

## 6. Việc nên làm ngay, song song

**Nhắn tuyển 7 người + 1 người pilot ngay bây giờ.** Đây là phần duy nhất phụ thuộc người khác.

Sau khi bạn báo kết quả P3 và xác nhận **C2 + U1 + cài Firefox**, mình lập `HW03/report_plan.md` + dàn ý và đưa lệnh cho AI nháp checklist.
````

**Xử lý:** [...]

---

## #7 | 17:09 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Ở HW02 mình đã làm các phần này: 
A - 	FR-01: Đăng ký
B - 	FR-07: Giỏ hàng
C - 	FR-15: Product CRUD
D -  FR-20: Đăng ký trên Mobile
===
Bạn nghĩ GUI này có nên làm lại các phần này không?
```

**Output:**
```
**Không nên lấy lại làm trọng tâm**, vì 3 lý do:

1. **Bug sẽ trùng.** Các lỗi GUI rõ nhất ở Đăng ký và Giỏ hàng bạn đã báo rồi: BUG-12/13/14 (form Đăng ký), BUG-16…29 (giỏ hàng), BUG-49/50 (form/bảng Admin sản phẩm), BUG-55/56/57 (Đăng ký mobile). Làm lại thì item vẫn Failed, nhưng phần lớn chỉ ghi "trùng BUG-xx", ít bug mới. Số bug lại là căn cứ phân hoá điểm.
2. **Đề chấm độ phủ "thorough and non-repetitive".** Lặp lại màn đã kiểm thì độ phủ thực của bạn trên SUT không tăng.
3. **Vấn đáp dễ bị hỏi:** "HW03 em kiểm gì mới so với HW02?"

Chỉ có một lý lẽ ngược lại: HW02 là Domain Testing (giá trị nhập vào), chưa xét thứ tự Tab, bố cục, màu nút, khả năng truy cập… trên các màn đó. Nhưng màn khác cũng có những khía cạnh này, nên lý lẽ này không đủ để chọn lại.

## Điều chỉnh đề xuất

| | Trước | Sau |
|---|---|---|
| **C2 (của bạn)** | Đăng nhập, Đăng ký, Quên mật khẩu, Hồ sơ + Lịch sử đơn | **Bỏ Đăng ký** → Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ + Lịch sử đơn, navbar khi đã đăng nhập |
| **U1 (usability)** | Giữ nguyên | Dùng tài khoản cho sẵn, không qua Đăng ký. Flow có đi qua Giỏ hàng, nhưng usability là kỹ thuật khác (đo người dùng thật, SUS), không lặp HW02. Bug giỏ hàng người tham gia vấp phải thì ghi "đã biết – BUG-xx" |

C2 bỏ Đăng ký vẫn đủ 41+ item cho 4 khía cạnh:
- `Profile.jsx` có 217 dòng: sửa thông tin, danh sách đơn, huỷ đơn.
- Quên mật khẩu có form 2 bước.
- Đăng nhập có khoá tài khoản sau 3 lần sai (FR-02), tức có trạng thái/phản hồi để kiểm.

**Cho nhóm:** bạn nào nhận C1 (Mua hàng) nên biết BUG-16…29 đã có trên fork `tkob-team/eshop-sut`, để kiểm trùng trước khi tạo issue.

Bạn xác nhận **C2 (bỏ Đăng ký) + U1** và chạy lệnh kiểm P3 ở trên. Xong mình lập `report_plan.md`.
```

**Xử lý:** [...]

---

## #8 | 17:11 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Rồi, viết lại cả C1, C2, C3 để mình đưa cho nhóm nhé. Mình oke với U1 nhé
===
còn lệnh P3 kia chạy trong SUT đúng không?
Còn phần tuyển người kia, tuyển người biết sử dụng code hay không? Và có bắt họ làm lâu không?
```

**Output:**
````
## 1. Tin nhắn chia việc cho nhóm (dán vào nhóm)

```
HW03 – chia phạm vi GUI checklist (đề §5: không ai trùng màn hình chính / flow usability)

C1 – Mua hàng (web :5173): Trang chủ, Chi tiết sản phẩm, Giỏ hàng, Thanh toán (+ navbar khi chưa đăng nhập)
  Lưu ý: fork tkob-team/eshop-sut đã có BUG-15…29 (giỏ hàng, trang chủ) → kiểm trùng trước khi tạo issue.

C2 – Tài khoản (web :5173): Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ + Lịch sử đơn / huỷ đơn (+ navbar khi đã đăng nhập)
  → Hiệp nhận.

C3 – Admin (web :5174): Đăng nhập admin, Dashboard, Danh mục, Sản phẩm, Coupon, Đơn hàng, Người dùng
  Lưu ý: tab Sản phẩm đã có BUG-35…50 trên fork.

(C4 – App mobile qua Expo Go, nếu nhóm có thêm người)
Màn Đăng ký (web + mobile) không ai lấy làm chính: đã kiểm kỹ ở HW02.

Flow usability (Task 2) – mỗi người 1 flow khác nhau:
  U1 Đăng nhập → tìm SP → thêm giỏ → thanh toán có mã giảm giá → xem đơn trong Hồ sơ  → Hiệp nhận.
  U2 Quên mật khẩu → đăng nhập lại → xem lịch sử đơn → huỷ đơn
  U3 Admin: thêm sản phẩm → tạo mã giảm giá → xác nhận/giao một đơn hàng
  U4 U1 trên app mobile (Expo Go)

Mọi người nhận C và U nào thì reply nhé. Không chia sẻ prompt/skill cho nhau (đề §17: chép prompt = 0 điểm cả hai).
```

## 2. Lệnh P3 chạy ở đâu?

**Chạy trong repo bài nộp**, như mọi lệnh HW02: mở Claude Code tại `D:\HK7\Testing\Exercise\HW\software-testing-2627`. Lệnh đã trỏ sang SUT bằng `..\eshop-sut\backend` và `..\eshop-sut\frontend-web`, nên không cần mở Claude Code trong thư mục SUT. Bước 1 (`gh issue list`) cần `gh` đang đăng nhập `ThachHaoo` như HW02.

## 3. Tuyển người

**Có cần biết code không? Không.** Đề ưu tiên người **không làm IT / không làm tester**. Hồ sơ người dùng mục tiêu cho U1:
- Từ 18 tuổi trở lên, **đã từng mua hàng online** (Shopee, Lazada, Tiki…), biết dùng máy tính.
- **Không học lớp CS423/HW03** kỳ này.
- Có Zalo hoặc số điện thoại để TA gọi kiểm chứng. Đề nói TA có thể gọi ngẫu nhiên 2 người, nên **báo trước cho họ** việc này.

Bạn cùng phòng ký túc xá, bạn khác ngành, người nhà… đều được. Cần **8 người**: 1 pilot (không tính vào 7) + 7 phiên chính.

**Có lâu không?** Khoảng **15–20 phút/người**:

| Phần | Thời gian |
|---|---|
| Giới thiệu, xin đồng ý quay màn hình + ghi âm | ~2 phút |
| Làm nhiệm vụ U1, vừa làm vừa nói suy nghĩ | ~5–8 phút |
| Điền SUS (10 câu) | ~2 phút |
| Câu hỏi mở | ~3–5 phút |

**Nên làm trực tiếp trên PC của bạn.** SUT chạy localhost nên người tham gia phải ngồi tại máy. Làm từ xa thì phải cho họ điều khiển máy bạn qua UltraViewer/AnyDesk, phức tạp hơn.

**Tin nhắn mời mẫu** (bạn sửa theo giọng mình):
```
Mình đang làm bài môn Kiểm thử phần mềm, cần nhờ bạn khoảng 15–20 phút dùng thử một trang web bán hàng trên máy mình (không cần biết code). Mình kiểm tra trang web chứ không kiểm tra bạn. Mình sẽ quay màn hình + ghi âm (nếu bạn đồng ý), và trợ giảng có thể gọi bạn để xác nhận là bạn có tham gia. Bạn rảnh lúc nào tối nay không?
```

Gửi lời mời ngay, rồi chạy lệnh kiểm P3. Trong lúc chờ kết quả, mình lập `report_plan.md`.
````

**Xử lý:** [...]

---

## #9 | 17:15 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – kiểm chứng P3 (chỉ kiểm, chưa commit gì)
1. gh issue list -R tkob-team/eshop-sut --state all -L 500 --json number,title,author > $env:TEMP\issues.json; in số issue theo author.
2. adb version; nếu thiếu: hỏi tôi trước khi tải platform-tools (dl.google.com), giải nén vào D:\Tools\platform-tools.
3. adb devices (phải thấy 1 thiết bị "device").
4. Chạy ..\eshop-sut\backend: node server.js (nền); ..\eshop-sut\frontend-web: npx vite --host 127.0.0.1 --port 5173 (nền).
5. adb reverse tcp:5173 tcp:5173; adb reverse tcp:3000 tcp:3000; adb reverse --list.
6. Dừng, chờ tôi mở Chrome trên điện thoại vào http://localhost:5173 và đăng nhập test@eshop.com/Test1234!.
Báo cáo ≤ 10 dòng: kết quả từng bước + lỗi nguyên văn nếu có.
```

**Output:**
```
Đã chạy bước 1–4. Bước 3 và 5 chặn vì adb không thấy điện thoại.

- **1. Issues:** tổng 158 — henry-banana 64, ThachHaoo 57, nphoang-itus 37. JSON ở `$env:TEMP\issues.json`.
- **2. adb:** lúc đầu chưa có (`The term 'adb' is not recognized…`). Sau khi bạn đồng ý, em đã tải và giải nén vào `D:\Tools\platform-tools`, chạy được (`adb version 1.0.41`, `Version 37.0.1-15733141`). Em không sửa PATH, nên phải gọi bằng đường dẫn đầy đủ `D:\Tools\platform-tools\adb.exe`.
- **3. adb devices:** **Fail** — chỉ in `List of devices attached`, không có thiết bị nào, kiểm lại vẫn trống.
- **4. Server:** backend đang lắng nghe `:3000` (log: `Database initialized and seeded (Phase 2).`); web đang chạy ở `http://127.0.0.1:5173/` (`VITE v8.0.12 ready`). Cả hai chạy nền, CSDL vừa seed lại.
- **5. adb reverse:** **chưa chạy được** — `adb.exe: no devices/emulators found`.
- **6.** Chưa tới bước này.

Để adb thấy máy: trên điện thoại bật Developer options → USB debugging, cắm cáp dữ liệu, chọn chế độ USB là "File transfer", rồi bấm Allow ở hộp thoại hỏi khoá RSA. Xong báo em để chạy lại bước 3 và 5.
```

**Xử lý:** [...]

---

## #10 | 17:21 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
3. Đã tuyển xong hết, không học lớp của tôi, một số non-IT, một số IT. Sau chạy nhớ đưa hết kịch bản để tôi đưa cho họ làm cho nhanh đỡ phiền nhé.

response: Đã chạy bước 1–4. Bước 3 và 5 chặn vì adb không thấy điện thoại.

- 1. Issues: tổng 158 — henry-banana 64, ThachHaoo 57, nphoang-itus 37. JSON ở $env:TEMP\issues.json.
- 2. adb: lúc đầu chưa có (The term 'adb' is not recognized…). Sau khi bạn đồng ý, em đã tải và giải nén vào D:\Tools\platform-tools, chạy được (adb version 1.0.41, Version 37.0.1-15733141). Em không sửa PATH, nên phải gọi bằng đường dẫn đầy đủ D:\Tools\platform-tools\adb.exe.
- 3. adb devices: Fail — chỉ in List of devices attached, không có thiết bị nào, kiểm lại vẫn trống.
- 4. Server: backend đang lắng nghe :3000 (log: Database initialized and seeded (Phase 2).); web đang chạy ở http://127.0.0.1:5173/ (VITE v8.0.12 ready). Cả hai chạy nền, CSDL vừa seed lại.
- 5. adb reverse: chưa chạy được — adb.exe: no devices/emulators found.
- 6. Chưa tới bước này.

Để adb thấy máy: trên điện thoại bật Developer options → USB debugging, cắm cáp dữ liệu, chọn chế độ USB là "File transfer", rồi bấm Allow ở hộp thoại hỏi khoá RSA. Xong báo em để chạy lại bước 3 và 5.
===
hướng dẫn mình bật nhé, mình đã kết nối USB laptop với điện thoại rồi\
```

**Output:**
````
## Bật Gỡ lỗi USB trên POCO F5 (HyperOS)

1. **Mở Tùy chọn nhà phát triển**
   - Cài đặt → **Giới thiệu điện thoại** → bấm liên tục **7 lần** vào ô **Phiên bản OS** (HyperOS 1.0.5…).
   - Nhập mật khẩu/mã khoá màn hình nếu được hỏi.
   - Thấy thông báo "Bạn đã là nhà phát triển" là xong.
2. **Bật Gỡ lỗi USB**
   - Cài đặt → **Cài đặt bổ sung** → **Tùy chọn nhà phát triển** → kéo xuống mục *Gỡ lỗi*.
   - Bật **Gỡ lỗi USB**. HyperOS bắt chờ đếm ngược vài giây rồi mới cho bấm **OK**.
3. **Chọn chế độ USB**
   - Kéo thanh thông báo xuống → chạm thông báo **"Đang sạc thiết bị qua USB"** → chọn **Truyền tệp**.
4. **Cho phép máy tính**
   - Trên điện thoại sẽ hiện hộp thoại **"Cho phép gỡ lỗi USB?"**.
   - Tick **"Luôn cho phép từ máy tính này"** → **Cho phép**.

Nếu không hiện hộp thoại ở bước 4, thử theo thứ tự:
- **Rút cáp ra rồi cắm lại.**
- **Đổi cáp.** Nhiều cáp chỉ sạc, không truyền dữ liệu. Ở bước 3 không thấy mục "Truyền tệp" là dấu hiệu cáp chỉ sạc.
- **Thu hồi quyền cũ:** Tùy chọn nhà phát triển → **Thu hồi ủy quyền gỡ lỗi USB** → rút ra, cắm lại.

## Lệnh cho Claude Code (sau khi bấm Cho phép)

```
HW03 – kiểm chứng P3, chạy lại bước 3, 5, 6 (backend + web vẫn chạy nền; nếu đã tắt thì chạy lại như bước 4).
- D:\Tools\platform-tools\adb.exe devices → phải là "<serial>  device". Nếu "unauthorized" → dừng, báo tôi.
- adb reverse tcp:5173 tcp:5173; adb reverse tcp:3000 tcp:3000; adb reverse --list.
- Dừng, chờ tôi mở Chrome trên điện thoại vào http://localhost:5173 và đăng nhập test@eshop.com / Test1234!.
Báo cáo ≤ 8 dòng.
```

Mở `localhost:5173` trên Chrome điện thoại. **Đạt** khi thấy danh sách 5 sản phẩm và đăng nhập được.

## Về kịch bản cho người tham gia

Ghi nhận rồi. Sau khi chốt P3, mình sẽ đưa **gói phát cho người tham gia** gồm 3 phần: kịch bản nhiệm vụ U1 (dạng mục tiêu), phiếu SUS 10 câu, câu hỏi mở. Đây là bản AI nháp nên bạn phải đọc duyệt trước khi phát. Bản AI nháp được đóng băng vào `ai-outputs/` cho Audit, và **phiên pilot** là để sửa chỗ khó hiểu trước 7 phiên chính.

Nhóm bạn có 3 người (đọc từ danh sách issue: henry-banana, nphoang-itus, bạn), khớp đúng 3 cụm C1/C2/C3.
````

**Xử lý:** [...]

---

## #11 | 17:31 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – kiểm chứng P3, chạy lại bước 3, 5, 6 (backend + web vẫn chạy nền; nếu đã tắt thì chạy lại như bước 4).
- D:\Tools\platform-tools\adb.exe devices → phải là "<serial>  device". Nếu "unauthorized" → dừng, báo tôi.
- adb reverse tcp:5173 tcp:5173; adb reverse tcp:3000 tcp:3000; adb reverse --list.
- Dừng, chờ tôi mở Chrome trên điện thoại vào http://localhost:5173 và đăng nhập test@eshop.com / Test1234!.
Báo cáo ≤ 8 dòng.
```

**Output:**
```
Bước 3 và 5 qua. Em dừng ở bước 6, chờ bạn mở Chrome trên điện thoại.

- **Server:** backend `:3000` và web `127.0.0.1:5173` vẫn chạy nền, em không khởi động lại.
- **3. adb devices:** `da87b223  device` (model 23049PCD8G), không báo `unauthorized`.
- **5. adb reverse:** lệnh cho 5173 và 3000 trả về `5173` và `3000`. `--list` có `UsbFfs tcp:5173 tcp:5173` và `UsbFfs tcp:3000 tcp:3000`.
- **6.** Bạn vào `http://localhost:5173` trên Chrome điện thoại, đăng nhập `test@eshop.com` / `Test1234!`, rồi báo em kết quả.

Nếu rút cáp hoặc adb restart thì phải chạy lại 2 lệnh `adb reverse`.
```

**Xử lý:** [...]

---

## #12 | 17:34 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Kết quả bước 6, đã đăng nhập bình thường
```

**Output:**
```
Đã kiểm xong P3: cả 6 bước đều đạt. Em chưa commit gì và cũng chưa xác nhận lượt đăng nhập từ phía server.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – kiểm chứng P3, chỉ kiểm, không commit.
- **Kết quả:**
  - Issues trên `tkob-team/eshop-sut`: tổng 158 — henry-banana 64, ThachHaoo 57, nphoang-itus 37.
  - adb: lúc đầu máy chưa có, em đã tải về `D:\Tools\platform-tools` (bản 37.0.1, không sửa PATH).
  - `adb devices`: `da87b223  device`.
  - Backend `:3000` và web `:5173` đang chạy nền. Cổng 5173 và 3000 đã được chuyển tiếp từ điện thoại về máy (`adb reverse`).
  - Bước 6: bạn mở Chrome trên điện thoại vào `http://localhost:5173` và đăng nhập `test@eshop.com` bình thường.
- **Commit:** không có.
- **Lưu ý:** rút cáp hoặc restart adb thì phải chạy lại 2 lệnh `adb reverse`. Restart backend thì CSDL bị seed lại.
- **Cần quyết định:** không.
```

**Xử lý:** [...]

---

## #13 | 17:35 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đã kiểm xong P3: cả 6 bước đều đạt. Em chưa commit gì và cũng chưa xác nhận lượt đăng nhập từ phía server.

Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03 – kiểm chứng P3, chỉ kiểm, không commit.
- Kết quả:
  - Issues trên tkob-team/eshop-sut: tổng 158 — henry-banana 64, ThachHaoo 57, nphoang-itus 37.
  - adb: lúc đầu máy chưa có, em đã tải về D:\Tools\platform-tools (bản 37.0.1, không sửa PATH).
  - adb devices: da87b223  device.
  - Backend :3000 và web :5173 đang chạy nền. Cổng 5173 và 3000 đã được chuyển tiếp từ điện thoại về máy (adb reverse).
  - Bước 6: bạn mở Chrome trên điện thoại vào http://localhost:5173 và đăng nhập test@eshop.com bình thường.
- Commit: không có.
- Lưu ý: rút cáp hoặc restart adb thì phải chạy lại 2 lệnh adb reverse. Restart backend thì CSDL bị seed lại.
- Cần quyết định: không.
===
Vậy là xong hết rồi nhỉ
```

**Output:**
````
P3 đã xong. Như vậy **phần chuẩn bị môi trường** đã xong, nhưng bài còn lại gần như nguyên vẹn. Mình đã viết bản đầu `report_plan.md`: bảng form, rubric, danh sách nộp, mâu thuẫn M1–M11, các quyết định đã chốt và lịch làm trong hôm nay.

## Bước tiếp theo: tạo khung HW03

Tải `report_plan.md` về, đặt vào `HW03\report_plan.md`, rồi dán lệnh này cho Claude Code:

```
HW03 – khung bài (commit "HW03: khung bài + report_plan")
1. tools/hw.toml: hw="HW03", since="2026-11-04", title="Prompt Log – HW03", log/notes/extra → HW03/appendix/… (giữ cấu hình HW02 dạng comment).
2. HW03/: giữ report_plan.md tôi đã đặt; tạo khung README.md và 23120255_HW03_Report.md theo mục c–d của report_plan (📝 = chỗ SV viết, 🔒 = phần cấm AI); thư mục checklist/evidence/{P1_chrome,P2_firefox,P3_android}, usability/sessions, bugs, excel, appendix/ai-outputs, ai-forms, skills (.gitkeep).
3. context/HW03_assignment.md = pdftotext đề <đường dẫn PDF đề trên máy>; slide HW03 → context/private/ (không commit).
4. CLAUDE.md mục 0: đề hiện tại = HW03; thêm mục "Quyết định HW03" trỏ tới HW03/report_plan.md mục e (không chép dài).
5. on_stop.py --manual; commit. Báo cáo ≤ 10 dòng.
```

Thay `<đường dẫn PDF đề trên máy>` trước khi dán. Claude Code sẽ dừng nếu còn chỗ trống.

## Bạn chốt giúp (trả lời theo mẫu `E1=a, O1=…`)

- **E1 – Excel:** (a) file mới cho HW03, dùng cấu trúc 3 sheet như HW01 (đề xuất, vì HW01 kiểm SUT khác là cái quạt); (b) thêm vào workbook HW01.
- **O1 – Overlay trên ảnh:**
  - Đề xuất cho PC: một cửa sổ Sticky Notes ghi email SV + MSSV + họ tên, chụp toàn màn hình sao cho thấy cả tên trình duyệt và URL.
  - Đề xuất cho điện thoại: thêm chữ bằng trình sửa ảnh của máy ngay sau khi chụp.
  - Cho mình **email sinh viên** của bạn (mình không đoán).
- **T – Thang đo:** SUS (đề xuất: 10 câu, tính điểm đơn giản, phổ biến) hay UEQ-S?
- **Giờ nộp** ngày 07/11?

Sau khi khung xong, mình đưa lệnh cho AI nháp checklist C2. Prompt đó sẽ dẫn AI đi theo từng nguồn checklist trong slide: đặc tả FR-21…24, heuristic, checklist theo control. Bản nháp được đóng băng trước khi bạn review.
````
*File AI ghi/gửi trong lượt này:* `report_plan.md`

**Xử lý:** [...]

---

## #14 | 17:38 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – khung bài (commit "HW03: khung bài + report_plan")
1. tools/hw.toml: hw="HW03", since="2026-11-04", title="Prompt Log – HW03", log/notes/extra → HW03/appendix/… (giữ cấu hình HW02 dạng comment).
2. HW03/: giữ report_plan.md tôi đã đặt; tạo khung README.md và 23120255_HW03_Report.md theo mục c–d của report_plan (📝 = chỗ SV viết, 🔒 = phần cấm AI); thư mục checklist/evidence/{P1_chrome,P2_firefox,P3_android}, usability/sessions, bugs, excel, appendix/ai-outputs, ai-forms, skills (.gitkeep).
3. context/HW03_assignment.md = pdftotext đề D:\HK7\Testing\Exercise\HW\HW03\2026.HW03.GUI Usability_En.pdf; slide HW03 → context/private/ (không commit).
4. CLAUDE.md mục 0: đề hiện tại = HW03; thêm mục "Quyết định HW03" trỏ tới HW03/report_plan.md mục e (không chép dài).
5. on_stop.py --manual; commit. Báo cáo ≤ 10 dòng.
```

**Output:**
```
Đã trích đề, chép slide. Giờ sửa `hw.toml`, dựng khung README/Report.

Missing files OK (script returns {}). Write hw.toml + notes/extra headers.

Now dirs + CLAUDE.md.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – dựng khung bài. Đã làm đủ 5 bước; một chỗ khác yêu cầu ở bước 3, xem "Cần quyết định".
- **File đã tạo/sửa:**
  - `tools/hw.toml`: chuyển sang HW03, cấu hình HW02 giữ lại dạng comment.
  - `HW03/README.md` và `HW03/23120255_HW03_Report.md`: khung theo mục c–d, có 📝/🔒.
  - Các thư mục đã yêu cầu, mỗi thư mục có `.gitkeep`.
  - `HW03/appendix/prompt_log_notes.toml` và `prompt_log_extra.toml`: hai file trống, chỉ có phần hướng dẫn ở đầu. Lệnh không yêu cầu, em thêm để cấu hình trong `hw.toml` trỏ tới.
  - `context/HW03_assignment.md`: trích bằng pdftotext của Git, dạng text giữ bố cục, không phải markdown như đề HW02.
  - Thêm mục "Quyết định HW03" vào CLAUDE.md, trỏ tới report_plan mục e.
  - `HW03/report_plan.md`: giữ nguyên bản bạn đặt, chỉ commit.
- **Kết quả kiểm tra:** `on_stop.py --manual` chạy được, prompt log ghi 10 lượt (Claude Opus 5.5). Bài HW03 không có bước check_domain, lint hay test.
- **Commit:** `c409e1c HW03: khung bài + report_plan`
- **Cần quyết định:**
  - Slide – thư mục đề `D:\HK7\Testing\Exercise\HW\HW03` không có slide nào. Em đã chép `S13_GUI Testing & Usability Testing.pdf` và `EN.GUI + Usability + Compatibility Testing AI-First (Combined).pdf` từ `D:\HK7\Testing\Slides\` vào `context/private/` (không commit). Hai bản đúng chưa, hay cần thêm các file trong `Slides\Refs\` và `Templates\UI Checklist\`?
  - CLAUDE.md mục 1 vẫn ghi "HW02 … (đang làm)". Đổi thành "đã nộp" không?
```
*File AI ghi/gửi trong lượt này:* `hw.toml`, `prompt_log_notes.toml`, `prompt_log_extra.toml`, `README.md`, `23120255_HW03_Report.md`

**Xử lý:** [...]

---

## #15 | 17:40 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
E1=a
01=OK. MSSV là được rồi, lấy email làm gì: 23120255
T= Bạn nghĩ cái tốt hơn.
```

**Output:**
````
Ghi nhận **E1=a**, **O1** như đề xuất.

## O1: vẫn nên có email sinh viên

Đề có hai chỗ nói về overlay, và chúng khác nhau:
- §6 Task 3: *"overlay your username in the form your student email"*
- §11: yêu cầu *"student ID and full name"*

Chỉ ghi MSSV thì thiếu đúng chữ "email" mà §6 nêu. Trong khi đó, thêm một dòng chữ không tốn gì. Mình đề xuất overlay đủ 3 thứ: **MSSV · họ tên · email sinh viên**.

Nếu email trường của bạn đúng dạng `23120255@student.hcmus.edu.vn` thì bạn xác nhận một chữ "đúng" là được. Mình không tự điền vì chưa chắc đây là email của bạn.

## T = SUS, kèm SEQ

Mình chọn **SUS + SEQ**:

| | SUS | UEQ-S |
|---|---|---|
| Số câu | 10 câu Likert 1–5 | 8 cặp tính từ đối lập, thang 7 điểm |
| Kết quả | 1 điểm 0–100, ngưỡng tham chiếu phổ biến khoảng 68 là trung bình | 2 chiều (thực dụng / cảm xúc), cần bảng benchmark riêng mới diễn giải được |
| Với 7 người | Dễ tính, dễ viết, dễ giải thích khi vấn đáp | Khó diễn giải với mẫu nhỏ |

Thêm **SEQ** (Single Ease Question) là 1 câu sau khi làm xong nhiệm vụ: "Nhiệm vụ này dễ hay khó?", chấm 1–7. Slide bài tập usability có nhắc "Likert + SEQ". SEQ cho thêm một số liệu đo ngay tại nhiệm vụ, chỉ tốn khoảng 10 giây mỗi người.

## Thêm vào lệnh khung (dán cùng lệnh trước)

```
6. HW03/report_plan.md mục e: thêm dòng E1=a (Excel mới 3 sheet như HW01), O1 (overlay MSSV 23120255 + Lê Tấn Hiệp + email SV <email>), T=SUS + SEQ; xoá 3 mục này khỏi "Còn chờ SV chốt".
```

Điền `<email>` trước khi dán. Báo cáo của Claude Code về là mình đưa lệnh nháp checklist C2.
````

**Xử lý:** [...]

---

## #16 | 17:42 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
email đúng, sao biết hay vậy. email chung của sv hcmus bị leak à
Vì có cả những người non-IT, và bạn mình cũng một vài đứa khá lười, nên đơn giản thôi nhé
Lệnh mình đã dùng lúc nãy rồi, xem lệnh hiện tại bạn đưa có cần thêm gì không để mình đưa Claude Code 1 lần luôn nhé
```

**Output:**
````
## Email

Không có rò rỉ gì cả. Mình đoán theo **dạng email sinh viên phổ biến** của trường: `MSSV@student.hcmus.edu.vn`. Dạng này thường thấy trên các thông báo công khai của trường. Vì chỉ là đoán nên mình mới hỏi bạn xác nhận trước khi dùng.

## Đơn giản cho người tham gia

- **SUS** vẫn giữ, vì đề bắt buộc một thang chuẩn. 10 câu đánh số 1–5, mất khoảng 2 phút.
- **SEQ** chỉ 1 câu.
- Câu hỏi mở chỉ **4 câu** đúng mức tối thiểu đề đòi: rõ ràng, khôi phục lỗi, tốc độ, tin cậy.
- Tất cả gói trong **1 trang**.

## Lệnh gộp (dán một lần)

Lệnh khung lúc nãy đã chạy, nên lệnh này gồm 3 việc, mỗi việc một commit:

```
HW03 – 3 việc, mỗi việc 1 commit. Đọc HW03/report_plan.md trước.

A. report_plan mục e (commit "HW03: chốt E1, O1, T"):
- E1=a: Excel mới HW03/excel/23120255_HW03_Checklist.xlsx, 3 sheet như HW01.
- O1: overlay "23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn"; PC = Sticky Notes + chụp toàn màn hình (thấy tên trình duyệt + URL); điện thoại = thêm chữ bằng trình sửa ảnh ngay sau khi chụp.
- T=SUS (10 câu tiếng Việt) + SEQ (1 câu sau nhiệm vụ); bộ câu hỏi tối giản vì có người non-IT.
- Xoá 3 mục này khỏi "Còn chờ SV chốt".

B. AI nháp checklist C2 (commit "HW03[T1] 1/6: AI nháp checklist C2"):
1. Khảo sát ..\eshop-sut\frontend-web: Login, ForgotPassword, Profile, navbar App.jsx (khi đã đăng nhập) → liệt kê control từng màn kèm file:dòng → HW03/checklist/c2_inventory.md.
2. Cùng file: trích yêu cầu UI từ SRS README.md (FR-21…24 + phần UI của FR-02, FR-03, FR-04, FR-11), ghi số dòng.
3. Sinh ≥ 45 item vào HW03/checklist/checklist.json theo 3 nguồn trong slide (context/private): (a) điều khoản SRS, (b) checklist theo control (text box, button, link, validation), (c) heuristic Nielsen/Norman/Shneiderman. Mỗi item: id CL-xx, ia (IA-01…04), man_hinh, muc_kiem_tra, can_cu, expected (quan sát được, có ngưỡng Pass/Fail), uu_tien (Mandatory/Optional), nen_tang (P1/P2/P3; N/A phải kèm giả định), nguon="AI". Đủ 4 IA, không trùng nhau.
4. Render checklist.md; chép nguyên bản JSON vào HW03/appendix/ai-outputs/T1_checklist_ai_v1.json (đóng băng). Không chạy SUT để chỉnh Expected theo hành vi quan sát.

C. AI nháp gói usability U1 (commit "HW03[T2] 1/10: AI nháp gói usability"):
HW03/usability/:
- plan.md: kế hoạch 9 phần theo slide, ngắn.
- participant_kit.md: 1 trang phát người tham gia — lời mở đầu (kiểm sản phẩm, không kiểm bạn; xin đồng ý quay màn hình + ghi âm; TA có thể gọi xác nhận), nhiệm vụ U1 dạng mục tiêu (không chỉ bước), SEQ, SUS 10 câu, 4 câu hỏi mở (rõ ràng / khôi phục lỗi / tốc độ / tin cậy).
- observation_sheet.md: phiếu trống cho SV (thời gian, lỗi, do dự, câu nói, lần cần trợ giúp).
Kiểm nhiệm vụ làm được trên dữ liệu seed (tài khoản test@eshop.com, mã giảm giá đủ ngưỡng). KHÔNG tạo bảng người tham gia (SV tự làm). Chép bản đầu vào appendix/ai-outputs/T2_*_v1.md (đóng băng).

Cuối: on_stop.py --manual. Báo cáo ≤ 15 dòng: đường dẫn, số item theo từng IA, các commit.
```

Lệnh B được viết để dẫn AI đi qua từng nguồn checklist trong slide, đúng tinh thần "không dùng một prompt chung chung" của đề.

## Sau khi báo cáo về

- **Task 1:** bạn review checklist, rồi **tự thêm item AI bỏ sót kèm lý do** (🔒). Ở bước này mình sẽ không gợi ý item nào. Mình chỉ kiểm cách viết: căn cứ, Expected, IA.
- **Task 2:** bạn đọc `participant_kit.md`, chạy **pilot** với 1 người, sửa chỗ khó hiểu, rồi mới làm 7 phiên chính.
````

**Xử lý:** [...]

---

## #17 | 17:44 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – 3 việc, mỗi việc 1 commit. Đọc HW03/report_plan.md trước.

A. report_plan mục e (commit "HW03: chốt E1, O1, T"):
- E1=a: Excel mới HW03/excel/23120255_HW03_Checklist.xlsx, 3 sheet như HW01.
- O1: overlay "23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn"; PC = Sticky Notes + chụp toàn màn hình (thấy tên trình duyệt + URL); điện thoại = thêm chữ bằng trình sửa ảnh ngay sau khi chụp.
- T=SUS (10 câu tiếng Việt) + SEQ (1 câu sau nhiệm vụ); bộ câu hỏi tối giản vì có người non-IT.
- Xoá 3 mục này khỏi "Còn chờ SV chốt".

B. AI nháp checklist C2 (commit "HW03[T1] 1/6: AI nháp checklist C2"):
1. Khảo sát ..\eshop-sut\frontend-web: Login, ForgotPassword, Profile, navbar App.jsx (khi đã đăng nhập) → liệt kê control từng màn kèm file:dòng → HW03/checklist/c2_inventory.md.
2. Cùng file: trích yêu cầu UI từ SRS README.md (FR-21…24 + phần UI của FR-02, FR-03, FR-04, FR-11), ghi số dòng.
3. Sinh ≥ 45 item vào HW03/checklist/checklist.json theo 3 nguồn trong slide (context/private): (a) điều khoản SRS, (b) checklist theo control (text box, button, link, validation), (c) heuristic Nielsen/Norman/Shneiderman. Mỗi item: id CL-xx, ia (IA-01…04), man_hinh, muc_kiem_tra, can_cu, expected (quan sát được, có ngưỡng Pass/Fail), uu_tien (Mandatory/Optional), nen_tang (P1/P2/P3; N/A phải kèm giả định), nguon="AI". Đủ 4 IA, không trùng nhau.
4. Render checklist.md; chép nguyên bản JSON vào HW03/appendix/ai-outputs/T1_checklist_ai_v1.json (đóng băng). Không chạy SUT để chỉnh Expected theo hành vi quan sát.

C. AI nháp gói usability U1 (commit "HW03[T2] 1/10: AI nháp gói usability"):
HW03/usability/:
- plan.md: kế hoạch 9 phần theo slide, ngắn.
- participant_kit.md: 1 trang phát người tham gia — lời mở đầu (kiểm sản phẩm, không kiểm bạn; xin đồng ý quay màn hình + ghi âm; TA có thể gọi xác nhận), nhiệm vụ U1 dạng mục tiêu (không chỉ bước), SEQ, SUS 10 câu, 4 câu hỏi mở (rõ ràng / khôi phục lỗi / tốc độ / tin cậy).
- observation_sheet.md: phiếu trống cho SV (thời gian, lỗi, do dự, câu nói, lần cần trợ giúp).
Kiểm nhiệm vụ làm được trên dữ liệu seed (tài khoản test@eshop.com, mã giảm giá đủ ngưỡng). KHÔNG tạo bảng người tham gia (SV tự làm). Chép bản đầu vào appendix/ai-outputs/T2_*_v1.md (đóng băng).

Cuối: on_stop.py --manual. Báo cáo ≤ 15 dòng: đường dẫn, số item theo từng IA, các commit.
```

**Output:**
```
Đang khảo sát SUT (đọc xong 4 màn), giờ đọc SRS.

Khảo sát xong. Viết `c2_inventory.md`.

Viết checklist JSON (dùng script tạm để đánh số tự động).

Checklist xong (65 item, commit `39f685c`). Giờ kiểm luồng U1 trên mã để viết gói usability.

Đã thử luồng U1 qua API: SAVE10 tính sai, VIP100/BIGBUY đúng. Restart backend để xoá đơn thử, rồi viết gói usability.

Empty → seed reset OK. Run prompt log.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – chốt E1/O1/T, AI nháp checklist C2, AI nháp gói usability U1. Cả 3 việc xong, mỗi việc một commit.
- **File:**
  - `HW03/report_plan.md` (mục e)
  - `HW03/checklist/c2_inventory.md`, `checklist.json`, `checklist.md`
  - `tools/render_checklist.py`: script render mới, cần khai trong Audit
  - `HW03/usability/plan.md`, `participant_kit.md`, `observation_sheet.md`
  - Bản đóng băng: `HW03/appendix/ai-outputs/T1_checklist_ai_v1.json` và `T2_{plan,participant_kit,observation_sheet}_v1.md`
- **Checklist: 65 item** — IA-01: 16 · IA-02: 23 · IA-03: 11 · IA-04: 15.
  - Theo căn cứ: SRS 40, heuristic 17, checklist theo control 8. Mandatory 48, Optional 17.
  - Có 3 giả định: NA1 (thứ tự Tab trên P3 ghi N/A), GA1 (định dạng ngày), GA2 (badge giỏ hàng).
- **Kiểm luồng U1:** chạy qua API trên dữ liệu seed, đi trọn từ đăng nhập → tìm "tai nghe" → áp mã → đặt hàng → đơn hiện trong lịch sử. Sau đó em restart backend, lịch sử đơn trả `[]`. Prompt log ghi 11 lượt; file `A_prompt_log.md` đã cập nhật nhưng chưa commit vì lệnh không yêu cầu.
- **Commit:**
  - `4ab90da HW03: chốt E1, O1, T`
  - `39f685c HW03[T1] 1/6: AI nháp checklist C2`
  - `c081f96 HW03[T2] 1/10: AI nháp gói usability`
- **Cần quyết định:**
  - **K1 – mã giảm giá trong nhiệm vụ.** `SAVE10` tính sai: đơn 6.000.000 ₫ ra `final_amount` 60.000.000, `discount_amount` −54.000.000 (`backend/server.js`, handler từ dòng 363). Gói usability đang dùng `VIP100` (tính đúng, giảm 100.000 ₫). Phương án: (a) giữ `VIP100`; (b) dùng `SAVE10` để người tham gia gặp lỗi này. Riêng việc có lập bug cho SAVE10 hay không, em chưa đưa vào đây, bạn quyết sau.
- **Bất thường (AI phát hiện):**
  - Quy tắc chặn sửa `ai-outputs/` và `A_prompt_log.md` trong `.claude/settings.json` mới chỉ áp cho HW02, HW03 chưa được bảo vệ. Có nên thêm quy tắc tương tự cho HW03 không?
```
*File AI ghi/gửi trong lượt này:* `c2_inventory.md`, `gen_checklist.py`, `render_checklist.py`, `plan.md`, `participant_kit.md`, `observation_sheet.md`

**Xử lý:** [...]

---

## #18 | 17:54 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03 – chốt E1/O1/T, AI nháp checklist C2, AI nháp gói usability U1. Cả 3 việc xong, mỗi việc một commit.
- File:
  - HW03/report_plan.md (mục e)
  - HW03/checklist/c2_inventory.md, checklist.json, checklist.md
  - tools/render_checklist.py: script render mới, cần khai trong Audit
  - HW03/usability/plan.md, participant_kit.md, observation_sheet.md
  - Bản đóng băng: HW03/appendix/ai-outputs/T1_checklist_ai_v1.json và T2_{plan,participant_kit,observation_sheet}_v1.md
- Checklist: 65 item — IA-01: 16 · IA-02: 23 · IA-03: 11 · IA-04: 15.
  - Theo căn cứ: SRS 40, heuristic 17, checklist theo control 8. Mandatory 48, Optional 17.
  - Có 3 giả định: NA1 (thứ tự Tab trên P3 ghi N/A), GA1 (định dạng ngày), GA2 (badge giỏ hàng).
- Kiểm luồng U1: chạy qua API trên dữ liệu seed, đi trọn từ đăng nhập → tìm "tai nghe" → áp mã → đặt hàng → đơn hiện trong lịch sử. Sau đó em restart backend, lịch sử đơn trả []. Prompt log ghi 11 lượt; file A_prompt_log.md đã cập nhật nhưng chưa commit vì lệnh không yêu cầu.
- Commit:
  - 4ab90da HW03: chốt E1, O1, T
  - 39f685c HW03[T1] 1/6: AI nháp checklist C2
  - c081f96 HW03[T2] 1/10: AI nháp gói usability
- Cần quyết định:
  - K1 – mã giảm giá trong nhiệm vụ. SAVE10 tính sai: đơn 6.000.000 ₫ ra final_amount 60.000.000, discount_amount −54.000.000 (backend/server.js, handler từ
    dòng 363). Gói usability đang dùng VIP100 (tính đúng, giảm 100.P100; (b) dùng SAVE10 để người tham gia gặp lỗi này. Riêng việc cólập bug cho SAVE10 hay không, em chưa đưa vào đây, bạn quyết sau.
- Bất thường (AI phát hiện):
  - Quy tắc chặn sửa ai-outputs/ và A_prompt_log.md trong .claude/sW02, HW03 chưa được bảo vệ. Có nên thêm quy tắc tương tự cho HW03không?
===
Nhắc 1 cái là HW02 tự dưng nộp cả các file dư thừa như "report_plan", hãy nhớ rằng trước khi zip thì chỉ nộp những file cần nộp thôi nhé
```

**Output:**
````
Ghi nhận: **chỉ nộp file cần nộp**. HW02 đóng gói bằng `git archive … HEAD HW02` nên lấy hết mọi file đã commit. HW03 sẽ dùng `.gitattributes` với `export-ignore` cho file làm việc (`report_plan.md`, ghi chú…), vì `git archive` bỏ qua các file có thuộc tính này. Trước khi zip, mình sẽ in danh sách file trong zip để bạn duyệt.

## K1 – mã giảm giá trong nhiệm vụ

Báo cáo bị cụt, nên mình đọc lại code. Có hai chỗ:
- `server.js:400` tính phần trăm bằng `total × (1 − discount_value)`. Với `SAVE10` thì `discount_value = 10`, nên đơn 6.000.000 ₫ ra mức giảm −54.000.000 và phải trả 60.000.000.
- AI phát hiện thêm: `server.js:379` dùng điều kiện ngưỡng `>`, trong khi FR-09 C3 ghi `>=`.

Hai phương án:
- **(a) Dùng VIP100** (đề xuất). Usability đo thiết kế giao diện. Nếu nhiệm vụ cố tình đưa người tham gia vào một lỗi tính tiền đã biết, lỗi đó sẽ lấn át điểm SUS và phần "khôi phục lỗi", làm phần phân tích bị nhiễu.
- **(b) Dùng SAVE10.** Thấy được phản ứng về độ tin cậy khi gặp số tiền vô lý, nhưng kết quả đo bị lệch vì một bug chức năng.

Có lập bug cho SAVE10 hay không thì quyết sau. Trước hết phải kiểm trùng: phần FR-09 có thể bạn cùng nhóm đã báo ở HW02.

## Bất thường: hook prompt log đang tắt

Commit `be8996e` (17:31 hôm nay) đã **gỡ hook Stop**. Từ lúc đó prompt log chỉ cập nhật khi chạy `--manual`. HW03 nên bật lại hook, đồng thời thêm quy tắc chặn sửa cho HW03 mà Claude Code đề xuất.

## Lệnh cho Claude Code

```
HW03 – cấu hình + K1 (commit "HW03: bật hook Stop, bảo vệ ai-outputs/prompt log, K1")
1. .claude/settings.json: thêm lại hook Stop on_stop.py (như trước be8996e); deny Edit/Write cho HW03/appendix/ai-outputs/** và HW03/appendix/A_prompt_log.md (giống HW02). Giữ includeCoAuthoredBy=false.
2. report_plan mục e: K1=a (VIP100; lý do: usability đo thiết kế, không để bug tính tiền đã biết làm nhiễu SUS). Mục f: "AI phát hiện khi kiểm luồng U1: SAVE10 tính sai (server.js:400), ngưỡng dùng > thay vì >= (server.js:379) – chưa quyết lập bug".
3. Kiểm trùng trong $env:TEMP\issues.json: issue nhắc SAVE10 / percent / mã giảm giá / apply-coupon → in số, tiêu đề, author.
4. HW03/.gitattributes: report_plan.md export-ignore. report_plan mục c thêm cột "Nộp?".
5. on_stop.py --manual (gồm A_prompt_log.md chưa commit); commit; nhắc tôi push. Báo cáo ≤ 10 dòng.
```

## Việc của bạn sau lệnh này

1. **Push** để mình đọc `checklist.json` (65 item) và kiểm nhất quán: căn cứ, Expected đo được, IA, giả định NA1/GA1/GA2. Mình chỉ kiểm item AI đã viết, không nhận xét "còn thiếu item nào".
2. **Review checklist rồi tự thêm item AI bỏ sót** (🔒). Mỗi item ghi lý do AI bỏ sót: do prompt, do giới hạn model, hay do đặc điểm giao diện. Commit file của bạn **trước** rồi mới hỏi AI "vì sao bỏ sót".
3. **Đọc `participant_kit.md`, chạy pilot** với 1 người.

Khi xong một mốc lớn, nói "xuất transcript" để mình xuất `claude-ai_session_HW03_p1.jsonl` cho prompt log.
````

**Xử lý:** [...]

---

## #19 | 17:56 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
À mình tắt hook vì nó cứ dí vào cho HW02 ấy mà
```

**Output:**
````
Hiểu rồi. Hook "dí vào HW02" là vì nó ghi theo `tools/hw.toml`, mà lúc đó file này vẫn trỏ HW02. Lệnh khung đã đổi `hw.toml` sang HW03, nên bật lại thì hook sẽ ghi vào `HW03/appendix/A_prompt_log.md`. Bạn chọn:

- **(a) Bật lại hook** (đề xuất): log tự cập nhật sau mỗi lượt, không phải nhớ.
- **(b) Để tắt:** mọi lệnh mình đưa đều kết thúc bằng `on_stop.py --manual`, vẫn đủ log. Rủi ro là lượt nào bạn tự gõ cho Claude Code mà không có lệnh này thì chỉ được ghi ở lần `--manual` kế tiếp. Không mất lượt, nhưng log commit trễ hơn.

## Cần sửa thêm dù chọn (a) hay (b)

`since` hiện chỉ lọc **theo ngày** (`extract_prompt_log.py:381` dùng `.date()`). Hôm nay 04/11 bạn còn các lượt kết thúc HW02, ví dụ lượt tạo `be8996e` lúc 17:31. Với `since = "2026-11-04"`, các lượt này sẽ lọt vào log HW03.

Thay bước 1 trong lệnh trước bằng:

```
1. Hook: <a: thêm lại Stop on_stop.py như trước be8996e | b: giữ tắt>. Deny Edit/Write HW03/appendix/ai-outputs/** và HW03/appendix/A_prompt_log.md.
1b. extract_prompt_log.py: --since/--until nhận thêm "YYYY-MM-DD HH:MM" (vẫn nhận ngày như cũ); hw.toml since = "2026-11-04 12:26". Chạy --list cho ngày 04/11, in giờ + 60 ký tự đầu prompt từng lượt để tôi kiểm còn lượt HW02 nào lọt vào không. Vá harness → commit riêng "HW03: vá harness – since theo giờ".
```

Chọn **a** hoặc **b** rồi điền vào chỗ `<…>`. Các bước 2–5 của lệnh trước giữ nguyên.
````

**Xử lý:** [...]

---

## #20 | 17:57 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – cấu hình + K1 (commit "HW03: bật hook Stop, bảo vệ ai-outputs/prompt log, K1")
1. Hook: <a: thêm lại Stop on_stop.py như trước be8996e | b: giữ tắt>. Deny Edit/Write HW03/appendix/ai-outputs/** và HW03/appendix/A_prompt_log.md.
1b. extract_prompt_log.py: --since/--until nhận thêm "YYYY-MM-DD HH:MM" (vẫn nhận ngày như cũ); hw.toml since = "2026-11-04 12:26". Chạy --list cho ngày 04/11, in giờ + 60 ký tự đầu prompt từng lượt để tôi kiểm còn lượt HW02 nào lọt vào không. Vá harness → commit riêng "HW03: vá harness – since theo giờ".
2. report_plan mục e: K1=a (VIP100; lý do: usability đo thiết kế, không để bug tính tiền đã biết làm nhiễu SUS). Mục f: "AI phát hiện khi kiểm luồng U1: SAVE10 tính sai (server.js:400), ngưỡng dùng > thay vì >= (server.js:379) – chưa quyết lập bug".
3. Kiểm trùng trong $env:TEMP\issues.json: issue nhắc SAVE10 / percent / mã giảm giá / apply-coupon → in số, tiêu đề, author.
4. HW03/.gitattributes: report_plan.md export-ignore. report_plan mục c thêm cột "Nộp?".
5. on_stop.py --manual (gồm A_prompt_log.md chưa commit); commit; nhắc tôi push. Báo cáo ≤ 10 dòng.
```

**Output:**
```
Đang vá `--since` theo giờ; kiểm chỗ khác dùng `since`.

epl module loaded → reuse parse_bound.

Đang sửa report_plan mục e/f, rồi `.gitattributes` và commit.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – bật lại hook Stop, chặn sửa file AI/prompt log, vá `since` theo giờ, chốt K1. Đã làm đủ, 2 commit.
- **File:**
  - `.claude/settings.json`: bật lại hook Stop, chép nguyên khối như trước `be8996e`; chặn Edit/Write `HW03/appendix/ai-outputs/**` và `HW03/appendix/A_prompt_log.md`.
  - `tools/extract_prompt_log.py`: `--since`/`--until` nhận thêm `YYYY-MM-DD HH:MM`.
  - `tools/audit_tables.py`: sửa theo, vì script này cũng đọc `since` — để nguyên sẽ báo lỗi với giá trị có giờ.
  - `tools/hw.toml`: `since = "2026-11-04 12:26"`.
  - `HW03/report_plan.md`: thêm K1 ở mục e, dòng "AI phát hiện" ở mục f, cột "Nộp?" ở mục c.
  - `HW03/.gitattributes`: `report_plan.md` không vào zip. Đã thử `git archive`: zip không có `report_plan.md`, nhưng có chính file `.gitattributes`.
- **Kiểm tra:**
  - Lọc theo ngày như cũ cho HW02 vẫn ra 407 lượt (cũ: 407).
  - Prompt log HW03 hiện có 12 lượt.
  - Danh sách lượt 04/11 (giờ | đầu prompt):
    - #1 17:15 | HW03 – kiểm chứng P3
    - **#2 17:24 | `d:\…\HW02\append…`**
    - **#3 17:27 | Mình chỉ cần giữ lại tất cả lệnh của hôm nay…**
    - **#4 17:28 | À thôi bỏ hết đi, vì log hiện tại không phải của HW02…**
    - **#5 17:29 | commit đi kiểu end HW02**
    - **#6 17:30 | Ủa khoan, Undo lại nhé…**
    - **#7 17:31 | Rồi commit nhé**
    - #8 17:31 | HW03 – kiểm chứng P3, chạy lại bước 3, 5, 6
    - #9 17:34 | Kết quả bước 6
    - #10 17:38 | HW03 – khung bài
    - #11 17:44 | HW03 – 3 việc
- **Issue trùng:** mã giảm giá thuộc nhóm FR09 của henry-banana.
  - SAVE10 tính sai: trùng **#126** "[FR09-03] A 10 percent coupon returns a negative discount and increases total".
  - Ngưỡng dùng `>` thay vì `>=`: trùng **#124** (fixed) và **#125** (percent) "…rejected at its exact minimum total".
  - Liên quan: #134 (mã 100% cho discount âm).
- **Commit:**
  - `eced5dd HW03: vá harness – since theo giờ`
  - `e4dcd91 HW03: bật hook Stop, bảo vệ ai-outputs/prompt log, K1`
- **Nhắc:** bạn tự push (`git push`).
- **Cần quyết định:**
  - **L1** – Lượt #2–#7 (17:24–17:31) là việc kết thúc HW02 nhưng nằm sau mốc 12:26 nên vẫn vào log HW03. Phương án: (a) dời `since` sang 17:32 (cũng loại luôn #1, vì #1 lúc 17:15); (b) giữ, ghi lý do trong `prompt_log_notes.toml`.
```
*File AI ghi/gửi trong lượt này:* `.gitattributes`

**Xử lý:** [...]

---

## #21 | 18:02 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03 – bật lại hook Stop, chặn sửa file AI/prompt log, vá since theo giờ, chốt K1. Đã làm đủ, 2 commit.
- File:
  - .claude/settings.json: bật lại hook Stop, chép nguyên khối như trước be8996e; chặn Edit/Write HW03/appendix/ai-outputs/** và HW03/appendix/A_prompt_log.md.
  - tools/extract_prompt_log.py: --since/--until nhận thêm YYYY-MM-DD HH:MM.
  - tools/audit_tables.py: sửa theo, vì script này cũng đọc since — để nguyên sẽ báo lỗi với giá trị có giờ.
  - tools/hw.toml: since = "2026-11-04 12:26".
  - HW03/report_plan.md: thêm K1 ở mục e, dòng "AI phát hiện" ở mục f, cột "Nộp?" ở mục c.
  - HW03/.gitattributes: report_plan.md không vào zip. Đã thử git archive: zip không có report_plan.md, nhưng có chính file .gitattributes.
- Kiểm tra:
  - Lọc theo ngày như cũ cho HW02 vẫn ra 407 lượt (cũ: 407).
  - Prompt log HW03 hiện có 12 lượt.
  - Danh sách lượt 04/11 (giờ | đầu prompt):
    - #1 17:15 | HW03 – kiểm chứng P3
    - #2 17:24 | d:\…\HW02\append…
    - #3 17:27 | Mình chỉ cần giữ lại tất cả lệnh của hôm nay…
    - #4 17:28 | À thôi bỏ hết đi, vì log hiện tại không phải của H
    - #5 17:29 | commit đi kiểu end HW02
    - #6 17:30 | Ủa khoan, Undo lại nhé…
    - #7 17:31 | Rồi commit nhé
    - #8 17:31 | HW03 – kiểm chứng P3, chạy lại bước 3, 5, 6
    - #9 17:34 | Kết quả bước 6
    - #10 17:38 | HW03 – khung bài
    - #11 17:44 | HW03 – 3 việc
- Issue trùng: mã giảm giá thuộc nhóm FR09 của henry-banana.
  - SAVE10 tính sai: trùng #126 "[FR09-03] A 10 percent coupon retuncreases total".
  - Ngưỡng dùng > thay vì >=: trùng #124 (fixed) và #125 (percent) "…rejected at its exact minimum total".
  - Liên quan: #134 (mã 100% cho discount âm).
- Commit:
  - eced5dd HW03: vá harness – since theo giờ
  - e4dcd91 HW03: bật hook Stop, bảo vệ ai-outputs/prompt log, K1
- Nhắc: bạn tự push (git push).
- Cần quyết định:
  - L1 – Lượt #2–#7 (17:24–17:31) là việc kết thúc HW02 nhưng nằm sHW03. Phương án: (a) dời since sang 17:32 (cũng loại luôn #1, vì #1lúc 17:15); (b) giữ, ghi lý do trong prompt_log_notes.toml.
===
Hiện tại thì bạn mình không thấy ai rảnh luôn. Đều bận cả. Nên có thể hoàn thành các task 1 và task 3 không phụ thuộc người khác trước được không?
```

**Output:**
````
**Được.** Task 1 và Task 3 không cần người tham gia, nên làm trước được: chạy checklist C2 trên 3 nền tảng chính là Task 3. Task 2 để khi bạn bè rảnh. Nhưng Task 2 nặng 40 điểm, nên mỗi khi có ai rảnh 20 phút thì chen một phiên vào ngay, kể cả đang làm dở Task 1.

## Thứ tự Task 1 + 3

| Bước | Việc | Ai |
|---|---|---|
| T1-2a | Mình kiểm nhất quán 65 item AI viết (căn cứ, Expected đo được, IA, giả định). **Cần bạn push trước**: origin hiện vẫn dừng ở `be8996e` | Phiên thảo luận |
| T1-2b 🔒 | Bạn review, tự thêm item AI bỏ sót kèm lý do → commit **trước** | Bạn |
| T1-2c | Hỏi AI "vì sao bỏ sót" → chốt checklist v2 | Claude Code |
| T1-3 | AI viết `RUN.md` để chạy theo từng màn hình: mỗi màn đi một lượt, mỗi lượt kiểm được nhiều item | Claude Code |
| T1-4 | Chạy P1 Chrome → P2 Firefox → P3 Android. Chụp ảnh cho item Failed, cộng 1 ảnh/màn/nền tảng làm bằng chứng cross-platform (có overlay) | Bạn |
| T1-5 | Gom kết quả vào Excel, tách bug mới khỏi bug trùng | Claude Code |
| T1-6 🔒 | Viết bug report, tạo issue | Bạn |

**Đề xuất cách chạy (E2):** chạy tay, kèm **1 đoạn script dán vào DevTools Console** cho mỗi màn. Script in ra số `<h1>`, type của các ô nhập, nhãn thiếu `*`, `alt` ảnh, thứ tự Tab. Các item đo được trên DOM nhờ vậy xong trong vài giây, còn mắt bạn chỉ cần kiểm các item về hình thức và tương tác.

Trên P3 cũng dùng được cách này: trên PC mở `chrome://inspect`, chọn tab Chrome của điện thoại (đang cắm USB), rồi dán script vào Console như trên máy tính.

Ước lượng: 65+ item × 3 nền tảng, khoảng 1,5–2 giờ.

## L1 – các lượt HW02 lọt vào log

Không chọn (a), vì sẽ mất lượt #1 (17:15), là lượt HW03 thật. Mình đề xuất **(c): thêm khoá `exclude` trong `hw.toml`**, dùng cùng cú pháp khoá với notes (`#k` cho lượt thứ k trong cùng phút). Lượt #7 và #8 cùng phút 17:31, nên không thể loại bằng một khoảng giờ đơn thuần.

```
HW03 – L1=c (commit "HW03: vá harness – exclude"):
extract_prompt_log.py + hw.toml: thêm exclude = ["2026-11-04 17:24 .. 2026-11-04 17:30", "2026-11-04 17:31#1"] (cùng cú pháp khoá notes); kiểm: log HW03 còn #1, #8–#11 và các lượt sau, HW02 dry-run vẫn 407. report_plan mục e: L1=c; mục f: issue trùng mã giảm giá (#126, #124, #125 – henry-banana) → không lập bug. on_stop.py --manual; commit. Báo cáo ≤ 6 dòng.
```

Trước khi chạy, đối chiếu lại `#1` có đúng là lượt "Rồi commit nhé" không, vì báo cáo liệt kê lượt này ở #7.

**Issue trùng:** cả hai lỗi mã giảm giá đã được henry-banana báo ở HW02 (#124, #125, #126), nên **không lập bug mới**. Usability vẫn dùng VIP100 như K1.

Chạy lệnh xong thì **push** để mình kiểm checklist.
````

**Xử lý:** [...]

---

## #22 | 18:06 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Mình chưa sử dụng prompt hiện tại bạn đưa nhé. Mình muốn hỏi bạn xem. Là mình có nên update CLAUDE.md; HARNESS_SETUP của mình hiện tại để thực hiện Homework này không. Hoặc bạn có nghĩ mình cần thêm một skill nào đó để làm về HW này, có thể là một skill đã được public trên mạng, hoặc là bạn tự tạo ra nếu như nó chưa có, còn nếu có nhưng thiếu có thể đem về custom lại. Bạn xem xét để mình hoàn thiện Harness system của mình nhé
```

**Output:**
````
Mình sẽ đọc `CLAUDE.md`, `HARNESS_SETUP.md` và các skill đang có trong repo, rồi tra thêm skill công khai liên quan đến GUI/usability.

## Kết luận ngắn

| Thành phần | Đề xuất |
|---|---|
| `CLAUDE.md` | **Nên cập nhật.** File đang 244 dòng, §1 và phần quyết định gần như toàn HW02 |
| `HARNESS_SETUP.md` | **Nên cập nhật nhẹ:** thêm mục "Bắt đầu bài mới" |
| Skill | **Tự tạo 2 skill**: `gui-checklist-testing` và `usability-evaluation`. Đây cũng chính là bài nộp Agent Skill 10 điểm. Skill công khai chỉ dùng làm tham khảo |

## 1. CLAUDE.md: tách theo bài

Tài liệu Claude Code cho biết: CLAUDE.md ở thư mục con **chỉ được nạp khi Claude đọc hoặc sửa file trong thư mục đó**, và nên giữ mỗi file dưới 200 dòng vì file dài làm giảm mức tuân thủ. Vì vậy nên tách thành 3 file:

| File | Nội dung |
|---|---|
| `CLAUDE.md` (gốc, ≤ 200 dòng) | Phần chung mọi bài: vai trò, khối báo cáo, giới hạn AI, prompt log, git (không amend, SV tự push), đóng gói bằng `git archive` + `export-ignore`, mẹo PowerShell, thông tin SUT chung |
| `HW02/CLAUDE.md` | Chuyển **nguyên văn** §1 và các quyết định HW02 vào đây (lưu trữ, chỉ nạp khi động vào HW02) |
| `HW03/CLAUDE.md` | Đề, rubric, phạm vi C2/U1, nền tảng P1–P3 + `adb reverse`, quyết định (trỏ tới `report_plan.md` mục e), giới hạn riêng HW03, quy trình + mẫu commit message |

Giới hạn riêng của HW03 cần ghi vào `HW03/CLAUDE.md`:
- 🔒 item bạn tự thêm vào checklist
- Dữ liệu người tham gia
- Ảnh có overlay
- SUS do chính người tham gia điền

## 2. Skill công khai mình tìm được

| Skill | Là gì | Dùng không |
|---|---|---|
| `web-design-guidelines` (Vercel) | Soát code UI theo bộ Web Interface Guidelines của Vercel (thiết kế, accessibility, UX). Mỗi lần chạy, nó tải luật mới nhất từ GitHub | **Không** dùng làm nguồn checklist: căn cứ của bài là SRS + slide; luật thay đổi theo thời gian nên chạy lại không ra cùng kết quả; bản nháp v1 cũng đã đóng băng |
| `webapp-testing` (Anthropic) | Bộ công cụ Playwright để test web chạy ở máy cục bộ: chụp ảnh, đọc log trình duyệt, quản lý server | Không cần: bạn đã có harness Playwright từ HW02 |
| `usability-testing` (prorise-cool) | Lập kế hoạch usability: tạo nhiệm vụ, think-aloud, kịch bản điều phối, định nghĩa chỉ số, khung phân tích | Chỉ tham khảo: trang mô tả không nhắc tới chấm điểm SUS. Tự viết theo slide (Rubin 9 phần, SUS + SEQ, severity × probability) sát đề hơn |

Nếu tham khảo skill nào, ghi nguồn trong `SKILL.md` và khai trong Audit. **Không chép nguyên** skill người khác vào bài nộp.

## 3. Hai skill tự tạo

Dựng theo mẫu `domain-bva-testing`: từng bước, một file JSON, có freeze, check, render, merge. Dùng skill **`testing-technique-skill-template`** (đã đồng bộ từ claude.ai) làm khung.

- **`gui-checklist-testing`** (làm ngay, để dùng luôn cho phần còn lại của Task 1/3):

  | Bước | Việc |
  |---|---|
  | 0 | Khảo sát control |
  | 1 | Nháp item theo 3 nguồn → freeze |
  | 2 🔒 | SV thêm item → hỏi AI vì sao bỏ sót |
  | 3 | `RUN.md` + `dom_probe.js` |
  | 4 | Chạy từng nền tảng → merge |
  | 5 | Excel + test summary |
  | 6 | Gom dữ kiện bug |

  Script: `check_checklist.py`, `render`, `freeze`, `merge_platform.py`, `build_excel.py`.

- **`usability-evaluation`** (làm trước pilot):
  - Bước: plan 9 phần → participant kit → phiếu quan sát → **`sus_score.py`** (SUS + SEQ) → khung tổng hợp (phần tổng hợp do SV viết) → findings xếp theo severity × probability.

**Khai trung thực:** checklist v1 được tạo **trước** khi có skill. Skill được đúc kết từ cách làm đó rồi dùng cho các bước sau. Video demo chạy skill trên một màn hình khác, ví dụ màn khác của C2 hoặc một màn ngoài phạm vi, trên nhánh tạm.

## 4. Lệnh gộp cho Claude Code (đã gồm L1 ở trên)

```
HW03 – harness, mỗi mục 1 commit. Phần skill dùng skill testing-technique-skill-template.
1. "HW03: tách CLAUDE.md theo bài": CLAUDE.md gốc chỉ giữ phần chung (vai trò, khối báo cáo, giới hạn AI, prompt log, git/push/amend, zip git archive + export-ignore, mẹo PowerShell, SUT chung), ≤ 200 dòng. Chuyển §1 + quyết định HW02 NGUYÊN VĂN sang HW02/CLAUDE.md. Tạo HW03/CLAUDE.md ≤ 120 dòng: đề, rubric, phạm vi C2/U1, P1–P3 + adb reverse (D:\Tools\platform-tools, vite --host 127.0.0.1), quyết định (trỏ report_plan mục e), giới hạn riêng (🔒 item SV thêm, dữ liệu người tham gia, ảnh overlay, SUS do người tham gia điền), quy trình T1/T2/T3 + mẫu commit. Kiểm không mất dòng: in số dòng trước/sau từng file.
2. "HW03: HARNESS_SETUP – bắt đầu bài mới": thêm mục checklist bắt đầu bài (hw.toml since theo giờ + exclude, deny ai-outputs/prompt log, HWxx/CLAUDE.md, slide → context/private, .gitattributes export-ignore, transcript claude-ai_session_<HW>_p1).
3. L1=c: (như lệnh trước — exclude trong hw.toml, dry-run HW02 vẫn 407).
4. "HW03: skill gui-checklist-testing (khung)": .claude/skills/gui-checklist-testing/ theo mẫu domain-bva-testing — SKILL.md 7 bước (0 khảo sát · 1 nháp theo 3 nguồn + freeze · 2 SV thêm 🔒 + gap · 3 RUN.md + dom_probe.js · 4 chạy từng nền tảng + merge · 5 Excel + test summary · 6 gom dữ kiện bug), references/schema-checklist.md, scripts check_checklist.py, freeze, render (từ tools/render_checklist.py), merge_platform.py, build_excel.py. Chạy check_checklist.py trên HW03/checklist/checklist.json để thử; chưa đổi dữ liệu HW03.
on_stop.py --manual. Báo cáo ≤ 15 dòng. Nhắc tôi push.
```

Báo cáo về xong thì **push**. Mình sẽ kiểm `CLAUDE.md` có mất dòng nào không, kiểm skill, và kiểm 65 item checklist, rồi bạn bắt đầu review và tự thêm item.

Sources:
- [Claude Code – How Claude remembers your project (CLAUDE.md, thư mục con, rules)](https://code.claude.com/docs/en/memory)
- [skills.sh – vercel-labs/agent-skills · web-design-guidelines](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines)
- [mdskills.ai – webapp-testing (anthropics/skills)](https://www.mdskills.ai/skills/webapp-testing)
- [agent-skills.md – prorise-cool · usability-testing](https://agent-skills.md/skills/prorise-cool/prorise-claude-skills/usability-testing)
````

**Xử lý:** [...]

---

## #23 | 18:10 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – harness, mỗi mục 1 commit. Phần skill dùng skill testing-technique-skill-template.
1. "HW03: tách CLAUDE.md theo bài": CLAUDE.md gốc chỉ giữ phần chung (vai trò, khối báo cáo, giới hạn AI, prompt log, git/push/amend, zip git archive + export-ignore, mẹo PowerShell, SUT chung), ≤ 200 dòng. Chuyển §1 + quyết định HW02 NGUYÊN VĂN sang HW02/CLAUDE.md. Tạo HW03/CLAUDE.md ≤ 120 dòng: đề, rubric, phạm vi C2/U1, P1–P3 + adb reverse (D:\Tools\platform-tools, vite --host 127.0.0.1), quyết định (trỏ report_plan mục e), giới hạn riêng (🔒 item SV thêm, dữ liệu người tham gia, ảnh overlay, SUS do người tham gia điền), quy trình T1/T2/T3 + mẫu commit. Kiểm không mất dòng: in số dòng trước/sau từng file.
2. "HW03: HARNESS_SETUP – bắt đầu bài mới": thêm mục checklist bắt đầu bài (hw.toml since theo giờ + exclude, deny ai-outputs/prompt log, HWxx/CLAUDE.md, slide → context/private, .gitattributes export-ignore, transcript claude-ai_session_<HW>_p1).
3. L1=c: (như lệnh trước — exclude trong hw.toml, dry-run HW02 vẫn 407).
4. "HW03: skill gui-checklist-testing (khung)": .claude/skills/gui-checklist-testing/ theo mẫu domain-bva-testing — SKILL.md 7 bước (0 khảo sát · 1 nháp theo 3 nguồn + freeze · 2 SV thêm 🔒 + gap · 3 RUN.md + dom_probe.js · 4 chạy từng nền tảng + merge · 5 Excel + test summary · 6 gom dữ kiện bug), references/schema-checklist.md, scripts check_checklist.py, freeze, render (từ tools/render_checklist.py), merge_platform.py, build_excel.py. Chạy check_checklist.py trên HW03/checklist/checklist.json để thử; chưa đổi dữ liệu HW03.
on_stop.py --manual. Báo cáo ≤ 15 dòng. Nhắc tôi push.
```

**Output:**
```
Item 1: tách CLAUDE.md. Dựng HW02/CLAUDE.md bằng script (chép nguyên văn dòng 55–248).

Giờ viết CLAUDE.md gốc (phần chung).

Global gitignore chặn `CLAUDE.md` → thêm ngoại lệ trong `.gitignore` của repo, commit tiếp (không amend).

Item 2: HARNESS_SETUP mục 6.

Implement `--exclude` + wire into on_stop and audit_tables.

Item 4: load skill template.

Đang dựng skill `gui-checklist-testing`; đọc cấu trúc Excel HW01 (qua zipfile, máy chưa có openpyxl).

Viết SKILL.md + schema.

Scripts: check, freeze, render, merge, excel.

Update render to include per-platform notes; then build_excel + assets.

Kiểm thử script (không đổi dữ liệu HW03; merge/freeze chạy trên bản sao trong tmp).

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – 4 việc harness. Xong cả 4, tổng 5 commit: mục 1 tốn 2 commit vì một chỗ chặn của gitignore toàn cục. Chưa đổi dữ liệu HW03.
- **1. Tách CLAUDE.md:**
  - Số dòng trước: `CLAUDE.md` 248. Sau: `CLAUDE.md` gốc 112, `HW02/CLAUDE.md` 205 (§1, §2, §5, §6 và các dòng HW02 của §3–§4, chép nguyên văn), `HW03/CLAUDE.md` 91.
  - Script so từng dòng: chỉ 6 dòng gốc không còn nguyên văn — các dòng 10, 34, 37, 38, 40, 42 (quy tắc ghi quyết định, danh sách "đọc gì trước", mục Quyết định HW03). Nội dung vẫn còn, chỉ viết lại cho chung.
- **2. HARNESS_SETUP:** thêm mục 6, checklist bắt đầu bài mới gồm 7 bước.
- **3. L1=c:**
  - `extract_prompt_log.py` thêm `--exclude` (lặp được); `on_stop.py` và `audit_tables.py` đọc `exclude` từ `hw.toml`.
  - `exclude` bỏ 17:24–17:30 và lượt 17:31 đầu tiên; lượt 17:31#2 là của HW03 nên giữ.
  - Prompt log HW03 còn 7 lượt. Lọc lại HW02 vẫn ra 407 lượt.
- **4. Skill `.claude/skills/gui-checklist-testing/`:**
  - `SKILL.md` 7 bước, `references/schema-checklist.md`, `assets/dom_probe.js`, `assets/RUN_template.md`.
  - Scripts: `check_checklist`, `freeze`, `render_checklist` (chuyển từ `tools/`, ở `tools/` để lại script chuyển tiếp), `merge_platform`, `build_excel`.
- **Kết quả kiểm tra:**
  - `check_checklist` trên `HW03/checklist/checklist.json`: 0 lỗi, 1 cảnh báo (CL-07 chưa có câu "Fail nếu").
  - `render_checklist` chạy lại cho ra `checklist.md` giống hệt bản đã commit.
  - Thử `merge_platform` và `freeze` trên bản sao trong thư mục tạm: chặn kết quả mâu thuẫn khi không có `--force`, từ chối N/A trên nền tảng đang áp dụng.
  - `build_excel`: **chưa chạy được** vì máy chưa cài `openpyxl`; mới chỉ kiểm cú pháp.
- **Commit:**
  - `e781197`, `24f1345` – tách CLAUDE.md (2 commit)
  - `2d16283` – HARNESS_SETUP
  - `b2e7ef8` – exclude
  - `a1df52c` – skill (khung)
- **Bất thường:** `~/.gitignore_global` dòng 5 chặn mọi file `CLAUDE.md` nên lần commit đầu thiếu `HW02/` và `HW03/CLAUDE.md`. Em thêm `!CLAUDE.md` vào `.gitignore` của repo và commit bổ sung, không amend.
- **Cần quyết định:**
  - X1 – cài `openpyxl` để chạy được `build_excel` (bước 5)? (a) `python -m pip install openpyxl`; (b) để tới bước 5.
  - X2 – `HW03/CLAUDE.md` có nộp trong zip không? (a) thêm `export-ignore`; (b) nộp như tài liệu harness.
- **Nhắc:** bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `CLAUDE.md`, `CLAUDE.md`, `xl.py`, `SKILL.md`, `schema-checklist.md`, `check_checklist.py`, `freeze.py`, `merge_platform.py`, `build_excel.py`, `dom_probe.js`, `RUN_template.md`

**Xử lý:** [...]

---

## #24 | 18:19 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03 – 4 việc harness. Xong cả 4, tổng 5 commit: mục 1 tốn 2 commit vì một chỗ chặn của gitignore toàn cục. Chưa đổi dữ liệu HW03.
- 1. Tách CLAUDE.md:
  - Số dòng trước: CLAUDE.md 248. Sau: CLAUDE.md gốc 112, HW02/CLAUDE.md 205 (§1, §2, §5, §6 và các dòng HW02 của §3–§4, chép nguyên văn), HW03/CLAUDE.md 91.
  - Script so từng dòng: chỉ 6 dòng gốc không còn nguyên văn — các dòng 10, 34, 37, 38, 40, 42 (quy tắc ghi quyết định, danh sách "đọc gì trước", mục Quyết định HW03). Nội dung vẫn còn, chỉ viết lại cho chung.
- 2. HARNESS_SETUP: thêm mục 6, checklist bắt đầu bài mới gồm 7 bước.
- 3. L1=c:
  - extract_prompt_log.py thêm --exclude (lặp được); on_stop.py và ừ hw.toml.
  - exclude bỏ 17:24–17:30 và lượt 17:31 đầu tiên; lượt 17:31#2 là của HW03 nên giữ.
  - Prompt log HW03 còn 7 lượt. Lọc lại HW02 vẫn ra 407 lượt.
- 4. Skill .claude/skills/gui-checklist-testing/:
  - SKILL.md 7 bước, references/schema-checklist.md, assets/dom_probe.js, assets/RUN_template.md.
  - Scripts: check_checklist, freeze, render_checklist (chuyển từ t chuyển tiếp), merge_platform, build_excel.
- Kết quả kiểm tra:
  - check_checklist trên HW03/checklist/checklist.json: 0 lỗi, 1 cảil nếu").
  - render_checklist chạy lại cho ra checklist.md giống hệt bản đã commit.
  - Thử merge_platform và freeze trên bản sao trong thư mục tạm: chg có --force, từ chối N/A trên nền tảng đang áp dụng.
  - build_excel: chưa chạy được vì máy chưa cài openpyxl; mới chỉ kiểm cú pháp.
- Commit:
  - e781197, 24f1345 – tách CLAUDE.md (2 commit)
  - 2d16283 – HARNESS_SETUP
  - b2e7ef8 – exclude
  - a1df52c – skill (khung)
- Bất thường: ~/.gitignore_global dòng 5 chặn mọi file CLAUDE.md nêvà HW03/CLAUDE.md. Em thêm !CLAUDE.md vào .gitignore của repo vàcommit bổ sung, không amend.
- Cần quyết định:
  - X1 – cài openpyxl để chạy được build_excel (bước 5)? (a) python -m pip install openpyxl; (b) để tới bước 5.
  - X2 – HW03/CLAUDE.md có nộp trong zip không? (a) thêm export-ignness.
- Nhắc: bạn tự push (git push).
```

**Output:**
````
Mình chưa thấy commit mới trên GitHub: `origin/main` vẫn dừng ở `be8996e`. Bạn **push** để mình kiểm `CLAUDE.md` (6 dòng được viết lại), skill và 65 item.

## X1, X2

- **X1 = a: cài ngay.** Lệnh tốn 10 giây, và `build_excel.py` được thử sớm thì lỗi lộ ra sớm, không phải đợi đến bước 5. Lưu ý dùng **cùng trình Python** với các script còn lại: ở HW02, việc nén ảnh chạy bằng `py -3.12`.
- **X2 = a: không nộp `HW03/CLAUDE.md`**, đúng ý bạn "chỉ nộp file cần nộp". File này chỉ là chỉ dẫn cho Claude Code, đề không yêu cầu. Audit vẫn khai nó là một artifact, dẫn bằng mã commit. Skill thì vẫn nộp như bình thường (`HW03/skills/` khi đóng gói).

## Lệnh cho Claude Code

```
HW03 – X1=a, X2=a (commit "HW03: X1, X2"):
1. Cài openpyxl cho đúng trình Python các script đang dùng; chạy thử build_excel.py ra bản nháp trong thư mục tạm (không commit file xlsx).
2. HW03/.gitattributes: thêm CLAUDE.md export-ignore. report_plan mục e: X1=a, X2=a.
3. Tạo khung trống HW03/checklist/sv_items.md (chỉ tiêu đề cột: id SV-xx, ia, man_hinh, muc_kiem_tra, can_cu, expected, nen_tang, ly_do_AI_bo_sot) — không ví dụ, không danh mục, không commit riêng (gộp vào commit này, khai Audit).
on_stop.py --manual; commit. Báo cáo ≤ 6 dòng.
```

## Việc của bạn (làm song song, không cần chờ mình)

1. **Push.**
2. Mở `HW03/checklist/checklist.md`, đọc 65 item AI viết. Item nào sai, thừa hoặc trùng thì ghi lại để báo mình. Mình sẽ đối chiếu với bước kiểm nhất quán của mình.
3. Điền `sv_items.md` 🔒 với những item AI bỏ sót. Mỗi item cần:
   - Đúng 1 IA.
   - Expected có căn cứ: điều khoản SRS, slide (heuristic, checklist theo control) hoặc giả định bạn chốt.
   - Ghi chỗ quan sát và ngưỡng Pass/Fail.
   - Cột `ly_do_AI_bo_sot` là phần **bạn tự giải thích** (đề chấm): do prompt, do giới hạn model, hay do đặc điểm giao diện.
4. Commit file của bạn **trước**, rồi mới hỏi AI "vì sao bỏ sót" (`ai_gap_answer.md`), giống bước 5 của HW02.

Ở bước 3, mình sẽ không gợi ý item nào. Mình chỉ kiểm cách viết của bạn.
````

**Xử lý:** [...]

---

## #25 | 18:33 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Ủa mới, bị reject push, bạn xem lại nhé. Mình chưa dùng prompt mới nhất đâu nhé
```

**Output:**
```
Bản push đã lên GitHub (`origin/main` = `a1df52c`). Mình kiểm checklist luôn.

## Push

`origin/main` đã có `a1df52c`, tức 11 commit HW03 đều đã lên GitHub. Có thể lần đầu bị từ chối rồi lần sau mới qua. Nếu bạn vẫn thấy lỗi khi push, dán nguyên văn thông báo lỗi để mình xem.

## Kiểm nhất quán 65 item AI

Mình chỉ kiểm căn cứ, Expected và phạm vi của các item đã có, **không nhận xét còn thiếu item nào**. Tổng thể cấu trúc tốt: đủ 4 IA, mỗi item đều có căn cứ, có ngưỡng Fail, trích SRS đúng số dòng. Còn 4 điểm cần bạn quyết và một số item cần sửa.

### Cần bạn quyết

| Mã | Câu hỏi | Đề xuất |
|---|---|---|
| G1 | 17 item dựa trên heuristic (Nielsen, Shneiderman, WCAG, checklist theo control). Có được tạo Fail khi SRS im lặng không? HW02 đã chốt "SRS im lặng → không Fail" | **(a) Được**, vì slide liệt kê heuristic, WCAG và checklist theo control là nguồn chính thức của checklist GUI. Ghi rõ trong report; bug từ những item này mặc định severity thấp, bạn tự quyết cụ thể |
| G2 | 3 giả định AI đề xuất: NA1 (Tab trên P3 → N/A), GA1 (ngày dạng dd/mm/yyyy), GA2 (badge = tổng số lượng) | Bạn chốt từng cái (đồng ý / sửa / bỏ), kèm lý do |
| G3 | Ngưỡng thời gian không có căn cứ: CL-44 "≤ 2 giây", CL-55 "≤ 1 giây" | Dùng mốc thời gian phản hồi của Nielsen (0,1 s / 1 s / 10 s) làm căn cứ, hoặc bỏ ngưỡng |
| G4 | Nhóm item kiểm **chức năng** Hồ sơ: CL-31, 32, 34, 37. FR-04 là feature HW02 của bạn cùng nhóm, nên bug ở đây dễ trùng issue cũ | (a) Giữ, kiểm trùng trước khi lập bug; (b) bỏ hẳn; (c) rút về phần GUI (vị trí và nội dung thông báo). Mình nghiêng (a) |

### Lỗi cách viết

| Item | Vấn đề | Cách sửa |
|---|---|---|
| CL-10, 11, 12 | Chuỗi thứ tự Tab trong Expected có vẻ chép từ thứ tự trong code. Oracle lấy từ code thì case luôn Pass, tức là vòng lặp | Expected = thứ tự **theo vị trí hiển thị** (trên→dưới, trái→phải) như FR-21.5; bỏ chuỗi lấy từ code |
| CL-13, CL-45 | Fail dựa trên chi tiết code (tên thư mục dự án, link có tải lại trang hay không) | CL-13 giữ phần "khác nhau giữa các trang"; CL-45 bỏ, hoặc chuyển thành item về điều hướng đúng trang |
| CL-28 | "Nhãn nêu 6 chữ số": SRS chỉ yêu cầu OTP có 6 chữ số, không yêu cầu nhãn nêu điều đó | Chỉ giữ "mã hiển thị có 6 chữ số" (có thể gộp với CL-54) |
| CL-33 | "Nhãn cho biết không đổi được": SRS không yêu cầu | Bỏ vế này; giữ "không sửa được + trông như bị khoá" |
| CL-17, CL-43 | Một item khẳng định 2–3 điều, nên khi Fail khó biết điều nào sai | Tách item, hoặc ghi rõ "Fail nếu bất kỳ vế nào sai" kèm vế cụ thể trong Notes |
| CL-23 | "Chỉ hiện alert → Fail" là cách diễn giải FR-22.4, SRS không nói thẳng | Cần bạn chốt thành giả định (GA3) hoặc bỏ vế này |
| CL-40 | Kiểm cả `/cart`, đó là phạm vi C1 của bạn cùng nhóm | Chỉ giữ các trang C2 |
| CL-59 | Trích FR-20, đó là yêu cầu mobile | Bỏ FR-20, giữ FR-10 |
| CL-58 | Cần đủ đơn ở 5 trạng thái, phải dựng bằng admin × 3 nền tảng | Ghi tiền điều kiện dựng dữ liệu một lần, dùng chung cho cả 3 nền tảng |

## Cách làm tiếp

1. Bạn trả lời theo mẫu: `G1=a, G2: NA1 ok / GA1 ok / GA2 …, G3=…, G4=…, sửa: tất cả | trừ CL-xx`.
2. Mình đưa lệnh cho Claude Code sửa **theo quyết định của bạn**. Item được sửa đổi nguồn thành `Both`; commit `HW03[T1] 2/6: SV review checklist AI`; bản v1 đã đóng băng giữ nguyên.
3. Song song, bạn viết `sv_items.md` 🔒 (lệnh X1/X2 ở trên tạo khung trống). Lệnh X1/X2 vẫn chạy được như cũ.
```

**Xử lý:** [...]

---

## #26 | 18:37 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
G1= Được
G2=3 giả định nào cơ
G3=Được
G4=a
CL=Sửa tất cả
```

**Output:**
````
## G2: các giả định cần bạn chốt

Ba giả định AI đặt trong `checklist.json` (mục `assumptions`), cộng thêm một giả định mới phát sinh từ việc sửa CL-23:

| Mã | Nội dung | Dùng ở | Đề xuất |
|---|---|---|---|
| NA1 | Trên P3 (bàn phím cảm ứng) không có phím Tab, nên các item thứ tự Tab ghi **N/A** trên P3 | CL-10, 11, 12 | **Giữ** |
| GA1 | Ngày hiển thị dạng **dd/mm/yyyy**. SRS im lặng; căn cứ là FR-21.1 (giao diện tiếng Việt) + Nielsen #4 (theo chuẩn quen thuộc) | CL-09 | **Giữ** |
| GA2 | Badge giỏ hàng = **tổng số lượng** (1 SP × 2 thì badge là 2) | CL-41 | **Bỏ**. SRS chỉ nói "badge số lượng". HW02 B cũng chỉ kiểm có badge hay không (BUG-20: không có badge). CL-41 chỉ cần kiểm "có badge hiển thị số > 0 sau khi thêm 1 SP", không cần giả định |
| GA3 (mới) | Thông báo lỗi **chỉ** hiện ở hộp thoại `alert` thì không đạt FR-22.4 (lỗi phải nằm phía trên nút submit) | CL-23 | **Chốt**. Hộp thoại alert không nằm ở vị trí nào trên form |

Với G3 = được: mình dùng mốc thời gian phản hồi của Nielsen (khoảng 1 giây để người dùng không bị đứt mạch suy nghĩ) cho CL-44 và CL-55.

## Lệnh cho Claude Code

Nếu bạn đồng ý với đề xuất G2, dán lệnh này. Mình đã gộp cả lệnh X1/X2 còn chờ:

```
HW03 – 2 commit. Không sửa ai-outputs/.

A. "HW03: X1, X2": cài openpyxl đúng trình Python các script đang dùng, chạy thử build_excel.py ra thư mục tạm (không commit xlsx). HW03/.gitattributes thêm CLAUDE.md export-ignore; report_plan mục e: X1=a, X2=a. Tạo khung trống HW03/checklist/sv_items.md (chỉ tiêu đề cột: id SV-xx, ia, man_hinh, muc_kiem_tra, can_cu, expected, nen_tang, ly_do_AI_bo_sot; không ví dụ, không danh mục).

B. "HW03[T1] 2/6: SV review checklist AI": item sửa → nguon="Both"; ghi meta.review_log (ngày, mã quyết định, "SV chốt").
- G1=a: heuristic/WCAG/checklist theo control là căn cứ hợp lệ (slide GUI "Where checklists come from"); severity bug từ các item này do SV quyết.
- G2: NA1 giữ; GA1 giữ; GA2 bỏ → CL-41 chỉ kiểm có badge hiển thị số > 0 sau khi thêm 1 SP (FR-23.2); GA3 mới "Thông báo lỗi chỉ ở hộp thoại alert không thoả FR-22.4" (AI đề xuất, SV chấp nhận).
- G3: CL-44, CL-55 ngưỡng ≤ 1 s, can_cu thêm "Nielsen – response time limits (1 s)".
- G4=a: giữ CL-31/32/34/37, notes "kiểm trùng issue FR-04 trước khi lập bug".
- Sửa: CL-10/11/12 Expected = thứ tự theo vị trí hiển thị (trên→dưới, trái→phải), bỏ chuỗi lấy từ code · CL-13 bỏ vế tên kỹ thuật · CL-45 thành "link tới đúng /forgot-password" (bỏ vế tải lại trang) · CL-28 chỉ giữ "mã hiển thị 6 chữ số" · CL-33 bỏ vế nhãn · CL-17 tách type=email / chặn sai định dạng · CL-43 tách 3 vế · CL-23 căn cứ thêm GA3 · CL-40 bỏ /cart · CL-59 bỏ FR-20 · CL-58 thêm tiền điều kiện dựng đơn 5 trạng thái một lần qua admin, dùng chung 3 nền tảng.
- Item tách: id mới từ CL-66, ghi "tách từ CL-xx"; không đánh số lại.
check_checklist + render; in số item theo IA và theo nguồn (AI/Both). on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

Không đồng ý chỗ nào thì sửa trực tiếp dòng `G2` trong lệnh trước khi dán.

## Song song: phần của bạn

Bạn viết `sv_items.md` 🔒. Những item bạn thêm phải là **item mới**, không phải những chỗ mình vừa sửa. Mỗi item ghi rõ lý do AI bỏ sót. Commit file này **trước** khi hỏi AI.
````

**Xử lý:** [...]

---

## #27 | 18:40 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NA1=giữ, GA1=giữ, GA2=Nếu trong SRS không có thì bỏ luôn nhé. GA3= được
Mình chưa sử dụng lệnh Claude Code nhé
```

**Output:**
```
Quyết định của bạn **khớp hết với lệnh** mình vừa đưa, nên dán nguyên lệnh đó, không cần sửa gì.

Giải thích thêm về GA2 "bỏ luôn": chỉ **giả định** bị bỏ, còn **item CL-41 vẫn giữ**. Lý do:
- SRS có yêu cầu badge (FR-23.2: link "Giỏ hàng" phải có badge số lượng). Phần này có căn cứ nên kiểm được.
- SRS không nói badge đếm theo kiểu nào (tổng số lượng hay số dòng), nên không đặt giả định cho chỗ đó.
- CL-41 vì vậy chỉ kiểm **có badge hiển thị số > 0** sau khi thêm 1 sản phẩm.

Lệnh đã ghi đúng như trên (`GA2 bỏ → CL-41 chỉ kiểm có badge…`).

Sau khi báo cáo về:
1. Push.
2. Viết `sv_items.md` 🔒 và commit file của bạn.
3. Báo mình để đưa lệnh hỏi AI "vì sao bỏ sót" và chốt checklist v2.
```

**Xử lý:** [...]

---

## #28 | 18:41 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – 2 commit. Không sửa ai-outputs/.

A. "HW03: X1, X2": cài openpyxl đúng trình Python các script đang dùng, chạy thử build_excel.py ra thư mục tạm (không commit xlsx). HW03/.gitattributes thêm CLAUDE.md export-ignore; report_plan mục e: X1=a, X2=a. Tạo khung trống HW03/checklist/sv_items.md (chỉ tiêu đề cột: id SV-xx, ia, man_hinh, muc_kiem_tra, can_cu, expected, nen_tang, ly_do_AI_bo_sot; không ví dụ, không danh mục).

B. "HW03[T1] 2/6: SV review checklist AI": item sửa → nguon="Both"; ghi meta.review_log (ngày, mã quyết định, "SV chốt").
- G1=a: heuristic/WCAG/checklist theo control là căn cứ hợp lệ (slide GUI "Where checklists come from"); severity bug từ các item này do SV quyết.
- G2: NA1 giữ; GA1 giữ; GA2 bỏ → CL-41 chỉ kiểm có badge hiển thị số > 0 sau khi thêm 1 SP (FR-23.2); GA3 mới "Thông báo lỗi chỉ ở hộp thoại alert không thoả FR-22.4" (AI đề xuất, SV chấp nhận).
- G3: CL-44, CL-55 ngưỡng ≤ 1 s, can_cu thêm "Nielsen – response time limits (1 s)".
- G4=a: giữ CL-31/32/34/37, notes "kiểm trùng issue FR-04 trước khi lập bug".
- Sửa: CL-10/11/12 Expected = thứ tự theo vị trí hiển thị (trên→dưới, trái→phải), bỏ chuỗi lấy từ code · CL-13 bỏ vế tên kỹ thuật · CL-45 thành "link tới đúng /forgot-password" (bỏ vế tải lại trang) · CL-28 chỉ giữ "mã hiển thị 6 chữ số" · CL-33 bỏ vế nhãn · CL-17 tách type=email / chặn sai định dạng · CL-43 tách 3 vế · CL-23 căn cứ thêm GA3 · CL-40 bỏ /cart · CL-59 bỏ FR-20 · CL-58 thêm tiền điều kiện dựng đơn 5 trạng thái một lần qua admin, dùng chung 3 nền tảng.
- Item tách: id mới từ CL-66, ghi "tách từ CL-xx"; không đánh số lại.
check_checklist + render; in số item theo IA và theo nguồn (AI/Both). on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

**Output:**
```
Excel chạy được (openpyxl qua pacman MSYS2). Giờ commit A.

Part B: áp review SV vào checklist.json.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – chốt X1, X2 và áp bản review của SV vào checklist (T1 2/6). Xong cả hai. Lệnh yêu cầu 2 commit, thực tế là 3: lần commit A, lệnh sửa `report_plan.md` bị lỗi mà em không thấy, nên phải thêm 1 commit ghi X1/X2 (không amend).
- **X1:** `python` của các script là MSYS2 (`C:\msys64\ucrt64\bin\python.exe` 3.14) và không có pip, nên em cài bằng `pacman -S mingw-w64-ucrt-x86_64-python-openpyxl`. Lệnh này kéo thêm `python-pillow` và vài thư viện ảnh. `openpyxl` 3.1.5 đã chạy được.
  - `build_excel.py` ra thư mục tạm: đủ 3 sheet, có công thức COUNTIF; file xlsx không commit.
- **X2:** `HW03/.gitattributes` thêm `CLAUDE.md export-ignore`. Thử `git archive`: zip không còn `report_plan.md` lẫn `CLAUDE.md`. Đã tạo khung `HW03/checklist/sv_items.md` (chỉ tiêu đề cột).
- **Review:** `checklist.json` và `.md` cập nhật đủ G1–G4 và các sửa.
  - Item tách: CL-66 (từ CL-17); CL-67, CL-68 (từ CL-43).
  - `assumptions`: bỏ GA2, thêm GA3.
  - `meta.review_log` có 5 mục (G1–G4, S), mỗi mục ghi "SV chốt".
  - `ai-outputs/` không sửa.
- **Số item: 68.** Theo IA: IA-01 16 · IA-02 24 · IA-03 13 · IA-04 15. Theo nguồn: AI 49 · Both 19.
  - CL-31/32/34/37 chỉ thêm notes nên em giữ `nguon` = AI. Nếu bạn muốn tính là "sửa" thì đổi thành Both.
- **Kết quả kiểm tra:** `check_checklist` 0 lỗi, 1 cảnh báo (CL-07 chưa có câu "Fail nếu"). Prompt log 8 lượt.
- **Commit:**
  - `b8a86e9 HW03: X1, X2`
  - `d7dc423 HW03: X1, X2 – ghi quyết định vào report_plan mục e`
  - `a8b8560 HW03[T1] 2/6: SV review checklist AI`
- **Cần quyết định:** không có điểm chặn. Lưu ý: commit 2/6 hiện mới là phần review; item SV tự thêm (`sv_items.md`) chưa có, và `HW03/CLAUDE.md` đang định nghĩa bước 2 gồm cả phần đó.
- **Nhắc:** bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `review_b.py`

**Xử lý:** [...]

---

## #29 | 18:46 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03 – chốt X1, X2 và áp bản review của SV vào checklist (T1 2/6). Xong cả hai. Lệnh yêu cầu 2 commit, thực tế là 3: lần commit A, lệnh sửa report_plan.md bị lỗi mà em không thấy, nên phải thêm 1 commit ghi X1/X2 (không amend).
- X1: python của các script là MSYS2 (C:\msys64\ucrt64\bin\python.exe 3.14) và không có pip, nên em cài bằng pacman -S mingw-w64-ucrt-x86_64-python-openpyxl. Lệnh này kéo thêm python-pillow và vài thư viện ảnh. openpyxl 3.1.5 đã chạy được.
  - build_excel.py ra thư mục tạm: đủ 3 sheet, có công thức COUNTIF; file xlsx không commit.
- X2: HW03/.gitattributes thêm CLAUDE.md export-ignore. Thử git archive: zip không còn report_plan.md lẫn CLAUDE.md. Đã tạo khung HW03/checklist/sv_items.md (chỉ tiêu đề cột).
- Review: checklist.json và .md cập nhật đủ G1–G4 và các sửa.
  - Item tách: CL-66 (từ CL-17); CL-67, CL-68 (từ CL-43).
  - assumptions: bỏ GA2, thêm GA3.
  - meta.review_log có 5 mục (G1–G4, S), mỗi mục ghi "SV chốt".
  - ai-outputs/ không sửa.                                                                                                                                           Số item: 68. Theo IA: IA-01 16 · IA-02 24 · IA-03 13 · IA-04 15.
  - CL-31/32/34/37 chỉ thêm notes nên em giữ nguon = AI. Nếu bạn muốn tính là "sửa" thì đổi thành Both.
- Kết quả kiểm tra: check_checklist 0 lỗi, 1 cảnh báo (CL-07 chưa có câu "Fail nếu"). Prompt log 8 lượt.
- Commit:                                                                                                                                                            - b8a86e9 HW03: X1, X2
  - d7dc423 HW03: X1, X2 – ghi quyết định vào report_plan mục e                                                                                                      - a8b8560 HW03[T1] 2/6: SV review checklist AI
- Cần quyết định: không có điểm chặn. Lưu ý: commit 2/6 hiện mới là phần review; item SV tự thêm (sv_items.md) chưa có, và HW03/CLAUDE.md đang định nghĩa bước 2 gồm cả phần đó.
- Nhắc: bạn tự push (git push).
===
Giúp mình viết trước format cho sv_items.md để mình tự điền vào luôn nhé. Có thể prompt cho Claude Code nhé
```

**Output:**
````
Bạn không cần dán prompt nào cả. Tải file `sv_items.md`, **ghi đè** lên `HW03\checklist\sv_items.md` rồi điền. Khung có:
- **Khối quy tắc viết** cho từng trường. Xoá khối này trước khi nộp.
- **Bảng giả định mới**, đánh mã từ GA4.
- **Khối item** `SV-01`, `SV-02`. Muốn thêm item thì chép nguyên khối, tăng số.

Trong khung có thêm trường `luc_them`. Item nghĩ ra trong lúc chạy thì ghi "trong lúc chạy Px". Ghi trung thực như vậy giúp phần giải thích "vì sao AI bỏ sót" có cơ sở.

## Về báo cáo vừa rồi

- **CL-31/32/34/37 giữ `nguon = AI`** là đúng. Chỉ thêm notes thì không đổi nội dung item.
- **CL-07** còn thiếu vế "Fail nếu…". Mình gộp phần sửa này vào lệnh dưới.
- **Đánh số bước:** `2/6` = review, `2/6b` = item SV thêm, `2/6c` = AI trả lời "vì sao bỏ sót", `2/6d` = chốt checklist v2.

## Lệnh dùng sau khi bạn điền xong

```
HW03[T1] 2/6b:
0. CL-07: thêm vế "Fail nếu chênh chiều cao > 2 px hoặc khác font-family/font-size" → commit "HW03[T1] 2/6: vá CL-07".
1. Kiểm HW03/checklist/sv_items.md (CHỈ ĐỌC, không sửa chữ của tôi): trường thiếu, ia hợp lệ, id trùng, can_cu trỏ tới dòng SRS có thật, item trùng nội dung với CL-xx → in danh sách.
2. Không có lỗi cấu trúc → commit "HW03[T1] 2/6b: SV bổ sung item" (chỉ sv_items.md + prompt log). Có lỗi → dừng, báo tôi.
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

Báo cáo về xong, mình đưa lệnh 2/6c để AI trả lời "vì sao bỏ sót", tách 3 nhóm như HW02: *đã nghĩ tới nhưng không đưa vào*, *không nghĩ tới*, *đã có nhưng bị gỡ theo quyết định của bạn*.
````
*File AI ghi/gửi trong lượt này:* `sv_items.md`

**Xử lý:** [...]

---

## #30 | 18:48 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đợi chút, trước khi mình viết, có thể cho mình một số hint để ra ý tưởng viết. Hoặc là một số chỗ cần xem kĩ để viết được không nhỉ?
```

**Output:**
```
Phần này mình không gợi ý được, kể cả dưới dạng "chỗ nên xem kỹ". Có hai lý do. Thứ nhất, đây là phần G9.3 được chấm: đề yêu cầu bạn tự tìm item AI bỏ sót và tự giải thích vì sao. Thứ hai, nếu mình chỉ chỗ, thì item đó không còn là "AI bỏ sót" nữa, vì chính AI đã nghĩ ra. Lúc đó cột `ly_do_AI_bo_sot` sẽ thành sai sự thật, và Audit phải khai lượt gợi ý này. Vào vấn đáp, TA hỏi "em tìm ra item này bằng cách nào" thì bạn cũng khó trả lời.

Mình giúp được ở mức phương pháp. Đó là các nguồn trong tài liệu môn và cách tự rà, không chỉ vào chỗ cụ thể nào trên SUT:

**Nguồn trong tài liệu môn.** Slide "GUI, Usability & Compatibility" (bản Combined) có đủ các nhóm sau:
- Checklist theo từng control: Text Box, Dropdown, Button, Checkbox/Radio, Hyperlink/Image/Grid/List/Date, input-field validation.
- Ba bộ heuristic: Nielsen 10, Norman 6, Shneiderman 8.
- Bảng nguồn của checklist ("Inputs to a good GUI checklist").
- Các link checklist tham khảo ở cuối slide usability.
- Đoạn thứ hai của Task 1 trong đề.

**Cách rà.** Mở từng màn C2 trên **thiết bị thật**, đi qua từng nguồn ở trên **một mục một lần**. Với mỗi mục, tự hỏi: mục này áp dụng cho màn này thế nào, và trong 68 item đã có item nào kiểm nó chưa. Item nghĩ ra trong lúc chạy P1/P2/P3 cũng tính, chỉ cần ghi đúng ở trường `luc_them`. Chạy trên nhiều nền tảng khác nhau thường tự lộ ra những thứ bản nháp chưa nghĩ tới.

**Sau khi bạn commit.** AI sẽ trả lời trung thực cho từng item bạn thêm: đã nghĩ tới nhưng không đưa vào, không nghĩ tới, hay đã có nhưng bị bỏ theo quyết định của bạn. Trong lúc bạn viết, mình kiểm được *cách viết*, ví dụ căn cứ có hợp lệ không, Expected có câu "Fail nếu" chưa, có trùng CL-xx không. Mình không nhận xét *nội dung* item nên có hay không.
```

**Xử lý:** [...]

---

## #31 | 18:52 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Rồi, vậy C2 mình cần xem qua các UI nào nhỉ.
===
Mà cho mình hỏi GUI testing này có tool mà nhỉ, có tool automation không nhỉ, như PlayWright có tự chạy E2E, rồi screenshot,...
```

**Output:**
```
## 1. Phạm vi C2: các màn hình và trạng thái cần mở

Danh sách control chi tiết của từng màn (kèm `file:dòng`) có trong `HW03/checklist/c2_inventory.md`. Dưới đây là đường đi để tới từng màn hình và trạng thái:

| Màn / trạng thái | Cách tới |
|---|---|
| **Đăng nhập** `/login` (chưa đăng nhập) | Navbar → "Đăng nhập" |
| ↳ sau khi đăng nhập sai / sai liên tiếp / đăng nhập thành công | Nhập sai mật khẩu với `test@eshop.com`; đăng nhập đúng `Test1234!` |
| **Quên mật khẩu – bước 1** `/forgot-password` | Từ trang Đăng nhập → link "Quên mật khẩu?" |
| ↳ **bước 2** (OTP, mật khẩu mới…) và sau khi đổi thành công | Nhập email ở bước 1 → gửi |
| **Hồ sơ** `/profile` khi đã đăng nhập | Navbar → tên người dùng |
| ↳ sau khi bấm Cập nhật (hợp lệ / không hợp lệ) | Sửa các ô trong form |
| **Lịch sử đơn** (nằm trong `/profile`): khi chưa có đơn | Ngay sau khi restart backend (CSDL seed lại, chưa có đơn nào) |
| ↳ khi có đơn, ở các trạng thái khác nhau, và khi huỷ đơn | Đặt đơn qua luồng mua hàng (C1), rồi đổi trạng thái đơn ở admin `:5174` (`admin@eshop.com` / `Admin123!`) |
| **`/profile` khi chưa đăng nhập** | Đăng xuất rồi gõ thẳng URL |
| **Navbar khi đã đăng nhập và sau khi đăng xuất** | Có trên mọi trang C2 |

Mỗi màn ở trên cần xem trên cả 3 nền tảng (P1 Chrome, P2 Firefox, P3 Chrome Android).

## 2. Tool automation cho GUI testing

**Có.** Slide liệt kê nhiều tool:
- **Playwright**: chạy E2E, `toHaveScreenshot` so ảnh, chạy được trên Chromium, Firefox và WebKit.
- **BackstopJS / Percy**: so sánh ảnh giao diện giữa các lần chạy (visual regression).
- **axe DevTools / Lighthouse**: kiểm accessibility.
- **Playwright MCP**: cho LLM tự lái trình duyệt.

Với HW03 có 2 giới hạn:
1. **Ảnh Playwright không thay được ảnh của Task 3.** Playwright chỉ chụp nội dung trang, không chụp thanh địa chỉ, tên trình duyệt hay overlay MSSV. Đề bắt ảnh cross-platform phải thấy các thứ đó, nên ảnh cho item Failed trên từng nền tảng vẫn phải chụp tay cửa sổ thật.
2. **Firefox của Playwright không phải Firefox bạn cài.** Đó là bản build riêng của Playwright. Chrome thì dùng được bản cài thật (`channel: 'chrome'`). Kết quả automation nên coi là **kết quả tự động** (`auto_status`, như HW02). Verdict chính thức là lượt chạy trên trình duyệt thật.

**E2 – chọn cách chạy:**
- **(a) Chạy tay + `dom_probe.js`** (skill đã có sẵn). Dán vào Console để đọc DOM; trên P3 thì dán qua `chrome://inspect`. Mọi thứ còn lại kiểm bằng mắt. Ước lượng 1,5–2 giờ cho cả 3 nền tảng.
- **(b) Kết hợp.** Playwright tự chạy trên P1/P2 các item kiểm được bằng DOM hoặc bàn phím (`<h1>`, type, nhãn, thứ tự Tab, chuyển trang…), xuất `auto_status` + ảnh phần tử. Bạn chỉ chạy tay các item kiểm bằng mắt/tương tác, chụp ảnh có overlay cho item Failed, và chạy tay toàn bộ P3. Tốn khoảng 20–30 phút để Claude Code viết và thử script, đổi lại bớt khoảng 1/3 thời gian chạy tay. Report cũng có thêm phần automation để trình bày.

Mình nghiêng về **(b)**, vì bạn muốn ít thao tác tay. Nhưng nếu đang gấp, (a) chắc chắn hơn vì không mất thời gian sửa script.

Dù chọn cách nào, **viết `sv_items.md` trước**: kế hoạch chạy (`RUN.md`) và script cần bao gồm cả item của bạn.
```

**Xử lý:** [...]

---

## #32 | 19:26 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Thiên về b nhé
===
Viết xong rồi. commit xong push hả? Giúp mình viết commit message nhé
```

**Output:**
````
Đúng, bạn tự commit rồi push. Commit do chính tài khoản bạn tạo là bằng chứng rõ ràng nhất cho Audit rằng phần này do bạn viết. **Chỉ add `sv_items.md`**. File prompt log (`A_prompt_log.md`) do hook tự cập nhật, để Claude Code commit ở lệnh sau.

```powershell
git add HW03/checklist/sv_items.md
git commit -m "HW03[T1] 2/6b: SV bổ sung item checklist (sv_items.md)"
git push
```

Push xong, mình đọc `sv_items.md` và kiểm **cách viết** (trường thiếu, căn cứ, câu "Fail nếu", trùng với CL-xx). Mình không nhận xét nội dung item.

## Lệnh tiếp theo cho Claude Code (dán sau khi push)

```
HW03 – 3 commit. Không sửa sv_items.md, không sửa ai-outputs/.
A. "HW03[T1] 2/6: vá CL-07": thêm vế "Fail nếu chênh chiều cao > 2 px hoặc khác font-family/font-size". report_plan mục e: E2=b (Playwright tự chạy item DOM/bàn phím trên P1 Chrome channel + P2 Firefox Playwright → auto_status; SV chạy tay phần còn lại + toàn bộ P3; verdict chính thức = lượt trên trình duyệt thật).
B. Kiểm sv_items.md (CHỈ ĐỌC): trường thiếu/"(SV chưa ghi)", ia hợp lệ, id trùng, can_cu trỏ tới dòng SRS có thật, item trùng nội dung CL-xx → ghi HW03/checklist/sv_items_check.md (chỉ liệt kê, không đề xuất câu chữ). Commit chung với C.
C. "HW03[T1] 2/6c: AI trả lời vì sao bỏ sót": HW03/checklist/ai_gap_answer.md — mỗi SV-xx xếp đúng 1 nhóm: (1) đã nghĩ tới nhưng không đưa vào, (2) không nghĩ tới, (3) đã có nhưng bị gỡ theo quyết định SV. Bằng chứng phải lấy từ bản v1 (T1_checklist_ai_v1.json, c2_inventory.md, prompt của lệnh 1/6): nhóm (1) chỉ khi inventory/v1 có nhắc tới; không có bằng chứng → nhóm (2) và ghi "không có dấu vết trong v1". Nêu nguyên nhân khả dĩ (prompt / giới hạn model / đặc điểm giao diện), ghi rõ là nhận định của AI. Không viết thay cột ly_do_AI_bo_sot của SV.
on_stop.py --manual (commit cả A_prompt_log.md). Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

Sau bước này, bạn so lý do bạn tự viết với câu trả lời của AI. Chỗ hai bên khác nhau là tư liệu tốt cho phần gap analysis và Critique. Sau đó Claude Code gộp item của bạn vào checklist v2 (`2/6d`) rồi viết script Playwright + `RUN.md`.
````

**Xử lý:** [...]

---

## #33 | 19:27 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – 3 commit. Không sửa sv_items.md, không sửa ai-outputs/.
A. "HW03[T1] 2/6: vá CL-07": thêm vế "Fail nếu chênh chiều cao > 2 px hoặc khác font-family/font-size". report_plan mục e: E2=b (Playwright tự chạy item DOM/bàn phím trên P1 Chrome channel + P2 Firefox Playwright → auto_status; SV chạy tay phần còn lại + toàn bộ P3; verdict chính thức = lượt trên trình duyệt thật).
B. Kiểm sv_items.md (CHỈ ĐỌC): trường thiếu/"(SV chưa ghi)", ia hợp lệ, id trùng, can_cu trỏ tới dòng SRS có thật, item trùng nội dung CL-xx → ghi HW03/checklist/sv_items_check.md (chỉ liệt kê, không đề xuất câu chữ). Commit chung với C.
C. "HW03[T1] 2/6c: AI trả lời vì sao bỏ sót": HW03/checklist/ai_gap_answer.md — mỗi SV-xx xếp đúng 1 nhóm: (1) đã nghĩ tới nhưng không đưa vào, (2) không nghĩ tới, (3) đã có nhưng bị gỡ theo quyết định SV. Bằng chứng phải lấy từ bản v1 (T1_checklist_ai_v1.json, c2_inventory.md, prompt của lệnh 1/6): nhóm (1) chỉ khi inventory/v1 có nhắc tới; không có bằng chứng → nhóm (2) và ghi "không có dấu vết trong v1". Nêu nguyên nhân khả dĩ (prompt / giới hạn model / đặc điểm giao diện), ghi rõ là nhận định của AI. Không viết thay cột ly_do_AI_bo_sot của SV.
on_stop.py --manual (commit cả A_prompt_log.md). Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

**Output:**
```
Đang kiểm `sv_items.md` (chỉ đọc): đối chiếu tên slide được trích.

Viết `sv_items_check.md` và `ai_gap_answer.md`.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – vá CL-07 + chốt E2, kiểm `sv_items.md` (chỉ đọc), AI trả lời vì sao bỏ sót. Xong cả 3, gộp thành 2 commit theo lệnh. Không sửa `sv_items.md` và `ai-outputs/`.
- **A – vá CL-07:** thêm vế "Fail nếu chênh chiều cao > 2 px hoặc khác font-family/font-size", `nguon` đổi thành Both, `review_log` thêm mục S2. `report_plan` mục e thêm E2=b.
  - `check_checklist`: 0 lỗi, 0 cảnh báo. 68 item: AI 48, Both 20.
- **B – kiểm `sv_items.md`** (kết quả ở `HW03/checklist/sv_items_check.md`):
  - Không thiếu trường nào; `ia` hợp lệ; id không trùng.
  - Không item nào trích dòng SRS. 6 tên slide được trích đều có trong slide; riêng SV-01 gộp 2 slide thành một tên.
  - SV-05: P1/P2 ghi N/A nhưng không kèm mã giả định.
  - SV-06 trùng một phần với CL-53.
  - `luc_them` ghi "trong lúc chạy P1/P2/P3", nhưng repo chưa có lượt chạy nào.
  - 6 item SV chưa được đưa vào `checklist.json`.
- **C – vì sao bỏ sót** (`HW03/checklist/ai_gap_answer.md`):
  - Nhóm (1) đã nghĩ tới nhưng không đưa vào: SV-06, bằng chứng là CL-53 của v1.
  - Nhóm (2) không nghĩ tới: SV-01…SV-05, đều "không có dấu vết trong v1". Riêng SV-03: đoạn slide có Golden Rule nằm trong phần AI đã đọc ở lượt 1/6 mà v1 vẫn không có item nào.
  - Nhóm (3) bị gỡ theo quyết định SV: không có.
- **Commit:**
  - `9463442 HW03[T1] 2/6: vá CL-07`
  - `de4c69a HW03[T1] 2/6c: AI trả lời vì sao bỏ sót` (gồm cả B và prompt log 9 lượt)
- **Cần quyết định:** M1 – đưa 6 item SV vào `checklist.json` thế nào? (a) AI chép nguyên văn sang JSON với id SV-xx, `nguon` = SV; (b) SV tự chép.
- **Nhắc:** bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `sv_items_check.md`, `ai_gap_answer.md`

**Xử lý:** [...]

---

## #34 | 19:35 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03 – vá CL-07 + chốt E2, kiểm sv_items.md (chỉ đọc), AI trả lời vì sao bỏ sót. Xong cả 3, gộp thành 2 commit theo lệnh. Không sửa sv_items.md và ai-outputs/.
- A – vá CL-07: thêm vế "Fail nếu chênh chiều cao > 2 px hoặc khác font-family/font-size", nguon đổi thành Both, review_log thêm mục S2. report_plan mục e thêm E2=b.
  - check_checklist: 0 lỗi, 0 cảnh báo. 68 item: AI 48, Both 20.
- B – kiểm sv_items.md (kết quả ở HW03/checklist/sv_items_check.md)
  - Không thiếu trường nào; ia hợp lệ; id không trùng.
  - Không item nào trích dòng SRS. 6 tên slide được trích đều có trong slide; riêng SV-01 gộp 2 slide thành một tên.
  - SV-05: P1/P2 ghi N/A nhưng không kèm mã giả định.
  - SV-06 trùng một phần với CL-53.
  - luc_them ghi "trong lúc chạy P1/P2/P3", nhưng repo chưa có lượt
  - 6 item SV chưa được đưa vào checklist.json.
- C – vì sao bỏ sót (HW03/checklist/ai_gap_answer.md):
  - Nhóm (1) đã nghĩ tới nhưng không đưa vào: SV-06, bằng chứng là CL-53 của v1.
  - Nhóm (2) không nghĩ tới: SV-01…SV-05, đều "không có dấu vết trode có Golden Rule nằm trong phần AI đã đọc ở lượt 1/6 mà v1 vẫnkhông có item nào.
  - Nhóm (3) bị gỡ theo quyết định SV: không có.
- Commit:
  - 9463442 HW03[T1] 2/6: vá CL-07
  - de4c69a HW03[T1] 2/6c: AI trả lời vì sao bỏ sót (gồm cả B và prompt log 9 lượt)
- Cần quyết định: M1 – đưa 6 item SV vào checklist.json thế nào? (a) AI chép nguyên văn sang JSON với id SV-xx, nguon = SV; (b) SV tự chép.
- Nhắc: bạn tự push (git push).
===
Mình cũng vừa push mới luôn rồi nhé
```

**Output:**
```
Mình đã đọc `sv_items.md`, `sv_items_check.md` và `ai_gap_answer.md`. Dưới đây chỉ là góp ý về **cách viết và dữ kiện**, không nhận xét item nào nên có hay không.

## 1. Một câu hỏi thẳng (hỏi một lần)

Phần này có dùng công cụ AI khác (ChatGPT, Gemini…) để viết không?

Mình hỏi vì hai dấu hiệu:
- Cả 5 item có `luc_them` = "trong lúc chạy P1/P2/P3", nhưng repo **chưa có lượt chạy nào**.
- Văn phong khác hẳn phần bạn viết ở HW02.

Nếu **có**: lượt đó phải khai vào `prompt_log_extra.toml`, và phần 🔒 phải tự viết lại. Item do AI khác nghĩ ra thì không còn là "item AI bỏ sót" nữa.
Nếu **không**: bỏ qua câu hỏi này, chỉ cần sửa các điểm bên dưới.

## 2. Phải sửa (sai dữ kiện)

| Chỗ | Vấn đề |
|---|---|
| `luc_them` của SV-01, 02, 04, 05, 06 | Commit `823f7b9` có trước mọi lượt chạy. Phải ghi **"trước khi chạy"**. Nếu sau này thêm item trong lúc chạy thật thì ghi đúng lúc đó |
| SV-05 `nen_tang` | P1/P2 N/A nhưng chưa có mã giả định |
| GA4 cột "Loại" | GA4 đang dùng làm căn cứ Expected của SV-05, nên loại là **"quyết định Expected"**, không phải "phạm vi" |

## 3. Nên xem lại (dữ kiện chưa khớp, hoặc khẳng định quá mức)

| Item | Điểm |
|---|---|
| SV-06 | Trùng một phần với CL-53, cùng oracle "chỉ 1 request". Cần ghi rõ phần khác nhau: mạng bình thường, các form khác Đăng nhập |
| SV-06 lý do | Bạn ghi "giới hạn model". Theo `ai_gap_answer.md`, AI có nghĩ tới (CL-53) nhưng slide "Double-submit" **nằm ngoài phần AI đã đọc**. Nguyên nhân vì vậy gần với "input/ngữ cảnh" hơn |
| SV-03 lý do | Bạn ghi "prompt chỉ yêu cầu kiểm tra sự xuất hiện của thông báo lỗi". Prompt 1/6 có yêu cầu nguồn "checklist theo control (… validation)". Ngoài ra, Golden Rule nằm trong phần slide AI đã đọc mà AI vẫn không dùng. Câu hiện tại chưa khớp với dữ kiện này |
| SV-03 expected | "Sau khi đóng thông báo" ngầm cho rằng thông báo là hộp thoại. Nếu thông báo hiện ngay trên trang thì không có bước "đóng" |
| SV-04 lý do | "AI **không thể** tính tỷ lệ tương phản" là khẳng định quá mức: AI tính được từ mã màu. Dữ kiện chỉ cho thấy prompt không nhắc accessibility và AI không chạy SUT |
| SV-05 lý do | "AI **không thể** mô phỏng" cũng vậy. Dữ kiện là AI không nghĩ tới, vì coi P3 chỉ như một trình duyệt nữa |
| SV-01 lý do | "AI **thường**…" là khái quát từ một bản v1. Nên viết "ở bản v1, AI chỉ…" |
| SV-01 căn cứ | "Text Box & Button" là 2 slide riêng, nên ghi đúng tên từng slide |
| SV-04 căn cứ | Slide "Accessibility & colour-blindness" nói về mô phỏng mù màu, không nói tỷ lệ tương phản. WCAG SC 1.4.3 đã đủ làm căn cứ |
| SV-02 expected | Autofill cần tiền điều kiện: trình duyệt đã lưu tài khoản. Item cũng đang khẳng định 2 điều (dán + autofill), nên ghi "Fail nếu bất kỳ vế nào…" |

## 4. M1: đưa item của bạn vào `checklist.json`

**(a) AI chép nguyên văn** sang JSON với `nguon = SV`, giữ nguyên chữ của bạn. Đây là cách đã làm ở HW02. Nhưng nên chép **sau khi bạn sửa xong**.

Thứ tự:
1. Bạn sửa `sv_items.md` rồi tự commit: `HW03[T1] 2/6b2: SV sửa item theo kiểm dữ kiện`, sau đó push.
2. Báo mình. Mình đưa lệnh `2/6d` (chép vào JSON, chốt v2), rồi lệnh viết Playwright + `RUN.md`.
```

**Xử lý:** [...]

---

## #35 | 19:44 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
push rồi nhé. Check lại nhé
```

**Output:**
````
Đã đọc commit `1e3b806`. Các điểm ở lượt trước đã sửa đúng:
- `luc_them` của 5 item đã thành "trước khi chạy".
- SV-06 đã tách khỏi CL-53 (thêm điều kiện mạng bình thường, các form khác Đăng nhập), lý do đã khớp dữ kiện.
- SV-01 tách 2 slide; SV-04 bỏ slide không liên quan.
- SV-02 đã có tiền điều kiện và câu "bất kỳ vế nào".
- Các lý do không còn "không thể" hay "thường".
- Nhãn nút bạn trích ('Sign In', 'Lấy mã OTP', 'Đặt lại mật khẩu', 'Cập nhật', 'Quên mật khẩu?', 'Đăng ký ngay') đều có trong inventory.

## Còn 3 điểm, đều ở SV-05 và GA4

| Chỗ | Vấn đề |
|---|---|
| SV-05 `nen_tang` | Ghi "P1, P2 (P3 N/A theo NA1)", nhưng Expected lại nói "Trên màn hình di động P3…". Hai chỗ mâu thuẫn nhau. NA1 cũng chỉ nói về phím Tab, không liên quan kích thước vùng bấm |
| SV-05 `can_cu` / `expected` | WCAG SC 2.5.8 quy định tối thiểu **24×24 px**. Mốc **44×44** là của SC 2.5.5 (mức AAA), không thuộc 2.5.8. Vế "không nằm quá sát nhau" chưa có ngưỡng, nên không chấm Pass/Fail được: cần thêm ngưỡng hoặc bỏ vế này |
| GA4 | SV-05 đã đổi nội dung nên **không còn item nào dùng GA4**. Ghi "(không dùng – SV-05 đổi nội dung ở 1e3b806)" hoặc xoá dòng này |

Sửa xong thì commit `HW03[T1] 2/6b3: SV sửa SV-05, GA4` rồi push. Không cần mình kiểm lại, cứ dán luôn lệnh dưới. Lệnh có bước kiểm cấu trúc, và sẽ dừng nếu còn lỗi.

Câu hỏi ở lượt trước (có dùng công cụ AI khác khi viết không) bạn chưa trả lời. Nếu không dùng thì bỏ qua; nếu có thì nhớ khai trong `prompt_log_extra.toml`.

## Lệnh tiếp theo (sau khi push 2/6b3)

```
HW03[T1] 2/6d – chốt checklist v2 (commit "HW03[T1] 2/6d: gộp item SV, chốt checklist v2"):
1. Kiểm lại sv_items.md (chỉ đọc) như 2/6b; còn lỗi cấu trúc → DỪNG, báo tôi.
2. M1=a: chép NGUYÊN VĂN SV-01…SV-06 vào checklist.json (id SV-xx, nguon="SV", thêm luc_them, ly_do_AI_bo_sot); giả định SV (nếu còn) vào assumptions. Không sửa chữ của tôi; trường trống → "(SV chưa ghi)".
3. check_checklist + render; meta.version = "v2 – chốt sau review SV". In số item theo IA và theo nguồn (AI/Both/SV).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

Sau 2/6d là bước 3/6: Claude Code viết script Playwright cho P1/P2 (E2=b) và `RUN.md` cho phần chạy tay. Tới đó bạn bắt đầu chạy trên trình duyệt thật.
````

**Xử lý:** [...]

---

## #36 | 19:47 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 2/6d – chốt checklist v2 (commit "HW03[T1] 2/6d: gộp item SV, chốt checklist v2"):
1. Kiểm lại sv_items.md (chỉ đọc) như 2/6b; còn lỗi cấu trúc → DỪNG, báo tôi.
2. M1=a: chép NGUYÊN VĂN SV-01…SV-06 vào checklist.json (id SV-xx, nguon="SV", thêm luc_them, ly_do_AI_bo_sot); giả định SV (nếu còn) vào assumptions. Không sửa chữ của tôi; trường trống → "(SV chưa ghi)".
3. check_checklist + render; meta.version = "v2 – chốt sau review SV". In số item theo IA và theo nguồn (AI/Both/SV).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

**Output:**
```
Em đã dừng ở bước 1: `sv_items.md` (bản `d173b63`) còn một lỗi cấu trúc, nên chưa gộp vào `checklist.json` và chưa commit.

- **Lỗi chặn – SV-05:** dòng 84 ghi `nen_tang: P3 (P1, P2 N/A)` nhưng không kèm mã giả định. Quy tắc ở đầu file yêu cầu N/A phải có mã, và `check_checklist.py` cũng đòi item có trường `na`. GA4 giờ đã ghi "không dùng" nên không còn mã nào để trỏ tới. Bạn chọn một trong ba cách:
  - (a) Thêm giả định mới, ví dụ GA5/NA2, vào bảng giả định, rồi ghi `P1, P2 N/A theo <mã>`.
  - (b) Dùng lại GA4 với nội dung mới.
  - (c) Cho SV-05 áp dụng cả P1 và P2.
- **Không chặn, ghi để bạn biết:**
  - SV-02 dòng 44: tiền điều kiện đang nằm trong `expected`, dạng `*Tiền điều kiện:* …<br>`. Nếu chép nguyên văn thì nó vẫn ở trong `expected`, không sang trường `tien_dieu_kien`.
  - Phần còn lại đạt: đủ trường, `ia` hợp lệ, id không trùng, mọi item có câu "Fail nếu", `luc_them` của cả 6 item đều ghi "trước khi chạy".

Sửa xong thì báo em chạy lại 2/6d.
```

**Xử lý:** [...]

---

## #37 | 19:48 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Không dùng AI. 
===
Em đã dừng ở bước 1: sv_items.md (bản d173b63) còn một lỗi cấu trúc, nên chưa gộp vào checklist.json và chưa commit.

- Lỗi chặn – SV-05: dòng 84 ghi nen_tang: P3 (P1, P2 N/A) nhưng không kèm mã giả định. Quy tắc ở đầu file yêu cầu N/A phải có mã, và check_checklist.py cũng đòi item có trường na. GA4 giờ đã ghi "không dùng" nên không còn mã nào để trỏ tới. Bạn chọn một trong ba cách:
  - (a) Thêm giả định mới, ví dụ GA5/NA2, vào bảng giả định, rồi ghi P1, P2 N/A theo <mã>.
  - (b) Dùng lại GA4 với nội dung mới.
  - (c) Cho SV-05 áp dụng cả P1 và P2.
- Không chặn, ghi để bạn biết:
  - SV-02 dòng 44: tiền điều kiện đang nằm trong expected, dạng *Tiền điều kiện:* …<br>. Nếu chép nguyên văn thì nó vẫn ở trong expected, không sang trường tien_dieu_kien.
  - Phần còn lại đạt: đủ trường, ia hợp lệ, id không trùng, mọi item có câu "Fail nếu", luc_them của cả 6 item đều ghi "trước khi chạy".

Sửa xong thì báo em chạy lại 2/6d.
```

**Output:**
````
Ghi nhận, bạn không dùng AI. Phần đó coi như xong.

## SV-05: chọn cách sửa N/A

Một dữ kiện để bạn cân nhắc: WCAG SC 2.5.8 (Target Size Minimum) áp dụng cho **mọi loại con trỏ**, kể cả chuột, không chỉ cho cảm ứng. Hai cách hợp lý:

- **(c) Áp dụng cả P1, P2, P3.** Đúng phạm vi của căn cứ bạn đã trích. Không cần giả định, và vùng bấm đo được bằng DevTools trên cả 3 nền tảng. Nếu chọn cách này, câu "thao tác bằng ngón tay" trong `muc_kiem_tra`/`expected` nên sửa cho chung, ví dụ "con trỏ (chuột hoặc ngón tay)". Không thì nội dung item vẫn lệch với P1/P2.
- **(a) Thêm giả định NA2.** Bạn tự viết nội dung, ví dụ ý "item này chỉ xét thao tác chạm, nên P1/P2 (dùng chuột) N/A". Khi đó trong phần căn cứ phải ghi rõ đây là phạm vi hẹp hơn WCAG.

Không nên chọn **(b)** (dùng lại GA4): mã GA4 đã ghi "không dùng", dùng lại với nghĩa khác sẽ gây nhầm khi đọc truy vết.

## SV-02: tiền điều kiện

Tách ra một dòng riêng trong khối SV-02, rồi xoá phần tương ứng khỏi `expected`:

```
- tien_dieu_kien: <câu của bạn>
```

Claude Code sẽ chép dòng này vào trường `tien_dieu_kien` của JSON.

## Sau khi sửa

Commit `HW03[T1] 2/6b4: SV sửa N/A SV-05, tách tiền điều kiện SV-02` → push, rồi dán lại **lệnh 2/6d** ở lượt trước, không cần đổi gì. Lệnh đó sẽ tự kiểm lại cấu trúc trước khi gộp.
````

**Xử lý:** [...]

---

## #38 | 19:53 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 2/6d – chốt checklist v2 (commit "HW03[T1] 2/6d: gộp item SV, chốt checklist v2"):
1. Kiểm lại sv_items.md (chỉ đọc) như 2/6b; còn lỗi cấu trúc → DỪNG, báo tôi.
2. M1=a: chép NGUYÊN VĂN SV-01…SV-06 vào checklist.json (id SV-xx, nguon="SV", thêm luc_them, ly_do_AI_bo_sot); giả định SV (nếu còn) vào assumptions. Không sửa chữ của tôi; trường trống → "(SV chưa ghi)".
3. check_checklist + render; meta.version = "v2 – chốt sau review SV". In số item theo IA và theo nguồn (AI/Both/SV).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

**Output:**
```
Cấu trúc đã sạch (SV-05 → P1–P3, SV-02 tách tiền điều kiện). Gộp vào JSON.

Chỉnh check (id SV-xx) + render (ly_do dạng dict).

Đã gộp 6 item SV vào checklist và commit, nhưng `check_checklist` còn báo 12 lỗi vì 6 item SV chưa có trường `loai_nguon`.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03[T1] 2/6d – gộp item SV, chốt checklist v2.
- **Kiểm `sv_items.md` @ `0600998`:** hết lỗi cấu trúc (SV-05 áp dụng cả P1–P3, tiền điều kiện của SV-02 đã tách thành trường riêng).
- **File:** `HW03/checklist/checklist.json` và `checklist.md`.
  - SV-01…SV-06 chép nguyên văn, `nguon` = SV, có `luc_them` và `ly_do_ai_bo_sot` (loại + giải thích). SV-01 ghi P3 N/A theo NA1.
  - GA4 bạn ghi "không dùng" nên không đưa vào `assumptions`.
  - Phiên bản: "v2 – chốt sau review SV".
  - Hai script của skill sửa theo: `check_checklist` nhận id dạng SV-xx và báo trường "(SV chưa ghi)"; `render_checklist` hiện lý do và lúc thêm của item SV.
- **Số item: 74.** Theo IA: IA-01 19 · IA-02 26 · IA-03 13 · IA-04 16. Theo nguồn: AI 48 · Both 20 · SV 6.
- **Kết quả kiểm tra:** `check_checklist` **Fail – 12 lỗi**, tất cả là `loai_nguon = (SV chưa ghi)` ở SV-01…SV-06, mỗi item 2 lỗi.
- **Commit:** `3f2328f HW03[T1] 2/6d: gộp item SV, chốt checklist v2`
- **Cần quyết định:** L2 – `loai_nguon` của SV-01…SV-06 phải là SRS, Control hoặc Heuristic; mẫu `sv_items.md` không có trường này nên em để "(SV chưa ghi)". Phương án: (a) bạn ghi vào `sv_items.md`, em gộp lại; (b) bạn đọc giá trị cho từng item, em điền vào JSON.
- **Nhắc:** bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `merge_sv.py`

**Xử lý:** [...]

---

## #39 | 19:55 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03[T1] 2/6d – gộp item SV, chốt checklist v2.
- Kiểm sv_items.md @ 0600998: hết lỗi cấu trúc (SV-05 áp dụng cả P1–P3, tiền điều kiện của SV-02 đã tách thành trường riêng).
- File: HW03/checklist/checklist.json và checklist.md.
  - SV-01…SV-06 chép nguyên văn, nguon = SV, có luc_them và ly_do_ai_bo_sot (loại + giải thích). SV-01 ghi P3 N/A theo NA1.
  - GA4 bạn ghi "không dùng" nên không đưa vào assumptions.
  - Phiên bản: "v2 – chốt sau review SV".
  - Hai script của skill sửa theo: check_checklist nhận id dạng SV-xx và báo trường "(SV chưa ghi)"; render_checklist hiện lý do và lúc thêm của item SV.
- Số item: 74. Theo IA: IA-01 19 · IA-02 26 · IA-03 13 · IA-04 16. Theo nguồn: AI 48 · Both 20 · SV 6.
- Kết quả kiểm tra: check_checklist Fail – 12 lỗi, tất cả là loai_nguon = (SV chưa ghi) ở SV-01…SV-06, mỗi item 2 lỗi.
- Commit: 3f2328f HW03[T1] 2/6d: gộp item SV, chốt checklist v2
- Cần quyết định: L2 – loai_nguon của SV-01…SV-06 phải là SRS, Control hoặc Heuristic; mẫu sv_items.md không có trường này nên em để "(SV chưa ghi)". Phương án: (a) bạn ghi vào sv_items.md, em gộp lại; (b) bạn đọc giá trị cho từng item, em điền vào JSON.
- Nhắc: bạn tự push (git push).
===
đã push rồi nhé
```

**Output:**
````
Lỗi này do **khung của mình**: `sv_items.md` thiếu trường `loai_nguon`, trong khi `checklist.json` bắt buộc có. Sửa đơn giản, chọn **(b)**.

`loai_nguon` không phải phân tích, chỉ là phân loại máy móc theo căn cứ bạn đã ghi. Mình áp đúng quy tắc mà bản AI v1 đã dùng: *xếp theo nguồn đứng đầu trong `can_cu`*.
- WCAG, Nielsen, Norman, Shneiderman → **Heuristic** (ví dụ CL-13, CL-14).
- "Checklist <control>" → **Control** (ví dụ CL-07, CL-38).
- Slide ví dụ chung như "Broken layout on resize" → **Heuristic** (ví dụ CL-15).

| Item | Nguồn đứng đầu trong `can_cu` của bạn | `loai_nguon` |
|---|---|---|
| SV-01 | WCAG 2.2 SC 2.4.7 | Heuristic |
| SV-02 | Shneiderman #8 | Heuristic |
| SV-03 | Slide "Checklist – input-field validation" | Control |
| SV-04 | WCAG 2.2 SC 1.4.3 | Heuristic |
| SV-05 | WCAG 2.2 SC 2.5.8 | Heuristic |
| SV-06 | Slide "Double-submit on double-click" | Heuristic |

Đồng ý thì dán lệnh này. Muốn đổi item nào thì sửa trực tiếp trong dòng lệnh:

```
HW03[T1] 2/6d2 (commit "HW03[T1] 2/6d2: SV chốt loai_nguon item SV"): L2=b — điền loai_nguon vào checklist.json: SV-01 Heuristic, SV-02 Heuristic, SV-03 Control, SV-04 Heuristic, SV-05 Heuristic, SV-06 Heuristic (SV chốt theo quy tắc "nguồn đứng đầu can_cu", giống v1). Thêm trường loai_nguon vào khung mẫu RUN/sv_items của skill để lần sau không thiếu. check_checklist phải 0 lỗi; render. on_stop.py --manual. Báo cáo ≤ 5 dòng.
```

Xong bước này, checklist v2 có **74 item**, đủ 4 IA. Tiếp theo là **bước 3/6**: Claude Code viết script Playwright cho P1/P2 và `RUN.md` cho phần chạy tay. Mình đưa lệnh đó khi báo cáo 2/6d2 về. Bạn cũng có thể dán luôn câu này vào cùng lượt để tiết kiệm một vòng: "xong thì làm tiếp 3/6 theo skill gui-checklist-testing bước 3, dừng trước khi chạy".
````

**Xử lý:** [...]

---

## #40 | 19:55 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 2/6d2 (commit "HW03[T1] 2/6d2: SV chốt loai_nguon item SV"): L2=b — điền loai_nguon vào checklist.json: SV-01 Heuristic, SV-02 Heuristic, SV-03 Control, SV-04 Heuristic, SV-05 Heuristic, SV-06 Heuristic (SV chốt theo quy tắc "nguồn đứng đầu can_cu", giống v1). Thêm trường loai_nguon vào khung mẫu RUN/sv_items của skill để lần sau không thiếu. check_checklist phải 0 lỗi; render. on_stop.py --manual. Báo cáo ≤ 5 dòng.
```

**Output:**
```
- `checklist.json`: đã điền `loai_nguon` cho SV-01…06 đúng như bạn chốt (5 Heuristic, SV-03 Control), ghi thêm mục L2 vào `review_log`. `check_checklist` giờ **0 lỗi, 0 cảnh báo**; tổng 74 item (SRS 43, Control 9, Heuristic 22); đã render lại `checklist.md`.
- Skill: thêm khung `assets/sv_items_template.md`, có trường `loai_nguon` và `tien_dieu_kien`. `SKILL.md` bước 2 ghi rõ AI chỉ dựng khung trống. Mẫu RUN không sửa vì RUN không có trường này.
- Commit: `17f747d HW03[T1] 2/6d2: SV chốt loai_nguon item SV` (gồm prompt log, 12 lượt).
- Bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `sv_items_template.md`

**Xử lý:** [...]

---

## #41 | 19:56 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
- checklist.json: đã điền loai_nguon cho SV-01…06 đúng như bạn chốt (5 Heuristic, SV-03 Control), ghi thêm mục L2 vào review_log. check_checklist giờ 0 lỗi, 0 cảnh báo; tổng 74 item (SRS 43, Control 9, Heuristic 22); đã render lại checklist.md.
- Skill: thêm khung assets/sv_items_template.md, có trường loai_nguon và tien_dieu_kien. SKILL.md bước 2 ghi rõ AI chỉ dựng khung trống. Mẫu RUN không sửa vì RUN không có trường này.
- Commit: 17f747d HW03[T1] 2/6d2: SV chốt loai_nguon item SV (gồm prompt log, 12 lượt).
- Bạn tự push (git push).
```

**Output:**
````
Checklist v2 đã chốt: **74 item**, 0 lỗi. Push xong thì sang bước 3.

Trước khi chạy, kiểm tra **Firefox đã cài trên máy chưa**. P2 cần Firefox thật để chạy tay và chụp ảnh có overlay. Playwright chỉ dùng bản Firefox riêng của nó để ra `auto_status`.

## Lệnh 3/6

```
HW03[T1] 3/6 – theo skill gui-checklist-testing bước 3 (commit "HW03[T1] 3/6: Playwright P1/P2 + RUN.md"). Không sửa expected trong checklist.json.
1. Phân loại 74 item vào trường che_do: auto (đo được bằng DOM/bàn phím/Network trên Playwright) / manual (cần mắt, thiết bị thật, đợi thời gian, tắt backend…) / mixed. In bảng đếm.
2. Playwright (HW03/tests/): chỉ item auto + phần auto của mixed. P1 = channel "chrome" (Chrome đã cài), P2 = firefox của Playwright (ghi rõ đây là bản build Playwright, không phải Firefox đã cài). expect.soft; oracle lấy từ expected của checklist.json (khoá sha1 như HW02). Dựng dữ liệu bằng API trước khi chạy (đơn 5 trạng thái qua admin, tài khoản seed). Ghi kết quả theo lượt có timestamp vào HW03/checklist/runs/<P>_auto_<ts>.json (auto_status) + ảnh phần tử vào evidence/auto/. Item nào Firefox Playwright không làm được (vd throttling) → để manual cho P2.
3. HW03/checklist/RUN.md cho phần chạy tay, theo thứ tự màn hình (không theo số item): mỗi nền tảng 1 lượt, đầu lượt restart backend + dựng dữ liệu; P3 nhắc adb reverse 2 cổng + chrome://inspect để dán dom_probe.js; mỗi item ghi cần nhìn gì, ảnh nào bắt buộc (item Failed + 1 ảnh/màn/nền tảng cho Task 3, có overlay Sticky Notes "23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn", thấy tên trình duyệt + URL), tên ảnh P<n>_<id>_<k>.png. Kèm file trống HW03/checklist/runs/<P>_manual_TEMPLATE.md để tôi ghi kết quả.
4. Chỉ chạy `npx playwright test --list`; KHÔNG chạy lượt thật (tôi chạy). In lệnh tôi cần chạy cho P1, P2.
on_stop.py --manual. Báo cáo ≤ 12 dòng. Nhắc tôi push.
```

## Sau khi báo cáo về

1. Chạy lệnh Playwright mà Claude Code in ra, lần lượt cho P1 và P2. **Nhớ restart backend trước mỗi lượt.**
2. Chạy tay theo `RUN.md`: P1 Chrome → P2 Firefox → P3 Android. Ghi kết quả vào file template, chụp ảnh đúng quy tắc trong RUN.
3. Claude Code gộp kết quả `auto` với kết quả chạy tay. Chỗ hai kết quả lệch nhau thì **bạn quyết verdict**.

Ảnh bạn đặt tên tuỳ ý cũng được. Sau đó Claude Code đổi tên và nén ảnh như HW02D (`compress_manual.py`).
````

**Xử lý:** [...]

---

## #42 | 19:57 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 3/6 – theo skill gui-checklist-testing bước 3 (commit "HW03[T1] 3/6: Playwright P1/P2 + RUN.md"). Không sửa expected trong checklist.json.
1. Phân loại 74 item vào trường che_do: auto (đo được bằng DOM/bàn phím/Network trên Playwright) / manual (cần mắt, thiết bị thật, đợi thời gian, tắt backend…) / mixed. In bảng đếm.
2. Playwright (HW03/tests/): chỉ item auto + phần auto của mixed. P1 = channel "chrome" (Chrome đã cài), P2 = firefox của Playwright (ghi rõ đây là bản build Playwright, không phải Firefox đã cài). expect.soft; oracle lấy từ expected của checklist.json (khoá sha1 như HW02). Dựng dữ liệu bằng API trước khi chạy (đơn 5 trạng thái qua admin, tài khoản seed). Ghi kết quả theo lượt có timestamp vào HW03/checklist/runs/<P>_auto_<ts>.json (auto_status) + ảnh phần tử vào evidence/auto/. Item nào Firefox Playwright không làm được (vd throttling) → để manual cho P2.
3. HW03/checklist/RUN.md cho phần chạy tay, theo thứ tự màn hình (không theo số item): mỗi nền tảng 1 lượt, đầu lượt restart backend + dựng dữ liệu; P3 nhắc adb reverse 2 cổng + chrome://inspect để dán dom_probe.js; mỗi item ghi cần nhìn gì, ảnh nào bắt buộc (item Failed + 1 ảnh/màn/nền tảng cho Task 3, có overlay Sticky Notes "23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn", thấy tên trình duyệt + URL), tên ảnh P<n>_<id>_<k>.png. Kèm file trống HW03/checklist/runs/<P>_manual_TEMPLATE.md để tôi ghi kết quả.
4. Chỉ chạy `npx playwright test --list`; KHÔNG chạy lượt thật (tôi chạy). In lệnh tôi cần chạy cho P1, P2.
on_stop.py --manual. Báo cáo ≤ 12 dòng. Nhắc tôi push.
```

**Output:**
````
Đang dựng harness Playwright; đọc API đổi trạng thái đơn để dựng dữ liệu.

Còn chặn: máy không có Chrome/Firefox cài sẵn (chỉ Cốc Cốc) — ghi vào báo cáo, vẫn dựng harness. Viết cấu hình Playwright.

Giờ `lib.ts` (helper đo DOM, API dựng dữ liệu, oracle khoá sha1).

Viết `oracle.ts` (tham số đo theo từng item) — hash điền bằng script.

Viết spec (một test cho mỗi item auto/mixed).

PowerShell nuốt `${}` — sửa bằng Edit.

Gán `che_do` vào checklist.json + vá merge_platform cho file lượt `kind: auto`.

Generate oracle, npm install, `--list`.

Harness Playwright list OK (142 = 71×2). Giờ RUN.md + mẫu ghi kết quả + script dựng đơn cho lượt tay.

Đã dựng xong phần chạy tự động (Playwright cho P1/P2) và RUN.md cho phần chạy tay. Mới chạy `--list`, chưa chạy lượt thật. Có một chỗ chặn: máy chưa cài Google Chrome và Firefox, chỉ thấy Cốc Cốc.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03[T1] 3/6 – Playwright P1/P2 + RUN.md. Không sửa `expected`; `check_checklist` 0 lỗi, 0 cảnh báo.
- **Phân loại `che_do` (74 item):**

  | Chế độ | Số item |
  |---|---|
  | auto | 59 |
  | mixed | 12 |
  | manual | 3 (CL-01, CL-52, CL-64) |

  - Firefox của Playwright không giả lập được mạng chậm và không cấp quyền clipboard, nên CL-53, CL-63, SV-02 chỉ chạy tự động trên P1; trên P2 chạy tay.
- **Playwright – `HW03/tests/`:**
  - Một test cho mỗi item auto/mixed: 71 test × 2 nền tảng = 142.
  - Ngưỡng đo nằm ở `oracle.src.json`; `oracle.ts` sinh từ đó, khoá bằng sha1 của `expected` như HW02. Hai ngưỡng màu không có số trong Expected (CL-04 xanh dương, CL-05 đỏ) em tự đặt theo dải hue và ghi lý do — bạn duyệt.
  - Dữ liệu: CL-62 chạy đầu khi tài khoản chưa có đơn; ngay sau đó dựng 7 đơn qua API (đủ 5 trạng thái + 2 đơn chờ để thử huỷ).
  - Kết quả mỗi lượt ghi vào `checklist/runs/<P>_auto_<ts>.json` (`auto_status`), ảnh vào `evidence/auto/`. `merge_platform.py` đã sửa để file lượt tự động chỉ ghi `auto_status`, không đụng `ket_qua`.
- **RUN.md** (sinh bằng `gen_run.py`): xếp theo màn hình — Bước A (CL-62) → dựng đơn → M1…M6 → cuối lượt (CL-52, CL-64).
  - Số item chạy tay: P1 15, P2 15, P3 70.
  - Có lệnh adb + `chrome://inspect` cho P3, quy tắc ảnh/overlay, cảnh báo khoá tài khoản.
  - Kèm `dom_probe.js`, `seed_orders.py` (dựng đơn, đặt lại mật khẩu) và 3 mẫu `runs/P{1,2,3}_manual_TEMPLATE.md`.
- **Bất thường:**
  - Backend: mỗi lần sai mật khẩu bộ đếm tăng 2 (`server.js:54`) và khoá 180 giây (`server.js:57`), trong khi SRS ghi tăng 1 và khoá 30 giây. Hệ quả: sai 2 lần là bị khoá; script tự đăng nhập đúng ngay sau mỗi lần sai để tránh.
  - Môi trường: không thấy Google Chrome và Firefox (đã tìm đường dẫn cài đặt, registry, Start Menu). Playwright mới có sẵn chromium-1140, chưa có bản Firefox.
- **Kết quả kiểm tra:** `npx playwright test --list` → 142 test, chưa chạy lượt thật.
- **Commit:** `07982fc HW03[T1] 3/6: Playwright P1/P2 + RUN.md` (gồm prompt log 13 lượt).
- **Cần quyết định:** C1 – P1 cần Google Chrome thật. (a) Bạn tự cài Chrome; (b) dùng `npx playwright install chrome` (cài Chrome chính thức, cần quyền admin). Firefox: cài bản thật cho lượt chạy tay P2, còn lượt tự động dùng `npx playwright install firefox`.

Lệnh chạy, mỗi nền tảng một lượt, restart backend trước mỗi lượt:

```powershell
cd HW03\tests
npx playwright install firefox          # một lần, bản build Firefox của Playwright
# P1: restart backend (CSDL seed) rồi:
npx playwright test --project=P1
python ..\..\.claude\skills\gui-checklist-testing\scripts\merge_platform.py ..\checklist\checklist.json (Get-ChildItem ..\checklist\runs\P1_auto_*.json | Sort LastWriteTime | Select -Last 1).FullName --platform P1 --dry-run
# P2: restart backend lần nữa rồi:
npx playwright test --project=P2
```

Bạn tự push (`git push`).
````
*File AI ghi/gửi trong lượt này:* `package.json`, `playwright.config.ts`, `global-setup.ts`, `lib.ts`, `oracle.src.json`, `gen_oracle.py`, `C2.spec.ts`, `reporter.ts`, `seed_orders.py`, `gen_run.py`

**Xử lý:** [...]

---

## #43 | 20:27 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Ghi nhớ những cái đang chạy. Tắt giúp mình để mình chạy về phòng. Rồi mình sẽ bảo bạn bật lại nhé
```

**Output:**
```
Em đã tắt hết, không còn tiến trình `node` hay `adb` nào chạy; bạn mang máy đi được.

Lúc tắt có:
- backend `:3000`;
- web vite `:5173`;
- adb server, với 2 cổng 5173 và 3000 đang nối sang POCO F5 (`da87b223`).

Em đã gỡ 2 cổng đó trước khi tắt adb.

Em đã ghi vào bộ nhớ danh sách này, cách bật lại, và việc HW03 đang chờ: bạn cài Chrome/Firefox (C1) rồi chạy Playwright cho P1/P2. Khi bạn nói "bật lại", em chạy lại backend và vite, rồi `adb devices` và 2 lệnh `adb reverse`. Lúc đó cắm cáp điện thoại và để USB debugging bật.

Backend khởi động lại sẽ seed lại CSDL, nên dữ liệu thử cũ sẽ mất (vốn không cần giữ). Mọi thay đổi đã commit (`07982fc`); nhớ `git push`.
```
*File AI ghi/gửi trong lượt này:* `hw03-runtime-state.md`

**Xử lý:** [...]

---

## #44 | 02:03 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
bật lại nhé
```

**Output:**
```
Bật lại xong, đủ như lúc tắt:
- **Backend** đang chạy ở `:3000`. CSDL vừa seed lại, nên đúng là trạng thái cần có trước lượt Playwright.
- **Web** đang chạy ở `127.0.0.1:5173`.
- **Điện thoại**: adb thấy `da87b223 device`, hai cổng `5173` và `3000` đã nối sang máy.

Việc tiếp theo bên bạn vẫn là C1: cài Chrome và Firefox, rồi chạy `npx playwright test --project=P1` trong `HW03\tests`. Restart backend trước mỗi lượt.
```

**Xử lý:** [...]

---

## #45 | 02:03 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03[T1] 3/6 – Playwright P1/P2 + RUN.md. Không sửa expected; check_checklist 0 lỗi, 0 cảnh báo.
- Phân loại che_do (74 item):

| Chế độ | Số item                 |
|--------|-------------------------|
| auto   | 59                      |
| mixed  | 12                      |
| manual | 3 (CL-01, CL-52, CL-64) |
  - Firefox của Playwright không giả lập được mạng chậm và không cấp quyền clipboard, nên CL-53, CL-63, SV-02 chỉ chạy tự động trên P1; trên P2 chạy tay.
- Playwright – HW03/tests/:
  - Một test cho mỗi item auto/mixed: 71 test × 2 nền tảng = 142.
  - Ngưỡng đo nằm ở oracle.src.json; oracle.ts sinh từ đó, khoá bằng sha1 của expected như HW02. Hai ngưỡng màu không có số trong Expected (CL-04 xanh dương, CL-05 đỏ) em tự đặt theo dải hue và ghi lý do — bạn duyệt.
  - Dữ liệu: CL-62 chạy đầu khi tài khoản chưa có đơn; ngay sau đó dựng 7 đơn qua API (đủ 5 trạng thái + 2 đơn chờ để thử huỷ).
  - Kết quả mỗi lượt ghi vào checklist/runs/<P>_auto_<ts>.json (auto_status), ảnh vào evidence/auto/. merge_platform.py đã sửa để file lượt tự động chỉ ghi auto_status, không đụng ket_qua.
- RUN.md (sinh bằng gen_run.py): xếp theo màn hình — Bước A (CL-62) → dựng đơn → M1…M6 → cuối lượt (CL-52, CL-64).
  - Số item chạy tay: P1 15, P2 15, P3 70.
  - Có lệnh adb + chrome://inspect cho P3, quy tắc ảnh/overlay, cảnh báo khoá tài khoản.
  - Kèm dom_probe.js, seed_orders.py (dựng đơn, đặt lại mật khẩu) và 3 mẫu runs/P{1,2,3}_manual_TEMPLATE.md.
- Bất thường:
  - Backend: mỗi lần sai mật khẩu bộ đếm tăng 2 (server.js:54) và khoá 180 giây (server.js:57), trong khi SRS ghi tăng 1 và khoá 30 giây. Hệ quả: sai 2 lần là bị khoá; script tự đăng nhập đúng ngay sau mỗi lần sai để tránh.
  - Môi trường: không thấy Google Chrome và Firefox (đã tìm đường dẫn cài đặt, registry, Start Menu). Playwright mới có sẵn chromium-1140, chưa có bản Firefox.
- Kết quả kiểm tra: npx playwright test --list → 142 test, chưa chạy lượt thật.
- Commit: 07982fc HW03[T1] 3/6: Playwright P1/P2 + RUN.md (gồm prompt log 13 lượt).
- Cần quyết định: C1 – P1 cần Google Chrome thật. (a) Bạn tự cài Chrome; (b) dùng npx playwright install chrome (cài Chrome chính thức, cần quyền admin). Firefox: cài bản thật cho lượt chạy tay P2, còn lượt tự động dùng npx playwright install firefox.

Lệnh chạy, mỗi nền tảng một lượt, restart backend trước mỗi lượt:

cd HW03\tests
npx playwright in

Lúc tắt có:
- backend :3000;
- web vite :5173;
- adb server, với 2 cổng 5173 và 3000 đang nối sang POCO F5 (da87b223).

Em đã gỡ 2 cổng đó trước khi tắt adb.

Em đã ghi vào bộ nhớ danh sách này, cách bật lại, và việc HW03 đang chờ: bạn cài Chrome/Firefox (C1) rồi chạy Playwright cho P1/P2. Khi bạn nói "bật lại", em chạy lại backend và vite, rồi adb devices và 2 lệnh adb reverse. Lúc đó cắm cáp điện thoại và để USB debugging bật.

Backend khởi động lại sẽ seed lại CSDL, nên dữ liệu thử cũ sẽ mất (vốn không cần giữ). Mọi thay đổi đã commit (07982fc); nhớ git push.
```

**Output:**
````
## 1. C1: Chrome và Firefox

Bạn nói máy có Chrome, nhưng Claude Code không tìm thấy. Mở Chrome, vào `chrome://version` và xem dòng **"Đường dẫn thực thi" / "Executable Path"**:
- **Có đường dẫn:** chép đường dẫn đó vào lệnh dưới. Claude Code sẽ dùng `executablePath` thay cho `channel`.
- **Không phải Chrome** (ví dụ Cốc Cốc), hoặc không có: cài Chrome từ google.com/chrome. Không cần quyền admin.

**Firefox:** cài bản thật từ mozilla.org để chạy tay P2. Lượt tự động thì dùng `npx playwright install firefox`.

## 2. H1: ngưỡng màu do AI tự đặt, cần bạn duyệt

Expected chỉ ghi "xanh dương" và "đỏ", không có số. Để máy chấm được, AI đã tự đặt ngưỡng đo theo màu nền nút:

| Item | Ngưỡng AI đặt |
|---|---|
| CL-04 xanh dương | hue 190–250°, độ bão hoà ≥ 0,3 |
| CL-05 đỏ | hue 340–20°, độ bão hoà ≥ 0,3 |

Dải này hợp lý, phủ đúng họ màu blue/red của Tailwind. Bạn **chấp nhận** hoặc sửa số, rồi ghi là "SV chốt". Ngưỡng này là quyết định oracle, nên phải có trong report.

## 3. Bất thường khoá tài khoản

Mình đã đọc lại code và xác nhận:
- `server.js:54`: mỗi lần nhập sai, bộ đếm **+2**.
- `server.js:57`: khoá **180 000 ms = 180 giây**.

SRS FR-02 ghi +1 và khoá 30 giây. Khi bạn chạy tay CL-52, kết quả sẽ lộ ra. Điểm này do **AI phát hiện khi đọc code**, nên ghi vào mục "Khai cho Audit". Bug chỉ được lập **sau khi bạn quan sát thấy khi chạy**, phải kiểm trùng issue FR-02 trước, và bạn tự viết.

## 4. P3A: thử tự động P3 bằng Playwright Android?

Hiện P3 phải chạy tay **70 item**. Playwright có hỗ trợ điều khiển Chrome trên Android qua adb, nhưng đây là tính năng **thử nghiệm** (experimental). Điều kiện:
- Chrome trên máy từ bản 105 trở lên.
- Bật cờ **"Enable command line on non-rooted devices"** trong `chrome://flags` trên điện thoại.

Tài liệu không nói rõ có chạy được trên Windows không. Nếu chạy được, số item chạy tay trên P3 giảm xuống khoảng 15. Ảnh Task 3 (có thanh địa chỉ và overlay) thì vẫn phải chụp tay.

Đề xuất **thử, giới hạn 15 phút**. Không chạy được thì quay lại chạy tay.

## 5. Lịch: nói thẳng

Bây giờ là 2 giờ sáng thứ Năm, deadline thứ Bảy. **Task 2 (40 điểm) chưa bắt đầu**, và đó là phần phụ thuộc người khác. Đề xuất:

| Khi | Việc |
|---|---|
| **Thứ Năm, sáng** | Chạy P1, P2 (tự động + tay), P3 → bug |
| **Thứ Năm, chiều tối** | Pilot + 3–4 phiên usability |
| **Thứ Sáu** | 3–4 phiên còn lại, phân tích, skill usability |
| **Thứ Bảy** | Report, Critique, form, video, zip |

**Hôm nay hẹn giờ cụ thể với 8 người.** Đây là rủi ro lớn nhất còn lại của bài.

## Lệnh khi bạn dậy (sau khi đã kiểm Chrome và cài Firefox)

```
HW03 – bật lại + chuẩn bị chạy (commit "HW03[T1] 3/6b: C1, H1, P3A"):
1. Bật lại backend + vite (--host 127.0.0.1) + adb devices + adb reverse 2 cổng.
2. C1: Chrome = <đường dẫn từ chrome://version | "đã cài mới">; npx playwright install firefox. Chạy --list lại.
3. H1: CL-04 hue 190–250, CL-05 hue 340–20, sat ≥ 0,3 — SV chốt; ghi review_log + report_plan mục e.
4. report_plan mục f: "AI phát hiện khi đọc code: login_attempts +2 (server.js:54), khoá 180 s (server.js:57) ≠ FR-02 – chờ CL-52 chạy tay; kiểm trùng issue FR-02 trong issues.json → in kết quả".
5. P3A (giới hạn 15 phút): thử Playwright _android với POCO (tôi đã bật flag "Enable command line on non-rooted devices"); được → thêm project P3 chạy item auto, cập nhật RUN.md (P3 chỉ còn manual/mixed); không được → báo lỗi nguyên văn, giữ P3 chạy tay.
on_stop.py --manual. Báo cáo ≤ 10 dòng.
```

Trước khi dán, điền `<…>` ở bước 2. Nếu bỏ qua P3A thì xoá bước 5.
````

**Xử lý:** [...]

---

## #46 | 02:09 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. Ủa hình như mình xoá Chrome rồi. Giờ chỉ còn Cốc Cốc với Edge thôi.
2. Chấp nhận, dù gì thì tôi cũng không nhạy cảm về màu cho lắm, nhìn thấy đúng màu xanh dương và đỏ là được rồi.
3. Oke
4. Bật rồi nhé.
5. Tối mình sẽ làm task 2, chứ giờ 2h sáng bạn mình ngủ rồi, còn ngày thì lại đi học.

===
Mình chưa sử dụng prompt của bạn đâu nhé. Do mình không biết có được dùng Cốc Cốc thay cho Chrome hay không?
```

**Output:**
````
**Không nên dùng Cốc Cốc hay Edge thay cho Chrome.** Đề ghi rõ nền tảng là *"Chrome, Firefox, Safari (or Android Chrome)"*. Cốc Cốc và Edge cùng engine với Chrome (Chromium), nhưng không phải Chrome. Ảnh chụp sẽ hiện logo và tên Cốc Cốc, TA dễ trừ điểm hoặc hỏi lại khi vấn đáp. Cài lại Chrome chỉ mất khoảng 3 phút, nên không đáng nhận rủi ro này.

**Cách cài:** vào google.com/chrome → tải về → chạy file cài. Máy không có quyền admin thì Chrome tự cài vào thư mục người dùng, Playwright vẫn tìm được. Cài xong vào `chrome://version` xem đường dẫn thực thi, để chắc chắn.

Cốc Cốc thì vẫn hữu ích theo cách khác: ở Task 2, nếu người tham gia quen dùng Cốc Cốc thì cho họ dùng.

## Lệnh (dán sau khi đã cài Chrome và Firefox)

```
HW03 – bật lại + chuẩn bị chạy (commit "HW03[T1] 3/6b: C1, H1, P3A"):
1. Bật lại backend + vite (--host 127.0.0.1) + adb devices + adb reverse 2 cổng.
2. C1: Chrome vừa cài lại (kiểm channel "chrome" tìm được; không thì dùng executablePath từ chrome://version); Firefox thật đã cài cho chạy tay P2; npx playwright install firefox cho lượt auto. Chạy --list lại.
3. H1: CL-04 hue 190–250, CL-05 hue 340–20, sat ≥ 0,3 — SV chốt (SV: "nhìn thấy đúng xanh dương/đỏ là được"); ghi review_log + report_plan mục e.
4. report_plan mục f: "AI phát hiện khi đọc code: login_attempts +2 (server.js:54), khoá 180 s (server.js:57) ≠ FR-02 – chờ CL-52 chạy tay"; kiểm trùng issue FR-02 trong issues.json → in kết quả.
5. P3A (giới hạn 15 phút): thử Playwright _android với POCO (flag "Enable command line on non-rooted devices" đã bật); được → thêm project P3 chạy item auto, cập nhật RUN.md (P3 chỉ còn manual/mixed); không được → báo lỗi nguyên văn, giữ P3 chạy tay.
on_stop.py --manual. Báo cáo ≤ 10 dòng.
```

## Task 2 tối nay

Hợp lý. Bạn bè ngủ rồi thì sáng nay tập trung chạy checklist. Có điều **nhắn hẹn giờ cụ thể ngay khi họ dậy**. Nhắn chung chung "tối rảnh không" thì dễ bị lùi sang thứ Sáu, mà thứ Sáu còn phải làm phần phân tích.
````

**Xử lý:** [...]

---

## #47 | 02:15 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Google Chrome	157.0.8103.39 (Official Build) (64-bit) (cohort: Stable Installs & Version Pins) 
Revision	9a31f0acec1854d44e49a73fbf8017598151a583-refs/branch-heads/8103@{#1035}
OS	Windows 11 Version 25H2 (Build 26200.9711)
JavaScript	V8 15.7.112.23
User Agent	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36
Command Line	"C:\Program Files\Google\Chrome\Application\chrome.exe" --from-installer --flag-switches-begin --flag-switches-end
Executable Path	C:\Program Files\Google\Chrome\Application\chrome.exe
Profile Path	C:\Users\tanhi\AppData\Local\Google\Chrome\User Data\Default
Variations Source	variations server
Command-line Variations
===
cài Firefox xong luôn rồi nhé
```

**Output:**
````
Chrome đã cài đúng đường dẫn chuẩn (`C:\Program Files\Google\Chrome\Application\chrome.exe`), nên Playwright tự tìm được qua `channel: "chrome"`. Firefox cũng đã cài. Dán lệnh này:

```
HW03 – bật lại + chuẩn bị chạy (commit "HW03[T1] 3/6b: C1, H1, P3A"):
1. Bật lại backend + vite (--host 127.0.0.1) + adb devices + adb reverse 2 cổng.
2. C1: Chrome 157 đã cài lại ở C:\Program Files\Google\Chrome\Application\chrome.exe (dùng channel "chrome"); Firefox thật đã cài cho chạy tay P2; npx playwright install firefox cho lượt auto. Chạy --list lại. Ghi phiên bản Chrome/Firefox/Firefox-Playwright vào HW03/env/environment.md (không ghi đường dẫn có tên người dùng Windows).
3. H1: CL-04 hue 190–250, CL-05 hue 340–20, sat ≥ 0,3 — SV chốt ("nhìn thấy đúng xanh dương/đỏ là được"); ghi review_log + report_plan mục e.
4. report_plan mục f: "AI phát hiện khi đọc code: login_attempts +2 (server.js:54), khoá 180 s (server.js:57) ≠ FR-02 – chờ CL-52 chạy tay"; kiểm trùng issue FR-02 trong issues.json → in kết quả.
5. P3A (giới hạn 15 phút): thử Playwright _android với POCO (flag "Enable command line on non-rooted devices" đã bật); được → thêm project P3 chạy item auto, cập nhật RUN.md (P3 chỉ còn manual/mixed); không được → báo lỗi nguyên văn, giữ P3 chạy tay.
on_stop.py --manual. Báo cáo ≤ 10 dòng.
```

`chrome://version` hiện cả đường dẫn hồ sơ có tên người dùng Windows của bạn (`C:\Users\…`). Khi chụp ảnh cho bài nộp, đừng để lộ trang `chrome://version` hay đường dẫn này. Bước 2 của lệnh cũng đã dặn Claude Code không ghi đường dẫn đó vào repo.

Báo cáo về rồi thì bắt đầu chạy: lượt tự động P1, P2 trước, sau đó chạy tay theo `RUN.md`.
````

**Xử lý:** [...]

---

## #48 | 02:17 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – bật lại + chuẩn bị chạy (commit "HW03[T1] 3/6b: C1, H1, P3A"):
1. Bật lại backend + vite (--host 127.0.0.1) + adb devices + adb reverse 2 cổng.
2. C1: Chrome 157 đã cài lại ở C:\Program Files\Google\Chrome\Application\chrome.exe (dùng channel "chrome"); Firefox thật đã cài cho chạy tay P2; npx playwright install firefox cho lượt auto. Chạy --list lại. Ghi phiên bản Chrome/Firefox/Firefox-Playwright vào HW03/env/environment.md (không ghi đường dẫn có tên người dùng Windows).
3. H1: CL-04 hue 190–250, CL-05 hue 340–20, sat ≥ 0,3 — SV chốt ("nhìn thấy đúng xanh dương/đỏ là được"); ghi review_log + report_plan mục e.
4. report_plan mục f: "AI phát hiện khi đọc code: login_attempts +2 (server.js:54), khoá 180 s (server.js:57) ≠ FR-02 – chờ CL-52 chạy tay"; kiểm trùng issue FR-02 trong issues.json → in kết quả.
5. P3A (giới hạn 15 phút): thử Playwright _android với POCO (flag "Enable command line on non-rooted devices" đã bật); được → thêm project P3 chạy item auto, cập nhật RUN.md (P3 chỉ còn manual/mixed); không được → báo lỗi nguyên văn, giữ P3 chạy tay.
on_stop.py --manual. Báo cáo ≤ 10 dòng.
```

**Output:**
```
Đã có version. Giờ ghi environment.md, rồi H1, mục f, kiểm issue, thử P3A.

Ngưỡng H1 đã khớp oracle.src.json. Chỉ ghi review_log + report_plan.

Kiểm trùng FR-02: tải lại issue kèm body để quét đủ.

Trùng nhiều: #1, #2, #3 khớp đúng finding. Ghi vào file, rồi thử P3A.

Giờ thử P3A (Playwright `_android`, giới hạn 15 phút).

P3A chạy được. Xem config/fixture để thêm project P3.

P3A chạy được (kết nối 5,7 s). Thêm project P3 vào harness.

Giờ sửa lib.ts (fixture P3), global-setup, reporter, config.

Giờ gen_run.py: P3 chỉ còn manual/mixed.

213 test (71 × 3). Smoke 1 test đọc-only (CL-03) trên P3 để kiểm fixture, xong xoá file kết quả.

Fixture chạy được trên máy thật. Nhưng reporter ghi 0 item và lượt chạy mất 1,1 phút. Đang xem log đầy đủ.

P1 cũng ghi 0 item. Đây là lỗi có sẵn của reporter, không riêng P3. Đang debug.

Reporter đã sửa xong: nguyên nhân là `r.annotations` chưa có ở Playwright 1.48. Còn lỗi ảnh phần tử trên P3: chụp không ra file và không báo lỗi. Đang kiểm.

Script lẻ chạy nhanh, ảnh phần tử chụp được. Nghi do fixture `page` mặc định mở tab mới trên Android. Sửa để P3 dùng tab sẵn có.

Đã sửa: smoke P3 chạy 4 s, ảnh và reporter đều đúng. Kiểm thêm cổng N/A (CL-10 trên P3) rồi dọn file smoke.

Thêm 1 dòng log P3A rồi commit.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** 3/6b xong, commit `1172c20 HW03[T1] 3/6b: C1, H1, P3A`. Backend :3000 và vite :5173 đang chạy, CSDL sạch (test@eshop.com chưa có đơn). adb thấy `da87b223 device`, đã reverse 2 cổng.
- **C1:** `HW03/env/environment.md` có Chrome 157.0.8103.39, Firefox thật 159.0.1, Firefox của Playwright 131.0, Chrome Android 156.0.8078.79. `--list` ra 213 test (71 × P1/P2/P3).
- **H1:** ngưỡng trong `oracle.src.json` vốn đã đúng H1, không phải đổi. Đã ghi review_log và thêm dòng H1 vào report_plan mục e.
- **Mục f:** đã ghi. Kiểm 158 issue: lỗi đếm +2 và khoá 180 s **đã có #1, #2, #3**. Các issue FR-02 khác (#4–#9, #62–#64) liệt kê ở `HW03/checklist/issue_dup_FR02.md`.
- **P3A:** chạy được. Đã thêm project P3; P3 chạy tay giờ còn 13 item (RUN.md và template đã sinh lại). Item N/A theo NA1 tự bỏ qua, không ghi vào kết quả. Chrome trên máy bị đóng/mở lại và xoá storage của localhost:5173/3000 trước mỗi test.
- **Bất thường harness (đã sửa):**
  - `tests/reporter.ts:24` ghi 0 item trên cả P1 lẫn P2 vì Playwright 1.48 chưa có `TestResult.annotations`. Không sửa thì lượt auto chạy thật sẽ ra JSON rỗng.
  - P3: fixture page mặc định mở tab mới trên điện thoại, làm ảnh phần tử chụp hỏng mà không báo lỗi. Đã đổi sang dùng tab sẵn có.
- **Kiểm tra:** check_checklist 0 lỗi. Chạy thử CL-03 (chỉ đọc) trên P3 và P1 để kiểm fixture/reporter, đã xoá file kết quả và ảnh của lượt thử. Lượt thật: Not run (SV chạy).
- **Cần quyết định:** không. Bước kế tiếp của SV: restart backend rồi chạy `npx playwright test --project=P1`, lặp lại cho P2 và P3, sau đó push.
```

**Xử lý:** [...]

---

## #49 | 02:27 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: 3/6b xong, commit 1172c20 HW03[T1] 3/6b: C1, H1, P3A. Backend :3000 và vite :5173 đang chạy, CSDL sạch (test@eshop.com chưa có đơn). adb thấy da87b223 device, đã reverse 2 cổng.
- C1: HW03/env/environment.md có Chrome 157.0.8103.39, Firefox thật 159.0.1, Firefox của Playwright 131.0, Chrome Android 156.0.8078.79. --list ra 213 test (71 × P1/P2/P3).
- H1: ngưỡng trong oracle.src.json vốn đã đúng H1, không phải đổi. Đã ghi review_log và thêm dòng H1 vào report_plan mục e.
- Mục f: đã ghi. Kiểm 158 issue: lỗi đếm +2 và khoá 180 s đã có #1, #2, #3. Các issue FR-02 khác (#4–#9, #62–#64) liệt kê ở HW03/checklist/issue_dup_FR02.md.
- P3A: chạy được. Đã thêm project P3; P3 chạy tay giờ còn 13 item (RUN.md và template đã sinh lại). Item N/A theo NA1 tự bỏ qua, không ghi vào kết quả. Chrome trên máy bị đóng/mở lại và xoá storage của localhost:5173/3000 trước mỗi test.
- Bất thường harness (đã sửa):
  - tests/reporter.ts:24 ghi 0 item trên cả P1 lẫn P2 vì Playwright 1.48 chưa có TestResult.annotations. Không sửa thì lượt auto chạy thật sẽ ra JSON rỗng.
  - P3: fixture page mặc định mở tab mới trên điện thoại, làm ảnh phần tử chụp hỏng mà không báo lỗi. Đã đổi sang dùng tab sẵn có.
- Kiểm tra: check_checklist 0 lỗi. Chạy thử CL-03 (chỉ đọc) trên P3 và P1 để kiểm fixture/reporter, đã xoá file kết quả và ảnh của lượt thử. Lượt thật: Not run (SV chạy).
- Cần quyết định: không. Bước kế tiếp của SV: restart backend rồi chạy npx playwright test --project=P1, lặp lại cho P2 và P3, sau đó push.
```

**Output:**
````
Mọi thứ sẵn sàng. P3 tự động chạy được nên P3 chỉ còn **13 item chạy tay**, đỡ nhiều thời gian. Lỗi khoá tài khoản đã có issue #1–#3: khi CL-52 Failed, ghi "trùng #1–#3" và không lập bug mới.

## Chạy lượt tự động (bạn tự chạy)

Backend đang chạy nền trong Claude Code. Để tự restart được trước mỗi lượt, bảo Claude Code **"tắt backend nền"**, rồi mở 2 cửa sổ PowerShell:

**Cửa sổ A – backend.** Trước mỗi lượt: Ctrl+C rồi chạy lại.
```powershell
cd D:\HK7\Testing\Exercise\HW\eshop-sut\backend
node server.js
```

**Cửa sổ B – test**
```powershell
cd D:\HK7\Testing\Exercise\HW\software-testing-2627\HW03\tests
npx playwright test --project=P1
# restart backend ở cửa sổ A
npx playwright test --project=P2
# restart backend; điện thoại: mở khoá, để màn hình sáng, không chạm vào máy
npx playwright test --project=P3
```

Sửa đường dẫn nếu thư mục của bạn khác. Trước khi chạy P3, chỉnh **thời gian tắt màn hình** của điện thoại lên 10 phút, vì màn hình tắt giữa chừng sẽ làm test lỗi.

## Sau đó: chạy tay theo `RUN.md`

| Nền tảng | Số item chạy tay | Ghi kết quả vào |
|---|---|---|
| P1 Chrome | 15 | `runs/P1_manual_TEMPLATE.md` (chép thành file theo ngày giờ) |
| P2 Firefox **thật** | 15 | `runs/P2_manual_…` |
| P3 Android | 13 | `runs/P3_manual_…` |

Mỗi lượt chạy tay vẫn bắt đầu bằng restart backend và dựng đơn (`seed_orders.py`), như hướng dẫn trong RUN.md. Ảnh chụp kèm Sticky Notes overlay; tên ảnh đặt tuỳ ý cũng được, Claude Code sẽ đổi tên sau.

**Z1 – ảnh cho item Failed ở phần tự động:** ảnh phần tử do Playwright chụp không có thanh địa chỉ và overlay. Mình đề xuất:
- **Task 1:** item Failed tự động dùng ảnh phần tử làm bằng chứng.
- **Task 3:** mỗi màn × mỗi nền tảng có **1 ảnh chụp tay kèm overlay**, đúng quy tắc trong RUN.md.

Như vậy bạn không phải chụp tay lại từng item Failed. Đồng ý thì ghi "Z1 ok" khi báo kết quả.

Chạy xong cả 3 nền tảng thì push, rồi báo mình. Bước kế tiếp (4/6) là gộp kết quả tự động với chạy tay, liệt kê chỗ hai bên lệch nhau để bạn quyết verdict, rồi lập danh sách Failed để kiểm trùng issue trước khi viết bug.
````

**Xử lý:** [...]

---

## #50 | 02:29 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
"Trước mỗi lượt: Ctrl+C rồi chạy lại." Hình như trước đó mình có viết script đẻ reset lại DB mà không cần Ctrl + C mở lại á. Bạn giúp mình xem lại nhé
```

**Output:**
````
Có. Script nằm ở `HW02/bugs/_repro_C_FR15/7c/restart_backend.ps1`, làm từ HW02 C. Cách hoạt động:
- Tắt tiến trình `node server.js` đang chạy.
- Mở lại backend trong một cửa sổ thu nhỏ.
- Chờ tới khi API trả đủ 5 sản phẩm, in `backend restart xong: 5 sản phẩm`.

Không cần Ctrl+C hay cửa sổ A nữa. Đường dẫn backend được ghi cứng là `D:\HK7\Testing\Exercise\HW\eshop-sut\backend`, đúng với máy bạn.

Script đang nằm sâu trong thư mục bug HW02, nên đưa ra `tools/` để dùng chung, rồi gắn vào lệnh chạy cho gọn.

Mình thấy thêm một chỗ mâu thuẫn trong `RUN.md`. Tiền điều kiện của CL-58 ghi *"không restart backend cho tới khi chạy xong CL-58/59 trên P1, P2, P3"*, nhưng mỗi lượt lại bắt đầu bằng restart. Nay `seed_orders.py` dựng lại đủ đơn 5 trạng thái sau mỗi lần restart, nên tiền điều kiện chỉ cần sửa thành *"chạy `seed_orders.py` sau khi restart"*. Expected không đổi.

## Lệnh cho Claude Code

```
HW03 – R1, R2 (commit "HW03[T1] 3/6c: restart_backend dùng chung, sửa tiền điều kiện CL-58/59"):
1. Chép HW02/bugs/_repro_C_FR15/7c/restart_backend.ps1 → tools/restart_backend.ps1 (giữ nguyên bản HW02). Tắt backend nền của phiên này.
2. HW03/tests/package.json thêm script: "p1"/"p2"/"p3" = restart_backend.ps1 rồi playwright test --project=Px (powershell -ExecutionPolicy Bypass -File ../../tools/restart_backend.ps1 && …).
3. RUN.md (sửa gen_run.py rồi sinh lại): bước restart = `powershell -ExecutionPolicy Bypass -File tools\restart_backend.ps1`; sau restart chạy seed_orders.py khi lượt cần đơn.
4. R2: tiền điều kiện CL-58, CL-59 trong checklist.json → "Sau restart backend, chạy seed_orders.py để có đủ đơn 5 trạng thái" (expected không đổi); review_log ghi R2 "SV chốt".
5. Chạy thử restart_backend.ps1 một lần, in kết quả. on_stop.py --manual. Báo cáo ≤ 6 dòng.
```

Sau đó, mỗi lượt chạy tự động chỉ còn một lệnh trong `HW03\tests`:

```powershell
npm run p1
npm run p2
npm run p3   # điện thoại mở khoá, màn hình sáng, không chạm vào
```
````

**Xử lý:** [...]

---

## #51 | 02:31 05/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
──
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #52 | 02:31 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – R1, R2 (commit "HW03[T1] 3/6c: restart_backend dùng chung, sửa tiền điều kiện CL-58/59"):
1. Chép HW02/bugs/_repro_C_FR15/7c/restart_backend.ps1 → tools/restart_backend.ps1 (giữ nguyên bản HW02). Tắt backend nền của phiên này.
2. HW03/tests/package.json thêm script: "p1"/"p2"/"p3" = restart_backend.ps1 rồi playwright test --project=Px (powershell -ExecutionPolicy Bypass -File ../../tools/restart_backend.ps1 && …).
3. RUN.md (sửa gen_run.py rồi sinh lại): bước restart = `powershell -ExecutionPolicy Bypass -File tools\restart_backend.ps1`; sau restart chạy seed_orders.py khi lượt cần đơn.
4. R2: tiền điều kiện CL-58, CL-59 trong checklist.json → "Sau restart backend, chạy seed_orders.py để có đủ đơn 5 trạng thái" (expected không đổi); review_log ghi R2 "SV chốt".
5. Chạy thử restart_backend.ps1 một lần, in kết quả. on_stop.py --manual. Báo cáo ≤ 6 dòng.
```

**Output:**
```
Backend nền đã tắt. Giờ sửa package.json, gen_run.py, CL-58/59.

package.json và checklist.json đã ghi. gen_run.py sửa bằng Edit.

Chạy thử restart_backend.ps1.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** R1 + R2 xong. Commit `9dfb111 HW03[T1] 3/6c: restart_backend dùng chung, sửa tiền điều kiện CL-58/59`.
- **R1:** `tools/restart_backend.ps1` chép nguyên bản từ HW02 (so `cmp`: giống hệt). Backend nền của phiên đã tắt. `HW03/tests/package.json` có `npm run p1`, `p2`, `p3` (restart rồi mới chạy `--project=Px`).
- **RUN.md:** sinh lại từ `gen_run.py`. Bước 1 dùng `restart_backend.ps1`. Bước B ghi rõ: chạy `seed_orders.py` ngay sau restart và Bước A, khi lượt đó cần đơn.
- **R2:** tiền điều kiện CL-58 và CL-59 giờ là "Sau restart backend, chạy seed_orders.py để có đủ đơn 5 trạng thái". Expected không đổi. review_log có R2 "SV chốt".
- **Kiểm tra:**
  - check_checklist: 0 lỗi.
  - Chạy thử `restart_backend.ps1`: in "backend restart xong: 5 sản phẩm", exit 0. Cổng 3000 đang listen (backend mới); vite :5173 vẫn chạy.
  - Đã chạy on_stop.py --manual: prompt log có 18 lượt.
- **Cần quyết định:** không. Lưu ý: backend giờ do script bật trong một cửa sổ riêng (thu nhỏ), không còn là tiến trình nền của phiên này.
```

**Xử lý:** [...]

---

## #53 | 02:33 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: R1 + R2 xong. Commit 9dfb111 HW03[T1] 3/6c: restart_backend dùng chung, sửa tiền điều kiện CL-58/59.
- R1: tools/restart_backend.ps1 chép nguyên bản từ HW02 (so cmp: giống hệt). Backend nền của phiên đã tắt. HW03/tests/package.json có npm run p1, p2, p3 (restart rồi mới chạy --project=Px).
- RUN.md: sinh lại từ gen_run.py. Bước 1 dùng restart_backend.ps1. Bước B ghi rõ: chạy seed_orders.py ngay sau restart và Bước A, khi lượt đó cần đơn.
- R2: tiền điều kiện CL-58 và CL-59 giờ là "Sau restart backend, chạy seed_orders.py để có đủ đơn 5 trạng thái". Expected không đổi. review_log có R2 "SV chốt".
- Kiểm tra:
  - check_checklist: 0 lỗi.
  - Chạy thử restart_backend.ps1: in "backend restart xong: 5 sản phẩm", exit 0. Cổng 3000 đang listen (backend mới); vite :5173 vẫn chạy.
  - Đã chạy on_stop.py --manual: prompt log có 18 lượt.
- Cần quyết định: không. Lưu ý: backend giờ do script bật trong một cửa sổ riêng (thu nhỏ), không còn là tiến trình nền của phiên này.
```

**Output:**
````
Mọi thứ đã sẵn sàng để chạy lượt thật. Vào `HW03\tests` rồi chạy lần lượt:

```powershell
npm run p1
npm run p2
npm run p3   # điện thoại: mở khoá, màn hình sáng, tắt màn hình sau ≥ 10 phút, không chạm vào máy
```

Mỗi lệnh tự restart backend trước khi chạy. Nếu một lượt dừng giữa chừng vì lỗi môi trường (thông báo bắt đầu bằng `[global-setup]` hoặc mất kết nối với điện thoại), chạy lại đúng lệnh đó. Không chạy lại cả 3.

Xong phần tự động thì chạy tay theo `RUN.md`: P1 (15 item) → P2 Firefox thật (15) → P3 (13). Mỗi lượt chạy tay bắt đầu bằng `restart_backend.ps1`, cần đơn thì thêm `seed_orders.py`, như RUN.md đã ghi. Ảnh chụp có Sticky Notes overlay. Ngoài ra mỗi màn × mỗi nền tảng có 1 ảnh cho Task 3 (Z1).

Chạy xong tất cả thì commit kết quả của bạn rồi push:

```powershell
git add HW03/checklist/runs HW03/checklist/evidence
git commit -m "HW03[T1] 4/6a: SV chạy checklist P1/P2/P3 (auto + tay)"
git push
```

Ảnh gốc mà quá nặng thì đừng add vội. Báo mình trước, Claude Code sẽ nén rồi đổi tên.

Khi báo lại, ghi kèm **"Z1 ok"** hoặc ý kiến khác về cách chụp ảnh cho item Failed tự động. Mình sẽ đưa lệnh 4/6 để gộp kết quả, liệt kê chỗ lệch giữa tự động và chạy tay để bạn quyết, rồi lập danh sách Failed kèm kết quả kiểm trùng issue.
````

**Xử lý:** [...]

---

## #54 | 02:48 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Mình chạy xong phần tự động rồi, giờ buồn ngủ quá nên đi ngủ nhé. Lần sau thực hiện tiếp RUN.md nhỉ
```

**Output:**
````
Ngủ đi. Đúng rồi, lần sau tiếp tục chạy tay theo `RUN.md`.

Trước khi tắt máy, chạy **1 lệnh** để lưu kết quả tự động. Mốc thời gian của commit cũng là bằng chứng lượt chạy:

```powershell
git add HW03/checklist/runs HW03/checklist/evidence/auto
git commit -m "HW03[T1] 4/6a: SV chạy Playwright P1/P2/P3"
git push
```

Lần sau mở lại:
1. Cắm điện thoại, rồi bảo Claude Code **"bật lại"** (vite + adb reverse). Backend thì `restart_backend.ps1` tự bật.
2. Chạy tay theo `RUN.md`: P1 → P2 → P3.

Sáng dậy nhớ **nhắn hẹn giờ cụ thể** với 8 người cho buổi tối.
````

**Xử lý:** [...]

---

## #55 | 02:49 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Lưu lại những gì đang chạy hiện tại, để lần sau mình yêu cầu bật lại thì mở lại hết như vậy nhé. Giờ tắt tất cả những gì đang chạy giúp mình
```

**Output:**
```
Đã ghi lại những gì đang chạy và tắt hết. Các cổng 3000, 5173, 5037 giờ không còn gì nghe, không còn tiến trình `node` hay `adb` nào.

Lúc tắt có 3 thứ chạy, lần sau bạn bảo "bật lại" mình sẽ mở lại đúng như vậy:
- **Backend `:3000`**: bật lại bằng `tools\restart_backend.ps1`. Mỗi lần bật, CSDL tự seed lại.
- **Web `:5173`**: vite chạy ở `127.0.0.1`.
- **adb**: điện thoại POCO `da87b223`, nối cổng `5173` và `3000` sang máy. Mình đã gỡ hai cổng này rồi tắt adb.

Admin `:5174` lúc đó không chạy nên sẽ không bật.

Khi bật lại, điện thoại cần cắm cáp và bật gỡ lỗi USB. Nếu adb báo `unauthorized`, mình sẽ dừng và báo bạn.

Việc tiếp theo bên bạn: chạy `npm run p1`, `npm run p2`, `npm run p3` trong `HW03/tests` (mỗi lệnh đã tự restart backend), rồi chạy tay theo RUN.md.
```
*File AI ghi/gửi trong lượt này:* `hw03-runtime-state.md`

**Xử lý:** [...]

---

## #56 | 22:31 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
mở lại nhé
```

**Output:**
```
Đã bật lại đủ như lúc tắt:
- **Backend** đang chạy ở `:3000` (bật bằng `restart_backend.ps1`), CSDL vừa seed lại.
- **Web** đang chạy ở `127.0.0.1:5173`.
- **Điện thoại**: adb thấy `da87b223 device`, hai cổng `5173` và `3000` đã nối sang máy.

Việc tiếp theo bên bạn: chạy `npm run p1`, `npm run p2`, `npm run p3` trong `HW03\tests` (mỗi lệnh tự restart backend), rồi chạy tay theo RUN.md.
```

**Xử lý:** [...]

---

## #57 | 22:34 09/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
chạy npm run p1, npm run p2, npm run p3 trong HW03/tests (mỗi lệnh đã tự restart backend)
Để làm gì nhỉ
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #58 | 22:40 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Cho tôi hỏi, hiện là tôi chưa lấy/viết các skills cần thiết cho HW này chưa nhỉ?
```

**Output:**
```
Trước khi trả lời về skill, có một việc quan trọng hơn: **deadline HW03 là 07/11, đã qua 2 ngày**. Commit cuối trên repo là `7ba0785` lúc 02:49 ngày 05/11 (lượt Playwright tự động), sau đó không có gì thêm.

Homework Policies ghi *"không nhận bài trễ"*, ngoại lệ duy nhất là có lý do nghiêm trọng, phải email kèm minh chứng. Bạn đã nộp bản nào lên Moodle chưa, hay thầy có gia hạn? Câu trả lời quyết định việc nên làm tiếp:
- **Đã nộp hoặc được gia hạn:** làm tiếp như kế hoạch.
- **Chưa nộp, không gia hạn:** việc đầu tiên là email cho thầy/TA ngay, kèm lý do. Hoàn thiện skill lúc này không còn ý nghĩa cho điểm.

## Trạng thái skill cho HW03

| Skill | Trạng thái |
|---|---|
| `gui-checklist-testing` | **Có khung** ở `.claude/skills/` (tạo 04/11, commit `a1df52c`): `SKILL.md` 78 dòng, 7 bước, 5 script, `dom_probe.js`, các mẫu RUN/sv_items. Đã dùng cho bước 0–3. Bước 4–6 (gộp kết quả, Excel, gom bug) chưa chạy thật; `build_excel.py` mới được thử ra thư mục tạm |
| `usability-evaluation` (Task 2) | **Chưa tạo.** Theo kế hoạch phải làm trước pilot |
| Skill công khai | Không lấy về. Đã chốt chỉ tham khảo, không cài |
| Bản nộp `HW03/skills/` | **Trống** (chỉ có `.gitkeep`). Chưa chép skill vào |
| Video demo skill (YouTube) | Chưa làm |

Phần Agent Skills chiếm 10 điểm và cần cả skill lẫn video. Hiện mới có khoảng nửa thứ nhất, và chưa nằm trong thư mục nộp.

Ngoài skill, theo repo còn thiếu các phần sau:
- **Task 1/3:** chưa chạy tay theo `RUN.md`, chưa gộp kết quả, chưa có bug, chưa có Excel.
- **Task 2:** chưa có phiên usability nào.
- **Báo cáo:** report, Critique, form AI-02/03/05, README, zip đều chưa có.

Bạn cho mình biết tình trạng nộp bài, mình sẽ đề xuất thứ tự làm cho phù hợp.
```

**Xử lý:** [...]

---

## #59 | 22:41 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Thật ra thì đó deadline tôi tự tạo, deadline thật là 10h sáng 11/11 cơ
```

**Output:**
````
Vậy là còn khoảng **35 giờ**, tính tới 10:00 thứ Tư 11/11. Đủ thời gian, nhưng phải xếp chặt. Task 2 (40 điểm) vẫn là đường găng, vì phụ thuộc giờ rảnh của bạn bè.

## Lịch đề xuất

| Khi | Bạn làm | Claude Code làm song song |
|---|---|---|
| **Tối nay (T2), tới khoảng 1:00** | Chạy tay `RUN.md` P1 → P2 → P3 (~1 giờ) | Tạo skill `usability-evaluation`; sửa deadline trong `report_plan` |
| **T3 ban ngày** (đi học) | Hẹn giờ cụ thể với 8 người cho tối T3; viết bug report lúc rảnh | Bước 4/6: gộp kết quả, Excel, danh sách Failed + kiểm trùng issue; dựng khung form AI-02/03/05 |
| **T3 tối** | Pilot + 7 phiên, mỗi phiên ~20 phút, khoảng 3 giờ liền. Mỗi phiên một commit | — |
| **Đêm T3 → sáng T4** | Phân tích usability, Critique, verdict Audit, tự chấm, quay video skill | Tính SUS, sinh bảng report, form, README, zip |
| **T4 trước 10:00** | Rà soát lần cuối, ký PDF, nộp | `hw-submission-audit` |

Nếu thiếu giờ thì **video skill là phần cắt đầu tiên**: phần Skill được 10 điểm, nhưng quay và dựng video mất khoảng 1 giờ. Phần bắt buộc thì không cắt được: Task 2, form AI và commit log.

## Lệnh cho Claude Code (dán ngay, rồi đi chạy tay RUN.md trong lúc nó làm)

```
HW03 – 2 việc (mỗi việc 1 commit):
A. "HW03: deadline thật 11/11 10:00": report_plan + HW03/CLAUDE.md: deadline = 10:00 11/11/2026; lịch mục h theo bảng: T2 tối chạy tay; T3 ngày 4/6 + form; T3 tối pilot + 7 phiên; đêm T3–sáng T4 phân tích + report + zip.
B. "HW03[T2] 2/10: skill usability-evaluation": .claude/skills/usability-evaluation/ theo mẫu domain-bva-testing/gui-checklist-testing, mỗi lần gọi 1 bước rồi dừng:
  0 plan 9 phần (Rubin, slide) · 1 participant kit 1 trang (nhiệm vụ dạng mục tiêu, SEQ, SUS 10 câu tiếng Việt, 4 câu hỏi mở) + freeze · 2 pilot → sửa kit (diff + lý do SV) · 3 phiếu quan sát/phiên (sessions/S0x.json: thời gian, hoàn thành, lỗi, do dự, trích lời, SEQ, 10 câu SUS) · 4 scripts/sus_score.py (SUS chuẩn: lẻ −1, chẵn 5−x, ×2,5; trung bình, SD, min/max; SEQ; tỉ lệ hoàn thành; thời gian) → bảng giữa marker REPORT · 5 khung findings (SV viết: điểm đau, tách bug lẻ / vấn đề thiết kế, severity × probability) · 6 gom dữ kiện bug (SV viết mô tả).
  Giới hạn trong SKILL.md: AI không tạo danh sách người tham gia, ghi chú quan sát, câu trả lời SUS, phần tổng hợp/findings; không đưa dữ liệu cá nhân người tham gia cho AI (che 4 số giữa SĐT).
  Áp bước 0–1 cho HW03 bằng file đã có (usability/plan.md, participant_kit.md: chỉ kiểm khớp skill, không viết lại); thử sus_score.py trên 2 phiếu GIẢ trong thư mục tạm (không commit dữ liệu giả).
on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

Hai việc còn lại cho skill làm lúc đóng gói: chép cả 2 skill vào `HW03/skills/` (bản nộp), và quay video demo.
````

**Xử lý:** [...]

---

## #60 | 22:42 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Task 2 tôi có thể deploy rồi bảo bạn tôi vào test được không? Chứ ban đầu tôi mời online, gần tôi cũng chả có ai quen cả
```

**Output:**
````
**Được.** Slide usability có liệt kê *"remote synchronous"* là một hình thức hợp lệ, cạnh in-lab và remote asynchronous. Đề chỉ bắt **moderated**, tức là bạn phải có mặt quan sát và hỏi. Cách làm: gọi **Google Meet**, người tham gia **chia sẻ màn hình** và vừa làm vừa nói suy nghĩ, bạn quan sát và ghi lại. Không nên để họ tự làm một mình rồi gửi kết quả: đó là unmoderated, sai yêu cầu của đề.

## Đưa SUT ra ngoài: dùng tunnel, không deploy

Có một trở ngại kỹ thuật: web gọi cứng `http://localhost:3000` ở 14 chỗ. Nếu chỉ mở cổng 5173 ra ngoài, trình duyệt của bạn bè sẽ gọi `localhost:3000` trên **máy của họ**, nên không chạy được.

| Cách | Nhược điểm |
|---|---|
| Deploy lên cloud (Vercel + Render…) | Lâu; khó reset CSDL giữa các phiên; môi trường khác hẳn lúc chạy checklist |
| Cho bạn điều khiển máy bạn (Chrome Remote Desktop) | Không sửa gì, nhưng có độ trễ, làm sai kết quả đo "tốc độ" và SUS |
| **Tunnel (đề xuất)** | Đổi URL API thành đường dẫn tương đối, thêm proxy `/api` trong Vite, rồi mở **một** tunnel Cloudflare miễn phí (không cần tài khoản) tới `:5173`. Backend vẫn chạy trên máy bạn, nên `restart_backend.ps1` vẫn reset được trước mỗi phiên |

Thay đổi chỉ làm trên **nhánh riêng của bản SUT trên máy bạn** (`usability-tunnel`), **không push lên fork của nhóm**. Lượt chạy tay checklist phải dùng code gốc: **chạy tay RUN.md xong rồi mới chuyển nhánh**, hoặc nhớ chuyển về `main` trước khi chạy. Report ghi rõ khác biệt môi trường: người tham gia dùng trình duyệt của họ qua Internet.

**Quay phiên:** dùng Xbox Game Bar (`Win + Alt + R`) hoặc OBS để quay cửa sổ Meet kèm tiếng, sau khi xin đồng ý ngay đầu video. Tính năng ghi hình của Meet có thể không có trên tài khoản của bạn, nên đừng dựa vào nó.

**Lưu ý thêm:**
- Mỗi phiên, bạn gửi link tunnel và tài khoản test riêng cho người đó, rồi tắt tunnel khi xong.
- Yêu cầu họ dùng **máy tính** (không dùng điện thoại) để các phiên giống nhau.

## Lệnh cho Claude Code (dán sau lệnh skill ở trên, hoặc gộp chung)

```
HW03[T2] – môi trường usability từ xa (commit trong repo bài: "HW03[T2] 2b/10: môi trường usability từ xa (tunnel)"):
1. Repo ..\eshop-sut: tạo nhánh local usability-tunnel (KHÔNG push). frontend-web: thay "http://localhost:3000" → đường dẫn tương đối; vite.config: proxy /api (và /uploads nếu có) → http://localhost:3000, server.allowedHosts cho *.trycloudflare.com. Commit trên nhánh đó. In git diff --stat.
2. Cài cloudflared (winget hoặc tải bản exe; hỏi tôi trước khi cài). tools/usability_session.ps1: restart_backend.ps1 → vite (nhánh tunnel) → cloudflared tunnel --url http://localhost:5173 → in link; Ctrl+C tắt tunnel. Kèm tools/sut_main.ps1 để quay về nhánh main của SUT (dùng trước khi chạy checklist).
3. Kiểm: mở link tunnel trên trình duyệt (tôi sẽ thử điện thoại dùng 4G) → đăng nhập test@eshop.com, thêm giỏ, áp VIP100, đặt hàng, thấy đơn trong Hồ sơ.
4. usability/plan.md: hình thức = remote synchronous moderated (Google Meet, người tham gia chia sẻ màn hình, think-aloud; quay bằng Game Bar/OBS khi được đồng ý); khác biệt môi trường so với checklist. participant_kit: thêm dòng "dùng máy tính, mở link SV gửi".
on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push repo bài.
```

Hẹn bạn bè ngay tối mai (T3), mỗi người một khung 20 phút, xếp liền nhau. Người làm pilot nên là người hẹn được sớm nhất.
````

**Xử lý:** [...]

---

## #61 | 23:30 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
khi chạy tay theo RUN.md có cần đọc thêm file khác không vậy?
```

**Output:**
```
Gần như không cần. RUN.md đã đủ thứ tự chạy, tiền điều kiện, ngưỡng Pass/Fail ("Cần nhìn" chép nguyên văn Expected), quy tắc chụp ảnh và lệnh cần chạy. Chỉ có 3 file đi kèm:

| File | Khi nào | Dùng để |
|---|---|---|
| `checklist/runs/Px_manual_TEMPLATE.md` | Đầu mỗi lượt | Chép thành `Px_manual_<YYYYMMDD-HHMM>.md`, ghi status, notes và tên ảnh từng item |
| `checklist/runs/Px_auto_*.json` | Item **mixed** | Cột "Cần nhìn" của item mixed ghi "Phần tự động: xem `runs/Px_auto_*.json`". Mở file, tìm mã item, đọc `notes` (số đo, chuỗi Tab, mã màu…) rồi bạn chấm phần còn lại bằng mắt. Vì vậy phải chạy `npm run px` **trước** lượt tay của nền tảng đó |
| `checklist/dom_probe.js` | Chỉ trên P3, khi cần đo DOM | Dán vào Console của `chrome://inspect`, chép JSON vào file kết quả. Giờ P3 đã có lượt auto nên ít khi cần |

Không cần đọc thêm:
- `checklist.md`/`checklist.json`: chỉ mở nếu muốn xem căn cứ SRS hoặc giả định của một item. Item N/A không có trong bảng RUN.md.
- `seed_orders.py`: chỉ chạy (Bước B) rồi chép bảng mã đơn mà nó in ra vào file kết quả.
- `issue_dup_FR02.md`: để dành cho bước viết bug (6/6), khi kiểm trùng issue.

Thứ tự mỗi nền tảng: `npm run px`, rồi mình gộp file auto, rồi bạn chạy tay theo RUN.md, ghi vào bản sao template.
```

**Xử lý:** [...]

---

## #62 | 23:31 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Màn hình này là sao: "Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ" là bao nhiêu màn hình
```

**Output:**
```
Chuỗi đó là **3 trang (URL) nhưng 4 màn hình cần xem**:

| # | Màn hình | URL | Nhận biết |
|---|---|---|---|
| 1 | Đăng nhập | `/login` | Form email + mật khẩu |
| 2 | Quên mật khẩu **B1** | `/forgot-password` | Ô "Nhập Email của bạn" + nút "Lấy mã OTP" |
| 3 | Quên mật khẩu **B2** | `/forgot-password` (cùng URL) | Bấm "Lấy mã OTP" xong thì hiện hộp xanh "Mã OTP của bạn là: …", ô OTP, ô mật khẩu mới, nút "← Quay lại" |
| 4 | Hồ sơ | `/profile` (phải đăng nhập) | Phần form hồ sơ. Lịch sử đơn cũng nằm ở trang này nhưng tính là màn M4 riêng |

B1 và B2 là hai bước trên cùng một trang, đổi bằng state (`setStep`), URL không đổi (`c2_inventory.md:38–53`).

Gặp item có màn hình như vậy, bạn kiểm cả 4 màn. Item **Failed** nếu **ít nhất 1 màn** vi phạm ngưỡng; notes ghi rõ màn nào, ví dụ "B2: …".

Ảnh tổng quan cho Task 3 vẫn theo M1–M5 (B1 và B2 chung M2), không phải mỗi item chụp riêng 4 màn.
```

**Xử lý:** [...]

---

## #63 | 00:22 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Firefox làm gì có lighthouse nhỉ
```

**Output:**
```
Đúng, Lighthouse chỉ có trên Chrome và Edge. Firefox có công cụ tương đương nằm ngay trong menu `»` bạn đang mở: **Accessibility**. Expected của SV-04 ghi *"DevTools Accessibility / Lighthouse"*, nên dùng công cụ này là đúng với Expected.

## Đo độ tương phản trên Firefox

1. Bấm `»` → **Accessibility**. Nếu có nút *Turn On Accessibility Features* thì bấm vào.
2. Trên thanh công cụ của tab này, ô **Check for issues** → chọn **Contrast**. Cây bên dưới sẽ chỉ còn những đoạn chữ **không đạt** ngưỡng WCAG, mỗi dòng có biểu tượng cảnh báo.
3. Bấm vào một dòng. Ở khung **Checks** bên phải sẽ hiện tỉ lệ tương phản (ví dụ `Contrast: 2.85`) kèm dòng *does not meet WCAG standards*.
4. Muốn đo một phần tử cụ thể (một nhãn, một nút), dùng nút chọn phần tử ở góc trái tab Accessibility, rồi chỉ vào phần tử đó trên trang.

Khi ghi kết quả, chú ý mấy điểm sau:
- **Ghi tỉ lệ thực đo được** vào Notes, ví dụ "nhãn 'Email' 3.2:1", không chỉ ghi Failed.
- Firefox chấm **chữ lớn** (từ 18pt, hoặc 14pt đậm) theo ngưỡng 3:1. SV-04 của bạn chỉ quy định 4.5:1 **cho chữ thường**, nên chữ lớn mà Firefox báo thì ghi vào Notes, không tính vào Pass/Fail của item.
- Nếu **placeholder** không xuất hiện trong danh sách, ghi Notes là "placeholder không đo được bằng Accessibility panel của Firefox". Đừng tự ước lượng tỉ lệ.
- Chụp ảnh tab Accessibility cho từng chỗ Failed, kèm Sticky Notes overlay như các ảnh khác.
```

**Xử lý:** [...]

---

## #64 | 00:53 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<task-notification>
<task-id>bnddydt0w</task-id>
<tool-use-id>toolu_019QpNyDpQYTeKpbzaPss5Pg</tool-use-id>
<output-file>C:\Users\tanhi\AppData\Local\Temp\claude\3d1ee2708df72d7d\e3928b55-32bd-47d5-a8e1-a4900f6a6dea\tasks\bnddydt0w.output</output-file>
<status>killed</status>
<summary>Background command "Start web frontend dev server" was stopped because the system is running low on memory</summary>
<note>This is not a failure of the command. Claude Code stopped it because the system was critically low on memory while the session was idle, which says nothing about the command or its own memory use, so there is nothing in it to debug. Do not start it again on your own, even if the work seems to need it: memory may still be short. Report what was stopped and why, and start it again only when asked. The user can turn this behavior off by starting Claude Code with CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1 in its environment; setting it from a shell command has no effect.</note>
</task-notification>
```

**Output:**
````
Web `:5173` (vite) vừa bị Claude Code tự dừng vì máy gần hết RAM lúc phiên đang rảnh. Không phải lỗi của vite. Mình chưa bật lại.

Backend `:3000` và adb (2 cổng) vẫn chạy: hai cái này không do phiên quản lý nên không bị dừng.

Cần web thì bảo mình bật lại, hoặc bạn tự chạy:

```powershell
cd ..\eshop-sut\frontend-web; npx vite --host 127.0.0.1 --port 5173
```

Bạn tự chạy trong cửa sổ riêng thì vite không bị Claude Code dừng theo kiểu này nữa. Trước lượt Playwright nên đóng bớt ứng dụng nặng.
````

**Xử lý:** [...]

---

## #65 | 02:00 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – 2 việc (mỗi việc 1 commit):
A. "HW03: deadline thật 11/11 10:00": report_plan + HW03/CLAUDE.md: deadline = 10:00 11/11/2026; lịch mục h theo bảng: T2 tối chạy tay; T3 ngày 4/6 + form; T3 tối pilot + 7 phiên; đêm T3–sáng T4 phân tích + report + zip.
B. "HW03[T2] 2/10: skill usability-evaluation": .claude/skills/usability-evaluation/ theo mẫu domain-bva-testing/gui-checklist-testing, mỗi lần gọi 1 bước rồi dừng:
  0 plan 9 phần (Rubin, slide) · 1 participant kit 1 trang (nhiệm vụ dạng mục tiêu, SEQ, SUS 10 câu tiếng Việt, 4 câu hỏi mở) + freeze · 2 pilot → sửa kit (diff + lý do SV) · 3 phiếu quan sát/phiên (sessions/S0x.json: thời gian, hoàn thành, lỗi, do dự, trích lời, SEQ, 10 câu SUS) · 4 scripts/sus_score.py (SUS chuẩn: lẻ −1, chẵn 5−x, ×2,5; trung bình, SD, min/max; SEQ; tỉ lệ hoàn thành; thời gian) → bảng giữa marker REPORT · 5 khung findings (SV viết: điểm đau, tách bug lẻ / vấn đề thiết kế, severity × probability) · 6 gom dữ kiện bug (SV viết mô tả).
  Giới hạn trong SKILL.md: AI không tạo danh sách người tham gia, ghi chú quan sát, câu trả lời SUS, phần tổng hợp/findings; không đưa dữ liệu cá nhân người tham gia cho AI (che 4 số giữa SĐT).
  Áp bước 0–1 cho HW03 bằng file đã có (usability/plan.md, participant_kit.md: chỉ kiểm khớp skill, không viết lại); thử sus_score.py trên 2 phiếu GIẢ trong thư mục tạm (không commit dữ liệu giả).
on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

**Output:**
```
Task A trước: sửa deadline + lịch mục h.

Xong A (`99a64dc`). Sang B: đọc mẫu skill + file usability hiện có.

Slide khớp plan.md (9 phần, criticality = severity × probability, thống kê thời gian mean/median/range/SD). Viết skill.

Giờ assets.

Assets xong. Giờ viết scripts (sus_score trước, quan trọng nhất).

Còn 5 script nhỏ: freeze, check_kit, kit_diff, new_session, bug_facts.

Scripts xong. Áp bước 0–1 cho HW03 (chỉ kiểm) + thử sus_score trên 2 phiếu giả ở scratchpad.

Lỗi ở script (regex bắt nhầm "Lời mở đầu"), không phải kit. Sửa.

HW03 plan + kit: 0 lỗi, trùng bản đóng băng v1. Sửa placeholder template cho khỏi cảnh báo, rồi thử sus_score.

Số tay khớp: S01 = 82,5, S02 = 57,5, SD = 17,7. Lỗi nhỏ: dòng chú thích dính ngay sau bảng (GFM sẽ coi là hàng bảng). Sửa.

Skill chạy đúng. Ghi khai Audit, chạy on_stop, commit chỉ skill + prompt log (không đụng file chạy tay của SV).

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** A + B xong, 2 commit: `99a64dc HW03: deadline thật 11/11 10:00` và `78c13d8 HW03[T2] 2/10: skill usability-evaluation`.
- **A:** đã sửa deadline thành 10:00 11/11/2026 ở `HW03/CLAUDE.md:8` và report_plan dòng 3. Mục h thay bằng bảng lịch 4 mốc (T2 tối → sáng T4).
- **B:** skill ở `.claude/skills/usability-evaluation/`, gồm SKILL.md (bước 0–6 và giới hạn AI), 2 reference, 3 asset, 6 script. `sus_score.py` báo lỗi thay vì điền thay khi phiếu thiếu SUS/SEQ, và từ chối phiếu có chuỗi số giống SĐT hoặc có email.
- **Áp bước 0–1 cho HW03:** `check_kit.py` trên plan.md + participant_kit.md ra 0 lỗi; hai file trùng bản đóng băng v1, không sửa.
- **Thử 2 phiếu giả (thư mục tạm, không commit):** SUS 82,5 và 57,5, khớp tính tay; SD 17,7; thời gian, hoàn thành, benchmark tính đúng; ghi bảng giữa marker được. kit_diff, bug_facts, new_session cũng chạy đúng.
- **Lỗi script, đã sửa:** check_kit bắt nhầm mục "Lời mở đầu"; sus_score để dòng chú thích dính vào bảng.
- **Kiểm tra:** check_kit 0 lỗi; sus_score đã chạy thử; on_stop.py --manual: prompt log 25 lượt. Không có lint/test tự động cho skill (Not run).
- **Cần quyết định:**
  - D1 – Report chưa có marker `<!-- REPORT:U1:usability_sessions/usability_summary:START/END -->`. Phương án: (a) AI chèn khung marker vào report, (b) SV tự chèn.
  - D2 – Có nhiều file chạy tay của bạn chưa commit: ảnh `evidence/P1–P3`, `runs/*_manual_*`, `runs/*_auto_*.json`, ảnh auto bị ghi đè, xoá 3 `.gitkeep`. Mình không động vào. Phương án: (a) bạn tự commit, (b) bảo mình commit cùng bước 4/6 gộp kết quả.
- **Nhắc push:** bạn tự push 2 commit mới (`99a64dc`, `78c13d8`); `7ba0785` cũng chưa push nếu bạn chưa push trước đó.
```
*File AI ghi/gửi trong lượt này:* `SKILL.md`, `plan-9-parts.md`, `schema-session.md`, `session_template.json`, `participant_kit_template.md`, `findings_template.md`, `sus_score.py`, `freeze.py`, `check_kit.py`, `kit_diff.py`, `new_session.py`, `bug_facts.py`

**Xử lý:** [...]

---

## #66 | 02:09 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
response prompt ở trên:
Báo cáo cho phiên thảo luận

- Nhiệm vụ: A + B xong, 2 commit: 99a64dc HW03: deadline thật 11/11 10:00 và 78c13d8 HW03[T2] 2/10: skill usability-evaluation.
- A: đã sửa deadline thành 10:00 11/11/2026 ở HW03/CLAUDE.md:8 và report_plan dòng 3. Mục h thay bằng bảng lịch 4 mốc (T2 tối → sáng T4).
- B: skill ở .claude/skills/usability-evaluation/, gồm SKILL.md (bước 0–6 và giới hạn AI), 2 reference, 3 asset, 6 script. sus_score.py báo lỗi thay vì điền thay khi phiếu thiếu SUS/SEQ, và từ chối phiếu có chuỗi số giống SĐT hoặc có email.
- Áp bước 0–1 cho HW03: check_kit.py trên plan.md + pai file trùng bản đóng băng v1, không sửa.
- Thử 2 phiếu giả (thư mục tạm, không commit): SUS 82,5 và 57,5, khớp tính tay; SD 17,7; thời gian, hoàn thành, benchmark tính đúng; ghi bảng giữa marker được. kit_diff, bug_facts, new_session cũng chạy đúng.                                                               i script, đã sửa: check_kit bắt nhầm mục "Lời mở hích dính vào bảng.
- Kiểm tra: check_kit 0 lỗi; sus_score đã chạy thử; on_stop.py --manual: prompt log 25 lượt. Không có lint/test tự động cho skill (Not run).
- Cần quyết định:
  - D1 – Report chưa có marker <!-- REPORT:U1:usability_sessions/usability_summary:START/END -->. Phương án: (a) AI chèn khung marker   vào report, (b) SV tự chèn.
  - D2 – Có nhiều file chạy tay của bạn chưa commit: ảnh evidence/P1–P3, runs/*_manual_*, runs/*_auto_*.json, ảnh auto bị ghi đè, xoá 3 .gitkeep. Mình không động vào. Phương án: (a) bạnit cùng bước 4/6 gộp kết quả.
- Nhắc push: bạn tự push 2 commit mới (99a64dc, 78c13d8); 7ba0785 cũng chưa push nếu bạn chưa push trước đó.
===
Hiện mình đã làm xong RUN.md rồi nhé. Thực hiện tiếp, đồng thời nhờ nó check các ảnh và những gì mình viết đã oke chưa nhé
```

**Output:**
````
RUN.md xong là đã qua được phần nặng nhất của Task 1/3. Trả lời 2 quyết định:
- **D1 = a:** AI chèn khung marker vào report. Phần chữ nằm ngoài marker vẫn là của bạn.
- **D2:** commit kết quả chạy tay **sau khi** kiểm và nén ảnh, gói chung vào bước 4/6.

Mình ngầm hiểu **Z1 ok**: item Failed ở phần tự động dùng ảnh phần tử làm bằng chứng; Task 3 dùng mỗi màn × nền tảng 1 ảnh có overlay. Nếu không đồng ý thì xoá dòng Z1 trong lệnh.

## Lệnh cho Claude Code

```
HW03[T1] 4/6 – kiểm + gộp. KHÔNG sửa chữ tôi viết trong runs/*_manual_*; chỉ liệt kê.
1. Kiểm (chỉ đọc) → HW03/checklist/run_check.md:
   a. Ảnh evidence/P1–P3 (xem từng ảnh): có overlay "23120255 · Lê Tấn Hiệp · email"; thấy tên trình duyệt/thiết bị + URL localhost; không lộ đường dẫn C:\Users\…, token, chrome://version; ảnh nhoè/cắt mất vùng lỗi. Đủ: mỗi item manual Failed ≥ 1 ảnh; mỗi màn × nền tảng 1 ảnh Task 3 (Z1: item auto Failed dùng ảnh phần tử).
   b. runs/*_manual_*: item nào chưa có kết quả; giá trị ngoài Passed/Failed/N/A; Failed thiếu Notes; N/A thiếu mã giả định; Notes mâu thuẫn với expected (vd ghi số liệu đạt ngưỡng mà chấm Failed).
   c. So auto ↔ manual cùng item/nền tảng: lệch → bảng để tôi quyết verdict.
   Dừng, báo cáo phần a–c nếu có lỗi chặn (thiếu kết quả/ảnh); không chặn thì làm tiếp.
2. Nén + đổi tên ảnh như HW02D (compress_manual.py; bản gốc → thư mục gitignore), tên P<n>_<id>_<k>.png. Commit "HW03[T1] 4/6a: SV chạy tay P1/P2/P3" (runs/, evidence/ đã nén, khôi phục .gitkeep nếu cần).
3. merge_platform.py: gộp auto + manual vào checklist.json (ket_qua theo nền tảng; item lệch để "CHỜ SV" trong bảng 1c, không tự chọn). build_excel.py → excel/23120255_HW03_Checklist.xlsx (recalc, 0 lỗi công thức). Danh sách Failed (item × nền tảng) + kiểm trùng issues.json (trùng → số issue; HW02 BUG-xx của tôi) → HW03/bugs/failed_list.md. Commit "HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed".
4. D1=a: chèn khung marker REPORT:U1 (sessions, summary) và REPORT:T1 (checklist summary, cross-platform) vào report; chạy script điền bảng T1.
on_stop.py --manual. Báo cáo ≤ 15 dòng: số item Passed/Failed/N/A theo nền tảng, số Failed mới (chưa có issue) / trùng, các điểm cần tôi quyết.
```

## Việc tiếp theo

1. **Push** 3 commit đang chờ (`7ba0785`, `99a64dc`, `78c13d8`) cùng các commit mới sau lệnh này.
2. **Lệnh tunnel ở lượt trước chưa chạy.** Bạn cần nó cho Task 2 tối nay, nên dán ngay sau lệnh này. Chạy đến bước 3 thì thử link tunnel bằng điện thoại dùng 4G.
3. Báo cáo 4/6 về là bạn viết bug cho các Failed mới (🔒). Mình chỉ kiểm dữ kiện, không nháp mô tả bug.

Đã 2 giờ sáng. Nếu mệt thì cho Claude Code chạy bước 1–4 rồi đi ngủ, sáng dậy đọc báo cáo. Việc nhất định phải xong trong sáng nay là **hẹn giờ với 8 người** cho tối nay.
````

**Xử lý:** [...]

---

## #67 | 02:11 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 4/6 – kiểm + gộp. KHÔNG sửa chữ tôi viết trong runs/*_manual_*; chỉ liệt kê.
1. Kiểm (chỉ đọc) → HW03/checklist/run_check.md:
   a. Ảnh evidence/P1–P3 (xem từng ảnh): có overlay "23120255 · Lê Tấn Hiệp · email"; thấy tên trình duyệt/thiết bị + URL localhost; không lộ đường dẫn C:\Users\…, token, chrome://version; ảnh nhoè/cắt mất vùng lỗi. Đủ: mỗi item manual Failed ≥ 1 ảnh; mỗi màn × nền tảng 1 ảnh Task 3 (Z1: item auto Failed dùng ảnh phần tử).
   b. runs/*_manual_*: item nào chưa có kết quả; giá trị ngoài Passed/Failed/N/A; Failed thiếu Notes; N/A thiếu mã giả định; Notes mâu thuẫn với expected (vd ghi số liệu đạt ngưỡng mà chấm Failed).
   c. So auto ↔ manual cùng item/nền tảng: lệch → bảng để tôi quyết verdict.
   Dừng, báo cáo phần a–c nếu có lỗi chặn (thiếu kết quả/ảnh); không chặn thì làm tiếp.
2. Nén + đổi tên ảnh như HW02D (compress_manual.py; bản gốc → thư mục gitignore), tên P<n>_<id>_<k>.png. Commit "HW03[T1] 4/6a: SV chạy tay P1/P2/P3" (runs/, evidence/ đã nén, khôi phục .gitkeep nếu cần).
3. merge_platform.py: gộp auto + manual vào checklist.json (ket_qua theo nền tảng; item lệch để "CHỜ SV" trong bảng 1c, không tự chọn). build_excel.py → excel/23120255_HW03_Checklist.xlsx (recalc, 0 lỗi công thức). Danh sách Failed (item × nền tảng) + kiểm trùng issues.json (trùng → số issue; HW02 BUG-xx của tôi) → HW03/bugs/failed_list.md. Commit "HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed".
4. D1=a: chèn khung marker REPORT:U1 (sessions, summary) và REPORT:T1 (checklist summary, cross-platform) vào report; chạy script điền bảng T1.
on_stop.py --manual. Báo cáo ≤ 15 dòng: số item Passed/Failed/N/A theo nền tảng, số Failed mới (chưa có issue) / trùng, các điểm cần tôi quyết.
```

**Output:**
```
Bắt đầu bước 1: đọc file kết quả chạy tay.

Ảnh nhỏ sẵn (≤ 225 KB). Xem 1 ảnh mẫu để biết bố cục trước.

Đang xem ảnh: P1 + P2 xong (phát hiện nhãn M lệch, ảnh hoán đổi, lộ tài khoản đã lưu). Còn P3.

P3 không có overlay. Xem nốt các ảnh P3 còn lại để xác nhận.

Ảnh xem xong. Giờ so auto ↔ manual (1c).

Đủ dữ kiện. Có lỗi chặn (thiếu ảnh M5, 26 ảnh P3 không overlay, ảnh đặt nhầm tên) → ghi `run_check.md` rồi dừng theo lệnh.
```
*File AI ghi/gửi trong lượt này:* `run_check.md`

**Xử lý:** [...]

---

## #68 | 02:18 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: 4/6 mục 1 (kiểm, chỉ đọc). Dừng ở mục 1 vì có lỗi chặn về ảnh; mục 2–4 (nén ảnh, gộp kết quả, Excel, marker) chưa làm. Chi tiết ở HW03/checklist/run_check.md.
- File đã tạo/sửa: HW03/checklist/run_check.md. Không sửa runs/*_manual_*. Chưa commit.
- Kết quả theo nền tảng:

| Nền tảng | Chạy tay: Passed / Failed / N/A | Auto: Passed / Failed / Blocked |
|----------|---------------------------------|---------------------------------|
| P1       | 5 / 9 / 1                       | 25 / 44 / 2                     |
| P2       | 3 / 11 / 1                      | 23 / 43 / 2                     |
| P3       | 1 / 11 / 1                      | 23 / 40 / 1                     |
  Số Failed mới (chưa có issue) và Failed trùng: chưa đếm, vì chưa gộp kết quả.
- Lỗi chặn (cần bạn xử lý):
  - B1: 25 ảnh P3_*.jpg không có overlay. Bạn thêm overlay hoặc chụp lại (AI không được ghép overlay).
  - B2: thiếu ảnh M5 (Navbar) trên cả P1, P2, P3.
  - B3: nhãn ảnh M ở P1, P2 không khớp nội dung (P2: login…).
  - B4: P2 ảnh CL-52 và CL-64 tráo nhau; P3_CL-52_1 chụp bảng Lịch sử đơn chứ không phải màn khoá đăng nhập.
  - B5: P1_SV-02-3 và P1_SV-02-4 lộ Gmail cá nhân và 6 tài khoản đã lưu (gồm tài khoản dự án khác). Cần che hoặc chụp lại.
- Cần quyết định:
  - Q1: P1 chạy tay trên Cốc Cốc 160, không phải Chro trên Chrome / (b) đổi P1 thành Cốc Cốc và khai lệchso với kế hoạch / (c) giữ kết quả, ghi vào phần giới hạn.
  - Q2: CL-64 ghi N/A trên cả 3 nền tảng nhưng item c định – (a) Blocked / (b) chạy lại với ô SĐT bỏ trống. Ảnh P2 nhập SĐT 10 số vẫn bị từ chối, trùng tiêu đề issue #111.
  - Lệch auto ↔ chạy tay: 8 dòng L1–L8 ở run_check.mdL-08 lệch trên P2/P3 là do Playwright giả lập localevi-VN, còn trình duyệt thật của bạn ra "6,000,000 ₫".
  - Verdict P1 cần xem lại: CL-08 và CL-09 chấm Passeg nhau giữa 3 nền tảng (R9, R11).
- Không chặn: 12 điểm R1–R12 ở mục 1b (Pass/Fail chưa đúng giá trị Passed/Failed, tiêu đề file P2 ghi nhầm "P1", P3 ghi Android 12 nhưng máy là 14, mã đơn để trống…). Ảnh PC không thấy tên trình duyệt (chỉ chụp vùng cửa sổ), nhưng URL thấy rõ.
- Kiểm tra: check_checklist chưa chạy (chưa gộp); lin--manual: 26 lượt.
- Nhắc push: vẫn còn 99a64dc và 78c13d8 chưa push nếu bạn chưa push.
===
Mình thấy còn nhiều file nó chưa commit mà nhỉ
Xong cái này hoặc đến phần mình làm tay thì mình sẽ dùng prompt tunnel nhé
```

**Output:**
````
Nhiều file chưa commit là **đúng, và nên giữ như vậy**. Claude Code dừng lại vì có lỗi chặn. Riêng **B5**: ảnh `P1_SV-02-3/4` lộ Gmail cá nhân và danh sách tài khoản đã lưu. Nếu commit rồi push, những ảnh đó nằm vĩnh viễn trong lịch sử git của repo công khai, kể cả khi sau này xoá file. Vì vậy **không commit ảnh nào** cho tới khi đã sửa xong. Phần kết quả dạng chữ thì commit được ngay để đánh dấu thời điểm chạy.

## Quyết định đề xuất

| Mã | Đề xuất | Lý do |
|---|---|---|
| **Q1** Cốc Cốc thay Chrome | **(a) Chạy lại 15 item tay của P1 trên Chrome.** Kết quả Cốc Cốc chỉ giữ làm lượt phụ, không tính | Đề yêu cầu Chrome. Đằng nào ảnh P1 cũng phải chụp lại (B3, B5, thiếu tên trình duyệt) |
| **Q2** CL-64 N/A không có giả định | **(b)** Chạy lại với ô SĐT bỏ trống. Vẫn bị từ chối thì ghi **Blocked bởi #111** | Theo luật: case bị lỗi khác chặn thì ghi Blocked kèm case gốc |
| **V1** Lệch auto ↔ tay (L1–L8) | **Lấy kết quả trên trình duyệt thật**, ghi nguyên nhân lệch (ví dụ CL-08: Playwright đặt locale vi-VN) | Đã chốt ở E2: verdict chính thức là lượt chạy trên trình duyệt thật |
| **Ảnh Task 3** thiếu tên trình duyệt | **Chụp toàn màn hình** (`Win + PrtScn`). Sticky Notes thêm dòng `Chrome 157 · Windows 11` / `Firefox 159 · Windows 11`; P3 thêm `Chrome 156 · Android 14 · POCO F5` | Đề bắt ảnh phải thấy trình duyệt/OS/thiết bị |

**Cách tránh lặp lại B5:** tạo một **hồ sơ Chrome mới** tên "HW03" và chỉ lưu đúng tài khoản `test@eshop.com`. Khi chạy SV-02, danh sách autofill sẽ chỉ hiện tài khoản test.

## Lệnh cho Claude Code

```
HW03[T1] 4/6 – xử lý run_check (chưa gộp):
1. Chuyển toàn bộ ảnh evidence/P1–P3 hiện có → HW03/checklist/evidence_raw/ (thêm vào .gitignore). KHÔNG commit ảnh nào (B5 lộ Gmail).
2. runs/*_manual_*: chỉ chuẩn hoá giá trị (Pass→Passed, Fail→Failed) và metadata theo R-list (tiêu đề file P2, Android 14); không sửa Notes. Commit "HW03[T1] 4/6a1: SV chạy tay – kết quả chữ (bản đầu)", message ghi "AI chuẩn hoá giá trị/metadata theo yêu cầu SV".
3. report_plan mục e: Q1=a (chạy lại 15 item tay P1 trên Chrome, hồ sơ mới "HW03"; lượt Cốc Cốc giữ làm lượt phụ, không tính, không nộp ảnh); Q2=b (CL-64 chạy lại với SĐT trống; vẫn bị từ chối → Blocked bởi #111); V1 (lệch auto↔tay → lấy trình duyệt thật, ghi nguyên nhân); ảnh Task 3 = toàn màn hình + overlay thêm dòng trình duyệt/OS/thiết bị.
4. HW03/checklist/RUN_retake.md: checklist việc tôi phải chạy/chụp lại, nhóm theo nền tảng (P1 Chrome 15 item; ảnh Task 3 P1/P2 toàn màn hình mỗi màn; M5 ×3; P3: 25 ảnh cần thêm overlay – liệt kê tên; P3 CL-52 chụp lại; CL-64 ×3; xem lại CL-08/09 P1 (R9, R11)). Tên ảnh đích P<n>_<id>_<k>.
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

## Thứ tự làm

1. **Ngay bây giờ:** dán lệnh trên, rồi dán luôn **lệnh tunnel**. Lệnh tunnel không phụ thuộc phần chụp lại; chạy sớm thì có thời gian sửa nếu lỗi, trước khi bạn bè vào tối nay.
2. **Lúc ở trường:** thêm overlay cho 25 ảnh P3 bằng trình sửa ảnh của Thư viện trên điện thoại (Sửa → Văn bản). Việc này chỉ cần điện thoại.
3. **Về nhà, trước các phiên usability:** làm theo `RUN_retake.md` (P1 trên Chrome, ảnh toàn màn hình, M5, CL-52, CL-64), khoảng 45–60 phút. Sau đó Claude Code chạy tiếp bước 2–4 của lệnh 4/6 cũ: nén ảnh, gộp kết quả, Excel, danh sách Failed.

Nhớ **push** các commit đang chờ (`99a64dc`, `78c13d8` và các commit mới).
````

**Xử lý:** [...]

---

## #69 | 02:23 10/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
Q1. Không, tôi không dùng Chrome, và tôi hết dung lượng, không có nhu cầu tải Chrome. Nên tôi sẽ giữ Cốc Cốc.
Q2. 
Task 3 chạy điện thoại thì sao mà mở thêm task khác được? Chẳng lẽ viết lên paint lên ảnh sao?
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #70 | 02:23 10/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
[Request interrupted by user]
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #71 | 02:24 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Q1. Không, tôi không dùng Chrome, và tôi hết dung lượng, không có nhu cầu tải Chrome. Nên tôi sẽ giữ Cốc Cốc.
Q2. a
Task 3 chạy điện thoại thì sao mà mở thêm task khác được? Chẳng lẽ viết lên paint lên ảnh sao?
```

**Output:**
````
## Q1: giữ Cốc Cốc

Được, đây là lựa chọn của bạn. Mình chỉ nhắc rủi ro một lần: đề liệt kê Chrome, nên TA có thể trừ điểm. Có hai điểm giúp giảm rủi ro này:
- P3 là **Chrome Android**, nên họ Chrome vẫn được kiểm.
- Cốc Cốc là trình duyệt phổ biến ở Việt Nam, đáng kiểm với người dùng Việt.

Report ghi trung thực:
- **P1 chính thức = Cốc Cốc 160 trên Windows 11** (cùng engine Chromium với Chrome).
- Lượt tự động P1 chạy trên Chrome 157 qua Playwright, chỉ dùng làm tham chiếu.
- Ghi vào mục **lệch so với kế hoạch**.

## Q2 = a

CL-64 ghi **Blocked**, nguyên nhân là issue #111 (SĐT 10 số bị từ chối).

## Overlay trên điện thoại

Ảnh **mới** dùng cách giống Sticky Notes trên PC: **cửa sổ nổi** của HyperOS. Mở app Ghi chú dạng cửa sổ nổi đè lên Chrome, rồi chụp màn hình. Ảnh sẽ có cả trang web lẫn ghi chú.
1. Mở Ghi chú, gõ `23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn · Chrome 156 · Android 14 · POCO F5`.
2. Vuốt lên rồi giữ để vào màn **Đa nhiệm** → nhấn giữ thẻ Ghi chú → chọn **Cửa sổ nổi**. Tuỳ bản HyperOS, nút này có thể nằm trong menu khi nhấn giữ.
3. Thu nhỏ cửa sổ, kéo vào góc không che vùng cần chụp → mở Chrome → chụp.

Với **25 ảnh đã chụp**: đúng, thêm chữ bằng **trình sửa ảnh trong Thư viện** (Sửa → Văn bản/Đánh dấu). Đây là cách O1 đã chốt cho điện thoại, và làm lại 25 trạng thái thì không đáng. Report ghi rõ hai cách: ảnh chụp trước thêm chữ sau khi chụp, ảnh chụp sau dùng cửa sổ nổi.

**B5:** không cần chụp lại. Dùng Snipping Tool/Paint vẽ ô đen che Gmail và các tài khoản khác, chỉ để lại tài khoản test. Đây là che thông tin, ghi vào AI-05.

## Lệnh cho Claude Code (thay lệnh trước)

```
HW03[T1] 4/6 – xử lý run_check (chưa gộp):
1. Chuyển toàn bộ ảnh evidence/P1–P3 → HW03/checklist/evidence_raw/ (thêm .gitignore). KHÔNG commit ảnh nào.
2. runs/*_manual_*: chỉ chuẩn hoá giá trị (Pass→Passed, Fail→Failed) và metadata theo R-list (tiêu đề file P2, Android 14); không sửa Notes. Commit "HW03[T1] 4/6a1: SV chạy tay – kết quả chữ (bản đầu)", message ghi "AI chuẩn hoá giá trị/metadata theo yêu cầu SV".
3. report_plan mục e: Q1 – P1 chính thức = Cốc Cốc 160/Windows 11 (Chromium; SV không dùng Chrome, máy hết dung lượng); lượt auto P1 = Chrome 157 Playwright, chỉ tham chiếu; ghi vào "lệch so với kế hoạch". Q2=a – CL-64 Blocked bởi #111. V1 – lệch auto↔tay → lấy trình duyệt thật, ghi nguyên nhân. Ảnh Task 3: PC chụp toàn màn hình, overlay thêm dòng trình duyệt/OS; P3: ảnh cũ thêm chữ bằng trình sửa ảnh Thư viện, ảnh mới dùng cửa sổ nổi Ghi chú. B5: che bằng ô đen (khai AI-05). Sửa environment.md + RUN/gen_run.py theo P1 = Cốc Cốc.
4. HW03/checklist/RUN_retake.md: việc tôi phải làm, nhóm theo nền tảng: P1/P2 ảnh Task 3 toàn màn hình mỗi màn; M5 ×3; sửa nhãn ảnh B3, tráo B4; P3 CL-52 chụp lại; P3 25 ảnh cần thêm chữ (liệt kê tên); che B5; xem lại CL-08/09 P1 (R9, R11).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

Sau đó dán **lệnh tunnel**. Bước 1 của lệnh tunnel tạo nhánh SUT riêng, nên trước khi chụp lại ảnh nhớ chạy `tools\sut_main.ps1` để quay về code gốc.
````

**Xử lý:** [...]

---

## #72 | 02:39 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Mình chưa sử dụng lệnh trên nhé.
Mình đã che đi thông tin ở P1. Và overlay thêm thông tin của mình ở các P3 chưa có: "23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn"
Và mình không thêm bất kì thông tin nào khác nhé. Mình sẽ không nói thêm. Giờ giúp mình sửa prompt cho phù hợp nhé
```

**Output:**
````
Đã ghi nhận: B5 bạn đã che xong, B1 đã thêm overlay `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn`, và overlay chỉ gồm đúng 3 thông tin này. Lệnh đã sửa theo:

```
HW03[T1] 4/6 – xử lý run_check (chưa gộp):
1. Kiểm lại ảnh evidence/P1–P3 (xem từng ảnh, chỉ đọc): B1 – mọi ảnh P3 có overlay "23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn"; B5 – P1_SV-02-3/4 không còn lộ Gmail/tài khoản khác. Liệt kê ảnh còn lỗi cùng B2 (thiếu M5), B3 (nhãn ảnh sai), B4 (CL-52/CL-64 tráo; P3_CL-52_1 sai màn).
2. Ảnh đạt → nén + đổi tên P<n>_<id>_<k> như HW02D (bản gốc → evidence_raw/, thêm .gitignore). Ảnh còn lỗi hoặc còn lộ thông tin → để evidence_raw/, KHÔNG commit.
3. runs/*_manual_*: chỉ chuẩn hoá giá trị (Pass→Passed, Fail→Failed) và metadata theo R-list (tiêu đề file P2, Android 14); không sửa Notes.
4. report_plan mục e: Q1 – P1 chính thức = Cốc Cốc 160/Windows 11 (Chromium; SV không dùng Chrome), lượt auto P1 = Chrome 157 Playwright chỉ tham chiếu, ghi vào "lệch so với kế hoạch"; Q2=a – CL-64 Blocked bởi #111; V1 – lệch auto↔tay lấy trình duyệt thật, ghi nguyên nhân; overlay = "23120255 - Lê Tấn Hiệp - email" (P1/P2 Sticky Notes; P3 thêm chữ bằng trình sửa ảnh); B5 che bằng ô đen (khai AI-05). Sửa environment.md + gen_run.py theo P1 = Cốc Cốc.
5. Commit "HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt" (message ghi "AI chuẩn hoá giá trị/metadata, nén/đổi tên ảnh theo yêu cầu SV").
6. HW03/checklist/RUN_retake.md: chỉ những ảnh/item còn phải làm (liệt kê tên đích).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

Xong lệnh này thì dán **lệnh tunnel**.
````

**Xử lý:** [...]

---

## #73 | 02:40 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 4/6 – xử lý run_check (chưa gộp):
1. Kiểm lại ảnh evidence/P1–P3 (xem từng ảnh, chỉ đọc): B1 – mọi ảnh P3 có overlay "23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn"; B5 – P1_SV-02-3/4 không còn lộ Gmail/tài khoản khác. Liệt kê ảnh còn lỗi cùng B2 (thiếu M5), B3 (nhãn ảnh sai), B4 (CL-52/CL-64 tráo; P3_CL-52_1 sai màn).
2. Ảnh đạt → nén + đổi tên P<n>_<id>_<k> như HW02D (bản gốc → evidence_raw/, thêm .gitignore). Ảnh còn lỗi hoặc còn lộ thông tin → để evidence_raw/, KHÔNG commit.
3. runs/*_manual_*: chỉ chuẩn hoá giá trị (Pass→Passed, Fail→Failed) và metadata theo R-list (tiêu đề file P2, Android 14); không sửa Notes.
4. report_plan mục e: Q1 – P1 chính thức = Cốc Cốc 160/Windows 11 (Chromium; SV không dùng Chrome), lượt auto P1 = Chrome 157 Playwright chỉ tham chiếu, ghi vào "lệch so với kế hoạch"; Q2=a – CL-64 Blocked bởi #111; V1 – lệch auto↔tay lấy trình duyệt thật, ghi nguyên nhân; overlay = "23120255 - Lê Tấn Hiệp - email" (P1/P2 Sticky Notes; P3 thêm chữ bằng trình sửa ảnh); B5 che bằng ô đen (khai AI-05). Sửa environment.md + gen_run.py theo P1 = Cốc Cốc.
5. Commit "HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt" (message ghi "AI chuẩn hoá giá trị/metadata, nén/đổi tên ảnh theo yêu cầu SV").
6. HW03/checklist/RUN_retake.md: chỉ những ảnh/item còn phải làm (liệt kê tên đích).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

**Output:**
```
Ảnh P3 (trừ M1–M4) và P1_SV-02-3/4 vừa được sửa. Xem lại.

Kết quả kiểm lại: P3 CL/SV có overlay, nhưng 5 ảnh P3 M1–M4 vẫn chưa có. B5 đã che. B2/B3/B4 chưa sửa. Xem `compress_manual.py`.

Kiểm overlay còn đọc được sau nén.

Ảnh nén vẫn đọc rõ chữ. Bước 3: chuẩn hoá runs (chỉ cột status + metadata).

Bước 4: report_plan, environment.md, gen_run.py.

Bước 6: viết `RUN_retake.md`.
```
*File AI ghi/gửi trong lượt này:* `RUN_retake.md`

**Xử lý:** [...]

---

## #74 | 02:46 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: HW03[T1] 4/6a1. Em kiểm lại ảnh, nén ảnh đạt, chuẩn hoá cột status trong runs/*_manual_* (Notes giữ nguyên), cập nhật report_plan mục e (Q1, Q2=a, V1, O2, B5), sửa environment.md và gen_run.py theo P1 = Cốc Cốc 160.
- File đã tạo/sửa: evidence/P1–P3 (ảnh đạt, nén từ 10,51 MB xuống 5,83 MB), runs/ (3 file tay + file auto), run_check.md, RUN_retake.md, tools/compress_hw03.py, .gitignore (thêm evidence_raw/), report_plan.md, environment.md, gen_run.py, RUN.md, checklist.json/.md, prompt log 27 lượt.
- Kết quả kiểm tra: check_checklist 0 lỗi. Đã chạy on_stop.py --manual. Đã xác nhận evidence_raw/ bị ignore.
- Commit: 107b67f HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt
- Còn lỗi (chưa commit, đang ở evidence_raw/):
  - B1: 5 ảnh P3_M* chưa có overlay.
  - B2: chưa có M5 trên cả 3 nền tảng.
  - B3: 5 ảnh M trên P1/P2 gắn nhầm nhãn.
  - B4: 3 ảnh CL-52/CL-64 bị tráo hoặc sai màn hình.
  - B5 đạt: ảnh P1_SV-02_3 và _4 đã che xong.
  - Tên đích của từng ảnh ghi trong HW03/checklist/RUN_retake.md.
- Cần quyết định: R-M5 – M5 chụp mới, hay dùng lại ảnh M3/M4 vì đã thấy navbar? Mục 2 của RUN_retake.md cần SV xác nhận rồi em mới đổi tên ảnh.
===
đã push
```

**Output:**
````
Bạn đã push. Phần còn lại hầu hết Claude Code làm được, chỉ còn 2 việc tay.

## R-M5: dùng lại ảnh M3/M4

Không cần chụp mới. Quy tắc "mỗi màn × nền tảng 1 ảnh" là do mình đặt ra (Z1), không phải yêu cầu của đề. Navbar là thành phần xuất hiện trên mọi trang, nên ảnh M3/M4 dùng được, với điều kiện ảnh đó **thấy rõ toàn bộ navbar ở trạng thái đã đăng nhập** (tên người dùng, Đăng xuất, Giỏ hàng). Report chỉ cần trỏ tới ảnh đó, **không chép thành file trùng**. Item navbar nào Failed thì đã có ảnh riêng.

## Việc tay còn lại

1. **B1:** thêm overlay cho 5 ảnh `P3_M*`, cách giống các ảnh trước.
2. **B4:** chụp lại `P3_CL-52` (màn hình bị khoá đăng nhập). Do lỗi đếm +2, chỉ cần nhập sai 2 lần là bị khoá.

Xong thì chép ảnh vào `evidence/` rồi bảo Claude Code "nén + đổi tên ảnh retake".

## Lệnh cho Claude Code (chạy được ngay)

```
HW03[T1] 4/6b:
1. R-M5: dùng lại ảnh M3/M4 nếu thấy đủ navbar đã đăng nhập (tên, Đăng xuất, Giỏ hàng) → ghi tham chiếu trong RUN_retake/report, không chép file trùng; ảnh nào không đủ → báo. B3, B4 (phần tráo tên): đổi tên theo tên đích trong RUN_retake.md (SV đồng ý), nén, commit "HW03[T1] 4/6a2: sửa nhãn ảnh B3/B4, M5 dùng ảnh M3/M4".
2. merge_platform.py: gộp auto + manual vào checklist.json theo V1 (lệch → kết quả trình duyệt thật + ghi nguyên nhân lệch). build_excel.py → excel/23120255_HW03_Checklist.xlsx (recalc, 0 lỗi công thức). HW03/bugs/failed_list.md: Failed (item × nền tảng), kiểm trùng issues.json + HW02 BUG-xx của tôi → cột "issue trùng"/"MỚI".
3. D1=a: chèn khung marker REPORT:U1 (sessions, summary) và REPORT:T1 (checklist summary, cross-platform) vào report; điền bảng T1 từ checklist.json.
Commit "HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed". on_stop.py --manual. Báo cáo ≤ 12 dòng: Passed/Failed/N/A/Blocked theo nền tảng; số Failed MỚI / trùng. Nhắc tôi push.
```

Sau đó dán **lệnh tunnel**. Báo cáo 4/6b về là bạn có danh sách Failed mới để tự viết bug.
````

**Xử lý:** [...]

---

## #75 | 02:47 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 4/6b:
1. R-M5: dùng lại ảnh M3/M4 nếu thấy đủ navbar đã đăng nhập (tên, Đăng xuất, Giỏ hàng) → ghi tham chiếu trong RUN_retake/report, không chép file trùng; ảnh nào không đủ → báo. B3, B4 (phần tráo tên): đổi tên theo tên đích trong RUN_retake.md (SV đồng ý), nén, commit "HW03[T1] 4/6a2: sửa nhãn ảnh B3/B4, M5 dùng ảnh M3/M4".
2. merge_platform.py: gộp auto + manual vào checklist.json theo V1 (lệch → kết quả trình duyệt thật + ghi nguyên nhân lệch). build_excel.py → excel/23120255_HW03_Checklist.xlsx (recalc, 0 lỗi công thức). HW03/bugs/failed_list.md: Failed (item × nền tảng), kiểm trùng issues.json + HW02 BUG-xx của tôi → cột "issue trùng"/"MỚI".
3. D1=a: chèn khung marker REPORT:U1 (sessions, summary) và REPORT:T1 (checklist summary, cross-platform) vào report; điền bảng T1 từ checklist.json.
Commit "HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed". on_stop.py --manual. Báo cáo ≤ 12 dòng: Passed/Failed/N/A/Blocked theo nền tảng; số Failed MỚI / trùng. Nhắc tôi push.
```

**Output:**
```
Step 1 first: check navbar in M3/M4 images.

Ảnh khớp. Cập nhật RUN_retake.md.

Step 2: merge. Read merge_platform.py.

Gộp kết quả: thấy đúng 8 chỗ lệch L1–L8 và auto Blocked CL-27/CL-48. Giờ viết script gộp.

Excel COM có sẵn → recalc + đếm lỗi công thức qua Excel.

Viết script PowerShell recalc có retry khi Excel báo bận.

Excel: 21 công thức, 0 lỗi, khớp JSON. Giờ làm failed_list — tìm issues.json và BUG HW02.

Step 3: report markers. Xem cấu trúc report.

Chèn marker vào report (giữ dòng 📝 của SV).

Phát hiện: P3 CL-30/CL-48 Failed do `TimeoutError` của harness, không phải do SUT. Rà toàn bộ ô auto Failed vì lỗi kỹ thuật.

Đã gộp kết quả, xuất Excel và lập danh sách Failed. Còn 2 ô P3 Failed chưa đáng tin vì Playwright bị Timeout, cần chạy lại (xem "Cần quyết định").

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: 4/6a2 (sửa nhãn ảnh B3/B4; M5 dùng lại `P1_M4_1`, `P2_M4_1`, `P3_M3_1`) + 4/6b (gộp kết quả, Excel, `failed_list`, marker trong report).
- File đã tạo/sửa:
  - `checklist.json`, `excel/23120255_HW03_Checklist.xlsx`, `bugs/failed_list.md`, `bugs/issues.json`, `runs/*_manual_*.csv`
  - report (đã chèn marker T1 + U1, đã điền 2 bảng T1), `RUN_retake.md`
  - script mới: `tools/merge_hw03.py`, `failed_list_hw03.py`, `report_t1_hw03.py`
- Kết quả theo nền tảng (Passed/Failed/N/A/Blocked): **P1 27/44/0/3 · P2 24/47/0/3 · P3 22/46/4/2**. Có 8 ô lệch auto↔tay (đúng L1–L8), đều lấy kết quả tay theo V1, nguyên nhân ghi trong cột `lech_auto_tay`.
- Failed: 49 item. Đối chiếu với issue nhóm và BUG HW02: **trùng 8**, **trùng một phần 5** (màn còn lại tính là mới), **MỚI 36**. Phân loại trùng do em làm theo tiêu đề issue, bạn cần xác nhận lại.
- Kiểm tra: check_checklist 0 lỗi; Excel mở bằng Excel thật: 21 công thức, 0 lỗi, số liệu khớp JSON; prompt log 28 lượt.
- Commit: `61858d4` 4/6a2 · `3ee3158` 4/6b
- Bất thường: P3 CL-30 và CL-48 Failed chỉ vì `TimeoutError` của Playwright, chưa có assertion nào fail (đã đánh dấu ⚠ trong `failed_list.md`). P2 CL-34 Failed chỉ trên Firefox Playwright (Họ Tên lưu thành ""), cần xem lại.
- Cần quyết định:
  - T-P3: chạy lại `npm run p3` cho CL-30/CL-48, hay bạn chạy tay 2 item này trên P3?
  - Q1-auto: 59 item auto của P1 đang lấy kết quả Chrome 157 vì Cốc Cốc chưa có lượt auto. Giữ như vậy và khai trong mục lệch kế hoạch, hay chạy lại auto bằng Cốc Cốc?
- Chưa xong: 5 ảnh `P3_M*` chưa có overlay (`RUN_retake.md` mục 1); R9/R11 (verdict CL-08/CL-09 trên P1) vẫn chờ bạn xem lại.

Bạn nhớ push nhé: `git push` (còn 2 commit chưa push).
```
*File AI ghi/gửi trong lượt này:* `RUN_retake.md`, `merge_hw03.py`, `recalc_xlsx.ps1`, `failed_list_hw03.py`, `report_t1_hw03.py`

**Xử lý:** [...]

---

## #76 | 03:01 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: 4/6a2 (sửa nhãn ảnh B3/B4; M5 dùng lại P1_M4_1, P2_M4_1, P3_M3_1) + 4/6b (gộp kết quả, Excel, failed_list, marker trong report).
- File đã tạo/sửa:
  - checklist.json, excel/23120255_HW03_Checklist.xlsx, bugs/failed_list.md, bugs/issues.json, runs/*_manual_*.csv
  - report (đã chèn marker T1 + U1, đã điền 2 bảng T1), RUN_retake.md
  - script mới: tools/merge_hw03.py, failed_list_hw03.py, report_t1_hw03.py
- Kết quả theo nền tảng (Passed/Failed/N/A/Blocked): P1 27/44/0/3 · P2 24/47/0/3 · P3 22/46/4/2. Có 8 ô lệch auto↔tay (đúng L1–L8), đều lấy kết quả tay theo V1, nguyên nhân ghi trong cột lech_auto_tay.
- Failed: 49 item. Đối chiếu với issue nhóm và BUG HW02: trùng 8, trùng một phần 5 (màn còn lại tính là mới), MỚI 36. Phân loại trùng do em làm theo tiêu đề issue, bạn cần xác nhận lại.
- Kiểm tra: check_checklist 0 lỗi; Excel mở bằng Excel thật: 21 công thức, 0 lỗi, số liệu khớp JSON; prompt log 28 lượt.
- Commit: 61858d4 4/6a2 · 3ee3158 4/6b
- Bất thường: P3 CL-30 và CL-48 Failed chỉ vì TimeoutError của Playwright, chưa có assertion nào fail (đã đánh dấu ⚠ trong failed_list.md). P2 CL-34 Failed chỉ trên Firefox Playwright (Họ Tên lưu thành ""), cần xem lại.
- Cần quyết định:
  - T-P3: chạy lại npm run p3 cho CL-30/CL-48, hay bạn chạy tay 2 item này trên P3?
  - Q1-auto: 59 item auto của P1 đang lấy kết quả Chrome 157 vì Cốc Cốc chưa có lượt auto. Giữ như vậy và khai trong mục lệch kế hoạch, hay chạy lại auto bằng Cốc Cốc?
- Chưa xong: 5 ảnh P3_M* chưa có overlay (RUN_retake.md mục 1); R9/R11 (verdict CL-08/CL-09 trên P1) vẫn chờ bạn xem lại.

Bạn nhớ push nhé: git push (còn 2 commit chưa push).
===
Oke, xem xem có thể dùng lệnh tunnel chưa nhé (mình sẽ không chạy lại đâu nhé)
```

**Output:**
````
## Lệnh tunnel: dùng được ngay

Lệnh tunnel không phụ thuộc phần checklist, nên dán nguyên lệnh ở lượt trước, không cần sửa. Hai lưu ý:
- Bước 2 sẽ hỏi trước khi cài **cloudflared**, file khoảng vài chục MB. Máy bạn đang thiếu dung lượng nên kiểm chỗ trống trước khi đồng ý.
- Lệnh tạo nhánh `usability-tunnel` trong SUT. Bạn không chạy lại checklist nữa, nên chỉ cần dùng `tools\sut_main.ps1` khi muốn quay về code gốc.

## Khi không chạy lại: xử lý trung thực các điểm còn treo

| Điểm | Xử lý |
|---|---|
| **T-P3** CL-30, CL-48 trên P3 | TimeoutError của Playwright là lỗi harness, chưa có assertion nào fail, nên **không được ghi Failed**. Ghi **Blocked (harness timeout)**, không lập bug |
| **P2 CL-34** chỉ fail trên Firefox Playwright | Không xác nhận được trên Firefox thật, nên **không lập bug** từ kết quả này. Giữ kết quả auto, ghi chú "chỉ Firefox Playwright, chưa xác nhận trên trình duyệt thật" |
| **Q1-auto** | Giữ kết quả Chrome 157, khai trong mục lệch kế hoạch |
| **B4** `P3_CL-52` sai màn | Không chụp lại thì CL-52 trên P3 **không có ảnh**. Giữ verdict, Notes ghi "thiếu ảnh". Item này vốn trùng #1–#3 nên không cần lập bug |
| **B1** 5 ảnh `P3_M*` thiếu overlay | Thêm chữ trong Thư viện, không cần chụp lại |
| **R9/R11** CL-08/09 trên P1 | Chỉ cần bạn xem lại ghi chú và ảnh đã có, rồi chốt verdict |

## Rủi ro lớn tiếp theo: 36 bug MỚI

Mỗi bug do bạn tự viết, khoảng 5 phút một bug, tức gần 3 giờ. Cách giảm hợp lệ: **một bug cho mỗi lỗi, không phải cho mỗi item**. Nhiều item Failed có thể cùng một nguyên nhân quan sát được (cùng phần tử, cùng hành vi, khác màn hình hay nền tảng). AI được phép dựng khung chỉ chứa dữ kiện; tiêu đề, mô tả, severity và priority để bạn viết.

**Lệnh dán sau lệnh tunnel:**
```
HW03[T1] 5/6a:
1. Quyết định (report_plan mục e + checklist.json): T-P3 – CL-30, CL-48 P3 = Blocked (Playwright timeout, không assertion fail), không lập bug; CL-34 P2 – giữ auto, ghi "chỉ Firefox Playwright, chưa xác nhận trên trình duyệt thật", loại khỏi danh sách lập bug; Q1-auto – giữ Chrome 157, khai lệch kế hoạch; CL-52 P3 – Notes "thiếu ảnh". Cập nhật Excel + failed_list + bảng T1 report.
2. bugs/bug_groups.md: gom Failed MỚI theo DỮ KIỆN giống nhau (cùng phần tử/cùng hành vi quan sát, khác màn/nền tảng) → nhóm G-xx kèm item, nền tảng, ảnh, expected (chép), actual (chép Notes/auto). Chỉ đề xuất nhóm, tôi xác nhận.
3. Mỗi nhóm 1 khung bugs/BUG-<số kế tiếp sau HW02>.md CHỈ dữ kiện: item, nền tảng, môi trường, bước tái hiện từ RUN/test, expected chép, actual chép, ảnh; để trống Tiêu đề / Mô tả / Severity / Priority / Nhận định (🔒 SV viết).
Commit "HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện)". on_stop.py --manual. Báo cáo ≤ 8 dòng: số nhóm, số khung. Nhắc tôi push.
```

Nhớ **push** 2 commit đang chờ. Bug viết lúc rảnh ở trường; tối nay dành cho Task 2.
````

**Xử lý:** [...]

---

## #77 | 03:03 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 5/6a:
1. Quyết định (report_plan mục e + checklist.json): T-P3 – CL-30, CL-48 P3 = Blocked (Playwright timeout, không assertion fail), không lập bug; CL-34 P2 – giữ auto, ghi "chỉ Firefox Playwright, chưa xác nhận trên trình duyệt thật", loại khỏi danh sách lập bug; Q1-auto – giữ Chrome 157, khai lệch kế hoạch; CL-52 P3 – Notes "thiếu ảnh". Cập nhật Excel + failed_list + bảng T1 report.
2. bugs/bug_groups.md: gom Failed MỚI theo DỮ KIỆN giống nhau (cùng phần tử/cùng hành vi quan sát, khác màn/nền tảng) → nhóm G-xx kèm item, nền tảng, ảnh, expected (chép), actual (chép Notes/auto). Chỉ đề xuất nhóm, tôi xác nhận.
3. Mỗi nhóm 1 khung bugs/BUG-<số kế tiếp sau HW02>.md CHỈ dữ kiện: item, nền tảng, môi trường, bước tái hiện từ RUN/test, expected chép, actual chép, ảnh; để trống Tiêu đề / Mô tả / Severity / Priority / Nhận định (🔒 SV viết).
Commit "HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện)". on_stop.py --manual. Báo cáo ≤ 8 dòng: số nhóm, số khung. Nhắc tôi push.
```

**Output:**
```
Bước 1: ghi quyết định vào `merge_hw03.py` dạng override, chạy lại thì không bị mất.

Quyết định đã áp, chạy lại vẫn giữ nguyên. Giờ ghi vào report_plan và cập nhật failed_list, Excel, report.

Giờ sửa failed_list để bỏ các ô `lap_bug: false`.

Bước 2: xuất dữ kiện các item MỚI để gom nhóm.

Viết script sinh `bug_groups.md` và các khung BUG.

Chuyển CL-01 sang TRÙNG rồi chạy.
```
*File AI ghi/gửi trong lượt này:* `bug_groups_hw03.py`

**Xử lý:** [...]

---

## #78 | 03:09 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Cho mình hỏi skill của prompt mà mình dùng trước prompt tunnel đã được sinh ra chưa, và nó ở đâu nhỉ?
===
response prompt trên mà mình sử dụng trước khi dùng prompt tunnel:
Báo cáo cho phiên thảo luận

- Nhiệm vụ: 5/6a – ghi quyết định treo (T-P3, CL-34, Q1-auto, CL-52 P3), gom nhóm dữ kiện, tạo khung bug. Kết quả theo nền tảng giờ là P1 27/44/0/3 · P2 24/47/0/3 · P3 22/44/4/4 (Passed/Failed/N/A/Blocked).
- File: report_plan.md (mục e, f), checklist.json/.md, Excel, failed_list.md, bảng T1 trong report, bugs/bug_groups.md, bugs/BUG-58…87.md, tools/bug_groups_hw03.py. Quyết định ghi trong tools/merge_hw03.py, chạy lại vẫn giữ.
- Kết quả: 30 nhóm (G-01…G-30) → 30 khung BUG-58…87, gom từ 37 item (33 mới + 4 trùng một phần). Failed: trùng 9 / trùng một phần 4 / mới 33; CL-34 bị loại khỏi lập bug. check_checklist 0 lỗi; Excel có 21 công thức, 0 lỗi.
- Khác lệnh: CL-01 chuyển thành trùng #9, vì notes cả 3 nền tảng chỉ nêu chuỗi tiếng Anh ở màn Đăng nhập. Các mục Tiêu đề/Mô tả/Steps/Severity/Priority/Nhận định để trống (🔒).
- Commit: 0679e25 HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện)
- Cần quyết định: bạn xác nhận cách chia 30 nhóm. Các nhóm em gộp nên xem kỹ: G-02 (title + lang), G-13 (CL-04 + CL-06), G-23 (CL-08 + CL-09); phương án là giữ gộp hoặc tách riêng.
===
đã push
```

**Output:**
````
## Skill ở đâu

Cả hai skill đã được tạo, nằm trong thư mục skill của Claude Code. **Thư mục nộp bài `HW03/skills/` hiện vẫn trống** (chỉ có `.gitkeep`).

| Skill | Đường dẫn | Commit tạo | Gồm |
|---|---|---|---|
| `gui-checklist-testing` (Task 1/3) | `.claude/skills/gui-checklist-testing/` | `a1df52c` (04/11), sửa thêm ở các bước sau | SKILL.md 7 bước, 5 script, `dom_probe.js`, các mẫu |
| `usability-evaluation` (Task 2) | `.claude/skills/usability-evaluation/` | `78c13d8` (10/11) | SKILL.md bước 0–6, 2 tài liệu tham khảo, 3 mẫu, 6 script (`sus_score.py`, `check_kit.py`…) |

Khi đóng gói, Claude Code sẽ chép 2 skill sang `HW03/skills/` để nộp, kèm link video.

Một điểm cần biết: một số script làm sau này nằm ở `tools/` (`merge_hw03.py`, `failed_list_hw03.py`, `bug_groups_hw03.py`…) chứ không nằm trong skill. Lúc đóng gói nên đưa các phần dùng lại được vào skill, để skill "dùng lại được cho màn/flow khác" đúng như đề yêu cầu.

## Xác nhận cách chia nhóm bug

Nguyên tắc: **mỗi lỗi một bug**. Hai item cùng một phần tử, cùng hành vi thì gộp. Khác thuộc tính hoặc khác yêu cầu thì tách, vì sửa cái này không làm cái kia hết lỗi.

| Nhóm | Gồm | Đề xuất | Lý do |
|---|---|---|---|
| G-02 | `title` "frontend-web" (CL-13) + `lang="en"` (CL-14) | **Tách** | Hai thuộc tính khác nhau, hai tiêu chí WCAG khác nhau (2.4.2 và 3.1.1). Sửa cái này không làm cái kia hết lỗi |
| G-13 | Nút "Đặt lại mật khẩu" xanh lá (CL-04) + nút chính/phụ giống nhau (CL-06) | **Xem lại.** Nếu CL-06 nói về chính nút đó thì giữ gộp; nếu CL-06 nói về cặp nút khác thì tách | Phụ thuộc phần tử nào bị lỗi |
| G-23 | Định dạng tiền (CL-08) + định dạng ngày (CL-09) | **Tách** | Hai trường khác nhau, hai quy tắc khác nhau (FR-21.3 và GA1) |

Tách theo cách trên thì từ 30 khung thành khoảng 32 bug, đều có lý do rõ ràng.

**Còn một việc kiểm trùng mà AI chưa làm hết.** Một số nhóm ghi "liên quan" tới issue số **#160–#170**: G-13 (#160), G-16 (#169), G-23 (#170), G-25 (#165), G-26 (#167). Các số này **lớn hơn 158**, tức là issue bạn cùng nhóm mới tạo cho HW03 sau lần lấy danh sách. Bạn mở từng issue xem có đúng cùng lỗi, cùng màn hình không:
- **Trùng** thì không lập bug, ghi "trùng #xxx".
- **Khác màn hình** thì vẫn lập, ghi "liên quan #xxx".

## Lệnh cho Claude Code

Điền phần G-13 và kết quả kiểm trùng trước khi dán:

```
HW03[T1] 5/6b: tách G-02 → CL-13, CL-14 riêng; tách G-23 → CL-08, CL-09 riêng; G-13 <giữ | tách>. Kết quả kiểm trùng issue mới của tôi: <#160: trùng/liên quan, #165: …, #167: …, #169: …, #170: …> → nhóm trùng bỏ khung, ghi "trùng #xxx" vào failed_list. Đánh lại số BUG liên tục, sinh lại khung (chỉ dữ kiện), cập nhật bug_groups.md. Commit "HW03[T1] 5/6b: SV chốt nhóm bug". on_stop.py --manual. Báo cáo ≤ 5 dòng. Nhắc tôi push.
```

Sau đó bạn viết các khung `BUG-xx.md` (🔒). Viết xong, mình kiểm dữ kiện: bước tái hiện, môi trường, ảnh có khớp với kết quả chạy không.
````

**Xử lý:** [...]

---

## #79 | 03:10 10/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 5/6b: tách G-02 → CL-13, CL-14 riêng; tách G-23 → CL-08, CL-09 riêng; G-13 <giữ | tách>. Kết quả kiểm trùng issue mới của tôi: <#160: trùng/liên quan, #165: …, #167: …, #169: …, #170: …> → nhóm trùng bỏ khung, ghi "trùng #xxx" vào failed_list. Đánh lại số BUG liên tục, sinh lại khung (chỉ dữ kiện), cập nhật bug_groups.md. Commit "HW03[T1] 5/6b: SV chốt nhóm bug". on_stop.py --manual. Báo cáo ≤ 5 dòng. Nhắc tôi push.
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #80 | 03:12 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
G-13 gộp; #160 trùng, #165 trùng #167 trùng #169 trùng #170 trùng
```

**Output:**
```
Khung chưa ai sửa → xoá được và sinh lại. Cập nhật DUP + nhóm.

Đã chốt nhóm bug theo quyết định của bạn: còn 28 nhóm, sinh lại khung BUG-58…85 (chỉ dữ kiện).

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: 5/6b – tách G-02 cũ thành CL-13 và CL-14; tách G-23 cũ, trong đó CL-08 trùng #170 nên chỉ còn nhóm CL-09; bỏ khung các item trùng (CL-04 #160, CL-08 #170, CL-40 #169, CL-60 #165, CL-62 #167). G-13 bạn chọn gộp, nhưng vì CL-04 đã trùng #160 nên nhóm này chỉ còn CL-06.
- File: `bugs/failed_list.md` (trùng 14 / trùng một phần 4 / mới 28), `bugs/bug_groups.md` (28 nhóm G-01…G-28), khung `bugs/BUG-58…85.md` sinh lại, `report_plan.md` mục e thêm dòng G-SV.
- Commit: `3ab505e` HW03[T1] 5/6b: SV chốt nhóm bug
- Cần quyết định: không có. Bước kế tiếp là bạn viết Tiêu đề/Mô tả/Steps/Severity/Priority cho 28 khung (🔒).

Bạn nhớ push nhé: `git push` (còn 1 commit chưa push là `3ab505e`).
```

**Xử lý:** [...]

---

## #81 | 03:13 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: 5/6b – tách G-02 cũ thành CL-13 và CL-14; tách G-23 cũ, trong đó CL-08 trùng #170 nên chỉ còn nhóm CL-09; bỏ khung các item trùng (CL-04 #160, CL-08 #170, CL-40 #169, CL-60 #165, CL-62 #167). G-13 bạn chọn gộp, nhưng vì CL-04 đã trùng #160 nên nhóm này chỉ còn CL-06.
- File: bugs/failed_list.md (trùng 14 / trùng một phần 4 / mới 28), bugs/bug_groups.md (28 nhóm G-01…G-28), khung bugs/BUG-58…85.md sinh lại, report_plan.md mục e thêm dòng G-SV.
- Commit: 3ab505e HW03[T1] 5/6b: SV chốt nhóm bug
- Cần quyết định: không có. Bước kế tiếp là bạn viết Tiêu đề/Mô tả/Steps/Severity/Priority cho 28 khung (🔒).
===
đã push
===
Vậy giờ dùng prompt tunnel nhé
```

**Output:**
````
Đúng, giờ là lúc chạy lệnh tunnel. Mình chép lại, chỉ thêm bước kiểm dung lượng trống trước khi cài:

```
HW03[T2] – môi trường usability từ xa (commit trong repo bài: "HW03[T2] 2b/10: môi trường usability từ xa (tunnel)"):
1. Repo ..\eshop-sut: tạo nhánh local usability-tunnel (KHÔNG push). frontend-web: thay "http://localhost:3000" → đường dẫn tương đối; vite.config: proxy /api (và /uploads nếu có) → http://localhost:3000, server.allowedHosts cho .trycloudflare.com. Commit trên nhánh đó. In git diff --stat.
2. In dung lượng trống ổ C/D. Cài cloudflared (winget hoặc bản exe vào D:\Tools; hỏi tôi trước khi cài). tools/usability_session.ps1: restart_backend.ps1 → vite (nhánh tunnel, --host 127.0.0.1) → cloudflared tunnel --url http://localhost:5173 → in link; Ctrl+C tắt tunnel. Kèm tools/sut_main.ps1 để quay SUT về nhánh main.
3. Chạy usability_session.ps1, in link, DỪNG chờ tôi mở link trên điện thoại dùng 4G: đăng nhập test@eshop.com, tìm SP, thêm giỏ, áp VIP100, đặt hàng, thấy đơn trong Hồ sơ.
4. usability/plan.md: hình thức = remote synchronous moderated (Google Meet, người tham gia chia sẻ màn hình, think-aloud; quay bằng Game Bar/OBS khi được đồng ý); khác biệt môi trường so với checklist (trình duyệt của người tham gia, qua Internet, nhánh usability-tunnel chỉ đổi URL API). participant_kit.md: thêm dòng "dùng máy tính, mở link người hướng dẫn gửi". Chạy check_kit.py của skill usability-evaluation.
on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push repo bài.
```

**Thử ở bước 3:** tắt Wi-Fi trên điện thoại, chỉ dùng 4G, để giống bạn bè ở xa. Đi hết luồng U1 mà thấy danh sách sản phẩm, áp được VIP100 và đơn hiện trong Hồ sơ là đạt. Nếu web mở được nhưng không có sản phẩm, nghĩa là proxy `/api` chưa chạy. Báo lỗi nguyên văn cho Claude Code sửa.

Tunnel chạy được thì việc chuẩn bị cho tối nay còn 3 việc:
1. **Đọc `participant_kit.md`**, vì đây là thứ bạn gửi cho bạn bè.
2. **Hẹn giờ cụ thể** với 8 người.
3. Mở thử **Game Bar** (`Win + Alt + R`) quay 10 giây cửa sổ Meet, xem có thu được cả tiếng không.
````

**Xử lý:** [...]

---

## #82 | 03:14 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T2] – môi trường usability từ xa (commit trong repo bài: "HW03[T2] 2b/10: môi trường usability từ xa (tunnel)"):
1. Repo ..\eshop-sut: tạo nhánh local usability-tunnel (KHÔNG push). frontend-web: thay "http://localhost:3000" → đường dẫn tương đối; vite.config: proxy /api (và /uploads nếu có) → http://localhost:3000, server.allowedHosts cho .trycloudflare.com. Commit trên nhánh đó. In git diff --stat.
2. In dung lượng trống ổ C/D. Cài cloudflared (winget hoặc bản exe vào D:\Tools; hỏi tôi trước khi cài). tools/usability_session.ps1: restart_backend.ps1 → vite (nhánh tunnel, --host 127.0.0.1) → cloudflared tunnel --url http://localhost:5173 → in link; Ctrl+C tắt tunnel. Kèm tools/sut_main.ps1 để quay SUT về nhánh main.
3. Chạy usability_session.ps1, in link, DỪNG chờ tôi mở link trên điện thoại dùng 4G: đăng nhập test@eshop.com, tìm SP, thêm giỏ, áp VIP100, đặt hàng, thấy đơn trong Hồ sơ.
4. usability/plan.md: hình thức = remote synchronous moderated (Google Meet, người tham gia chia sẻ màn hình, think-aloud; quay bằng Game Bar/OBS khi được đồng ý); khác biệt môi trường so với checklist (trình duyệt của người tham gia, qua Internet, nhánh usability-tunnel chỉ đổi URL API). participant_kit.md: thêm dòng "dùng máy tính, mở link người hướng dẫn gửi". Chạy check_kit.py của skill usability-evaluation.
on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push repo bài.
```

**Output:**
```
Bước 1: xem SUT.

Ổ đĩa: C trống 146G, D trống 83G. Chưa có cloudflared. Em viết script trước, hỏi cài sau.

Chữ ký hợp lệ (Cloudflare, Inc.). Chạy phiên ở chế độ nền.

Windows PowerShell 5.1 đọc file UTF-8 không BOM sai mã. Thêm BOM như `restart_backend.ps1`.

Check parse lỗi, chạy lại luôn.

`param` phải đứng đầu file. Tắt lượt đang chạy, sửa lại.

Kiểm tra link từ phía Internet (qua tunnel) trước khi bạn mở bằng điện thoại.
```
*File AI ghi/gửi trong lượt này:* `usability_session.ps1`, `sut_main.ps1`

**Xử lý:** [...]

---

## #83 | 03:14 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Trong lúc đang chạy prompt trên thì tôi up 2 skill kia lên cho bạn nhé
```

**Output:**
````
Không cần upload. Bạn đã push nên mình đọc thẳng 2 file `SKILL.md` từ repo được. Nhận xét ngắn:

## `usability-evaluation`: dùng được

Cấu trúc tốt: đủ 7 bước, giới hạn AI rõ ràng, script chặn dữ liệu cá nhân và từ chối điền thay SUS. Chỉ thiếu một điểm: **bước 0 chưa có lựa chọn "remote synchronous"** (Meet + tunnel) như bạn sắp làm. Nên thêm vào phần Method/Environment của kế hoạch, kèm ghi chú về việc reset dữ liệu và quay phiên từ xa.

## `gui-checklist-testing`: lệch so với cách bạn thực sự làm

Skill được viết lúc 18:17 ngày 04/11, **trước khi** quyết định dùng Playwright (E2=b). Nếu nộp nguyên như vậy, skill sẽ không khớp với Audit và video demo:

| Chỗ lệch | Trong skill | Thực tế |
|---|---|---|
| Quy tắc 9 | "AI chỉ chạy `dom_probe.js`" | Playwright tự chạy 71 item trên P1/P2/P3 |
| Bước 3–4 | Chỉ chạy tay, file CSV | Lượt auto (`auto_status`) + lượt tay, gộp theo **V1** (lệch thì lấy trình duyệt thật) |
| Verdict | Không có loại lỗi harness | Timeout của Playwright → Blocked, không lập bug (T-P3) |
| Ảnh | "Chỉ chụp item Failed" | Thêm ảnh Task 3 cho mỗi màn × nền tảng, overlay MSSV · tên · email (Z1, O2) |
| Bước 6 | Gom nhóm, kiểm trùng bằng `gh` | Thực tế dùng `failed_list` + `bug_groups` + khung bug chỉ có dữ kiện, nhưng các script đó nằm ở `tools/*_hw03.py`, **không nằm trong skill** |
| Bước 1 | Không nói phải đọc hết slide | Gap analysis cho thấy AI chỉ đọc một phần slide, bỏ sót "Double-submit". Nên thêm quy tắc "đọc toàn bộ phần nguồn checklist trong slide trước khi sinh item". Đây là bài học rút ra từ G9.3, hợp lệ để đưa vào skill |

## Khi nào sửa

**Không sửa bây giờ.** Để tới lúc đóng gói (đêm T3), sau khi Task 2 xong. Lúc đó dán:

```
HW03 – hoàn thiện 2 skill trước khi nộp (commit "HW03: cập nhật skill theo cách làm thực tế"):
1. gui-checklist-testing: thêm chế độ Playwright (bước 3: phân loại che_do auto/manual/mixed, oracle khoá sha1; bước 4: lượt auto → auto_status, gộp auto+tay theo V1, Blocked khi lỗi harness); quy tắc ảnh Task 3 + overlay; bước 1 thêm "đọc toàn bộ phần nguồn checklist trong slide"; đưa tools/merge_hw03.py, failed_list_hw03.py, bug_groups_hw03.py vào scripts/ dạng tổng quát (không gắn HW03), cập nhật bảng Script.
2. usability-evaluation: bước 0 thêm lựa chọn remote synchronous (Meet, chia sẻ màn hình, tunnel, reset dữ liệu mỗi phiên, quay khi được đồng ý).
3. Chạy lại script đã chuyển trên dữ liệu HW03, kết quả phải giống hệt (diff). Chép 2 skill → HW03/skills/ (bản nộp).
on_stop.py --manual. Báo cáo ≤ 8 dòng.
```

Ngay bây giờ, ưu tiên vẫn là: tunnel chạy được → đọc `participant_kit.md` → hẹn giờ 8 người.
````

**Xử lý:** [...]

---

## #84 | 03:18 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Tunnel đã chạy. Em kiểm tra từ PC qua Internet: trang trả HTTP 200, API qua tunnel trả đủ 5 sản phẩm.

Link: https://attractive-radio-scripting-mobiles.trycloudflare.com

Em dừng ở bước 3 theo lệnh. Bạn tắt Wi-Fi, mở link bằng 4G rồi làm hết luồng:

1. Đăng nhập test@eshop.com / Test1234!
2. Tìm sản phẩm, thêm vào giỏ.
3. Thanh toán, áp mã VIP100, đặt hàng.
4. Vào Hồ sơ, xem đơn vừa đặt có hiện không.

Xong thì báo em kết quả (được, hoặc lỗi ở bước nào kèm thông báo). Em sẽ làm tiếp bước 4 (plan.md, participant_kit.md, check_kit.py), rồi commit HW03[T2] 2b/10: môi trường usability từ xa (tunnel) trong repo bài.

Đã xong trước đó:
- Nhánh usability-tunnel ở ../eshop-sut, commit e33212d (local, không push): 8 file, +21/−13.
- Cloudflared 2026.10.7 đã cài vào D:\Tools\cloudflared\, chữ ký hợp lệ của Cloudflare.
- Hai script tools/usability_session.ps1 và tools/sut_main.ps1.
- Ổ C còn trống 146G, ổ D còn 83G.

Link sẽ đổi mỗi lần chạy lại script. Tunnel còn chạy cho tới khi tắt task nền.
===
Giờ đưa link cho các bạn chạy là xong nhỉ
```

**Output:**
```
**Chưa phải chỉ gửi link là xong.** Đề yêu cầu phiên **moderated**: bạn phải có mặt quan sát từng người. Nếu chỉ gửi link cho họ tự làm, đó là unmoderated, sai yêu cầu, và Task 2 có thể mất phần lớn điểm. Còn 3 việc phải làm trước.

## 1. Tự thử bằng 4G (Claude Code đang chờ)

Tắt Wi-Fi, mở link, đi hết 4 bước, rồi báo kết quả cho Claude Code để nó làm tiếp bước 4 và commit.

## 2. Pilot với 1 người

Pilot dùng để sửa những chỗ khó hiểu trong kit trước 7 phiên chính. Phiên pilot không tính vào 7 phiên.

## 3. Quy trình mỗi phiên (pilot và 7 phiên chính)

| Bước | Việc |
|---|---|
| Trước phiên | Chạy `tools\usability_session.ps1`: script reset CSDL và **tạo link mới**. Gửi link riêng cho người sắp vào. Tạo phiếu: `new_session.py HW03/usability/sessions S0x` |
| Mở đầu (~2 phút) | Gọi Meet → người tham gia **chia sẻ màn hình**. Bật Game Bar (`Win + Alt + R`) → đọc lời mở đầu trong kit, **xin đồng ý quay ngay trong video**, nhắc họ vừa làm vừa nói suy nghĩ |
| Nhiệm vụ (~5–8 phút) | Đọc nhiệm vụ U1 → im lặng quan sát, ghi giờ bắt đầu và kết thúc, lỗi, do dự, câu nói. Chỉ trợ giúp khi họ bí hẳn, và ghi lại lần trợ giúp đó |
| Sau nhiệm vụ (~5 phút) | SEQ → 10 câu SUS → 4 câu hỏi mở. **Họ tự trả lời**: gõ vào khung chat Meet hoặc Google Form, bạn chụp lại làm bằng chứng |
| Sau phiên | Tắt tunnel (Ctrl+C) → nhập phiếu `S0x.json` → `sus_score.py … --check` → commit `HW03[T2] k/10: phiên S0x` |

**Lưu ý:**
- **Mỗi lần chỉ một người.** Tất cả dùng chung tài khoản test và chung CSDL, chạy song song sẽ làm sai dữ liệu của nhau.
- Phiếu JSON chỉ ghi mã `P01…P07`. Họ tên và liên hệ (đã che 4 số giữa SĐT) ghi riêng trong bảng người tham gia do bạn tự lập.
- Không đăng link tunnel lên nhóm chat công khai.

**Phiếu SUS:** nếu có 10 phút, tạo một **Google Form** (SEQ + 10 câu SUS thang 1–5 + 4 câu hỏi mở, ô đầu tiên ghi mã P0x). Câu trả lời do chính người tham gia điền, có mốc giờ, nên là bằng chứng mạnh khi TA gọi kiểm chứng. Không kịp thì cho họ trả lời trong khung chat Meet rồi chụp lại.

Đã 3:18 sáng. Thử 4G xong, báo Claude Code chạy tiếp bước 4, rồi đi ngủ. Pilot và 7 phiên để tối nay.
```

**Xử lý:** [...]

---

## #85 | 03:21 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đã thử hết luồng bạn nói, vào hồ sơ kiểm tra thì thấy 1 đơn hàng đã được giảm giá nhé. Thực hiện tiếp bước 4 nhé
```

**Output:**
```
check_kit: 0 lỗi. Tắt tunnel (không để SUT công khai khi không có phiên), ghi khai báo, commit.

Đã xong bước 4 và commit. Môi trường usability từ xa đã sẵn sàng.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: T2 2b – dựng môi trường usability từ xa qua Cloudflare tunnel.
- SUT `../eshop-sut`: nhánh local `usability-tunnel`, commit `e33212d`, không push. Thay đổi: 8 file, +21/−13 (7 file `frontend-web` đổi `http://localhost:3000/api` thành `/api`; `vite.config.js` thêm proxy `/api` sang `:3000` và cho phép host `.trycloudflare.com`). Không có `/uploads` nên không cần proxy.
- Ổ đĩa: C trống 146G, D trống 83G. Cloudflared 2026.10.7 cài vào `D:\Tools\cloudflared\` (bạn đã đồng ý), chữ ký Cloudflare hợp lệ.
- Script mới:
  - `tools/usability_session.ps1`: restart backend → Vite → tunnel → in link; Ctrl+C để tắt.
  - `tools/sut_main.ps1`: đưa SUT về nhánh `main`.
- Kiểm tra:
  - Tunnel chạy được: trang trả HTTP 200, API qua tunnel trả 5 sản phẩm.
  - Bạn đã thử hết luồng U1 qua 4G, đơn có giảm giá VIP100 hiện trong Hồ sơ.
  - check_kit: 0 lỗi. Prompt log: 33 lượt.
- File trong repo bài: `usability/plan.md` (mục 5 hình thức remote qua Meet; mục 6 môi trường và khác biệt so với checklist), `usability/participant_kit.md` (thêm dòng dùng máy tính, mở link), `report_plan.md` (mục e thêm U-R, mục f thêm khai báo).
- Commit: `4199810` HW03[T2] 2b/10: môi trường usability từ xa (tunnel)
- Trạng thái máy: đã tắt tunnel, Vite và backend để SUT không bị công khai khi không có phiên.
- Cần quyết định: không có.

SUT đang ở nhánh `usability-tunnel`; trước khi chạy lại checklist hay HW khác, nhớ chạy `tools/sut_main.ps1`.

Bạn nhớ push repo bài nhé: `git push` (còn 1 commit chưa push là `4199810`). Repo `eshop-sut` thì không push.
```

**Xử lý:** [...]

---

## #86 | 03:24 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: T2 2b – dựng môi trường usability từ xa qua Cloudflare tunnel.
- SUT ../eshop-sut: nhánh local usability-tunnel, commit e33212d, không push. Thay đổi: 8 file, +21/−13 (7 file frontend-web đổi http://localhost:3000/api thành /api; vite.config.js thêm proxy /api sang :3000 và cho phép host .trycloudflare.com). Không có /uploads nên không cần proxy.
- Ổ đĩa: C trống 146G, D trống 83G. Cloudflared 2026.10.7 cài vào D:\Tools\cloudflared\ (bạn đã đồng ý), chữ ký Cloudflare hợp lệ.
- Script mới:
  - tools/usability_session.ps1: restart backend → Vite → tunnel → in link; Ctrl+C để tắt.
  - tools/sut_main.ps1: đưa SUT về nhánh main.
- Kiểm tra:
  - Tunnel chạy được: trang trả HTTP 200, API qua tunnel trả 5 sản phẩm.
  - Bạn đã thử hết luồng U1 qua 4G, đơn có giảm giá VIP100 hiện trong Hồ sơ.
  - check_kit: 0 lỗi. Prompt log: 33 lượt.
- File trong repo bài: usability/plan.md (mục 5 hình thức remote qua Meet; mục 6 môi trường và khác biệt so với checklist), usability/participant_kit.md (thêm dòng dùng máy tí(mục e thêm U-R, mục f thêm khai báo).
- Commit: 4199810 HW03[T2] 2b/10: môi trường usability từ xa (tunnel)
- Trạng thái máy: đã tắt tunnel, Vite và backend để SUT không bị công khai khi không có phiên.
- Cần quyết định: không có.

SUT đang ở nhánh usability-tunnel; trước khi chạy lại checklist hay HW khác, nhớ chạy tools/sut_main.ps1.
===
đã push
Nếu oke rồi thì mình hoàn thành nốt cái prompt hoàn thiện 2 skill rồi đi ngủ
```

**Output:**
````
Môi trường từ xa đã xong. Claude Code tắt tunnel khi không có phiên là đúng. Làm nốt phần skill rồi ngủ được.

Mình sửa một chỗ trong lệnh: **chưa chép skill vào `HW03/skills/`**. Sau pilot và các phiên usability, skill có thể còn sửa, nên để tới lúc đóng gói mới chép, tránh nộp bản cũ.

```
HW03 – hoàn thiện 2 skill theo cách làm thực tế (commit "HW03: cập nhật skill theo cách làm thực tế"):
1. gui-checklist-testing: thêm chế độ Playwright (bước 3: phân loại che_do auto/manual/mixed, oracle khoá sha1; bước 4: lượt auto → auto_status, gộp auto+tay theo V1, lỗi harness → Blocked không lập bug); quy tắc ảnh: item Failed + 1 ảnh/màn/nền tảng cho cross-platform, overlay theo đề; bước 1 thêm "đọc toàn bộ phần nguồn checklist trong slide trước khi sinh item"; sửa quy tắc 9 cho khớp; đưa tools/merge_hw03.py, failed_list_hw03.py, bug_groups_hw03.py vào scripts/ dạng tổng quát (tham số hoá, không gắn HW03), tools/ giữ wrapper gọi sang skill; cập nhật bảng Script.
2. usability-evaluation: bước 0 thêm lựa chọn remote synchronous (Meet, người tham gia chia sẻ màn hình, tunnel + reset dữ liệu mỗi phiên, link mới mỗi phiên, mỗi lần 1 người, quay khi được đồng ý); thêm tham chiếu tools/usability_session.ps1 như ví dụ.
3. Chạy lại các script đã chuyển trên dữ liệu HW03: checklist.json, Excel, failed_list, bug_groups phải giống hệt (diff, Excel so số liệu). check_checklist 0 lỗi.
4. CHƯA chép sang HW03/skills (để lúc đóng gói). Ghi vào report_plan mục c: "chép 2 skill → HW03/skills khi đóng gói".
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

## Sáng mai dậy

1. Đọc báo cáo của lệnh trên, rồi **push**.
2. **Hẹn giờ cụ thể** với 8 người cho tối nay, mỗi người 20 phút, xếp liền nhau.
3. Lúc rảnh ở trường:
   - Viết **28 khung bug** (🔒).
   - Thêm overlay cho **5 ảnh `P3_M*`**.
   - Chốt **R9/R11** (CL-08/09 trên P1).
   - Đọc `participant_kit.md`.
   - Tạo Google Form SUS nếu muốn dùng.
````

**Xử lý:** [...]

---

## #87 | 03:24 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – hoàn thiện 2 skill theo cách làm thực tế (commit "HW03: cập nhật skill theo cách làm thực tế"):
1. gui-checklist-testing: thêm chế độ Playwright (bước 3: phân loại che_do auto/manual/mixed, oracle khoá sha1; bước 4: lượt auto → auto_status, gộp auto+tay theo V1, lỗi harness → Blocked không lập bug); quy tắc ảnh: item Failed + 1 ảnh/màn/nền tảng cho cross-platform, overlay theo đề; bước 1 thêm "đọc toàn bộ phần nguồn checklist trong slide trước khi sinh item"; sửa quy tắc 9 cho khớp; đưa tools/merge_hw03.py, failed_list_hw03.py, bug_groups_hw03.py vào scripts/ dạng tổng quát (tham số hoá, không gắn HW03), tools/ giữ wrapper gọi sang skill; cập nhật bảng Script.
2. usability-evaluation: bước 0 thêm lựa chọn remote synchronous (Meet, người tham gia chia sẻ màn hình, tunnel + reset dữ liệu mỗi phiên, link mới mỗi phiên, mỗi lần 1 người, quay khi được đồng ý); thêm tham chiếu tools/usability_session.ps1 như ví dụ.
3. Chạy lại các script đã chuyển trên dữ liệu HW03: checklist.json, Excel, failed_list, bug_groups phải giống hệt (diff, Excel so số liệu). check_checklist 0 lỗi.
4. CHƯA chép sang HW03/skills (để lúc đóng gói). Ghi vào report_plan mục c: "chép 2 skill → HW03/skills khi đóng gói".
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

**Output:**
```
Lưu bản chuẩn trước khi chuyển script để so sánh sau.

Viết `merge_runs.py` tổng quát trong skill.

merge giống hệt. Giờ chuyển failed_list.

Giờ bug_groups.

Toàn bộ `failed_list`, `bug_groups`, BUG-58…85 giống hệt. Kiểm checklist.md + Excel.

Kết quả trùng khớp hoàn toàn (Excel: 2144 ô, 0 ô khác). Khôi phục file xlsx đã commit để khỏi phát sinh diff nhị phân, rồi cập nhật SKILL.md.

Heredoc quá dài bị shell cắt. Ghi script ra file tạm rồi chạy.

Giờ skill usability-evaluation, bước 0.

Ghi vào report_plan mục c.

Đã cập nhật 2 skill và chuyển 3 script vào skill. Chạy lại trên dữ liệu HW03 thì mọi output giống hệt.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: cập nhật 2 skill theo cách làm thực tế.
- `gui-checklist-testing` (`SKILL.md` + `references/schema-checklist.md`):
  - Bước 1: đọc toàn bộ phần nguồn checklist trong slide trước khi sinh item.
  - Bước 3: chế độ Playwright (phân loại `che_do`, oracle khoá sha1) và quy tắc ảnh.
  - Bước 4: gộp auto + tay theo V1, lỗi harness → Blocked.
  - Đã sửa quy tắc 9, cập nhật bảng Script.
  - Schema thêm các trường của lượt auto (`auto_status`, `nguon_kq`, `lech_auto_tay`, `lap_bug`…).
- Script mới trong skill, tổng quát, nhận config JSON: `merge_runs.py`, `failed_list.py`, `bug_groups.py`. Ba file `tools/*_hw03.py` giờ chỉ giữ dữ liệu riêng HW03 rồi gọi sang skill.
- `usability-evaluation`: bước 0 thêm lựa chọn trực tiếp hoặc remote synchronous (Meet, tunnel, reset dữ liệu và link mới mỗi phiên, quay khi được đồng ý), lấy `tools/usability_session.ps1` làm ví dụ.
- Kiểm tra: các file sau chạy lại giống hệt từng byte: `checklist.json`, 3 CSV, `checklist.md`, `failed_list.md`, `bug_groups.md`, BUG-58…85, report. Excel so từng ô: 2144 ô, 0 ô khác. check_checklist 0 lỗi.
- Chưa chép sang `HW03/skills`; đã ghi việc này vào `report_plan.md` mục c (dòng 9), mục f thêm khai báo. Prompt log 34 lượt.
- Commit: `d811ea2` HW03: cập nhật skill theo cách làm thực tế

Bạn nhớ push nhé: `git push` (còn 1 commit chưa push là `d811ea2`).
```
*File AI ghi/gửi trong lượt này:* `merge_runs.py`, `failed_list.py`, `bug_groups.py`, `upd_skill.py`

**Xử lý:** [...]

---

## #88 | 03:31 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: cập nhật 2 skill theo cách làm thực tế.
- gui-checklist-testing (SKILL.md + references/schema-checklist.md):
  - Bước 1: đọc toàn bộ phần nguồn checklist trong slide trước khi sinh item.
  - Bước 3: chế độ Playwright (phân loại che_do, oracle khoá sha1) và quy tắc ảnh.
  - Bước 4: gộp auto + tay theo V1, lỗi harness → Blocked.
  - Đã sửa quy tắc 9, cập nhật bảng Script.
  - Schema thêm các trường của lượt auto (auto_status, nguon_kq, lech_auto_tay, lap_bug…).
- Script mới trong skill, tổng quát, nhận config JSON: merge_runs.py, failed_list.py, bug_groups.py. Ba file tools/*_hw03.py giờ chỉ giữ dữ liệu riêng HW03 rồi gọi sang skill.
- usability-evaluation: bước 0 thêm lựa chọn trực tiếp hoặc remote synchronous (Meet, tunnel, reset dữ liệu và link mới mỗi phiên, quay khi được đồng ý), lấy tools/usability_session.ps1 làm ví dụ.
- Kiểm tra: các file sau chạy lại giống hệt từng byte: checklist.json, 3 CSV, checklist.md, failed_list.md, bug_groups.md, BUG-58…85, report. Excel so từng ô: 2144 ô, 0 ô khác. check_checklist 0 lỗi.
- Chưa chép sang HW03/skills; đã ghi việc này vào report_plan.md mục c (dòng 9), mục f thêm khai báo. Prompt log 34 lượt.
- Commit: d811ea2 HW03: cập nhật skill theo cách làm thực tế
===
đã push rồi 
===
Nếu oke rồi thì có lẽ là mình viết handoff cho Claude Code, rồi viết handoff cho session này để ngày mai bắt đầu với phiên mới nhé
```

**Output:**
````
Đã viết **handoff cho phiên thảo luận** vào Project: `claude/HW03_handoff.md`. File gồm phạm vi và các quyết định, trạng thái từng Task, việc còn lại theo thứ tự, prompt log, ghi chú cho Audit (có cả lỗi của phiên này). Phiên mới chỉ cần đọc file đó cùng `HW02_handoff.md` (phần quy ước chung).

**Handoff cho Claude Code**: dán lệnh này để nó tự cập nhật, vì nó nắm repo rõ hơn:

```
HW03 – handoff trước khi nghỉ (commit "HW03: handoff 10/11"):
1. HW03/CLAUDE.md: thêm/ghi đè mục "Trạng thái 10/11 03:35" (≤ 25 dòng): deadline 10:00 11/11; T1 xong tới khung BUG-58…85 (SV chưa viết); treo: 5 ảnh P3_M* chưa overlay, R9/R11; T2 chưa có phiên – quy trình mỗi phiên (usability_session.ps1 → new_session.py → Meet → nhập JSON → sus_score --check → commit "HW03[T2] k/10: phiên S0x"); SUT đang ở nhánh usability-tunnel (sut_main.ps1 để về main); skill chưa chép sang HW03/skills; việc còn lại theo thứ tự (bug → T2 → skill/README/form/zip).
2. Kiểm git status sạch (trừ evidence_raw/ bị ignore); liệt kê nếu còn file chưa commit.
on_stop.py --manual. Báo cáo ≤ 5 dòng. Nhắc tôi push.
```

Mình đang xuất transcript phiên này (`_p1`), gửi ngay sau tin này.
````

**Xử lý:** [...]

---

## #89 | 03:33 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – handoff trước khi nghỉ (commit "HW03: handoff 10/11"):
1. HW03/CLAUDE.md: thêm/ghi đè mục "Trạng thái 10/11 03:35" (≤ 25 dòng): deadline 10:00 11/11; T1 xong tới khung BUG-58…85 (SV chưa viết); treo: 5 ảnh P3_M* chưa overlay, R9/R11; T2 chưa có phiên – quy trình mỗi phiên (usability_session.ps1 → new_session.py → Meet → nhập JSON → sus_score --check → commit "HW03[T2] k/10: phiên S0x"); SUT đang ở nhánh usability-tunnel (sut_main.ps1 để về main); skill chưa chép sang HW03/skills; việc còn lại theo thứ tự (bug → T2 → skill/README/form/zip).
2. Kiểm git status sạch (trừ evidence_raw/ bị ignore); liệt kê nếu còn file chưa commit.
on_stop.py --manual. Báo cáo ≤ 5 dòng. Nhắc tôi push.
```

**Output:**
```
Đã ghi handoff vào `HW03/CLAUDE.md` và commit; repo bài sạch.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: handoff. Đã thêm mục 7 "Trạng thái 10/11 03:35" vào `HW03/CLAUDE.md` (14 dòng), gồm:
  - Deadline 10:00 11/11.
  - T1 xong tới khung BUG-58…85, bạn chưa viết.
  - Việc treo: 5 ảnh `P3_M*` chưa có overlay, R9/R11.
  - Quy trình 5 bước cho mỗi phiên T2.
  - SUT đang ở nhánh `usability-tunnel`; skill chưa chép sang `HW03/skills`.
  - Việc còn lại theo thứ tự: bug → T2 → skill/README/form/zip.
- Git status sạch, không còn file nào chưa commit (`evidence_raw/` bị ignore). Prompt log 35 lượt.
- Commit: `cfa861e` HW03: handoff 10/11
- Cần quyết định: không có.

Bạn nhớ push nhé: `git push` (còn 1 commit chưa push là `cfa861e`).
```

**Xử lý:** [...]

---

## #90 | 03:35 10/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
Tôi mới thêm transcript của claude.ai, giúp tôi chạy on_stop.py --manual rồi commit nó nhé
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

**Tổng:** 90 lượt; Claude Sonnet 4.6 2 lượt (#1, #2); Claude Opus 5.5 81 lượt (#3, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #27, #28, #29, #30, #31, #32, #33, #34, #35, #36, #37, #38, #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #52, #53, #54, #55, #56, #58, #59, #60, #61, #62, #63, #64, #65, #66, #67, #68, #71, #72, #73, #74, #75, #76, #77, #78, #80, #81, #82, #83, #84, #85, #86, #87, #88, #89); Claude (không rõ model) 7 lượt (#4, #51, #57, #69, #70, #79, #90).

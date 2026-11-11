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

## #90 | 03:35 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Tôi mới thêm transcript của claude.ai, giúp tôi chạy on_stop.py --manual rồi commit nó nhé
```

**Output:**
```
Đã chạy `on_stop.py --manual` và commit prompt log. Log giờ có 90 lượt (trước là 35); phần tăng thêm là từ `claude-ai_session_HW03_p1.jsonl`.

- Commit: `c6e9465` HW03: prompt log thêm transcript phiên claude.ai (p1)
- Git status sạch.
- Bạn nên xem lại 55 lượt mới. Lượt nào thuộc bài khác lẫn vào thì thêm vào `exclude` trong `tools/hw.toml`. Phần Section / Mục đích / Xử lý của từng lượt bạn tự ghi trong `HW03/appendix/prompt_log_notes.toml`.

Bạn nhớ push nhé: `git push`.
```

**Xử lý:** [...]

---

## #91 | 03:41 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – bài học dùng chung (commit "harness: bài học từ HW03"):
1. CLAUDE.md gốc: thêm mục "Bài học kỹ thuật" ≤ 15 dòng (giữ tổng ≤ 200 dòng): Playwright 1.48 không có TestResult.annotations; Firefox Playwright không throttle/clipboard; locale giả lập ≠ trình duyệt thật; timeout = Blocked không Failed; Playwright _android cần flag "Enable command line on non-rooted devices"; adb reverse cần vite --host 127.0.0.1; web gọi cứng localhost:3000 → tunnel cần nhánh đổi /api + proxy + allowedHosts; Python MSYS2 cài gói bằng pacman; kiểm từng ảnh trước khi commit (repo public), ảnh gốc ở thư mục gitignore.
2. HARNESS_SETUP.md mục 6 (bắt đầu bài mới) thêm: hỏi SV deadline thật + trình duyệt/thiết bị dùng thật; quy tắc ảnh (overlay, tên file theo item) chốt trước lượt chạy tay; khung cho SV điền sinh từ schema/check script.
on_stop.py --manual. Báo cáo ≤ 4 dòng. Nhắc tôi push.
```

**Output:**
```
Đã thêm bài học vào `CLAUDE.md` gốc và bổ sung `HARNESS_SETUP.md` mục 6, đã commit.

### Báo cáo cho phiên thảo luận
- `CLAUDE.md` gốc: thêm mục 6 "Bài học kỹ thuật" (11 dòng, tổng file 124 dòng). Ngoài danh sách của lệnh, em thêm 2 ý gặp trong phiên này: file `.ps1` có tiếng Việt phải lưu UTF-8 có BOM và `param()` phải đứng đầu file; `_android` phải dùng tab có sẵn.
- `HARNESS_SETUP.md` mục 6: thêm bước 7–9 (hỏi deadline thật và trình duyệt/thiết bị thật; chốt quy tắc ảnh trước lượt chạy tay; khung cho SV điền sinh từ schema/check script). Bước prompt log cũ chuyển thành bước 10.
- Commit: `a46ea4d` harness: bài học từ HW03. Prompt log 91 lượt, git status sạch.

Bạn nhớ push nhé: `git push`.
```

**Xử lý:** [...]

---

## #92 | 18:18 10/11/2026 | Claude Sonnet 4.6 | [...]
**Mục đích:** [...]

**Prompt:**
```
/cs423-ai-first-homework Tiếp tục HW03 (GUI & Usability), deadline 10:00 11/11/2026.
1. Đọc Project doc claude/HW03_handoff.md (toàn bộ, gồm mục 6 Bài học) và claude/HW02_handoff.md mục 1, 3, 4 (Bug), 5b (quy ước chung, xuất transcript). Dùng kèm skill two-session-workflow.
2. Clone repo ThachHaoo/software-testing-2627 (đọc), kiểm HEAD + HW03/CLAUDE.md mục 7 "Trạng thái" — tin repo hơn handoff nếu lệch.
3. Báo ngắn: trạng thái hiện tại, việc còn lại theo thứ tự, việc tôi cần làm tiếp theo.
Transcript phiên này là _p2.
```

**Output:**
```
Em đọc skill, clone repo rồi đối chiếu trạng thái với handoff.

No response requested.
```

**Xử lý:** [...]

---

## #93 | 18:18 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Continue with the task described in the conversation above. Your most recent mcp__claude-code-remote__add_repo call has not run yet; nothing is wrong with the tool or its input. Run it now from the beginning with the tools you have, without assuming any result, file or state from it, and use the working directory and file locations you have now rather than ones earlier steps assumed.

The user's timezone is Asia/Saigon (UTC+07:00).
```

**Output:**
```
Đã kiểm repo. Nó khớp handoff, chỉ có thêm 1 commit.

**Trạng thái (repo, HEAD `a46ea4d` 03:41 10/11, đã push)**
- `a46ea4d` "harness: bài học từ HW03" nằm sau `c6e9465`. Commit này chỉ sửa CLAUDE.md gốc, HARNESS_SETUP.md và prompt log (hiện 91 lượt).
- **Task 1:** checklist, Excel và bảng T1 trong report đã xong. Cả 28 khung `BUG-58…85.md` vẫn còn `🔒 SV viết`, chưa có issue nào.
- **Task 1 còn treo:** R9/R11 (verdict P1 của CL-08 và CL-09, `checklist/run_check.md` dòng 38–51). Còn 5 ảnh `P3_M*` chưa overlay; thư mục `evidence_raw` không có trên repo vì bị gitignore, ảnh nằm trên máy em.
- **Task 2 (40đ, phần nặng nhất):** `usability/sessions/` đang trống, chưa có phiên nào, kể cả pilot. Em cũng chưa duyệt kit (plan, participant_kit, observation_sheet).
- **Skill:** chưa chép sang `HW03/skills/`, chưa quay video.
- **Báo cáo:** chưa có Critique, Audit, AI-02/03/05, README test summary, commit log và zip.

**Việc còn lại theo thứ tự.** Còn khoảng 16 giờ. Tối nay là đường găng vì phụ thuộc người khác.
1. **Trước phiên (khoảng 30 phút):** đọc lướt `participant_kit.md` và `observation_sheet.md` vì đây là thứ em sẽ đọc to cho người tham gia. Sau đó chạy pilot S00: `tools\usability_session.ps1` → `new_session.py … S00` → tự chạy hoặc nhờ 1 người chạy U1 → nhập JSON → `sus_score.py --check` → commit `HW03[T2] 2/10`.
2. **Tối nay:** chạy S01…S07, mỗi phiên một commit. Giữa các phiên, nếu có thời gian chết thì viết bug T1.
3. **Sau phiên:** chạy `sus_score.py --report` vào REPORT:U1. Em viết findings và bug Task 2.
4. **Bug T1:** em viết 28 bug. Sau đó Claude Code kiểm dữ kiện, rồi tái hiện; bước này phải đưa SUT về main bằng `sut_main.ps1`, nên làm **sau** các phiên usability. Cuối cùng tạo issue và chụp ảnh trang Issues.
5. **Đóng gói:** chép skill, README/test summary, AI-02/03/05, Mandatory Disclosure, commit log, `hw-submission-audit`, zip. Em lo phần Critique, verdict Audit, điểm tự chấm, ký, quay video (cắt nếu thiếu giờ) và nộp trước 10:00 ngày 11/11.

**Việc em cần làm tiếp theo**
- Cho anh biết **mấy giờ phiên đầu tiên bắt đầu** và đã chốt đủ 7 người chưa. Anh sẽ xếp lịch ngược lại cho pilot và bug.
- Trả lời nhanh R9 và R11, giữ Passed hay đổi Failed (chữ của em). Hai việc này chỉ mất vài phút và chặn bảng T1 cuối cùng.
- Nếu muốn, anh đưa ngay khối lệnh cho Claude Code để chuẩn bị pilot S00: kiểm SUT đang ở `usability-tunnel`, chạy thử tunnel, tạo khung S00.

Transcript phiên này sẽ xuất thành `_p2`. Anh sẽ đề nghị xuất sau khi xong các phiên usability.
```

**Xử lý:** [...]

---

## #94 | 18:20 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Thôi giờ tôi chấp nhận bỏ Task 2, có thể làm full Task 1, 3 cùng với skill để ăn các điểm còn lại được không?
```

**Output:**
```
Được, nhưng có một rủi ro cần xử lý trước.

**Rủi ro lớn nhất: "thiếu tài liệu bắt buộc = 0 điểm"**
Đề §14 liệt kê trong danh sách bắt buộc của zip cả "báo cáo usability" và "bằng chứng phiên usability (kịch bản, ghi chú quan sát, SUS, findings, bảng 7 người)". §17 ghi: *"Missing any required document results in 0 points."* Nếu bỏ hẳn Task 2 mà không có gì, người chấm có thể đọc thành thiếu tài liệu → 0 cả bài, không chỉ mất 40đ.

Cách giảm rủi ro:
- Vẫn nộp phần Task 2 đã có: `plan.md` (có task scenario U1), `participant_kit.md`, `observation_sheet.md`, câu hỏi probe, SUS. Kèm một mục "Task 2" trong report ghi thẳng: đã thiết kế nhưng **không chạy phiên nào**, lý do do em viết. Ghi rõ không có ghi chú quan sát, SUS, findings hay bảng người tham gia.
- Tự chấm Task 2 trung thực: 0, hoặc vài điểm cho task scenario nếu em thấy hợp lý. **Không** để trống mục mà không giải thích.
- Nếu kịp, email hoặc đăng forum hỏi TA tối nay: "nộp thiếu phần chạy phiên của Task 2 thì có bị coi là thiếu tài liệu không". Đây là cách duy nhất chắc chắn.

**Điểm tối đa thực tế**
- Task 1 = 30 khi viết đủ 28 bug, tạo issue và ảnh trang Issues.
- Task 3 = 20; số liệu P1/P2/P3 và ảnh đã có, chỉ còn R9/R11 và 5 ảnh `P3_M*`.
- Skill = 10, nhưng có rủi ro mất một phần. Đề yêu cầu video cho thấy dùng skill "end to end trên một screen hoặc flow". Skill `gui-checklist-testing` demo được; skill `usability-evaluation` không có phiên thật để demo. Nên nộp cả 2 skill, video chỉ demo trọn skill GUI checklist, còn skill usability ghi rõ là chưa dùng trên phiên thật.
- Tổng khoảng **60**, cộng vài điểm T2 nếu có. Tên zip phải khớp tổng tự chấm.

**Một lựa chọn trung gian**
Chạy pilot và 1–2 phiên với bạn cùng phòng tối nay, mỗi phiên khoảng 20 phút. Điều đó vẫn có điểm một phần cho "sessions + analysis" và giảm rủi ro "thiếu tài liệu". Nếu em đã quyết bỏ thì bỏ qua lựa chọn này.

**Thứ tự nếu bỏ Task 2**
1. R9/R11 và 5 ảnh `P3_M*`. Mất khoảng 15 phút, xong Task 3.
2. Viết 28 bug. Đây là việc nặng nhất, khoảng 3–5 giờ. Sau đó Claude Code đưa SUT về main bằng `sut_main.ps1`, kiểm dữ kiện, tái hiện, tạo issue và chụp ảnh trang Issues.
3. Chép skill, quay video skill GUI checklist.
4. Report mục Task 2 (ghi chưa chạy), Critique, Audit, AI-02/03/05, README, commit log, `hw-submission-audit`, zip.

Em chốt bỏ hẳn hay chạy 1–2 phiên? Nếu bỏ, em trả lời luôn R9/R11 để anh đưa lệnh đầu tiên cho Claude Code.
```

**Xử lý:** [...]

---

## #95 | 18:23 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Giờ tôi muốn hoàn thành Task 1 hoặc Task 3 cũng như Skill ngay, Còn Task 2 thì nếu dư thời gian sẽ làm, nếu không thì nộp các phần kia (plan, participant_kit, observation_sheet,...) nhưng không có phiên nào nên để là 10 điểm cũng được
```

**Output:**
````
Được. Về 10 điểm Task 2: mức này em tự quyết. Đề chấm "task scenario + 7 sessions + analysis", mà em mới có phần đầu và chưa chạy cả pilot. Nên ở §13 cần một dòng căn cứ: đã có plan, kịch bản U1, công cụ SUS/SEQ và câu hỏi probe; chưa có phiên, chưa có analysis. Không có căn cứ thì 10 dễ bị coi là tự chấm quá tay.

**Ngay bây giờ, 2 việc chạy song song**

**A. Em quyết R9/R11**, trả lời theo mẫu `R9=a/b, R11=a/b`:

| Mã | Câu hỏi | Phương án | Khuyến nghị |
|---|---|---|---|
| R9 | CL-08 trên P1 (Cốc Cốc hiện "30.000.000 ₫", P2/P3 hiện "6,000,000 ₫") | a) giữ Passed · b) đổi Failed | **b**: Expected ghi "Fail nếu kiểu phân cách khác nhau giữa các nền tảng", vế này cũng áp cho P1 |
| R11 | CL-09 trên P1 (ảnh hiện "9/11/2026") | a) giữ Passed · b) đổi Failed | **b**: Expected yêu cầu dd/mm/yyyy và giống nhau trên cả 3 nền tảng, trong khi ảnh có ngày 1 chữ số và khác P2/P3 |

Sau đó em overlay 5 ảnh `P3_M1_1, P3_M2_1, P3_M2_2, P3_M3_1, P3_M4_1` bằng trình sửa ảnh trên điện thoại rồi chép vào `checklist/evidence_raw/P3_android/`. Xong hai việc này là xong Task 3.

**B. Dán lệnh này cho Claude Code** (việc không phụ thuộc em, chạy trong lúc em làm A):

```
NHIỆM VỤ: chuẩn bị phần Skill để nộp HW03. Không push, không amend.
1. Chép .claude/skills/gui-checklist-testing và .claude/skills/usability-evaluation → HW03/skills/ (giữ cấu trúc). Kiểm mỗi skill tự đủ: mọi script SKILL.md gọi tới nằm trong scripts/ của skill, không trỏ tools/*_hw03.py; thiếu thì liệt kê, KHÔNG tự sửa.
2. Tạo HW03/skills/VideoLinks.md: 2 dòng, link = `<SV điền>`; ghi chú usability-evaluation "chưa dùng trên phiên thật".
3. Đề xuất phạm vi demo video cho gui-checklist-testing (1 màn nhỏ, chạy được trong ≤ 10 phút, nhánh tạm demo-video, không freeze vào ai-outputs): chỉ liệt kê bước + lệnh, ghi ra HW03/skills/demo_plan.md (file này export-ignore).
Commit `HW03[Skill] 1/3: chép skill + VideoLinks`.
Báo cáo ≤ 12 dòng: file chép, script thiếu (nếu có), tóm tắt demo_plan, hash.
```

**Tiếp theo: em viết 28 bug.** Viết thẳng vào `HW03/bugs/BUG-58…85.md`, thay các dòng `🔒`: Tiêu đề, Mô tả, Steps, Severity (Critical/High/Medium/Low), Priority (High/Medium/Low), Nhận định. Steps viết lại từ "Nguồn bước tái hiện" có sẵn trong mỗi file. Nên viết theo lô khoảng 7 file, commit lô đó (`HW03[T1] 5/6c: SV viết BUG-58…64`) rồi push. Anh kiểm dữ kiện từng lô trên repo luôn, không đợi đủ 28.
````

**Xử lý:** [...]

---

## #96 | 18:24 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: chuẩn bị phần Skill để nộp HW03. Không push, không amend.
1. Chép .claude/skills/gui-checklist-testing và .claude/skills/usability-evaluation → HW03/skills/ (giữ cấu trúc). Kiểm mỗi skill tự đủ: mọi script SKILL.md gọi tới nằm trong scripts/ của skill, không trỏ tools/*_hw03.py; thiếu thì liệt kê, KHÔNG tự sửa.
2. Tạo HW03/skills/VideoLinks.md: 2 dòng, link = `<SV điền>`; ghi chú usability-evaluation "chưa dùng trên phiên thật".
3. Đề xuất phạm vi demo video cho gui-checklist-testing (1 màn nhỏ, chạy được trong ≤ 10 phút, nhánh tạm demo-video, không freeze vào ai-outputs): chỉ liệt kê bước + lệnh, ghi ra HW03/skills/demo_plan.md (file này export-ignore).
Commit `HW03[Skill] 1/3: chép skill + VideoLinks`.
Báo cáo ≤ 12 dòng: file chép, script thiếu (nếu có), tóm tắt demo_plan, hash.
```

**Output:**
```
Đang chép skill, kiểm tham chiếu script xong; giờ tạo file và commit.

Sửa demo_plan: Quên mật khẩu nằm trong C2 → đổi sang màn Đăng ký, rồi commit.

Xong. Đã chép 2 skill vào `HW03/skills/`, tạo `VideoLinks.md` và `demo_plan.md`, commit `fcab9e1`. Không push, không amend.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: chép skill vào `HW03/skills/`, tạo `VideoLinks.md`, đề xuất phạm vi demo video.
- File đã tạo/sửa: `HW03/skills/gui-checklist-testing/` (13 file, không lấy `__pycache__`), `HW03/skills/usability-evaluation/` (12 file); `diff -r` so với `.claude/skills` không khác gì. Thêm `HW03/skills/VideoLinks.md` (2 link `<SV điền>`, usability ghi "chưa dùng trên phiên thật") và `HW03/skills/demo_plan.md`. Thêm dòng `skills/demo_plan.md export-ignore` vào `HW03/.gitattributes`; `git archive` đã loại file này. Xoá `.gitkeep`.
- Script thiếu: không có. Mọi script mà `SKILL.md` gọi để chạy đều nằm trong `scripts/`, script trong đó chỉ gọi nhau trong cùng thư mục. Có 4 chỗ ngoài skill, chưa sửa:
  - `gui-checklist-testing/SKILL.md:48-49` nhắc `gen_oracle.py`, `gen_run.py` ở `HW03/tests/`. Đây là phần chế độ Playwright (tuỳ chọn), skill không kèm 2 script này nên chế độ đó chưa tự đủ.
  - `gui-checklist-testing/SKILL.md:82` nhắc `tools/*_hw03.py`. Chỉ là ví dụ wrapper, không bắt buộc.
  - `usability-evaluation/SKILL.md:45` nhắc `tools/usability_session.ps1`, `tools/sut_main.ps1`. Cũng chỉ là ví dụ.
  - `scripts/render_checklist.py:33`: file sinh ra ghi nguồn là `tools/render_checklist.py`, sai đường dẫn (chỉ ảnh hưởng chữ hiển thị).
- Tóm tắt demo_plan: màn Đăng ký `/register` (nằm ngoài C2), chạy tay trên P1, trên nhánh `demo-video`. Freeze vào `HW03/demo/ai-outputs`, không vào `appendix/ai-outputs`. Đi qua bước 0 → 1 (`--min 8`) → bước 2 SV chỉ nói bằng lời → 3 (`dom_probe`) → 4 (`merge_platform`) → 5 (`build_excel`), tổng khoảng 10 phút.
- Kết quả kiểm tra: diff Pass; `check_checklist.py --help` chạy được từ bản đã chép.
- Commit: `fcab9e1` HW03[Skill] 1/3: chép skill + VideoLinks
- Cần quyết định:
  - D1 – Có đưa `gen_oracle.py`/`gen_run.py` vào skill không? Phương án: (a) chép vào `scripts/`; (b) ghi rõ trong SKILL.md là chỉ có ở repo ví dụ; (c) giữ nguyên.
  - D2 – Các lượt Claude lúc quay demo: (a) khai trong prompt log; (b) thêm `exclude` vào `tools/hw.toml`.
```
*File AI ghi/gửi trong lượt này:* `demo_plan.md`

**Xử lý:** [...]

---

## #97 | 18:24 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Hiện tại Task 1 chỉ còn viết 28 bug là xong nhỉ. Vậy còn Task 3 đã làm gì chưa nhỉ
```

**Output:**
```
Chưa đúng hẳn: Task 1 còn nhiều hơn 28 bug. Task 3 thì phần chạy đã xong, chỉ còn ảnh và chữ trong report.

**Task 3: đã làm gì**
- **Chạy:** cả 74 item đã chạy trên 3 nền tảng: P1 Cốc Cốc/Win 11, P2 Firefox/Win 11, P3 Chrome Android/POCO F5. Mỗi nền tảng có lượt auto và lượt tay. Kết quả gộp: P1 27/44/0/3 · P2 24/47/0/3 · P3 22/44/4/4.
- **Ảnh có overlay:** P1 34 ảnh, P2 32 ảnh, P3 24 ảnh (`checklist/evidence/`).
- **Report §4.1 đã sinh bằng script:** bảng 4 item khác kết quả giữa các nền tảng (CL-08, CL-09, CL-30, CL-34), bảng 8 chỗ lệch auto ↔ tay, bảng ảnh tổng quan theo màn.

**Task 3 còn thiếu**
1. **5 ảnh tổng quan P3** (`P3_M1_1, M2_1, M2_2, M3_1, M4_1`) chưa overlay, nên cột P3 trong bảng ảnh tổng quan đang ghi "chưa có". Đề bắt mỗi ảnh có overlay email, nên đây là phần bắt buộc.
2. **R9/R11:** verdict P1 của CL-08 và CL-09. Hai item này ảnh hưởng thẳng bảng "khác nhau giữa các nền tảng".
3. **Chữ report:** §4.2 "Khác biệt giữa các nền tảng" và §4.3 "Ảnh có overlay" vẫn là khối 📝 trống. Đây là phần phân tích, em quyết AI nháp (gắn 📝 "AI nháp – SV duyệt" như HW02) hay em tự viết.

**Task 1 thực tế còn**
- 28 bug (em viết, 🔒), sau đó tái hiện, tạo issue và chụp ảnh trang Issues.
- Report §3.2, 3.3 (bảng checklist chép từ Excel, script làm được), 3.5, 3.6 vẫn là 📝 trống. Claude Code sinh hoặc nháp được.
- **§3.4 "Item em bổ sung + vì sao AI bỏ sót" là 🔒, em tự viết** (giống gap analysis HW02). Dữ kiện có sẵn ở `sv_items.md` và `ai_gap_answer.md`.

Để tiết kiệm giờ, anh đề xuất 3 việc chạy song song:
- **Em:** quyết R9/R11, overlay 5 ảnh, rồi viết bug.
- **Claude Code:** chép skill (lệnh lúc nãy), sau đó sinh §3.3, 3.5, 3.6, 4.3 bằng script và nháp §3.2, 4.2 có nhãn 📝.
- **Em viết §3.4** sau hoặc xen giữa các lô bug.

Em trả lời `R9=?, R11=?` và chọn §4.2: AI nháp hay em viết?
```

**Xử lý:** [...]

---

## #98 | 18:26 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Xong. Đã chép 2 skill vào HW03/skills/, tạo VideoLinks.md và demo_plan.md, commit fcab9e1. Không push, không amend.

Báo cáo cho phiên thảo luận

- Nhiệm vụ: chép skill vào HW03/skills/, tạo VideoLinks.md, đề xuất phạm vi demo video.
- File đã tạo/sửa: HW03/skills/gui-checklist-testing/ (13 file, không lấy __pycache__), HW03/skills/usability-evaluation/ (12 file); diff -r so với .claude/skills không khác gì. Thêm HW03/skills/VideoLinks.md (2 link <SV điền>, usability ghi "chưa dùng trên phiên thật") và HW03/skills/demo_plan.md. Thêm dòng skills/demo_plan.md export-ignore vào HW03/.gitattributes; git archive đã loại file này. Xoá .gitkeep.
- Script thiếu: không có. Mọi script mà SKILL.md gọi để chạy đều nằm trong scripts/, script trong đó chỉ gọi nhau trong cùng thư mục. Có 4 chỗ ngoài skill, chưa sửa:
  - gui-checklist-testing/SKILL.md:48-49 nhắc gen_oracle.py, gen_run.py ở HW03/tests/. Đây là phần chế độ Playwright (tuỳ chọn), skill không kèm 2 script này nên chế độ đó chưa tự đủ.
  - gui-checklist-testing/SKILL.md:82 nhắc tools/*_hw03.py. Chỉ là ví dụ wrapper, không bắt buộc.
  - usability-evaluation/SKILL.md:45 nhắc tools/usability_session.ps1, tools/sut_main.ps1. Cũng chỉ là ví dụ.
  - scripts/render_checklist.py:33: file sinh ra ghi nguồn là tools/render_checklist.py, sai đường dẫn (chỉ ảnh hưởng chữ hiển thị).
- Tóm tắt demo_plan: màn Đăng ký /register (nằm ngoài C2), demo-video. Freeze vào HW03/demo/ai-outputs, không vàoappendix/ai-outputs. Đi qua bước 0 → 1 (--min 8) → bước 2 SV chỉ nói bằng lời → 3 (dom_probe) → 4 (merge_platform) → 5 (build_excel), tổng khoảng 10 phút.
- Kết quả kiểm tra: diff Pass; check_checklist.py --help chạy được từ bản đã chép.
- Commit: fcab9e1 HW03[Skill] 1/3: chép skill + VideoLinks                                                                                            n quyết định:
  - D1 – Có đưa gen_oracle.py/gen_run.py vào skill không? Phương án: (a) chép vào scripts/; (b) ghi rõ trong SKILL.md là chỉ có ở repo ví dụ; (c) giữ nguyên.
  - D2 – Các lượt Claude lúc quay demo: (a) khai trong prompt log; (b) thêm exclude vào tools/hw.toml.
===
R9: b
R11: b
4.2: AI nháp
```

**Output:**
````
Anh ghi các quyết định như sau. Riêng R9/R11 em chưa ghi lý do, nên anh lấy lý do từ khuyến nghị lúc nãy (Expected áp cho cả P1); em sửa nếu muốn.

**D1, D2**
- **D2 = a, không có lựa chọn khác.** Các lượt demo vẫn là lượt dùng AI, AI-01 bắt buộc khai. Thêm `exclude` để giấu chúng là vi phạm khai báo.
- **D1:** chép `gen_oracle.py`/`gen_run.py` vào skill nếu không dính đường dẫn cứng HW03 (a); nếu dính thì ghi rõ trong SKILL.md (b). Lý do: skill được chấm theo tính dùng lại được, và video cũng không dùng chế độ Playwright.
- Phạm vi demo là màn /register: dùng được, vì demo trên màn ngoài C2 cho thấy skill dùng lại được. Video đừng nói đây là kết quả của bài.

Dán cho Claude Code:

```
NHIỆM VỤ: R9/R11 + D1/D2 + điền chữ report T1/T3. SV chốt: R9=b, R11=b (lý do: Expected "cùng kiểu phân cách / dd/mm/yyyy và giống nhau trên P1, P2, P3" áp cho cả P1 – lấy từ khuyến nghị, SV có thể sửa); D1 = chép gen_oracle.py, gen_run.py vào scripts/ nếu không hardcode HW03 (sửa SKILL.md:48-49 trỏ scripts/), nếu có thì ghi rõ trong SKILL.md "chỉ có ở repo ví dụ" (cập nhật cả .claude/skills và HW03/skills, diff -r = 0); sửa chữ nguồn render_checklist.py:33; D2 = a (lượt demo vào prompt log, KHÔNG exclude). Ghi các quyết định vào report_plan mục e. Không push, không amend.
1. R9/R11: đổi verdict P1 CL-08, CL-09 = Failed ở lượt tay P1 (ghi "SV chốt R9=b/R11=b" + lý do vào notes, cập nhật run_check.md R9/R11/L1 = đã chốt). Chạy lại chuỗi merge_hw03 → failed_list_hw03 → bug_groups_hw03 → report_t1_hw03 → build_excel (recalc 0 lỗi). Nếu 2 Failed mới làm đổi bug_groups (nhóm mới/G nào thêm item/BUG-xx khung nào đổi) → DỪNG, báo, chưa sửa khung BUG.
2. Report: §3.3 (bảng checklist từ dữ liệu), §3.5, §3.6, §4.3 sinh bằng script giữa marker mới. §3.2 và §4.2: AI nháp, giọng "em", mở đầu dòng "📝 AI nháp – SV duyệt/sửa", chỉ dùng dữ kiện trong repo (lượt, commit, run_check, report_plan). KHÔNG đụng §3.4 (🔒 SV viết).
3. Ghi report_plan mục f (khai Audit): AI nháp §3.2, §4.2.
Commit riêng: `HW03[T1] 4/6c: SV chốt R9, R11`; `HW03[Skill] 1/3b: D1`; `HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2`.
Báo cáo ≤ 15 dòng: số liệu P1 mới, bug_groups có đổi không, marker mới, hash.
```

Việc của em lúc này:
1. Overlay 5 ảnh `P3_M*` rồi chép vào `checklist/evidence_raw/P3_android/`. Xong thì báo một câu, anh đưa lệnh nén và commit.
2. Bắt đầu viết bug lô 1 (BUG-58…64). Nhớ chờ Claude Code báo bug_groups có đổi không đã: nếu R9/R11 làm thêm nhóm thì số BUG có thể dịch.
````

**Xử lý:** [...]

---

## #99 | 18:27 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: R9/R11 + D1/D2 + điền chữ report T1/T3. SV chốt: R9=b, R11=b (lý do: Expected "cùng kiểu phân cách / dd/mm/yyyy và giống nhau trên P1, P2, P3" áp cho cả P1 – lấy từ khuyến nghị, SV có thể sửa); D1 = chép gen_oracle.py, gen_run.py vào scripts/ nếu không hardcode HW03 (sửa SKILL.md:48-49 trỏ scripts/), nếu có thì ghi rõ trong SKILL.md "chỉ có ở repo ví dụ" (cập nhật cả .claude/skills và HW03/skills, diff -r = 0); sửa chữ nguồn render_checklist.py:33; D2 = a (lượt demo vào prompt log, KHÔNG exclude). Ghi các quyết định vào report_plan mục e. Không push, không amend.
1. R9/R11: đổi verdict P1 CL-08, CL-09 = Failed ở lượt tay P1 (ghi "SV chốt R9=b/R11=b" + lý do vào notes, cập nhật run_check.md R9/R11/L1 = đã chốt). Chạy lại chuỗi merge_hw03 → failed_list_hw03 → bug_groups_hw03 → report_t1_hw03 → build_excel (recalc 0 lỗi). Nếu 2 Failed mới làm đổi bug_groups (nhóm mới/G nào thêm item/BUG-xx khung nào đổi) → DỪNG, báo, chưa sửa khung BUG.
2. Report: §3.3 (bảng checklist từ dữ liệu), §3.5, §3.6, §4.3 sinh bằng script giữa marker mới. §3.2 và §4.2: AI nháp, giọng "em", mở đầu dòng "📝 AI nháp – SV duyệt/sửa", chỉ dùng dữ kiện trong repo (lượt, commit, run_check, report_plan). KHÔNG đụng §3.4 (🔒 SV viết).
3. Ghi report_plan mục f (khai Audit): AI nháp §3.2, §4.2.
Commit riêng: `HW03[T1] 4/6c: SV chốt R9, R11`; `HW03[Skill] 1/3b: D1`; `HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2`.
Báo cáo ≤ 15 dòng: số liệu P1 mới, bug_groups có đổi không, marker mới, hash.
```

**Output:**
```
Dùng `override` trong `merge_hw03.py` (skill cấm sửa file lượt tay của SV), rồi chạy lại chuỗi gộp.

Now apply override + run chain.

bug_groups đổi: G-23/BUG-80 thêm nền tảng P1 → theo lệnh sẽ dừng sau khi xong bước 1. Chạy nốt report_t1 + build_excel.

Recalc kiểm bằng Excel COM.

Em đã làm xong bước 1 (chốt R9/R11) rồi dừng theo lệnh, vì kết quả làm đổi `bug_groups.md`. D1 và phần report (bước 2, 3) chưa làm.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: chốt R9/R11 rồi chạy lại chuỗi merge → failed_list → bug_groups → report_t1 → build_excel. Dừng ở điều kiện "bug_groups đổi".
- Cách đổi verdict: thêm `override` cho CL-08/CL-09 P1 trong `tools/merge_hw03.py` (ket_qua = Failed, notes ghi "SV chốt R9=b/R11=b" + lý do). File lượt tay của SV không sửa, vì skill quy định file này không được sửa.
- File đã sửa: `checklist.json`, `run_check.md` (R9, R11, L1 = đã chốt), `failed_list.md`, `bug_groups.md`, Report §3.5/§4.1 (marker cũ), Excel, `report_plan.md` mục e (thêm dòng R9, R11).
- Kết quả kiểm tra: chuỗi script chạy hết, không thiếu kết quả nào; Excel tính lại bằng Excel: 21 công thức, 0 lỗi.
- Số liệu P1 mới (Passed/Failed/N/A/Blocked): **25/46/0/3**, trước là 27/44/0/3; tỉ lệ Passed 33,8%. Ô Failed tổng là 137. P2, P3 giữ nguyên.
- bug_groups có đổi: vẫn 28 nhóm, không có nhóm hay item mới. Riêng G-23 (`BUG-80`, CL-09) thêm nền tảng P1 và thêm dòng Actual P1. CL-08 trùng #170 nên không có khung bug.
- Khung `HW03/bugs/BUG-80.md` chưa sửa, vẫn ghi "Nền tảng Failed: P2, P3" (dòng 21), chưa có môi trường, Actual, ảnh của P1 (dòng 25, 41, 46).
- Bất thường: mục "lệch auto/tay" của report còn dòng CL-09 P1 "auto Failed / tay Failed", vì dữ liệu lệch ghi theo verdict tay trước khi override. Phần nguyên nhân có ghi "SV chốt R11=b".
- Commit: `090cabb` HW03[T1] 4/6c: SV chốt R9, R11
- Chưa làm: D1 (commit `1/3b`), bước 2 report, bước 3 report_plan mục f. Chưa ghi D1, D2 vào mục e.
- Cần quyết định:
  - B80 – Cập nhật khung BUG-80 thêm dữ kiện P1? (a) AI sinh lại khung bằng `--skeleton`, chỉ phần dữ kiện; (b) SV tự thêm vào bản đang viết.
  - TIẾP – Làm tiếp D1 và phần report với số liệu mới? (a) làm tiếp; (b) chờ chốt B80 xong.
```

**Xử lý:** [...]

---

## #100 | 18:33 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: chốt R9/R11 rồi chạy lại chuỗi merge → failed_list → bug_groups → report_t1 → build_excel. Dừng ở điều kiện "bug_groups đổi".
- Cách đổi verdict: thêm override cho CL-08/CL-09 P1 trong tools/merge_hw03.py (ket_qua = Failed, notes ghi "SV chốt R9=b/R11=b" + lý do). File lượt tay của SV không sửa, vì skill quy định file này không được sửa.
- File đã sửa: checklist.json, run_check.md (R9, R11, L1 = đã chốt), failed_list.md, bug_groups.md, Report §3.5/§4.1 (marker cũ), Excel, report_plan.md mục e (thêm dòng R9, R11).
- Kết quả kiểm tra: chuỗi script chạy hết, không thiếu kết quả nào; Excel tính lại bằng Excel: 21 công thức, 0 lỗi.
- Số liệu P1 mới (Passed/Failed/N/A/Blocked): 25/46/0/3, trước là 27/44/0/3; tỉ lệ Passed 33,8%. Ô Failed tổng là 137. P2, P3 giữ nguyên.
- bug_groups có đổi: vẫn 28 nhóm, không có nhóm hay item mới. Riêng G-23 (BUG-80, CL-09) thêm nền tảng P1 và thêm dòng Actual P1. CL-08 trùng #170 nên không có khung bug.
- Khung HW03/bugs/BUG-80.md chưa sửa, vẫn ghi "Nền tảng Failed: P2, P3" (dòng 21), chưa có môi trường, Actual, ảnh của P1 (dòng 25, 41, 46).
- Bất thường: mục "lệch auto/tay" của report còn dòng CL-09 P1 "auto Failed / tay Failed", vì dữ liệu lệch ghi theo verdict tay trước khi override. Phần nguyên nhân có ghi "SV chốt R11=b".
- Commit: 090cabb HW03[T1] 4/6c: SV chốt R9, R11
- Chưa làm: D1 (commit 1/3b), bước 2 report, bước 3 report_plan mục f. Chưa ghi D1, D2 vào mục e.
- Cần quyết định:
  - B80 – Cập nhật khung BUG-80 thêm dữ kiện P1? (a) AI sinh lại khung bằng --skeleton, chỉ phần dữ kiện; (b) SV tự thêm vào bản đang viết.
  - TIẾP – Làm tiếp D1 và phần report
===
Giúp mình viết thêm prompt để kiểm trùng các issues mà mình đã đăng trên github nhé: https://github.com/tkob-team/eshop-sut/issues/17. Cũng như đổi lại khung bug theo mẫu HW02, chỉnh lại tiền tố tiêu đề của Github nữa nhé
```

**Output:**
````
Có 3 điểm cần nói trước khi đưa lệnh:

- **Kiểm trùng phải làm lại.** `issues.json` hiện là ảnh chụp lúc 02:55 10/11, gồm 158 issue tới #203, tức chưa có issue HW03 nào của bạn cùng nhóm. Bạn nhóm vẫn đang đăng, nên cần lấy danh sách mới (mọi tác giả, kể cả đã đóng) rồi đối chiếu lại cả 28 nhóm "MỚI" lẫn 4 nhóm "trùng một phần".
- **Tiền tố:** HW02 dùng `[FR-xx]` theo feature (#17 là `[FR-01]`). C2 trải nhiều FR, nên anh đề xuất lấy FR trong cột Căn cứ của item đầu nhóm, ví dụ CL-10 → FR-21.5 → `[FR-21]`. Tiền tố chỉ đặt trên GitHub, không ghi vào file. Nếu bạn nhóm đã dùng tiền tố khác cho HW03 thì Claude Code dừng để em chọn theo nhóm.
- **B80 = a**, làm luôn trong lần dựng lại khung. Khung mới theo mẫu B `d0d0e05:HW02/bugs/BUG-22.md`, giống cấu trúc #17.

```
NHIỆM VỤ: kiểm trùng issue + dựng lại khung BUG-58…85 theo mẫu HW02. SV chốt: B80=a; tiền tố GitHub = [FR-xx] lấy từ Căn cứ của item đầu nhóm (chỉ trên GitHub, không vào tiêu đề trong file). Không push, không amend. KHÔNG viết/sửa chữ SV.
1. `gh auth status` phải là ThachHaoo. `gh issue list -R tkob-team/eshop-sut --state all --limit 1000 --json number,title,author,state,createdAt,labels,body` → cập nhật HW03/bugs/issues.json.
2. Đối chiếu lại 28 nhóm MỚI + 4 trùng một phần + 14 trùng với MỌI issue (mọi tác giả, mọi trạng thái; chú ý issue > #203 của henry-banana, nphoang-itus). Ghi HW03/bugs/dup_check.md: mỗi G – issue nghi trùng (số, tác giả, tiêu đề, câu chứng cứ) – mức (trùng/một phần/không). Chỉ liệt kê, SV quyết. Liệt kê luôn tiền tố tiêu đề bạn nhóm dùng cho HW03; nếu khác [FR-xx] → DỪNG ở bước 3, báo.
3. Nếu file BUG nào đã có chữ SV (dòng 🔒 đã bị thay) → không đụng file đó, báo. Còn lại sinh lại khung theo `git show d0d0e05:HW02/bugs/BUG-22.md`: ID; Tiêu đề / Severity / Priority = `<SV viết>`; dòng "Tiền tố GitHub: [FR-xx]"; Môi trường (gạch đầu dòng giá trị thật từng nền tảng Failed, gồm P1 cho BUG-80); Tiền điều kiện, Các bước tái hiện, Expected (trích căn cứ – câu SRS chép nguyên văn có nhãn "(AI chép nguyên văn)"), Actual = `<SV viết>`; Bằng chứng (ảnh từng nền tảng); Item liên quan; Yêu cầu (AI điền từ bug_groups, SV duyệt); Ghi chú cô lập → Dữ kiện (AI chép: Actual nguyên văn theo nền tảng + Nguồn bước tái hiện) và Nhận định `<SV viết>`; Link GitHub Issue. Không chép Expected vào Dữ kiện. Sinh bằng script (đặt cạnh bug_groups_hw03.py), không viết tay.
Commit `HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02`.
Báo cáo ≤ 15 dòng: số issue mới so với snapshot cũ, G nào đổi mức trùng, tiền tố bạn nhóm, file bị bỏ qua, hash.
```

Lệnh này chạy xong thì gửi tiếp lệnh ngắn sau. Cách này tách khỏi lệnh trên để không bị lẫn:

```
Làm tiếp phần còn dở của lệnh trước: D1 (commit 1/3b), bước 2 report (§3.3, 3.5, 3.6, 4.3 bằng script; AI nháp §3.2, §4.2), bước 3 report_plan mục f; ghi D1, D2 vào mục e. Sửa luôn dòng "lệch auto/tay" CL-09 P1: hiển thị đúng sau override (tay = Failed theo R11 → không còn lệch thì bỏ dòng, ghi nguyên nhân trong notes). Báo cáo ≤ 10 dòng + hash.
```

Em đợi `dup_check.md` rồi hãy viết bug: nhóm nào thành trùng thì khỏi viết, đỡ được vài file. Trong lúc chờ, em làm overlay 5 ảnh `P3_M*`.
````

**Xử lý:** [...]

---

## #101 | 18:35 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: kiểm trùng issue + dựng lại khung BUG-58…85 theo mẫu HW02. SV chốt: B80=a; tiền tố GitHub = [FR-xx] lấy từ Căn cứ của item đầu nhóm (chỉ trên GitHub, không vào tiêu đề trong file). Không push, không amend. KHÔNG viết/sửa chữ SV.
1. `gh auth status` phải là ThachHaoo. `gh issue list -R tkob-team/eshop-sut --state all --limit 1000 --json number,title,author,state,createdAt,labels,body` → cập nhật HW03/bugs/issues.json.
2. Đối chiếu lại 28 nhóm MỚI + 4 trùng một phần + 14 trùng với MỌI issue (mọi tác giả, mọi trạng thái; chú ý issue > #203 của henry-banana, nphoang-itus). Ghi HW03/bugs/dup_check.md: mỗi G – issue nghi trùng (số, tác giả, tiêu đề, câu chứng cứ) – mức (trùng/một phần/không). Chỉ liệt kê, SV quyết. Liệt kê luôn tiền tố tiêu đề bạn nhóm dùng cho HW03; nếu khác [FR-xx] → DỪNG ở bước 3, báo.
3. Nếu file BUG nào đã có chữ SV (dòng 🔒 đã bị thay) → không đụng file đó, báo. Còn lại sinh lại khung theo `git show d0d0e05:HW02/bugs/BUG-22.md`: ID; Tiêu đề / Severity / Priority = `<SV viết>`; dòng "Tiền tố GitHub: [FR-xx]"; Môi trường (gạch đầu dòng giá trị thật từng nền tảng Failed, gồm P1 cho BUG-80); Tiền điều kiện, Các bước tái hiện, Expected (trích căn cứ – câu SRS chép nguyên văn có nhãn "(AI chép nguyên văn)"), Actual = `<SV viết>`; Bằng chứng (ảnh từng nền tảng); Item liên quan; Yêu cầu (AI điền từ bug_groups, SV duyệt); Ghi chú cô lập → Dữ kiện (AI chép: Actual nguyên văn theo nền tảng + Nguồn bước tái hiện) và Nhận định `<SV viết>`; Link GitHub Issue. Không chép Expected vào Dữ kiện. Sinh bằng script (đặt cạnh bug_groups_hw03.py), không viết tay.
Commit `HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02`.
Báo cáo ≤ 15 dòng: số issue mới so với snapshot cũ, G nào đổi mức trùng, tiền tố bạn nhóm, file bị bỏ qua, hash.
```

**Output:**
```
Snapshot cũ 158 → mới 179 (21 issue mới, đều của nphoang-itus, tiền tố `[HW03-C3-xx]`). Giờ đối chiếu với các nhóm.

Now dup_check.md (generated by script for the table rows, evidence quoted from issue titles/bodies).

Em đã làm bước 1 và 2, rồi dừng trước bước 3 (dựng khung bug), vì bạn nhóm đặt tiền tố HW03 khác `[FR-xx]` mà SV đã chốt.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: kiểm trùng issue. Bước 3 (khung BUG theo mẫu HW02) chưa làm.
- File đã tạo/sửa: `HW03/bugs/issues.json` (lấy lại, có thêm `body`/`createdAt`), `HW03/bugs/dup_check.md` (mới), `HW03/bugs/failed_list.md` (chạy lại, chỉ đổi dòng đầu "179 issue, tới #224").
- Kiểm tra: `gh auth status` = ThachHaoo. Mọi issue dùng làm căn cứ trùng vẫn OPEN.
- Issue mới: snapshot cũ có 158 issue (tới #203), bây giờ 179 (tới #224). Có **21 issue mới, #204–#224, đều của nphoang-itus**. henry-banana không có issue nào sau #203.
- 21 issue mới đều thuộc ứng dụng **admin** (body ghi "Admin cô lập http://localhost:5175"). C2 của SV là web người dùng nên không trùng nhóm nào.
- Đổi mức trùng: **không G nào** (đây là đề xuất của AI). 28 nhóm vẫn MỚI, 4 trùng một phần, 14 trùng.
- Một số issue cùng loại nhưng khác ứng dụng hoặc khác màn được liệt kê để SV xét: #221 → G-01, #206 → G-04, #209/#121 → G-05, #205/#195 → G-06, #210 → G-07, #222 → G-21/G-22, #219 → G-24. Chi tiết trong `dup_check.md` §3–4.
- Tiền tố bạn nhóm: nphoang-itus dùng `[HW03-C3-xx]` cho HW03 (`[BUG-FRxx-xx]` ở HW02). henry-banana dùng `[FRxx-xx]`, SV dùng `[FR-xx]`, cả hai chỉ có ở HW02.
- File bị bỏ qua: không có. Cả 28 file `BUG-58…85.md` vẫn đủ 6 dòng 🔒, chưa có chữ SV.
- Commit: `e9a2c85` HW03[T1] 5/6c: kiểm trùng issue (khung bug chờ chốt tiền tố). Em đổi message so với lệnh vì phần khung bug chưa làm. Commit khung sẽ dùng message gốc `HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02`.
- Cần quyết định:
  - PFX – Tiền tố tiêu đề GitHub: (a) giữ `[FR-xx]` như HW02 của SV; (b) theo bạn nhóm `[HW03-C2-xx]`; (c) kết hợp, ví dụ `[HW03-C2-xx][FR-xx]`.
  - DUP – SV xác nhận "không đổi mức trùng" cho cả 28 nhóm, nhất là G-16 với #123 (đang ghi "liên quan").
- Việc còn treo từ lượt trước: D1 (`1/3b`), phần report §3.2/§3.3/§3.5/§3.6/§4.2/§4.3, `report_plan` mục f, và ghi D1/D2 vào mục e.
```

**Xử lý:** [...]

---

## #102 | 18:37 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Làm tiếp phần còn dở của lệnh trước: D1 (commit 1/3b), bước 2 report (§3.3, 3.5, 3.6, 4.3 bằng script; AI nháp §3.2, §4.2), bước 3 report_plan mục f; ghi D1, D2 vào mục e. Sửa luôn dòng "lệch auto/tay" CL-09 P1: hiển thị đúng sau override (tay = Failed theo R11 → không còn lệch thì bỏ dòng, ghi nguyên nhân trong notes). Báo cáo ≤ 10 dòng + hash.
```

**Output:**
```
gen_oracle/gen_run hardcode HW03 (đường dẫn, màn C2, overlay, adb) → ghi "chỉ có ở repo ví dụ".

Giờ phần report. Xem cấu trúc report §3–§4 và script hiện có.

Sửa `merge_runs.py` (bỏ lệch khi override làm tay = auto, chép nguyên nhân vào notes), rồi thêm 4 khối mới vào report script.

Phát sinh: CL-08 P1 thành lệch (auto Passed ≠ kết quả cuối Failed). Lệch này có thật nên em giữ, thêm nguyên nhân; đồng thời dọn phần notes CL-09 bị lặp.

Thêm 4 khối vào `report_t1_hw03.py`.

Đang viết nháp §3.2, §4.2 (chỉ dùng dữ kiện trong repo), rồi ghi mục f và commit.

Phần còn dở đã xong, 2 commit. Không push, không amend, không đụng §3.4.

### Báo cáo cho phiên thảo luận
- **D1:** `gen_oracle.py` và `gen_run.py` gắn cứng HW03 (đường dẫn, màn C2, overlay, adb) nên em không chép vào `scripts/`. `SKILL.md` ghi "chỉ có ở repo ví dụ". Đã sửa chữ nguồn trong `render_checklist.py`. `.claude/skills` và `HW03/skills` giống nhau hoàn toàn (`diff -r` = 0). D1, D2 đã ghi vào `report_plan` mục e.
- **Lệch auto/tay CL-09 P1:** dòng này đã bỏ khỏi report. `merge_runs.py` giờ tự bỏ dòng lệch khi quyết định của SV làm kết quả tay trùng auto, và chép nguyên nhân vào notes "[trước quyết định: …]".
- **Phát sinh CL-08 P1:** sau override R9, auto Passed còn kết quả cuối là Failed, nên thành một dòng lệch mới. Lệch này có thật: auto chấm riêng từng nền tảng, thấy "6.000.000 ₫". Em giữ dòng và ghi nguyên nhân. P1 vẫn 25/46/0/3 (Passed/Failed/N/A/Blocked).
- **Marker mới trong report:**
  - `REPORT:T1:checklist_table` cho §3.3 (74 dòng)
  - `REPORT:T1:execution` cho §3.5, nằm trước bảng tổng: 6 lượt, thứ tự và giờ
  - `REPORT:T1:failed_items` cho §3.6 (47 item, gồm notes, ảnh, issue trùng / nhóm bug)
  - `REPORT:T1:overlay` cho §4.3. Bảng ảnh tổng quan chuyển từ §4.1 sang đây; P3 vẫn chưa có ảnh nào.
- **AI nháp §3.2 và §4.2:** đều mở đầu bằng dòng "📝 AI nháp – SV duyệt/sửa", chỉ dùng dữ kiện có trong repo. Phần khai Audit đã ghi vào `report_plan` mục f.
- **Kiểm tra:** `check_checklist` 0 lỗi; Excel tính lại 21 công thức, 0 lỗi; `checklist.md` sinh lại (bản cũ còn ghi P1 Passed từ trước 4/6c).
- **Commit:** `0d8fd34` HW03[Skill] 1/3b: D1 · `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2
- **Còn chờ:** PFX (tiền tố tiêu đề GitHub) để dựng khung BUG-58…85; giờ chạy tay P1 trong file lượt chưa khớp nhau (run_check R4).
```
*File AI ghi/gửi trong lượt này:* `patch_report.py`, `report_blocks.py`, `drafts.py`

**Xử lý:** [...]

---

## #103 | 18:44 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: kiểm trùng issue. Bước 3 (khung BUG theo mẫu HW02) chưa làm.
- File đã tạo/sửa: HW03/bugs/issues.json (lấy lại, có thêm body/createdAt), HW03/bugs/dup_check.md (mới), HW03/bugs/failed_list.md (chạy lại, chỉ đổi dòng đầu "179 issue, tới #224").
- Kiểm tra: gh auth status = ThachHaoo. Mọi issue dùng làm căn cứ trùng vẫn OPEN.
- Issue mới: snapshot cũ có 158 issue (tới #203), bây giờ 179 (tới #224). Có 21 issue mới, #204–#224, đều của nphoang-itus. henry-banana không có issue nào sau #203.
- 21 issue mới đều thuộc ứng dụng admin (body ghi "Admin cô lập http://localhost:5175"). C2 của SV là web người dùng nên không trùng nhóm nào.
- Đổi mức trùng: không G nào (đây là đề xuất của AI). 28 nhóm vẫn MỚI, 4 trùng một phần, 14 trùng.
- Một số issue cùng loại nhưng khác ứng dụng hoặc khác màn được liệt kê để SV xét: #221 → G-01, #206 → G-04, #209/#121 → G-05, #205/#195 → G-06, #210 → G-07, #222 → G-21/G-22, #219 → G-24. Chi tiết trong dup_check.md §3–4.
- Tiền tố bạn nhóm: nphoang-itus dùng [HW03-C3-xx] cho HW03 ([BUG-FRxx-xx] ở HW02). henry-banana dùng [FRxx-xx], SV dùng [FR-xx], cả hai chỉ có ở HW02.
- File bị bỏ qua: không có. Cả 28 file BUG-58…85.md vẫn đủ 6 dòng 🔒, chưa có chữ SV.
- Commit: e9a2c85 HW03[T1] 5/6c: kiểm trùng issue (khung bug chờ chốt tiền tố). Em đổi message so với lệnh vì phần khung bug chưa làm. Commit khung sẽ dùng message gốc HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02.
- Cần quyết định:
  - PFX – Tiền tố tiêu đề GitHub: (a) giữ [FR-xx] như HW02 của SV; (b) theo bạn nhóm [HW03-C2-xx]; (c) kết hợp, ví dụ [HW03-C2-xx][FR-xx].
  - DUP – SV xác nhận "không đổi mức trùng" cho cả 28 nhóm, nhất là G-16 với #123 (đang ghi "liên quan").
- Việc còn treo từ lượt trước: D1 (1/3b), phần report §3.2/§3.3/§3.5/§3.6/§4.2/§4.3, report_plan mục f, và ghi D1/D2 vào mục e.

===
Báo cáo cho phiên thảo luận

- D1: gen_oracle.py và gen_run.py gắn cứng HW03 (đường dẫn, màn C2, overlay, adb) nên em không chép vào scripts/. SKILL.md ghi "chỉ có ở repo ví dụ". Đã sửa chữ nguồn trong render_checklist.py. .claude/skills và HW03/skills giống nhau hoàn toàn (diff -r = 0). D1, D2 đã ghi vào report_plan mục e.
- Lệch auto/tay CL-09 P1: dòng này đã bỏ khỏi report. merge_runs.py giờ tự bỏ dòng lệch khi quyết định của SV làm kết quả tay trùng auto, và chép nguyên nhân vào notes "[trước quyết định: …]".
- Phát sinh CL-08 P1: sau override R9, auto Passed còn kết quả cuối là Failed, nên thành một dòng lệch mới. Lệch này có thật: auto chấm riêng từng nền tảng, thấy "6.000.000 ₫". Em giữ dòng và ghi nguyên nhân. P1 vẫn 25/46/0/3 (Passed/Failed/N/A/Blocked).
- Marker mới trong report:
  - REPORT:T1:checklist_table cho §3.3 (74 dòng)
  - REPORT:T1:execution cho §3.5, nằm trước bảng tổng: 6 lượt, thứ tự và giờ
  - REPORT:T1:failed_items cho §3.6 (47 item, gồm notes, ảnh, issue trùng / nhóm bug)
  - REPORT:T1:overlay cho §4.3. Bảng ảnh tổng quan chuyển từ §4.1 sang đây; P3 vẫn chưa có ảnh nào.
- AI nháp §3.2 và §4.2: đều mở đầu bằng dòng "📝 AI nháp – SV duyệt/sửa", chỉ dùng dữ kiện có trong repo. Phần khai Audit đã ghi vào report_plan mục f.
- Kiểm tra: check_checklist 0 lỗi; Excel tính lại 21 công thức, 0 lỗi; checklist.md sinh lại (bản cũ còn ghi P1 Passed từ trước 4/6c).
- Commit: 0d8fd34 HW03[Skill] 1/3b: D1 · ad992bc HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2
- Còn chờ: PFX (tiền tố tiêu đề GitHub) để dựng khung BUG-58…85; giờ chạy tay P1 trong file lượt chưa khớp nhau (run_check R4).
```

**Output:**
````
Hai lượt báo cáo đều ổn: D1 hợp lý và dòng lệch CL-08 P1 giữ là đúng. Còn 3 quyết định:

| Mã | Câu hỏi | Phương án | Khuyến nghị |
|---|---|---|---|
| PFX | Tiền tố tiêu đề GitHub | a) `[FR-xx]` như HW02 · b) `[HW03-C2-xx]` theo bạn nhóm · c) `[HW03-C2-xx][FR-xx]` | **b**, với xx = số BUG (58…85). Lý do: cùng quy ước HW03 của nhóm; ảnh trang Issues lọc được bằng một chuỗi `"HW03-C2"` + `author:ThachHaoo`. Với (a), C2 trải nhiều FR nên phải lọc nhiều lần. Số BUG trong tiêu đề còn truy ngược được về file |
| DUP | Giữ "không đổi mức trùng" cho cả 28 nhóm? | a) giữ · b) đổi một số G (ghi G nào → mức nào) | Em quyết. Tiêu chí như HW02: **trùng = cùng app + cùng màn + cùng triệu chứng**. 21 issue mới là app admin, không cùng app nên không trùng. Riêng **G-16 với #123** em đọc kỹ trong `dup_check.md` |
| R4 | Giờ chạy tay P1 trong file lượt không khớp nhau | Em mở `checklist/run_check.md` dòng R4 xem lệch gì | Nếu chỉ là giờ ghi trong file khác giờ thật thì sửa theo giờ thật em nhớ hoặc theo giờ chụp ảnh, ghi "SV chốt". Không đoán |

Em trả lời theo mẫu `PFX=b, DUP=a, R4=<...>` rồi dán lệnh này (thay đúng các chỗ `<...>`):

```
NHIỆM VỤ: dựng khung BUG-58…85 (bước 3 lệnh trước, message gốc). SV chốt: PFX=<...> (nếu b: tiền tố [HW03-C2-<số BUG>]); DUP=<...>; R4=<...>. Còn <...> → DỪNG. Ghi PFX, DUP, R4 vào report_plan mục e. Không push, không amend, KHÔNG viết chữ SV.
1. Làm bước 3 lệnh trước (khung theo mẫu d0d0e05:HW02/bugs/BUG-22.md, sinh bằng script, BUG-80 có P1); dòng "Tiền tố GitHub" theo PFX. Nhóm DUP đổi thành trùng → không sinh khung, ghi lại trong bug_groups/failed_list, đánh lại số BUG KHÔNG được (giữ khoảng trống số, ghi lý do).
2. R4: sửa theo SV chốt, chạy lại chuỗi report nếu giờ hiện trong report.
Commit `HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02` (+ `HW03[T1] 4/6d: R4` nếu có sửa).
Báo cáo ≤ 10 dòng: số khung sinh, số dòng <SV viết> mỗi file, hash. Rồi push giúp? KHÔNG – SV tự push.
```

Khung xong thì em push và viết bug theo lô 7 file. Mỗi lô commit và push xong, báo anh để anh kiểm dữ kiện trên repo.

Ảnh `P3_M*` vẫn là phần duy nhất Task 3 còn thiếu, P3 hiện chưa có ảnh tổng quan nào. Em làm xen trong lúc Claude Code chạy lệnh.
````

**Xử lý:** [...]

---

## #104 | 18:47 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
PFX=B; DUP=a; R4=phần jpg do mình lấy từ điện thoại, còn png là do chụp screenshot từ máy tính, nếu thấy thiếu ảnh nào cứ kêu tôi chụp thêm.
```

**Output:**
````
Câu trả lời R4 của em là giải thích nguồn gốc ảnh, chưa phải một mốc giờ. Anh đưa nó vào lệnh như căn cứ: Claude Code lấy giờ từ ảnh (EXIF với .jpg điện thoại, mtime với .png máy tính) để xác định giờ thật của lượt tay P1. Suy không ra thì nó liệt kê, không đoán. Ảnh nào thiếu nó cũng liệt kê để em chụp thêm.

Dán cho Claude Code:

```
NHIỆM VỤ: dựng khung BUG-58…85 (bước 3 lệnh trước, message gốc). SV chốt: PFX=b → tiền tố GitHub [HW03-C2-<số BUG>] (vd [HW03-C2-58]); DUP=a (giữ nguyên mức trùng cả 28 nhóm, kể cả G-16 ↔ #123 = liên quan); R4: SV giải thích ".jpg là ảnh lấy từ điện thoại, .png là ảnh chụp màn hình máy tính". Ghi PFX, DUP, R4 vào report_plan mục e. Không push, không amend, KHÔNG viết chữ SV.
1. Bước 3 lệnh trước: sinh khung theo mẫu d0d0e05:HW02/bugs/BUG-22.md bằng script (BUG-80 có P1); dòng "Tiền tố GitHub: [HW03-C2-xx]".
2. R4: dựa vào giải thích SV, lấy giờ thật lượt tay P1 từ ảnh (EXIF DateTimeOriginal cho .jpg nếu còn trong bản gốc evidence_raw, mtime cho .png). Khớp được → sửa giờ trong file lượt/report, ghi "SV giải thích R4 + giờ lấy từ ảnh <tên>". Không suy được → giữ nguyên, ghi vào run_check R4 lý do, KHÔNG đoán.
3. Liệt kê ảnh còn thiếu so với RUN.md/report (mọi nền tảng, gồm 5 ảnh P3_M*): tên file cần có, item, nền tảng, nội dung cần thấy trong ảnh. Ghi HW03/checklist/missing_photos.md.
Commit `HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02` (+ `HW03[T1] 4/6d: R4` nếu có sửa).
Báo cáo ≤ 12 dòng: số khung sinh, R4 kết quả, danh sách ảnh thiếu (tên), hash.
```

Xong lệnh này thì em làm theo thứ tự:
1. Push.
2. Chụp các ảnh trong `missing_photos.md`, nhớ overlay email.
3. Viết bug lô 1, BUG-58…64.
````

**Xử lý:** [...]

---

## #105 | 18:48 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: dựng khung BUG-58…85 (bước 3 lệnh trước, message gốc). SV chốt: PFX=b → tiền tố GitHub [HW03-C2-<số BUG>] (vd [HW03-C2-58]); DUP=a (giữ nguyên mức trùng cả 28 nhóm, kể cả G-16 ↔ #123 = liên quan); R4: SV giải thích ".jpg là ảnh lấy từ điện thoại, .png là ảnh chụp màn hình máy tính". Ghi PFX, DUP, R4 vào report_plan mục e. Không push, không amend, KHÔNG viết chữ SV.
1. Bước 3 lệnh trước: sinh khung theo mẫu d0d0e05:HW02/bugs/BUG-22.md bằng script (BUG-80 có P1); dòng "Tiền tố GitHub: [HW03-C2-xx]".
2. R4: dựa vào giải thích SV, lấy giờ thật lượt tay P1 từ ảnh (EXIF DateTimeOriginal cho .jpg nếu còn trong bản gốc evidence_raw, mtime cho .png). Khớp được → sửa giờ trong file lượt/report, ghi "SV giải thích R4 + giờ lấy từ ảnh <tên>". Không suy được → giữ nguyên, ghi vào run_check R4 lý do, KHÔNG đoán.
3. Liệt kê ảnh còn thiếu so với RUN.md/report (mọi nền tảng, gồm 5 ảnh P3_M*): tên file cần có, item, nền tảng, nội dung cần thấy trong ảnh. Ghi HW03/checklist/missing_photos.md.
Commit `HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02` (+ `HW03[T1] 4/6d: R4` nếu có sửa).
Báo cáo ≤ 12 dòng: số khung sinh, R4 kết quả, danh sách ảnh thiếu (tên), hash.
```

**Output:**
```
Trước khi sinh khung, xử lý R4 (giờ lượt tay P1) vì khung sẽ ghi giờ chạy.

Ảnh P1 đều là `.png` (mtime). Ảnh item P1 có mtime từ 23:24 09/11 đến 00:10 10/11, khớp với giờ bắt đầu 22:58 09/11. Không có `.jpg` nên không dùng EXIF.

P2 kiểm chéo khớp (mtime ảnh 00:13–00:36, file lượt ghi 00:10–00:38), nên dùng mtime được. Sửa header P1.

Giờ viết script sinh khung bug.

Write generator script.

Ghi missing_photos.md rồi commit.

Đã sinh lại 28 khung bug theo mẫu HW02, sửa giờ R4 từ ảnh, và lập danh sách ảnh thiếu. Không push, không amend, không viết chữ SV.

### Báo cáo cho phiên thảo luận
- **Khung bug:** sinh lại 28 khung BUG-58…85 bằng `tools/bug_skeleton_hw03.py`. Không file nào bị bỏ qua: cả 28 vẫn còn đủ 🔒, chưa có chữ SV.
  - Mỗi khung có dòng "Tiền tố GitHub: [HW03-C2-xx]". Tiêu đề, Severity, Priority, Tiền điều kiện, Các bước, Expected của bug, Actual, Nhận định để `<SV viết>`.
  - 14 khung có câu SRS chép nguyên văn từ README @ de0f48f, gắn nhãn "(AI chép nguyên văn)". Khung căn cứ heuristic chỉ chép căn cứ + giả định.
  - BUG-80 có thêm P1.
- **R4 đã sửa:** ảnh P1 đều là `.png` nên lấy giờ từ mtime ảnh gốc trong `evidence_raw/P1_chrome`. Ảnh item từ 23:24 09/11 đến 00:10 10/11 (`P1_CL-64_1`).
  - File lượt P1 giờ ghi: kết thúc 00:10 10/11, restart 22:56 09/11 (vì restart phải trước ảnh đầu tiên). Giờ bản gốc vẫn giữ trong dòng ghi chú.
  - Kiểm chéo cách lấy giờ: mtime ảnh P2 (00:13–00:36) khớp giờ file lượt P2 (00:10–00:38).
  - Đã cập nhật run_check R4 và report §3.5.
- **Ảnh còn thiếu (bắt buộc):** `P3_M1_1`, `P3_M2_1`, `P3_M2_2`, `P3_M3_1` (dùng lại cho M5), `P3_M4_1`. Bản gốc `.jpg` có trong `evidence_raw/P3_android/` nhưng chưa overlay. Ảnh item Failed không thiếu cái nào.
- **Ghi thêm (không bắt buộc), trong `HW03/checklist/missing_photos.md`:**
  - `RUN.md` ghi "bắt buộc" ảnh `P1/P2/P3_M6_1` ở tiêu đề nhóm M6, ngược với mục 2 của chính nó (chỉ M1…M5).
  - File lượt P3 trỏ tới `P3_CL-64_1.jpg` nhưng file không có (CL-64 Blocked, đã có `P3_CL-64_2.png`).
- PFX, DUP, R4 đã ghi vào `report_plan` mục e.
- **Commit:** `4b4c64c` HW03[T1] 4/6d: R4 · `9ede85b` HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02
- **Cần quyết định:** M6 – Ảnh `P*_M6_1` (nhóm "Chung – tất cả màn C2"): (a) bỏ, vì M6 không phải một màn; (b) chụp.
```
*File AI ghi/gửi trong lượt này:* `bug_skeleton_hw03.py`, `missing_photos.md`

**Xử lý:** [...]

---

## #106 | 18:52 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Khung bug: sinh lại 28 khung BUG-58…85 bằng tools/bug_skeleton_hw03.py. Không file nào bị bỏ qua: cả 28 vẫn còn đủ 🔒, chưa có chữ SV.
  - Mỗi khung có dòng "Tiền tố GitHub: [HW03-C2-xx]". Tiêu đề, Severity, Priority, Tiền điều kiện, Các bước, Expected của bug, Actual, Nhận định để <SV viết>.
  - 14 khung có câu SRS chép nguyên văn từ README @ de0f48f, gắn nhãn "(AI chép nguyên văn)". Khung căn cứ heuristic chỉ chép căn cứ + giả định.
  - BUG-80 có thêm P1.
- R4 đã sửa: ảnh P1 đều là .png nên lấy giờ từ mtime ảnh gốc trong evidence_raw/P1_chrome. Ảnh item từ 23:24 09/11 đến 00:10 10/11 (P1_CL-64_1).
  - File lượt P1 giờ ghi: kết thúc 00:10 10/11, restart 22:56 09/11 (vì restart phải trước ảnh đầu tiên). Giờ bản gốc vẫn giữ trong dòng ghi chú.
  - Kiểm chéo cách lấy giờ: mtime ảnh P2 (00:13–00:36) khớp giờ file lượt P2 (00:10–00:38).
  - Đã cập nhật run_check R4 và report §3.5.
- Ảnh còn thiếu (bắt buộc): P3_M1_1, P3_M2_1, P3_M2_2, P3_M3_1 (dùng lại cho M5), P3_M4_1. Bản gốc .jpg có trong evidence_raw/P3_android/ nhưng chưa overlay. Ảnh item Failed không thiếu cái nào.
- Ghi thêm (không bắt buộc), trong HW03/checklist/missing_photos.md:
  - RUN.md ghi "bắt buộc" ảnh P1/P2/P3_M6_1 ở tiêu đề nhóm M6, ngược với mục 2 của chính nó (chỉ M1…M5).
  - File lượt P3 trỏ tới P3_CL-64_1.jpg nhưng file không có64_2.png).
- PFX, DUP, R4 đã ghi vào report_plan mục e.
- Commit: 4b4c64c HW03[T1] 4/6d: R4 · 9ede85b HW03[T1] 5/6cg theo mẫu HW02
- Cần quyết định: M6 – Ảnh P*_M6_1 (nhóm "Chung – tất cả màn C2"): (a) bỏ, vì M6 không phải một màn; (b) chụp.
```

**Output:**
````
Khung ổn, R4 kiểm chéo bằng P2 là đủ chắc.

**M6 = a (khuyến nghị):** M6 là nhóm "Chung – tất cả màn C2", không phải một màn. Mục 2 của RUN.md cũng chỉ yêu cầu ảnh M1…M5. Lỗi nằm ở tiêu đề nhóm trong RUN.md do AI viết, nên sửa RUN.md và khai Audit, không cần chụp thêm. Nếu em muốn khác thì trả lời `M6=b`.

**Việc của em bây giờ:**
1. **Push** (repo đang có 5–6 commit chưa push).
2. **Overlay 5 ảnh:** `P3_M1_1, P3_M2_1, P3_M2_2, P3_M3_1, P3_M4_1`. Bản gốc .jpg đang ở `evidence_raw/P3_android/` trên máy em; mở bằng Paint/Photos, hoặc chép sang điện thoại sửa rồi chép lại. Overlay đúng dòng `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn`, ghi đè vào cùng thư mục, cùng tên.
3. Xong thì dán lệnh dưới cho Claude Code, rồi bắt đầu viết bug lô 1 (BUG-58…64).

```
NHIỆM VỤ: ảnh tổng quan P3 + dọn RUN.md. SV chốt M6=a (bỏ ảnh P*_M6_1 vì M6 không phải một màn; sửa tiêu đề nhóm M6 trong RUN.md cho khớp mục 2, ghi report_plan mục e + mục f "lỗi RUN.md do AI"). Không push, không amend.
1. SV đã overlay 5 ảnh P3_M1_1, P3_M2_1, P3_M2_2, P3_M3_1, P3_M4_1 trong checklist/evidence_raw/P3_android/. Mở xem từng ảnh: có dòng overlay "23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn", thấy trình duyệt + URL localhost, không lộ thông tin khác (tài khoản lưu, Gmail, thông báo riêng). Ảnh nào không đạt → DỪNG, báo tên + lý do.
2. Đạt → `python tools/compress_hw03.py --exclude ""` → chạy lại report (bảng ảnh §4.3 hết "chưa có").
3. Tham chiếu P3_CL-64_1.jpg không tồn tại: nếu ảnh cùng item đã có (tên khác) thì sửa tham chiếu về file thật, ghi notes; không có thì liệt kê, KHÔNG tự tạo.
Commit `HW03[T1] 4/6e: ảnh tổng quan P3 + M6`.
Báo cáo ≤ 8 dòng: 5 ảnh đạt/không, §4.3 còn ô trống không, CL-64, hash.
```

Sau lệnh này, Task 3 coi như xong. Phần còn lại của T1/T3 là 28 bug của em và §3.4 (🔒).
````

**Xử lý:** [...]

---

## #107 | 18:54 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: ảnh tổng quan P3 + dọn RUN.md. SV chốt M6=a (bỏ ảnh P*_M6_1 vì M6 không phải một màn; sửa tiêu đề nhóm M6 trong RUN.md cho khớp mục 2, ghi report_plan mục e + mục f "lỗi RUN.md do AI"). Không push, không amend.
1. SV đã overlay 5 ảnh P3_M1_1, P3_M2_1, P3_M2_2, P3_M3_1, P3_M4_1 trong checklist/evidence_raw/P3_android/. Mở xem từng ảnh: có dòng overlay "23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn", thấy trình duyệt + URL localhost, không lộ thông tin khác (tài khoản lưu, Gmail, thông báo riêng). Ảnh nào không đạt → DỪNG, báo tên + lý do.
2. Đạt → `python tools/compress_hw03.py --exclude ""` → chạy lại report (bảng ảnh §4.3 hết "chưa có").
3. Tham chiếu P3_CL-64_1.jpg không tồn tại: nếu ảnh cùng item đã có (tên khác) thì sửa tham chiếu về file thật, ghi notes; không có thì liệt kê, KHÔNG tự tạo.
Commit `HW03[T1] 4/6e: ảnh tổng quan P3 + M6`.
Báo cáo ≤ 8 dòng: 5 ảnh đạt/không, §4.3 còn ô trống không, CL-64, hash.
```

**Output:**
```
Em dừng ở bước 1: cả 5 ảnh tổng quan P3 đều chưa đạt nên chưa nén, chưa chạy lại report, chưa sửa RUN.md và CL-64, chưa commit gì.

### Báo cáo cho phiên thảo luận
- **5 ảnh P3_M\* chưa đạt:** `P3_M1_1`, `P3_M2_1`, `P3_M2_2`, `P3_M3_1`, `P3_M4_1` (.jpg trong `evidence_raw/P3_android/`) **đều không có dòng overlay** "23120255 - Lê Tấn Hiệp - …".
  - Giờ sửa file của cả 5 vẫn là 01:53 10/11, tức là chưa được lưu lại sau khi chụp. Có thể bản overlay đang nằm ở chỗ khác trên điện thoại hoặc trong thư mục khác.
  - Phần còn lại đạt: thấy thanh URL `localhost:5173/...` (Chrome Android), không lộ thông tin riêng. Chỉ hiện `test@eshop.com` (tài khoản seed) và "Test User".
- **P3_M4_1:** ảnh hiện "Bạn chưa có đơn hàng nào" (Lịch sử đơn trống) và gần trùng `P3_M3_1` (cùng `/profile`, chỉ cuộn xuống). Nếu cần ảnh có ≥ 1 đơn như các nền tảng khác thì phải chụp lại sau khi chạy `seed_orders.py`.
- **§4.3:** P3 vẫn "chưa có" ở M1–M5, vì chưa nén.
- **CL-64 P3 (chỉ đọc, chưa sửa):** file lượt P3 dòng 21 trỏ `P3_CL-64_1.jpg` và `P3_CL-64_2.jpg`. Chỉ có `_2` (raw `.jpg`, bản nén `.png`); `P3_CL-64_1` không có ở thư mục nào nên không có file để sửa tham chiếu về.
- **M6 (sửa RUN.md, ghi report_plan e/f):** chưa làm, sẽ làm cùng commit `HW03[T1] 4/6e: ảnh tổng quan P3 + M6`.
- **Commit:** không có.
- **Cần quyết định:**
  - IMG – Thêm overlay cho 5 ảnh rồi lưu đè vào `evidence_raw/P3_android/` (tên giữ nguyên), hoặc chỉ đường dẫn bản đã overlay.
  - M6 – Làm trước phần M6 + CL-64 rồi commit riêng, hay chờ có ảnh?
```

**Xử lý:** [...]

---

## #108 | 18:55 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- 5 ảnh P3_M* chưa đạt: P3_M1_1, P3_M2_1, P3_M2_2, P3_M3_1, P3_M4_1 (.jpg trong evidence_raw/P3_android/) đều không có dòng overlay "23120255 - Lê Tấn Hiệp - …".
  - Giờ sửa file của cả 5 vẫn là 01:53 10/11, tức là chưa được lưu lại sau khi chụp. Có thể bản overlay đang nằm ở chỗ khác trên điện thoại hoặc trong thư mục khác.
  - Phần còn lại đạt: thấy thanh URL localhost:5173/... (Chrome Android), không lộ thông tin riêng. Chỉ hiện test@eshop.com (tài khoản seed) và "Test User".
- P3_M4_1: ảnh hiện "Bạn chưa có đơn hàng nào" (Lịch sử đơn trống) và gần trùng P3_M3_1 (cùng /profile, chỉ cuộn xuống). Nếu cần ảnh có ≥ 1 đơn như các nền tảng khác thì phải chụp lại sau khi chạy seed_ord
- §4.3: P3 vẫn "chưa có" ở M1–M5, vì chưa nén.
- CL-64 P3 (chỉ đọc, chưa sửa): file lượt P3 dòng 21 trỏ P3_CL-64_1.jpg và P3_CL-64_2.jpg. Chỉ có _2 (raw .jpg, bản nén .png); P3_CL-64_1 không có ở thư mục nào nên không có file để sửa tham chiếu về.
- M6 (sửa RUN.md, ghi report_plan e/f): chưa làm, sẽ làm cùng commit HW03[T1] 4/6e: ảnh tổng quan P3 + M6.
- Commit: không có.
- Cần quyết định:
  - IMG – Thêm overlay cho 5 ảnh rồi lưu đè vào evidence_ra), hoặc chỉ đường dẫn bản đã overlay.
  - M6 – Làm trước phần M6 + CL-64 rồi commit riêng, hay chờ có ảnh?
```

**Output:**
````
Ảnh chưa đạt vì em chưa overlay: giờ sửa file vẫn là 01:53 sáng nay. Phần overlay phải do em làm, không giao cho Claude Code được: AI-01 xếp ảnh có username vào danh mục chống gian lận, AI không được tạo.

**Quyết định**
- **IMG:** em overlay 5 ảnh rồi lưu đè đúng tên vào `evidence_raw/P3_android/`. Trên PC chỉ cần Paint: mở ảnh → Text → gõ dòng `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn` → Ctrl+S. Mỗi ảnh khoảng 1 phút.
- **P3_M4_1 (Lịch sử đơn trống):** khuyến nghị **giữ**. Ảnh vẫn là màn M4, đủ cho mục đích ảnh tổng quan nền tảng. Chụp lại sẽ phải dựng lại SUT, adb reverse và seed_orders, mất 15–20 phút. Ghi notes "P3: lịch sử đơn trống lúc chụp". Nếu em muốn đồng bộ với P1/P2 thì trả lời `M4=chụp lại`.
- **M6 + CL-64:** làm ngay, commit riêng, không chờ ảnh. Với CL-64: bỏ tham chiếu `_1` không tồn tại, giữ `_2`. Việc này chỉ là sửa đường dẫn trỏ sai, không tạo bằng chứng mới.

Dán cho Claude Code luôn:

```
SV chốt: M6 làm ngay (commit riêng `HW03[T1] 4/6e: M6 + tham chiếu CL-64`); CL-64 P3: bỏ tham chiếu P3_CL-64_1.jpg (file không tồn tại ở đâu), giữ _2, ghi notes "ảnh _1 không có; chỉ _2" + run_check; P3_M4_1 giữ ảnh Lịch sử đơn trống, ghi notes "lịch sử đơn trống lúc chụp". Ghi report_plan e/f. Không push, không amend.
Sau đó DỪNG chờ SV báo đã overlay 5 ảnh, rồi mới làm bước 1–2 của lệnh trước (commit `HW03[T1] 4/6f: ảnh tổng quan P3`).
Báo cáo ≤ 5 dòng + hash.
```

Overlay xong thì em gõ cho Claude Code một câu "đã overlay 5 ảnh, làm tiếp", rồi chuyển sang viết bug.
````

**Xử lý:** [...]

---

## #109 | 18:56 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
SV chốt: M6 làm ngay (commit riêng `HW03[T1] 4/6e: M6 + tham chiếu CL-64`); CL-64 P3: bỏ tham chiếu P3_CL-64_1.jpg (file không tồn tại ở đâu), giữ _2, ghi notes "ảnh _1 không có; chỉ _2" + run_check; P3_M4_1 giữ ảnh Lịch sử đơn trống, ghi notes "lịch sử đơn trống lúc chụp". Ghi report_plan e/f. Không push, không amend.
Sau đó DỪNG chờ SV báo đã overlay 5 ảnh, rồi mới làm bước 1–2 của lệnh trước (commit `HW03[T1] 4/6f: ảnh tổng quan P3`).
Báo cáo ≤ 5 dòng + hash.
```

**Output:**
```
Đã xong phần M6, CL-64 và ghi chú P3_M4_1. Em dừng ở đây chờ SV báo đã overlay 5 ảnh.

### Báo cáo cho phiên thảo luận
- **M6:** tiêu đề 3 nhóm M6 trong `RUN.md` giờ ghi "không chụp ảnh tổng quan", khớp mục 2 (chỉ M1…M5). Đã sửa cả `tests/gen_run.py` để sinh lại không ra lỗi cũ. `report_plan` mục e có thêm dòng M6, CL64-P3, M4-P3; mục f ghi "Lỗi RUN.md do AI".
- **CL-64 P3:** đã bỏ tham chiếu `P3_CL-64_1.jpg` khỏi file lượt P3, chỉ còn `_2`. Notes ghi "ảnh _1 không có; chỉ _2". Đã cập nhật `run_check.md` và `missing_photos.md`.
- **P3_M4_1:** report §4.3 ghi "(lịch sử đơn trống lúc chụp)". Ô P3 vẫn là "chưa có" vì 5 ảnh chưa overlay nên chưa nén.
- **Kiểm tra:** chạy lại chuỗi gộp và report, không còn cảnh báo thiếu ảnh CL-64.
- **Commit:** `f6e85c3` HW03[T1] 4/6e: M6 + tham chiếu CL-64. Commit `4/6f` sẽ làm sau khi SV báo đã overlay.
```

**Xử lý:** [...]

---

## #110 | 18:58 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
overlay 5 ảnh nào đây nhỉ
```

**Output:**
```
Đây là 5 ảnh tổng quan màn hình chụp trên điện thoại (P3 = Chrome Android, POCO F5). Trên máy em, chúng nằm ở:

`HW03\checklist\evidence_raw\P3_android\`

| File | Màn |
|---|---|
| `P3_M1_1.jpg` | Đăng nhập |
| `P3_M2_1.jpg` | Quên mật khẩu – bước 1 |
| `P3_M2_2.jpg` | Quên mật khẩu – bước 2 |
| `P3_M3_1.jpg` | Hồ sơ (dùng lại cho M5 Navbar) |
| `P3_M4_1.jpg` | Lịch sử đơn (đang trống, giữ nguyên) |

Cách làm với từng file:
1. Mở bằng Paint.
2. Chọn công cụ Text (chữ A) và gõ đúng dòng `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn`. Đặt ở chỗ không che nội dung, ví dụ mép dưới, chữ đủ to để đọc được.
3. Lưu đè bằng Ctrl+S, giữ nguyên tên và định dạng .jpg.

Xong cả 5 file thì gõ cho Claude Code: "đã overlay 5 ảnh, làm tiếp".
```

**Xử lý:** [...]

---

## #111 | 19:02 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
overlay xong 5 ảnh rồi nhé
```

**Output:**
```
Cả 5 đạt (overlay rõ, URL localhost, Chrome Android, không lộ thông tin riêng). Nén + chạy lại report.

Em đã xem từng ảnh: cả 5 ảnh tổng quan P3 đều đạt, đã nén và đưa vào report.

### Báo cáo cho phiên thảo luận
- **5 ảnh đạt:** `P3_M1_1`, `P3_M2_1`, `P3_M2_2`, `P3_M3_1`, `P3_M4_1`. Ảnh nào cũng có dòng overlay "23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn", thấy thanh URL `localhost:5173/...` trên Chrome Android, không lộ thông tin riêng (chỉ có tài khoản seed `test@eshop.com`).
  - Ở `P3_M3_1`, dòng overlay đè nhẹ lên tiêu đề "Hồ sơ của bạn" nhưng vẫn đọc được.
  - Ở `P3_M4_1`, overlay nằm ngay trên khung Lịch sử đơn.
- **Nén:** `tools/compress_hw03.py` đã tạo 5 file `.png` trong `evidence/P3_android/`. Chạy lại report thì §4.3 không còn ô "chưa có"; P3 M4 có ghi chú "(lịch sử đơn trống lúc chụp)". Đã cập nhật `missing_photos.md` (không còn ảnh thiếu) và `report_plan` mục f.
- **Commit:** `6069790` HW03[T1] 4/6f: ảnh tổng quan P3
```

**Xử lý:** [...]

---

## #112 | 19:03 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Em đã xem từng ảnh: cả 5 ảnh tổng quan P3 đều đạt, đã nén và đưa vào report.

Báo cáo cho phiên thảo luận

- 5 ảnh đạt: P3_M1_1, P3_M2_1, P3_M2_2, P3_M3_1, P3_M4_1. Ảnh nào cũng có dòng overlay "23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn", thấy thanh URL localhost:5173/... trên Chrome Android, không lộ thông tin riêng (chỉ có tài khoản seed test@eshop.com).
  - Ở P3_M3_1, dòng overlay đè nhẹ lên tiêu đề "Hồ sơ của bạn" nhưng vẫn đọc được.
  - Ở P3_M4_1, overlay nằm ngay trên khung Lịch sử đơn.
- Nén: tools/compress_hw03.py đã tạo 5 file .png trong evidence/P3_android/. Chạy lại report thì §4.3 không còn ô "chưa có"; P3 M4 có ghi chú "(lịch sử đơn trống lúc chụp)". Đã cập nhật missing_photos.md (không còn ảnh thiếu) và report_plan mục f.
- Commit: 6069790 HW03[T1] 4/6f: ảnh tổng quan P3
```

**Output:**
````
Task 3 coi như xong: ảnh tổng quan đủ 3 nền tảng, ma trận kết quả có, chỗ lệch có ghi chú.

Một điểm cần kiểm: báo cáo chỉ có commit `6069790` (4/6f), không thấy commit `4/6e: M6 + tham chiếu CL-64`. Em hỏi Claude Code một câu "4/6e đã commit chưa?". Nếu chưa thì bảo nó làm luôn.

**Em làm tiếp, theo thứ tự**
1. **Push.**
2. **Viết bug lô 1, BUG-58…64:** thay mọi `` `<SV viết>` `` trong file. Commit `HW03[T1] 5/6d: SV viết BUG-58…64`, push, báo anh kiểm dữ kiện. Lô sau làm tương tự, mỗi lô 7 file.
3. **§3.4 trong report (🔒):** item em bổ sung và vì sao AI bỏ sót. Dữ kiện ở `checklist/sv_items.md` và `ai_gap_answer.md`.
4. **Video skill:** theo `HW03/skills/demo_plan.md`, giọng em, khoảng 10 phút.

**Song song, Claude Code làm phần đóng gói không cần em:**

```
NHIỆM VỤ: chuẩn bị đóng gói HW03 (phần không cần SV). Không push, không amend, KHÔNG viết phần 🔒 / <SV viết>.
1. Report §5 Task 2: giữ phần plan/kịch bản/công cụ đã có (trỏ usability/plan.md, participant_kit.md, observation_sheet.md); §5.4–5.9 thay bằng 1 dòng "Không thực hiện phiên usability nào" + `<SV viết lý do>`. Không bịa số liệu.
2. README HW03: test summary sinh bằng script (checklist P1/P2/P3, số bug 28 + trùng 14 + một phần 4, link VideoLinks), chỗ tự chấm = `<SV điền>`.
3. Dựng khung AI-02 (artifact lấy từ git: bản đóng băng + việc phụ, cột #n = "[chờ chốt transcript]", verdict/lý do = <SV viết>), AI-03 (khai Opus 5.5 + Sonnet 4.6 + lượt không rõ model theo dòng Tổng của A_prompt_log.md), Mandatory Disclosure §11 (📝 AI nháp – SV xác nhận) theo report_plan mục f, g. Mẫu định dạng: HW02/ai-forms (không chép số liệu). AI-05 CHƯA làm.
4. Thêm Task 2 = <SV điền> vào §12, tên zip chờ điểm.
Commit theo từng việc. Báo cáo ≤ 12 dòng + hash; liệt kê mọi chỗ <SV viết>/<SV điền> còn lại (file:dòng).
```

Viết xong lô bug nào thì báo anh lô đó.
````

**Xử lý:** [...]

---

## #113 | 19:04 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Cho tôi xem tiến độ các task hiện tại (bao gồm cả task 2)
```

**Output:**
```
Tiến độ dưới đây lấy theo các báo cáo của Claude Code tới 19:03. Trên GitHub vẫn chỉ có tới `a46ea4d` (03:41 sáng): **chưa push** khoảng 9 commit của tối nay, em nên push ngay.

**Task 1 – GUI Checklist (30đ): ~70%**

| Hạng mục | Trạng thái |
|---|---|
| Checklist 74 item (AI 48 · Both 20 · SV 6), bản AI đóng băng | ✅ |
| Chạy auto và tay trên P1/P2/P3, gộp kết quả, Excel 0 lỗi | ✅ |
| R9/R11 chốt, P1 mới là 25/46/0/3 | ✅ |
| Kiểm trùng issue (179 issue, tới #224): 28 mới · 4 một phần · 14 trùng | ✅ |
| Khung BUG-58…85 theo mẫu HW02, tiền tố `[HW03-C2-xx]` | ✅ |
| Report §3.3, 3.5, 3.6 (sinh bằng script) | ✅ |
| Report §3.2 (AI nháp) | ⏳ em duyệt và xoá dòng 📝 |
| **Viết 28 bug (🔒)** | ❌ chưa bắt đầu, việc nặng nhất |
| Tái hiện bug, tạo 28 issue, ảnh trang Issues | ❌ phụ thuộc bước trên |
| **Report §3.4: item em bổ sung, vì sao AI bỏ sót (🔒)** | ❌ |

**Task 3 – Cross-platform (20đ): ~95%**

| Hạng mục | Trạng thái |
|---|---|
| 3 nền tảng: Cốc Cốc, Firefox, Chrome Android | ✅ |
| Ma trận kết quả, bảng lệch auto ↔ tay | ✅ |
| Ảnh overlay đủ (gồm 5 ảnh tổng quan P3 vừa xong) | ✅ |
| Report §4.1, §4.3 | ✅ |
| Report §4.2 (AI nháp) | ⏳ em duyệt và xoá dòng 📝 |
| M6 và tham chiếu CL-64 (commit 4/6e) | ❓ chưa thấy báo, cần hỏi Claude Code |

**Task 2 – Usability (40đ): ~15%, chỉ có phần chuẩn bị**

| Hạng mục | Trạng thái |
|---|---|
| Plan (9 phần), kịch bản U1, SUS và SEQ, câu hỏi probe | ✅ (AI nháp, **em chưa duyệt**) |
| Môi trường remote (tunnel), đã thử luồng U1 qua 4G | ✅ |
| Pilot S00 | ❌ |
| 7 phiên, bảng 7 người tham gia | ❌ |
| Kết quả SUS, pain point, findings, bug Task 2 | ❌ |
| Report §5.4–5.9 ghi "không thực hiện" kèm lý do của em | ⏳ trong lệnh vừa gửi Claude Code |

Lưu ý: kit đang là AI nháp mà em chưa duyệt. Nếu nộp làm căn cứ cho 10 điểm Task 2, em nên đọc lướt một lượt, khoảng 15 phút.

**Skill (10đ): ~50%**

| Hạng mục | Trạng thái |
|---|---|
| 2 skill chép vào `HW03/skills/`, tự đủ (D1 đã xử lý) | ✅ |
| VideoLinks.md, demo_plan.md | ✅ |
| **Quay video demo (giọng em) và link YouTube** | ❌ |

**Báo cáo và form: ~20%**

| Hạng mục | Trạng thái |
|---|---|
| README test summary, khung AI-02/AI-03, Mandatory Disclosure | ⏳ Claude Code đang làm |
| Critique 200–300 từ, verdict Audit, điểm tự chấm, ký (em) | ❌ |
| AI-05, PDF, commit log, `hw-submission-audit`, zip | ❌ làm cuối |
| Xuất transcript `_p2` và trích prompt log | ❌ làm trước khi điền #n vào Audit |

**Thời gian còn lại khoảng 15 giờ.** Ước lượng việc của em:
- 28 bug: 3–4 giờ
- §3.4: 30 phút
- Video: 45 phút
- Critique: 30 phút
- Verdict Audit: 1 giờ
- Duyệt §3.2, §4.2, kit Task 2: 30 phút

Tổng khoảng 6–7 giờ, nên vẫn còn dư cho pilot và 1–2 phiên usability nếu em muốn gỡ thêm điểm Task 2 tối nay. Muốn làm thì làm **trước** khi tái hiện bug, vì bước tái hiện sẽ đưa SUT về nhánh main.
```

**Xử lý:** [...]

---

## #114 | 19:04 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: chuẩn bị đóng gói HW03 (phần không cần SV). Không push, không amend, KHÔNG viết phần 🔒 / <SV viết>.
1. Report §5 Task 2: giữ phần plan/kịch bản/công cụ đã có (trỏ usability/plan.md, participant_kit.md, observation_sheet.md); §5.4–5.9 thay bằng 1 dòng "Không thực hiện phiên usability nào" + `<SV viết lý do>`. Không bịa số liệu.
2. README HW03: test summary sinh bằng script (checklist P1/P2/P3, số bug 28 + trùng 14 + một phần 4, link VideoLinks), chỗ tự chấm = `<SV điền>`.
3. Dựng khung AI-02 (artifact lấy từ git: bản đóng băng + việc phụ, cột #n = "[chờ chốt transcript]", verdict/lý do = <SV viết>), AI-03 (khai Opus 5.5 + Sonnet 4.6 + lượt không rõ model theo dòng Tổng của A_prompt_log.md), Mandatory Disclosure §11 (📝 AI nháp – SV xác nhận) theo report_plan mục f, g. Mẫu định dạng: HW02/ai-forms (không chép số liệu). AI-05 CHƯA làm.
4. Thêm Task 2 = <SV điền> vào §12, tên zip chờ điểm.
Commit theo từng việc. Báo cáo ≤ 12 dòng + hash; liệt kê mọi chỗ <SV viết>/<SV điền> còn lại (file:dòng).
```

**Output:**
```
Việc 1: §5.

Việc 2: script test summary cho README (và §8 report, cùng bảng).

Việc 3: script sinh khung AI-02, AI-03, §11.

Sửa: "commit tạo" lấy theo file chính (đường dẫn đầu) thay vì file sớm nhất (vd `restart_backend.ps1` từ HW02).

Việc 4: §12.

Bốn việc đóng gói đã xong, mỗi việc một commit. Không push, không amend, không viết phần 🔒 / `<SV viết>`.

### Báo cáo cho phiên thảo luận
- **Report §5:** giữ nguyên các dòng 📝 cũ của §5.1–5.3, thêm dòng trỏ tới `usability/plan.md`, `participant_kit.md`, `observation_sheet.md`. §5.4–5.9 gộp thành một dòng "Không thực hiện phiên usability nào. Lý do: `<SV viết lý do>`", bỏ luôn 2 marker U1. `c51665d`
- **README + report §8:** test summary sinh bằng `tools/summary_hw03.py`. Số liệu:
  - P1/P2/P3 (Passed/Failed/N/A/Blocked): 25/46/0/3 · 24/47/0/3 · 22/44/4/4
  - item trùng 14, trùng một phần 4, MỚI 28 → 28 bug BUG-58…85; chưa bug nào có link GitHub Issue (0/28)
  - nguồn item: AI 48, AI + SV sửa 20, SV 6; usability: không có phiên
  - link video trỏ `skills/VideoLinks.md`; bảng tự chấm để `<SV điền>`. `70aa585`
- **AI-02, AI-03, §11** (`tools/forms_hw03.py`): `c2aa7ae`
  - AI-02 có 22 artifact, commit tạo/sửa lấy từ git, cột #n = "[chờ chốt transcript]", Verdict/Lý do = `<SV viết>`.
  - AI-03 lấy theo dòng Tổng của prompt log lúc 19:03 10/11: tổng 99 lượt = Sonnet 4.6 2, Opus 5.5 91, không rõ model 6 (#4, #51, #57, #69, #70, #79). Cần chạy lại script sau lần trích prompt log cuối.
  - §11 mở đầu "📝 AI nháp – SV xác nhận", gồm 7 việc AI làm; phần "em xem xét và sửa" / "em tự làm" để `<SV viết>`.
- **Report §12:** bảng tự chấm 4 tiêu chí (gồm Task 2) để `<SV điền>`; tên zip `23120255_HW03_AI_GUIUsability_<ggg>.zip` chờ điểm. `00cea6a`
- **Bất thường:** report §5.3 (dòng 📝 cũ) ghi "SUS / UEQ-S", nhưng plan và participant kit dùng SEQ + SUS.
- **Chỗ `<SV viết>` / `<SV điền>` còn lại:**
  - `HW03/23120255_HW03_Report.md`: 326 (lý do không có phiên), 379, 381 (§11), 394–398 (§12)
  - `HW03/README.md`: 11–15 (tự chấm)
  - `HW03/ai-forms/AI-02_Audit_Report_23120255.md`: 52 (S3: link video), 64–85 (Verdict/Lý do 22 hàng), 89 (kết luận chung)
  - `HW03/ai-forms/AI-03_Disclosure_Form_23120255.md`: 34, 44, 50 và mục 5 (cách rà soát)
  - `HW03/skills/VideoLinks.md`: 5, 6
  - `HW03/bugs/BUG-58…85.md`: mỗi file 8 chỗ
  - Ngoài ra còn các dòng 📝 cũ trong report (§3.1, §4.1, §5.1–5.3, §7, §9, §13D) và `[...]` ở Ngày / Chữ ký / Cam đoan của AI-02, AI-03.
```
*File AI ghi/gửi trong lượt này:* `summary_hw03.py`, `forms_hw03.py`

**Xử lý:** [...]

---

## #115 | 19:09 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Report §5: giữ nguyên các dòng 📝 cũ của §5.1–5.3, thêm dòng trỏ tới usability/plan.md, participant_kit.md, observation_sheet.md. §5.4–5.9 gộp thành một dòng "Không thực hiện phiên usability nào. Lý do: <SV viết lý do>", bỏ luôn 2 marker U1. c51665d
- README + report §8: test summary sinh bằng tools/summary_hw03.py. Số liệu:
  - P1/P2/P3 (Passed/Failed/N/A/Blocked): 25/46/0/3 · 24/47/0/3 · 22/44/4/4
  - item trùng 14, trùng một phần 4, MỚI 28 → 28 bug BUG-58…85; chưa bug nào có link GitHub Issue (0/28)
  - nguồn item: AI 48, AI + SV sửa 20, SV 6; usability: không có phiên
  - link video trỏ skills/VideoLinks.md; bảng tự chấm để <SV điền>. 70aa585
- AI-02, AI-03, §11 (tools/forms_hw03.py): c2aa7ae
  - AI-02 có 22 artifact, commit tạo/sửa lấy từ git, cột #n = "[chờ chốt transcript]", Verdict/Lý do = <SV viết>.
  - AI-03 lấy theo dòng Tổng của prompt log lúc 19:03 10/11: tổng 99 lượt = Sonnet 4.6 2, Opus 5.5 91, không rõ model 6 (#4, #51, #57, #69, #70, #79). Cần chạy lại script sau lần trích prompt log cuối.
  - §11 mở đầu "📝 AI nháp – SV xác nhận", gồm 7 việc AI làm; phần "em xem xét và sửa" / "em tự làm" để <SV viết>.
- Report §12: bảng tự chấm 4 tiêu chí (gồm Task 2) để <SV điền>; tên zip 23120255_HW03_AI_GUIUsability_<ggg>.zip chờ điểm. 00cea6a
- Bất thường: report §5.3 (dòng 📝 cũ) ghi "SUS / UEQ-S", nhưng plan và participant kit dùng SEQ + SUS.
- Chỗ <SV viết> / <SV điền> còn lại:
  - HW03/23120255_HW03_Report.md: 326 (lý do không có phiên), 379, 381 (§11), 394–398 (§12)
  - HW03/README.md: 11–15 (tự chấm)
  - HW03/ai-forms/AI-02_Audit_Report_23120255.md: 52 (S3: l do 22 hàng), 89 (kết luận chung)
  - HW03/ai-forms/AI-03_Disclosure_Form_23120255.md: 34, 44, 50 và mục 5 (cách rà soát)
  - HW03/skills/VideoLinks.md: 5, 6
  - HW03/bugs/BUG-58…85.md: mỗi file 8 chỗ
  - Ngoài ra còn các dòng 📝 cũ trong report (§3.1, §4.1, §5.1–5.3, §7, §9, §13D) và [...] ở Ngày / Chữ ký / Cam đoan của AI-02, AI-03.
===
Sao có ảnh này chưa commit nhỉ
```

**Output:**
````
Anh không thấy ảnh nào đính kèm trong tin nhắn này, có thể bị rơi khi gửi. Em dán lại ảnh, hoặc dán output của:

```
git status --short
```

Nếu đó là file ảnh untracked, thường có 3 khả năng:
1. **Ảnh gốc trong `evidence_raw/`:** bị gitignore có chủ đích, không commit (bài học B5: ảnh gốc có thể lộ thông tin). Trường hợp này `git status` không hiện nó.
2. **Ảnh nén trong `evidence/` mà script không `git add`:** cần commit. Bảo Claude Code kiểm xem report có trỏ tới ảnh đó không rồi commit.
3. **Ảnh lẻ em vừa chụp hoặc ảnh tạm** (ví dụ chụp màn hình Paint lúc overlay): không thuộc bài thì xoá hoặc bỏ qua.

Gửi tên file hoặc ảnh, anh nói cụ thể là loại nào.

Về báo cáo vừa rồi: §5.3 ghi "SUS / UEQ-S" là sai so với plan, vì plan dùng SEQ + SUS. Đây là dòng 📝 cũ nên em sửa thành "SEQ + SUS" khi duyệt §5, hoặc bảo Claude Code sửa vì đó là dữ kiện chứ không phải chữ của em.
````

**Xử lý:** [...]

---

## #116 | 19:09 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
PS D:\HK7\Testing\Exercise\HW\software-testing-2627> git status --short
 M HW03/appendix/A_prompt_log.md
?? HW03/checklist/evidence/P3_android/P3_M2_2.png
===
bảo Claude Code sửa nhé, mà cái đó là của task 2 nhỉ
```

**Output:**
````
Đúng, §5.3 thuộc Task 2: nó là phần "Công cụ: thang đo + câu hỏi probe" của usability.

Còn `P3_M2_2.png` là 1 trong 5 ảnh tổng quan P3 vừa nén (Quên mật khẩu bước 2). Commit `6069790` bỏ sót file này, trong khi report §4.3 đã trỏ tới nó. Không commit thì ảnh không vào zip (`git archive` chỉ lấy file đã commit), và report sẽ có link ảnh hỏng.

`A_prompt_log.md` (M) là hook Stop tự trích sau mỗi lượt, bình thường. Commit riêng là được.

Dán cho Claude Code:

```
1. P3_M2_2.png (evidence/P3_android) chưa được add trong 6069790 → kiểm 4 ảnh còn lại đã tracked, report §4.3 trỏ đúng; add + commit `HW03[T1] 4/6g: thêm ảnh P3_M2_2 bị sót`. Tìm vì sao sót (compress_hw03.py có git add không, hay add theo danh sách) – nếu do script thì vá, commit riêng `HW03: vá harness – compress_hw03 add đủ ảnh`.
2. Report §5.3: sửa "SUS / UEQ-S" → "SEQ + SUS" cho khớp usability/plan.md (dữ kiện, không phải chữ SV). Commit `HW03[T2]: sửa thang đo §5.3`.
3. Commit prompt log: `HW03: cập nhật prompt log`.
4. `git status --short` phải sạch. Không push, không amend.
Báo cáo ≤ 6 dòng: nguyên nhân sót ảnh, hash.
```

Sau đó em push, rồi bắt đầu viết bug lô 1.
````

**Xử lý:** [...]

---

## #117 | 19:10 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. P3_M2_2.png (evidence/P3_android) chưa được add trong 6069790 → kiểm 4 ảnh còn lại đã tracked, report §4.3 trỏ đúng; add + commit `HW03[T1] 4/6g: thêm ảnh P3_M2_2 bị sót`. Tìm vì sao sót (compress_hw03.py có git add không, hay add theo danh sách) – nếu do script thì vá, commit riêng `HW03: vá harness – compress_hw03 add đủ ảnh`.
2. Report §5.3: sửa "SUS / UEQ-S" → "SEQ + SUS" cho khớp usability/plan.md (dữ kiện, không phải chữ SV). Commit `HW03[T2]: sửa thang đo §5.3`.
3. Commit prompt log: `HW03: cập nhật prompt log`.
4. `git status --short` phải sạch. Không push, không amend.
Báo cáo ≤ 6 dòng: nguyên nhân sót ảnh, hash.
```

**Output:**
```
Script không add (không có lệnh git) → lỗi do lệnh add tay của em, không vá harness. Giờ §5.3.

sed không khớp (UTF-8), commit §5.3 chưa tạo. Sửa bằng Python.

Đã thêm ảnh bị sót, sửa §5.3 và commit prompt log; `git status --short` hiện sạch.

### Báo cáo cho phiên thảo luận
- **Vì sao sót `P3_M2_2.png`:** lỗi ở lệnh add tay của em, không phải do script. Em add bằng mẫu `P3_M*_1.png` nên không khớp file `_2`. `compress_hw03.py` không chạy lệnh git nào, nên không vá harness. 4 ảnh còn lại đã được commit từ `6069790`; report §4.3 dòng 296 trỏ đúng `P3_M2_1`, `P3_M2_2`.
- **Commit:** `df6a396` HW03[T1] 4/6g: thêm ảnh P3_M2_2 bị sót · `62280b4` HW03[T2]: sửa thang đo §5.3 (giờ ghi "SEQ + SUS (`usability/plan.md` mục 8)") · `5fddef5` HW03: cập nhật prompt log
- **Thứ tự commit khác lệnh:** lần sửa §5.3 đầu bằng `sed` không khớp nên commit sau prompt log.
- **Lưu ý:** hook Stop sẽ sinh lại `A_prompt_log.md` sau lượt này, nên trước khi zip cần commit prompt log thêm một lần.
```

**Xử lý:** [...]

---

## #118 | 19:11 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đã thêm ảnh bị sót, sửa §5.3 và commit prompt log; git status --short hiện sạch.

Báo cáo cho phiên thảo luận

- Vì sao sót P3_M2_2.png: lỗi ở lệnh add tay của em, không phải do script. Em add bằng mẫu P3_M*_1.png nên không khớp file _2. compress_hw03.py không chạy lệnh git nào, nên không vá harness. 4 ảnh còn lại đã được commit từ 6069790; report §4.3 dòng 296 trỏ đúng P3_M2_1, P3_M2_2.
- Commit: df6a396 HW03[T1] 4/6g: thêm ảnh P3_M2_2 bị sót · 62280b4 HW03[T2]: sửa thang đo §5.3 (giờ ghi "SEQ + SUS (usability/plan.md mục 8)") · 5fddef5 HW03: cập nhật prompt log
- Thứ tự commit khác lệnh: lần sửa §5.3 đầu bằng sed không khớp nên commit sau prompt log.
- Lưu ý: hook Stop sẽ sinh lại A_prompt_log.md sau lượt này, nên trước khi zip cần commit prompt log thêm một lần.
===
Rồi giờ mình viết từng bug nhỉ
```

**Output:**
```
Đúng, giờ em viết bug. Trước hết em **push**: GitHub vẫn đang ở `a46ea4d`, chưa push thì anh không kiểm được bài em viết.

**Cách làm**
- Viết thẳng vào `HW03/bugs/BUG-58.md` … `BUG-85.md`, thay từng `` `<SV viết>` ``. Mỗi file có 8 chỗ.
- Mỗi lô 7 file: BUG-58…64, 65…71, 72…78, 79…85.
- Xong lô nào thì commit `HW03[T1] 5/6d: SV viết BUG-58…64`, push và báo anh. Anh kiểm dữ kiện lô đó trong lúc em viết lô sau.

**Quy ước viết (giống HW02, anh chỉ nhắc cách viết, không gợi nội dung)**
- **Tiêu đề:** nêu triệu chứng, màn hình, điều kiện. **Không** ghi tiền tố `[HW03-C2-xx]` trong file; tiền tố chỉ thêm khi tạo issue.
- **Severity:** Critical/High/Medium/Low. **Priority:** High/Medium/Low. Không dùng "Major".
- **Tiền điều kiện:** nêu trạng thái quan sát được. Màn cần đăng nhập thì ghi rõ `test@eshop.com`/`Test1234!` và backend vừa restart.
- **Các bước tái hiện:** viết lại từ "Nguồn bước tái hiện" ở phần Dữ kiện. Phải chạy được, vì Claude Code sẽ chạy thật từng bước của em. Ghi rõ URL, nền tảng, thao tác (bấm gì, Tab mấy lần, viewport bao nhiêu).
- **Expected:** có căn cứ là câu SRS hoặc Căn cứ của item. Được dùng câu "(AI chép nguyên văn)" có sẵn trong khung. Mỗi Expected chỉ một nhánh.
- **Actual:** đối chiếu với Dữ kiện (AI chép); nhiều nền tảng thì ghi theo từng nền tảng.
- **Nhận định:** câu tác động phải có dữ kiện. Không có dữ kiện thì ghi "(chưa kiểm chứng)" hoặc bỏ. Tránh khẳng định quá mức.
- Trường **Yêu cầu** do AI điền sẵn: em chỉ duyệt, sai thì báo anh.
- Lô đầu viết xong để anh xem cách viết đã ổn chưa. Ổn rồi thì các lô sau em viết nhanh hơn.

Push xong em báo một câu "đã push", anh mở BUG-58 kiểm khung trước khi em viết.
```

**Xử lý:** [...]

---

## #119 | 19:16 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Theo bạn, giờ tôi đưa link cho bạn tôi để làm task 2. Thì họ cần làm những gì, điền những form gì. Họ có thể làm trong 5 phút được không?
```

**Output:**
```
Không thể chỉ gửi link cho bạn tự làm. Đề yêu cầu **moderated**: em phải có mặt (qua Meet), quan sát người tham gia làm và ghi chú. Bạn tự làm một mình thì thành unmoderated, sai đề và không có ghi chú quan sát. Link tunnel cũng chỉ sống khi script trên máy em đang chạy.

**5 phút thì không đủ. Thực tế khoảng 10 phút một người:**

| Bước | Người tham gia làm | Em làm | Thời gian |
|---|---|---|---|
| 1. Mở đầu | Vào Meet, chia sẻ màn hình, tick 3 ô đồng ý (quay màn hình, ghi âm, TA liên hệ) | Đọc lời mở đầu, bật quay Game Bar | ~1 phút |
| 2. Nhiệm vụ U1 | Mở link, đăng nhập `test@eshop.com`, tìm tai nghe, thêm giỏ, thanh toán mã VIP100, xem đơn trong Hồ sơ. Vừa làm vừa nói to suy nghĩ | **Im lặng quan sát**, ghi `observation_sheet.md`: chỗ dừng, lỗi, câu than | 3–5 phút |
| 3. SEQ | Chọn 1 số từ 1–7: khó hay dễ | Ghi | 10 giây |
| 4. SUS | 10 câu, mỗi câu chọn 1–5 | Ghi | 1–2 phút |
| 5. 4 câu hỏi mở | Trả lời về rõ ràng, khôi phục lỗi, tốc độ, tin cậy | Hỏi sâu vào chỗ khó vừa thấy, ghi lại | 2–3 phút |

**Người tham gia điền gì:** chỉ 3 ô đồng ý, SEQ (1 số), SUS (10 số) và trả lời 4 câu hỏi, đúng nội dung `participant_kit.md`. Cho nhanh, em đưa các câu này vào **Google Form** (khoảng 10 phút làm một lần, dùng chung cho cả 7 người) hoặc cho bạn gõ số vào chat Meet.

**Em cần thêm cho mỗi người:** họ tên và SĐT (để TA gọi xác minh; trong bảng 7 người thì che 4 số giữa), ngày giờ phiên. Trong JSON phiên chỉ ghi mã P01…P07.

**Mấy điểm quan trọng:**
- **Mỗi lần 1 người.** Cả 7 người dùng chung tài khoản `test@eshop.com`, và script restart backend làm reset CSDL giữa các phiên.
- **Pilot S00 trước**, có thể với bạn cùng phòng, để kiểm link, luồng và thời gian.
- **Tổng thời gian:** 8 phiên × 10 phút + chuẩn bị khoảng **1,5–2 giờ** nếu bạn em có mặt liên tục. Sau đó phân tích và viết findings (🔒, em viết) thêm khoảng 1 giờ.
- Phải chạy **trước** bước tái hiện bug, vì bước đó đưa SUT về nhánh main, còn tunnel cần nhánh `usability-tunnel`.

Nếu em có thể gom đủ 7 người tối nay thì đây là 30 điểm còn lại của Task 2, đáng làm hơn bất kỳ việc nào khác. Em muốn anh đưa lệnh chuẩn bị Google Form và các bước bật phiên S00 không?
```

**Xử lý:** [...]

---

## #120 | 19:19 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Giúp tôi làm google form cho những cái cần thiết luôn được không, bạn có thể thao tác trên trình duyệt của tôi mà
```

**Output:**
```
Đã viết sẵn script tạo form trong Apps Script, giờ Google đòi cấp quyền. Bước cấp quyền OAuth này anh không tự bấm thay em được.

Em mở tab **Apps Script ("Untitled project")** trong Chrome và làm:
1. Bấm **Review permissions**, chọn tài khoản `tanhiep24135@gmail.com`.
2. Google sẽ báo "Google hasn't verified this app", vì đây là script của chính em. Bấm **Advanced** → **Go to Untitled project (unsafe)**.
3. Bấm **Allow**. Script chỉ xin quyền tạo và quản lý Google Forms của em.

Xong em báo "đã cấp quyền". Anh sẽ chạy script, lấy 2 link (link sửa form và link gửi người tham gia), rồi mở form ra kiểm từng câu.

Form gồm 4 trang, nội dung theo đúng `participant_kit.md`:
- **Thông tin:** mã phiên, họ tên, SĐT/Zalo (để TA xác minh), nghề nghiệp (không bắt buộc), 3 câu đồng ý Có/Không (quay màn hình, ghi âm, TA liên hệ).
- **SEQ:** thang 1–7, từ Rất khó tới Rất dễ.
- **SUS:** lưới 10 câu × 5 mức.
- **4 câu hỏi mở:** rõ ràng, khôi phục lỗi, tốc độ, tin cậy.

Form không thu email người điền. Đây là bản AI dựng từ kit, cần khai Audit và Mandatory Disclosure.
```

**Xử lý:** [...]

---

## #121 | 19:23 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
https://docs.google.com/forms/d/1JMFzxKdVIvbXoNI9PLH4s3CK_d8PA_ehi7Pw4QCPUug/edit
===
https://docs.google.com/forms/d/e/1FAIpQLScZPV1xgaQLVw8nUl8wmY8EqEol7BeoMwhDjaCw1rEXGoNuqQ/viewform
===
2 link này à
```

**Output:**
```
Đúng hai link đó. Anh đã mở form kiểm: 4 trang đúng nội dung kit, câu bắt buộc đúng chỗ, form không thu email.

- **Link gửi người tham gia** (dán vào chat Meet): `https://docs.google.com/forms/d/e/1FAIpQLScZPV1xgaQLVw8nUl8wmY8EqEol7BeoMwhDjaCw1rEXGoNuqQ/viewform`
- **Link sửa** (chỉ em dùng, không gửi ai): `…/1JMFzxKdVIvbXoNI9PLH4s3CK_d8PA_ehi7Pw4QCPUug/edit`. Câu trả lời xem ở tab Responses.

**Cách dùng trong mỗi phiên**
1. Đọc lời mở đầu, lấy đồng ý bằng lời, bật quay.
2. Người tham gia làm nhiệm vụ U1 với link tunnel. Em quan sát và ghi `observation_sheet`.
3. Xong nhiệm vụ: gửi link form, đọc mã phiên (S01…), bạn điền khoảng 3–4 phút.
4. Trong lúc bạn điền câu hỏi mở, em hỏi sâu thêm vào chỗ khó vừa thấy.

**Lưu ý quan trọng**
- **Repo đang public.** Câu trả lời form có họ tên và SĐT, nên **không được** commit bản CSV xuất từ form. Vào repo chỉ có JSON phiên với mã P0x và các số SEQ/SUS. Bảng 7 người tham gia thì che 4 số giữa SĐT.
- **Trước phiên đầu, em tự điền thử 1 lần (pilot)** để biết form chạy đúng. Điền xong thì xoá câu trả lời thử trong tab Responses.
- Form do AI dựng từ kit, nên phải khai vào Audit và Mandatory Disclosure. Khi rảnh, gõ cho Claude Code: "ghi report_plan mục f: AI dựng Google Form từ participant_kit.md bằng Apps Script (phiên thảo luận, 19:23 10/11)".

Em định chạy phiên mấy giờ? Nếu bắt đầu luôn thì chạy `tools\usability_session.ps1` để lấy link tunnel, rồi `new_session.py HW03/usability/sessions S00` cho pilot.
```

**Xử lý:** [...]

---

## #122 | 19:26 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
tưởng có 2 form chứ, có 1 form thôi à
```
*Đính kèm:* `EShop_-_Phi_u_ng__i_tham_gia___nh_gi__HW03.csv`

**Output:**
```
Chỉ có **1 form**. Hai link là hai cách mở **cùng một form**:
- `…/edit` là link **chủ form**: sửa câu hỏi, xem tab Responses, tải CSV. Chỉ em dùng.
- `…/viewform` là link **điền form**: gửi cho người tham gia. Người có link này chỉ điền được, không xem được câu trả lời của người khác.

File CSV em vừa tải là câu trả lời thử ("z") của chính em. Nó cho thấy form chạy đúng: đủ 23 cột, gồm mã phiên, 3 câu đồng ý, SEQ, 10 câu SUS và 4 câu hỏi mở.

Hai việc nhỏ:
1. **Xoá câu trả lời thử** để tab Responses sạch trước phiên thật: link edit → Responses → ⋮ → *Delete all responses*.
2. Cột SUS ở mức 1 và 5 ghi kèm nhãn ("5 - Hoàn toàn đồng ý"), còn mức 2–4 chỉ là số. Khi nhập JSON phiên, em lấy chữ số đầu là được. Nếu sau này cần thì Claude Code viết script đọc CSV, nhưng CSV có họ tên và SĐT nên **chỉ để ngoài repo** (ví dụ `evidence_raw/` đã gitignore).

Em chạy pilot luôn chưa?
```

**Xử lý:** [...]

---

## #123 | 19:28 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
SEQ và 10 câu SUS là gì nhỉ
```

**Output:**
```
Đây là hai thang đo chuẩn trong đánh giá usability, cả hai nằm trong form vừa tạo.

**SEQ (Single Ease Question): 1 câu, hỏi ngay sau nhiệm vụ**
- Câu hỏi: "Nhìn chung, nhiệm vụ vừa rồi khó hay dễ?", chọn từ 1 (Rất khó) tới 7 (Rất dễ).
- Nó đo độ khó của **riêng nhiệm vụ U1**: đăng nhập, tìm sản phẩm, thêm giỏ, thanh toán VIP100, xem đơn.
- Trung bình thường gặp khoảng 5,5. Thấp hơn nghĩa là nhiệm vụ khó hơn bình thường, rất hợp để đối chiếu với chỗ người tham gia bị vấp trong ghi chú quan sát.

**SUS (System Usability Scale): 10 câu, hỏi sau SEQ**
- Đây là bảng câu hỏi chuẩn (Brooke, 1986) đo **cảm nhận chung về cả trang web**, không riêng nhiệm vụ. Mỗi câu chấm 1–5, từ Hoàn toàn không đồng ý tới Hoàn toàn đồng ý.
- Câu lẻ (1, 3, 5, 7, 9) là câu khen: dễ dùng, tự tin, muốn dùng thường xuyên…
- Câu chẵn (2, 4, 6, 8, 10) là câu chê: phức tạp, rườm rà, phải học nhiều…
- Cách tính điểm:
  - Câu lẻ = điểm − 1.
  - Câu chẵn = 5 − điểm.
  - Cộng 10 câu rồi nhân 2,5, ra **điểm 0–100**.
- Trung bình khoảng 68. Dưới 68 là dưới mức trung bình, trên 80 là tốt.
- Hai câu đảo chiều có chủ đích, để phát hiện người chọn bừa (ví dụ chọn 5 hết).

Em không cần tự tính: `sus_score.py` trong skill tính điểm cho từng người và trung bình cả nhóm.

Riêng câu trả lời thử của em lúc nãy cho thấy đúng hiện tượng đó: em chọn 4–5 cho cả câu khen lẫn câu chê. Điểm ra khoảng 50, mâu thuẫn với SEQ = 7. Đây là ví dụ hay để biết đọc kết quả, nhưng nhớ xoá trước phiên thật.
```

**Xử lý:** [...]

---

## #124 | 19:29 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Rồi, giúp tôi viết các kịch bản: 
Kịch bản mời bạn và moderated, quay phim,...
Kịch bản đưa bạn nhiệm vụ,...
```

**Output:**
```
File `moderator_script.md` có đủ các phần:

- **A. Tin nhắn mời và câu lọc:** đã mua online, chưa dùng EShop, không học HW03.
- **B. Tin nhắn chốt giờ.**
- **C. Việc em chuẩn bị trước mỗi phiên:** tunnel, `new_session.py`, phiếu quan sát.
- **D. Mở đầu:** cảm ơn, xin quay (bật quay rồi hỏi lại để lời đồng ý có trong video), chia sẻ màn hình, think-aloud.
- **E. Khối nhiệm vụ** dán vào chat Meet. Chỉ nêu mục tiêu, không nêu bước.
- **F. Trong phiên:** câu nhắc trung tính, cách đáp khi bị hỏi "bấm đâu?", 3 mức can thiệp, những điều không được làm.
- **G. Sau nhiệm vụ:** gửi form kèm mã phiên, gợi ý câu hỏi sâu.
- **H. Kết thúc.**
- **I. Việc sau mỗi phiên:** tắt tunnel, JSON phiên, commit.

Một số điểm:
- Phiên rút còn khoảng **12–15 phút**, plan cũ ghi 20 phút. Nếu giữ con số này thì sửa plan mục 5 cho khớp.
- Đây là bản **AI nháp**, em đọc lại và sửa giọng cho tự nhiên. Muốn đưa vào bài thì đặt ở `HW03/usability/moderator_script.md`, commit, và khai vào Audit cùng Google Form.
- Repo public, nên video có mặt hoặc giọng người tham gia để ngoài repo, chỉ ghi tên file trong phiếu.

Pilot với bạn cùng phòng trước để canh giờ, rồi gửi tin mời 7 người với khung giờ cụ thể.
```
*File AI ghi/gửi trong lượt này:* `moderator_script.md`

**Xử lý:** [...]

---

## #125 | 19:31 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
12-15 phút luôn à. Có thể rút gọn còn 10 phút được không. Vì mấy người tôi nhờ nó bảo chỉ làm tối đa 5-10 phút
```

**Output:**
```
Rút được còn khoảng 10 phút. Anh đã sửa file `moderator_script.md`:

| Phần | Trước | Giờ |
|---|---|---|
| Mở đầu (xin quay, chia sẻ màn hình, think-aloud) | 2' | **1'**, nói nhanh, gộp 4 ý |
| Nhiệm vụ U1 | ≤ 10' | **≤ 6'**. Quá 6 phút thì dừng, ghi "Không hoàn thành". Can thiệp khi kẹt 1,5 phút |
| Form (SEQ, SUS, 4 câu mở) | 4' | **3'**, câu mở chỉ cần trả lời 1 câu ngắn |
| Hỏi sâu | bắt buộc | **chỉ khi người tham gia không vội**, 1 câu |
| Kết thúc | 1' | 10 giây |

Không cắt thêm được nữa, vì:
- **4 câu hỏi mở** (rõ ràng, khôi phục lỗi, tốc độ, tin cậy) là yêu cầu tối thiểu của đề. Chúng vẫn nằm trong form, chỉ rút thành 1 câu mỗi ý.
- **SUS 10 câu** là thang chuẩn, bỏ câu thì không tính được điểm.

Còn 2 việc nhỏ:
1. Plan mục 3 đang ghi benchmark ≤ 5 phút, mục 5 ghi phiên khoảng 20 phút. Bảo Claude Code sửa thành "~10 phút, nhiệm vụ ≤ 6 phút" cho khớp, và ghi lý do: người tham gia chỉ có 5–10 phút.
2. Lúc mời, cứ nói **10 phút**. Bạn đến muộn hay nói chuyện ngoài lề là sẽ lố, nên giữ đúng nhịp.

Nhờ được bạn cùng phòng thì pilot ngay để canh giờ thật. Nếu pilot ra trên 10 phút, chỗ bị lố gần như chắc chắn là phần nhiệm vụ, và đó cũng là một finding.
```
*File AI ghi/gửi trong lượt này:* `moderator_script.md`

**Xử lý:** [...]

---

## #126 | 19:34 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Có cần lưu file này vào trong software-testing không
```

**Output:**
````
Nên lưu, vì 3 lý do:
- Đề chấm theo "quantity and quality of the deliverables", trong đó có **usability-evaluation design**. Kịch bản điều phối là một phần của thiết kế đó, cạnh plan, kit và observation sheet.
- Nó là bằng chứng phiên của em đúng kiểu **moderated**: có lời mở đầu, xin đồng ý, câu nhắc trung tính, quy tắc can thiệp. Khi TA vấn đáp, em có file để chỉ.
- File do AI nháp nên phải có trong repo thì Audit mới có artifact để chấm.

Cách lưu:
1. Tải file `moderator_script.md` trong chat về, đặt vào `HW03\usability\moderator_script.md`.
2. Dán cho Claude Code:

```
1. HW03/usability/moderator_script.md (SV đặt vào, AI nháp ở phiên thảo luận 19:29–19:31 10/11): giữ nguyên nội dung, add + commit `HW03[T2] 2c/10: kịch bản điều phối (AI nháp)`.
2. usability/plan.md: mục 3 benchmark → "≤ 6 phút", mục 5 thứ tự phiên → "~10 phút: mở đầu 1' → nhiệm vụ ≤ 6' → Google Form (SEQ + SUS + 4 câu mở) 3'"; lý do: người tham gia chỉ có 5–10 phút (SV chốt). Thêm dòng: SEQ/SUS/câu mở thu bằng Google Form (AI dựng bằng Apps Script từ participant_kit.md, 19:23 10/11); CSV form có họ tên/SĐT → KHÔNG vào repo. Commit `HW03[T2] 2d/10: plan theo phiên 10 phút + Google Form`.
3. report_plan mục f: khai 2 việc AI (Google Form, kịch bản điều phối). Không push, không amend.
Báo cáo ≤ 4 dòng + hash.
```

Lưu ý: file vẫn còn dòng "📝 AI nháp – SV duyệt/sửa" ở đầu. Em đọc và sửa giọng xong thì xoá dòng đó, rồi commit lại.
````

**Xử lý:** [...]

---

## #127 | 19:35 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. HW03/usability/moderator_script.md (SV đặt vào, AI nháp ở phiên thảo luận 19:29–19:31 10/11): giữ nguyên nội dung, add + commit `HW03[T2] 2c/10: kịch bản điều phối (AI nháp)`.
2. usability/plan.md: mục 3 benchmark → "≤ 6 phút", mục 5 thứ tự phiên → "~10 phút: mở đầu 1' → nhiệm vụ ≤ 6' → Google Form (SEQ + SUS + 4 câu mở) 3'"; lý do: người tham gia chỉ có 5–10 phút (SV chốt). Thêm dòng: SEQ/SUS/câu mở thu bằng Google Form (AI dựng bằng Apps Script từ participant_kit.md, 19:23 10/11); CSV form có họ tên/SĐT → KHÔNG vào repo. Commit `HW03[T2] 2d/10: plan theo phiên 10 phút + Google Form`.
3. report_plan mục f: khai 2 việc AI (Google Form, kịch bản điều phối). Không push, không amend.
Báo cáo ≤ 4 dòng + hash.
```

**Output:**
```
Kịch bản không chứa dữ liệu cá nhân (chỉ placeholder `[tên]`, `[link Meet]` và tài khoản seed). `BUG-58/59` đang có thay đổi chưa commit của SV, em không đụng.

Đã commit kịch bản điều phối và cập nhật plan. Không push, không amend.

### Báo cáo cho phiên thảo luận
- **Kịch bản điều phối:** commit `moderator_script.md` nguyên văn, sau khi đọc hết (chỉ có placeholder `[tên]`, `[link Meet]` và tài khoản seed, không có dữ liệu cá nhân). `70f26ef` HW03[T2] 2c/10: kịch bản điều phối (AI nháp)
- **plan.md:** mục 3 benchmark đổi thành ≤ 6 phút. Mục 5 thứ tự phiên đổi thành ~10 phút (mở đầu 1' → nhiệm vụ ≤ 6' → Google Form 3'), kèm lý do 5–10 phút và dòng Google Form: CSV/Responses có họ tên + SĐT không vào repo. `report_plan` mục f có thêm 2 dòng khai (Google Form, kịch bản điều phối). `2485116` HW03[T2] 2d/10: plan theo phiên 10 phút + Google Form
- **Chưa commit:** `BUG-58.md`, `BUG-59.md` đang có thay đổi chưa commit, em đoán là SV đang viết nên không đụng. `A_prompt_log.md` hook tự sinh lại sau mỗi lượt.
- **Có thể lệch:** `participant_kit.md` vẫn ghi theo phiên dài cũ, em chưa kiểm vì lệnh không yêu cầu sửa file này.
```

**Xử lý:** [...]

---

## #128 | 19:36 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Kịch bản điều phối: commit moderator_script.md nguyên văn, sau khi đọc hết (chỉ có placeholder [tên], [link Meet] và tài khoản seed, không có dữ liệu cá nhân). 70f26ef HW03[T2] 2c/10: kịch bản điều phối (AI nháp)
- plan.md: mục 3 benchmark đổi thành ≤ 6 phút. Mục 5 thứ tự phiên đổi thành ~10 phút (mở đầu 1' → nhiệm vụ ≤ 6' → Google Form 3'), kèm lý do 5–10 phút và dòng Google Form: CSV/Responses có họ tên + SĐT không vào repo. report_plan mục f có thêm 2 dòng khai (Google Form, kịch bản điều phối). 2485116 HW03[T2] 2d/10: plan theo phiên 10 phút + Google Form
- Chưa commit: BUG-58.md, BUG-59.md đang có thay đổi chưa commit, em đoán là SV đang viết nên không đụng. A_prompt_log.md hook tự sinh lại sau mỗi lượt.
- Có thể lệch: participant_kit.md vẫn ghi theo phiên dài cũ, em chưa kiểm vì lệnh không yêu cầu sửa file này.
```

**Output:**
```
Hai commit đều ổn.

`participant_kit.md` không cần sửa. Anh đã đọc file này lúc đầu phiên: nó không ghi thời lượng, và nội dung câu hỏi trùng khớp Google Form. Chỗ lệch duy nhất là chữ "khoanh một số" của bản giấy. Muốn gọn thì thêm một dòng đầu file: "Bản thu thực tế: Google Form, nội dung giống phiếu này". Việc nhỏ, để lúc đóng gói làm cũng được.

Anh thấy em đang viết BUG-58, 59. Giờ em cần chốt thứ tự cho tối nay:
- **Nếu bạn em hẹn được trong 1–2 giờ tới:** viết bug trong lúc chờ. Tới giờ hẹn thì commit lô bug đang dở (kể cả chưa đủ 7 file), chạy pilot rồi các phiên.
- **Nếu bạn hẹn muộn (sau 22:00):** viết xong lô 1 (58…64), push, báo anh kiểm, rồi viết tiếp lô 2.

Bạn em hẹn mấy giờ, và đã được bao nhiêu người đồng ý?
```

**Xử lý:** [...]

---

## #129 | 20:13 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Viết xong các bug rồi, commit luôn hay là bảo Claude Code check rồi mới commit nhỉ
```

**Output:**
````
**Commit luôn, trước khi Claude Code kiểm.** Đây là quy ước từ HW02: bản em viết phải được commit trước, để lịch sử git chứng minh chữ là của em. Mọi chỗ AI sửa sau đó (dữ kiện sai) sẽ nằm ở commit riêng, so diff được.

Em chạy:
```
git add HW03/bugs/BUG-*.md
git commit -m "HW03[T1] 5/6d: SV viết BUG-58…85"
git push
```
(Nếu chưa xong cả 28 file thì ghi đúng dải đã viết vào message.)

Push xong, dán lệnh này cho Claude Code:

```
NHIỆM VỤ: kiểm bug SV viết (BUG-58…85) – T1 bước 5/6e. KHÔNG sửa chữ SV (Tiêu đề, Mô tả/Steps, Expected, Actual, Severity, Priority, Nhận định). Không push, không amend.
1. Kiểm (chỉ đọc), ghi HW03/bugs/bug_check.md, mỗi BUG 1 khối: còn `<SV viết>`/🔒 không; thang Severity (Critical/High/Medium/Low) + Priority (High/Medium/Low); tiêu đề có tiền tố [HW03-C2] không (KHÔNG được có trong file); Actual khớp Dữ kiện (AI chép) không; Expected có căn cứ (SRS/Căn cứ item) không, có quá 1 nhánh không; Yêu cầu chỉ ghi yêu cầu bị vi phạm; câu Tác động/khẳng định không có dữ kiện → đề nghị "(chưa kiểm chứng)"; tên trường/màn/nút không có trong SUT. Chỉ liệt kê, không đề xuất câu chữ.
2. Tái hiện: `tools\sut_main.ps1` (SUT về main) → restart backend → chạy thật Steps SV viết (UI: Playwright hoặc tay theo nền tảng ghi trong bug; ít nhất P1/P2 trên máy này; P3 chỉ đối chiếu ảnh). Ghi kết quả từng bug vào bug_check.md: tái hiện được / không / bước nào không chạy được. Không sửa Steps.
3. Xong: đưa SUT về nhánh usability-tunnel (`git -C ..\eshop-sut switch usability-tunnel`), kiểm `git -C ..\eshop-sut log -1` = e33212d.
Commit `HW03[T1] 5/6e: kiểm dữ kiện + tái hiện bug (AI)`.
Báo cáo ≤ 15 dòng: số bug sạch / có điểm cần SV sửa (liệt kê mã), số bug không tái hiện được, hash.
```

Trong lúc Claude Code chạy, anh cũng đọc trên repo và góp ý riêng các chỗ dữ kiện hoặc khẳng định quá mức. Sau đó em sửa theo cả hai danh sách, commit `5/6f`, rồi mới tạo issue.
````

**Xử lý:** [...]

---

## #130 | 20:14 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: kiểm bug SV viết (BUG-58…85) – T1 bước 5/6e. KHÔNG sửa chữ SV (Tiêu đề, Mô tả/Steps, Expected, Actual, Severity, Priority, Nhận định). Không push, không amend.
1. Kiểm (chỉ đọc), ghi HW03/bugs/bug_check.md, mỗi BUG 1 khối: còn `<SV viết>`/🔒 không; thang Severity (Critical/High/Medium/Low) + Priority (High/Medium/Low); tiêu đề có tiền tố [HW03-C2] không (KHÔNG được có trong file); Actual khớp Dữ kiện (AI chép) không; Expected có căn cứ (SRS/Căn cứ item) không, có quá 1 nhánh không; Yêu cầu chỉ ghi yêu cầu bị vi phạm; câu Tác động/khẳng định không có dữ kiện → đề nghị "(chưa kiểm chứng)"; tên trường/màn/nút không có trong SUT. Chỉ liệt kê, không đề xuất câu chữ.
2. Tái hiện: `tools\sut_main.ps1` (SUT về main) → restart backend → chạy thật Steps SV viết (UI: Playwright hoặc tay theo nền tảng ghi trong bug; ít nhất P1/P2 trên máy này; P3 chỉ đối chiếu ảnh). Ghi kết quả từng bug vào bug_check.md: tái hiện được / không / bước nào không chạy được. Không sửa Steps.
3. Xong: đưa SUT về nhánh usability-tunnel (`git -C ..\eshop-sut switch usability-tunnel`), kiểm `git -C ..\eshop-sut log -1` = e33212d.
Commit `HW03[T1] 5/6e: kiểm dữ kiện + tái hiện bug (AI)`.
Báo cáo ≤ 15 dòng: số bug sạch / có điểm cần SV sửa (liệt kê mã), số bug không tái hiện được, hash.
```

**Output:**
```
Đang đọc Dữ kiện BUG-66…85 để đối chiếu Actual, sau đó viết bug_check.md rồi tái hiện.

Đã đọc xong 28 bug + Dữ kiện. Giờ dựng script Playwright tái hiện Steps SV (P1 Chromium, P2 Firefox).

Đã viết script tái hiện. Giờ đưa SUT về main, khởi động backend + web.

P1 xong lượt đầu; sửa 3 chỗ đo (throttle, Steps login, kiểm huỷ đơn), chạy lại P1 rồi P2.

Tái hiện P1/P2 xong (23/23 chạy). Giờ đối chiếu ảnh P3.

Ảnh P3 đã xem xong. Viết bug_check.md.

Lines đúng. Đưa SUT về usability-tunnel, tắt Vite, commit.

Xong bước 5/6e. Có 14 bug sạch, 14 bug có điểm SV cần xem. Không bug nào hoàn toàn không tái hiện được, nhưng 4 bug chỉ tái hiện được một phần.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: T1 5/6e – kiểm BUG-58…85 (chỉ đọc) + tái hiện trên P1 (Chrome), P2 (Firefox Playwright); P3 đối chiếu 8 ảnh lượt tay.
- File: `HW03/bugs/bug_check.md` (28 khối, chi tiết từng điểm); `HW03/bugs/repro/repro_P1.json`, `repro_P2.json` (số đo thô); `HW03/tests/repro_bugs.spec.ts` + `repro.config.ts` (script tái hiện, AI viết → cần khai Audit).
- Chung: không file nào còn `<SV viết>`/🔒; Severity/Priority đều đúng thang; không tiêu đề nào có `[HW03-C2]`.
- Sạch: 14 – BUG-59, 60, 61, 65, 66, 67, 68, 69, 71, 74, 77, 83, 84, 85.
- Cần SV xem: 14 – BUG-58, 70, 72, 80 (Nhận định có câu khẳng định chưa ghi "(chưa kiểm chứng)"); 62, 63 (tên trường không có trong SUT: "Email" ở trang Đăng nhập, nhãn thật là "Username"; BUG-63 Expected còn nêu ô "Xác nhận mật khẩu"); 73 (tiêu đề bỏ sót Họ Tên); 75, 79 (Actual có ý không có trong Dữ kiện; ảnh P3 CL-63 trái với Actual P3); 76, 82 (Expected 2 nhánh; tiêu đề 82 trái Actual P1); 78 (Actual nêu TimeoutError là lỗi của test tự động, không phải hành vi SUT); 64 (hộp thoại khác Actual); 81 (số đơn #8…#12 không khớp khi làm đúng Tiền điều kiện).
- Không tái hiện được: 0. Tái hiện một phần: 4.
  - BUG-62: làm đúng Steps thì ô Mật khẩu trống chặn submit, 0 request.
  - BUG-64: SĐT `123` ra hộp thoại "Số điện thoại không hợp lệ…", không phải "Cập nhật thành công!".
  - BUG-75: làm theo Steps thì sau F5 tên vẫn "Test User", phần "cập nhật sau F5" không ra.
  - BUG-82: bước Autofill không chạy được bằng Playwright, cần SV chạy tay.
- "Slow 3G" thay bằng trễ request 3000 ms (route của Playwright), không phải throttling thật.
- Cô lập (bất thường SUT):
  - `Profile.jsx:43` regex SĐT `^[1-9][0-9]{8,9}$` chặn SĐT bắt đầu bằng 0. Đây là nguyên nhân trực tiếp ở BUG-73, 75, 78 (Hồ sơ) và CL-21. Với SĐT `912345678` thì cả 3 trường lưu bền; nhấp đúp gửi 2 PUT.
  - `ForgotPassword.jsx:26` regex mật khẩu bắt buộc có khoảng trắng (BUG-70, 78).
- 1 điểm ngoài 28 bug: `Login.jsx:24` tiêu đề form là "Đăng Ký"; `Login.jsx:40` ô Mật khẩu `type="text"`.
- Kết quả kiểm tra: repro P1 23/23, P2 23/23 chạy hết (sau 2 lần sửa script); lint không chạy.
- SUT đã về `usability-tunnel` @ `e33212d`; Vite và backend đã tắt.
- Commit: `715c4eb HW03[T1] 5/6e: kiểm dữ kiện + tái hiện bug (AI)` (chưa push, `A_prompt_log.md` chưa commit).
- Cần quyết định: BUG-73/75/78 – kết quả cô lập cho thấy gốc là regex SĐT (liên quan #113) – SV giữ bug như đang viết / viết lại theo nguyên nhân / gộp với #113.
```
*File AI ghi/gửi trong lượt này:* `repro.config.ts`, `repro_bugs.spec.ts`, `bug_check.md`

**Xử lý:** [...]

---

## #131 | 21:54 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- Nhiệm vụ: T1 5/6e – kiểm BUG-58…85 (chỉ đọc) + tái hiện trên P1 (Chrome), P2 (Firefox Playwright); P3 đối chiếu 8 ảnh lượt tay.
- File: HW03/bugs/bug_check.md (28 khối, chi tiết từng điểm); HW03/bugs/repro/repro_P1.json, repro_P2.json (số đo thô); HW03/tests/repro_bugs.spec.ts + repro.config.ts (script tái hiện, AI viết → cần khai Audit).
- Chung: không file nào còn <SV viết>/🔒; Severity/Priority đều đúng thang; không tiêu đề nào có [HW03-C2].
- Sạch: 14 – BUG-59, 60, 61, 65, 66, 67, 68, 69, 71, 74, 77, 83, 84, 85.
- Cần SV xem: 14 – BUG-58, 70, 72, 80 (Nhận định có câu khẳng định chưa ghi "(chưa kiểm chứng)"); 62, 63 (tên trường không có trong SUT: "Email" ở trang Đăng nhập, nhãn thật là "Username"; BUG-63 Expected còn nêu ô "Xác nhận mật khẩu"); 73 (tiêu đề bỏ sót Họ Tên); 75, 79 (Actual có ý không có trong Dữ kiện; ảnh P3 CL-63 trái với Actual P3); 76, 82 (Expected 2 nhánh; tiêu đề 82 trái Actual P1); 78 (Actual nêu TimeoutError là lỗi của test tự động, không phải hành vi SUT); 64 (hộp thoại khác Actual); 81 (số đơn #8…#12 không khớp khi làm đúng Tiền điều kiện).
- Không tái hiện được: 0. Tái hiện một phần: 4.
  - BUG-62: làm đúng Steps thì ô Mật khẩu trống chặn submit, 0 request.
  - BUG-64: SĐT 123 ra hộp thoại "Số điện thoại không hợp lệ…", không phải "Cập nhật thành công!".
  - BUG-75: làm theo Steps thì sau F5 tên vẫn "Test User", phần "cập nhật sau F5" không ra.
  - BUG-82: bước Autofill không chạy được bằng Playwright, cần SV chạy tay.
- "Slow 3G" thay bằng trễ request 3000 ms (route của Playwright), không phải throttling thật.
- Cô lập (bất thường SUT):
  - Profile.jsx:43 regex SĐT ^[1-9][0-9]{8,9}$ chặn SĐT bắt đầu bằng 0. Đây là nguyên nhân trực tiếp ở BUG-73, 75, 78 (Hồ sơ) và CL-21. Với SĐT 912345678 thì cả 3 trường lưu bền; nhấp đúp gửi 2 PUT.
  - ForgotPassword.jsx:26 regex mật khẩu bắt buộc có khoảng trắng (BUG-70, 78).
- 1 điểm ngoài 28 bug: Login.jsx:24 tiêu đề form Mật khẩu type="text".
- Kết quả kiểm tra: repro P1 23/23, P2 23/23 chạy hết (sau 2 lần sửa script); lint không chạy.
- SUT đã về usability-tunnel @ e33212d; Vite và
- Commit: 715c4eb HW03[T1] 5/6e: kiểm dữ kiện + tái hiện bug (AI) (chưa push, A_prompt_log.md chưa commit).
- Cần quyết định: BUG-73/75/78 – kết quả cô lập ên quan #113) – SV giữ bug như đang viết / viếtlại theo nguyên nhân / gộp với #113.
===
thực hiện xong cái này thì giúp mình bảo Claude Code mở tunnel nhá
```

**Output:**
````
Bug đã push (`af92e6d`), còn bản kiểm `715c4eb` của Claude Code thì chưa push.

**Về BUG-73/75/78 và #113:** anh đã đọc #113. Đó là issue của henry-banana về trang **Đăng ký**, triệu chứng là SĐT 10 số có đầu số khác 0 không hợp lệ mà vẫn **được nhận**. Bug của em là trang **Hồ sơ**, và theo cô lập của Claude Code thì triệu chứng **ngược lại**: SĐT bắt đầu bằng 0 bị chặn. Khác màn và khác triệu chứng, nên theo tiêu chí trùng (cùng app + cùng màn + cùng triệu chứng) thì **không gộp** với #113. Có thể ghi #113 vào mục "Liên quan" vì cùng loại regex.

Còn giữ nguyên hay viết lại theo nguyên nhân là em quyết. Câu hỏi để em tự soát: nếu đổi sang SĐT không bắt đầu bằng 0 (ví dụ 912345678) mà triệu chứng mất, thì Tiền điều kiện và Nhận định của em đang mô tả đúng lỗi chưa?

**Thứ tự đề xuất, vì đã 21:54:** nếu bạn em có mặt bây giờ thì làm **usability trước**. Sửa 14 bug để sau, vì phần đó chỉ phụ thuộc em, còn người tham gia thì có giờ giấc của họ.

Dán cho Claude Code:

```
1. Commit A_prompt_log.md (`HW03: cập nhật prompt log`). Ghi report_plan mục f: AI viết tests/repro_bugs.spec.ts + repro.config.ts (5/6e).
2. Mở tunnel cho phiên usability: kiểm SUT ..\eshop-sut đang ở usability-tunnel @ e33212d; chạy `powershell -ExecutionPolicy Bypass -File tools\usability_session.ps1` ở chế độ nền (run_in_background), đợi tới khi in link https://….trycloudflare.com, mở link bằng curl/Playwright kiểm trang chủ tải được (200, có danh sách sản phẩm).
3. Báo ≤ 3 dòng: link tunnel, kiểm trang chủ OK/không. Giữ tunnel chạy; KHÔNG tự tắt.
Giữa các phiên khi SV nói "phiên mới": dừng tunnel cũ, chạy lại script (restart backend + link mới), báo link mới.
```

Lưu ý: link tunnel đổi mỗi lần chạy, nên mỗi phiên em phải gửi link mới cho người tham gia. Nếu muốn tự chủ hơn, em có thể chạy script trong một cửa sổ PowerShell riêng, rồi Ctrl+C và chạy lại khi sang phiên mới, khỏi phụ thuộc Claude Code.
````

**Xử lý:** [...]

---

## #132 | 21:55 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. Commit A_prompt_log.md (`HW03: cập nhật prompt log`). Ghi report_plan mục f: AI viết tests/repro_bugs.spec.ts + repro.config.ts (5/6e).
2. Mở tunnel cho phiên usability: kiểm SUT ..\eshop-sut đang ở usability-tunnel @ e33212d; chạy `powershell -ExecutionPolicy Bypass -File tools\usability_session.ps1` ở chế độ nền (run_in_background), đợi tới khi in link https://….trycloudflare.com, mở link bằng curl/Playwright kiểm trang chủ tải được (200, có danh sách sản phẩm).
3. Báo ≤ 3 dòng: link tunnel, kiểm trang chủ OK/không. Giữ tunnel chạy; KHÔNG tự tắt.
Giữa các phiên khi SV nói "phiên mới": dừng tunnel cũ, chạy lại script (restart backend + link mới), báo link mới.
```

**Output:**
```
Có link. Kiểm trang chủ qua tunnel bằng Playwright.

Tunnel đang chạy, trang chủ tải được: https://scheduling-shipped-oakland-immigration.trycloudflare.com
- Trang chủ trả 200 và hiện danh sách sản phẩm (có AirPods, 5 nút "Thêm"); `/api/products` cũng trả 200. Tunnel để chạy, AI không tắt.
- Đã commit `575b28c HW03: cập nhật prompt log` (gồm prompt log và report_plan mục f ghi `repro_bugs.spec.ts`, `repro.config.ts`).
```

**Xử lý:** [...]

---

## #133 | 21:56 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
đưa tôi mấy cái sheet luôn nhé, tôi bắt đầu mở meet rồi
```

**Output:**
````
Đây là bản rút gọn để em mở bên cạnh Meet.

**1. Trước khi bạn vào (S00 = pilot)**
- Tunnel đã có link → copy sẵn.
- Claude Code (hoặc em) chạy `python .claude/skills/usability-evaluation/scripts/new_session.py HW03/usability/sessions S00`.

**2. Nói khi bạn vào (1 phút)**
> Cảm ơn bạn. Mình kiểm tra trang web, không kiểm tra bạn, nên không có đúng sai. Mình xin quay màn hình và ghi âm, chỉ dùng cho bài tập; trợ giảng có thể liên hệ bạn để xác nhận. Bạn đồng ý không?

→ Bật **Win + Alt + R**, rồi nói: *"Mình quay rồi, bạn xác nhận đồng ý giúp mình."*
> Bạn chia sẻ màn hình giúp mình. Trong lúc làm, bạn nói to mình đang nghĩ gì, định bấm gì. Mình sẽ không hướng dẫn.

**3. Dán vào chat Meet**
```
Link: <link tunnel>

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản: test@eshop.com / Test1234!
Xong thì nói "Xong".
```
→ **Bấm đồng hồ** khi bạn mở link.

**4. Trong lúc làm (≤ 6 phút)**
- Im lặng, ghi chép.
- Bạn im lặng hơn 20 giây: *"Bạn đang nghĩ gì?"*
- Bạn hỏi "bấm đâu?": *"Nếu không có mình thì bạn sẽ làm gì?"*
- Kẹt hơn 1,5 phút: *"Bạn thử nhìn lại toàn bộ trang xem?"* (ghi **T**).
- Quá 6 phút: *"Không sao, mình dừng ở đây nhé."* (Không hoàn thành).
- Khi bạn nói Xong: *"Đơn của bạn đang ở trạng thái nào?"*

**5. Gửi form**
```
https://docs.google.com/forms/d/e/1FAIpQLScZPV1xgaQLVw8nUl8wmY8EqEol7BeoMwhDjaCw1rEXGoNuqQ/viewform
Mã phiên: S00
```
> 4 câu cuối bạn trả lời 1 câu ngắn là đủ.

Bạn bấm Gửi thì nói: *"Cảm ơn bạn, bạn dừng chia sẻ màn hình giúp mình."* Rồi dừng quay (**Win + Alt + R**).

**6. Phiếu ghi nhanh (chép vào Notepad)**
```
Phiên: S0_   Ngày: 10/11/2026   Quay: có/không   Video: ________
Trình duyệt/OS của bạn: ________

MỐC (mm:ss)
Đăng nhập xong:
Thấy tai nghe:
Thêm giỏ:
Áp mã VIP100:
Đặt hàng xong:
Thấy đơn trong lịch sử:
Nói Xong / bỏ cuộc:

Kết quả: Hoàn thành không trợ giúp / có trợ giúp / Không hoàn thành
Nói đúng trạng thái đơn: có/không – "_____"

DIỄN BIẾN (L=lỗi/chọn sai · D=do dự · N=câu nói nguyên văn · T=trợ giúp)
mm:ss | màn hình | loại | mô tả
     |          |      |

Tổng: lỗi __  do dự __  trợ giúp __
```

**7. Sau phiên**
- Bảo Claude Code "phiên mới": tunnel và backend restart, ra link mới.
- Sang phiên tiếp theo thì đổi mã thành S01, S02, …

Chúc em chạy pilot suôn sẻ. Xong S00 thì báo anh: hết bao nhiêu phút, đề bài có chỗ nào bạn hỏi lại.
````

**Xử lý:** [...]

---

## #134 | 22:14 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
S00: Thấy nút thêm vào giỏ hàng bị lag, thấy bấm không hiện, sau đó đã được.
Làm theo từng bước thì đúng như yêu cầu, còn mật khẩu hơi kỳ kỳ.
===
đây là những gì bạn ấy trả lời trong lúc làm, còn những lúc làm thì bạn ấy cũng làm nhanh thôi.
```

**Output:**
````
Pilot ổn: luồng chạy hết, đề bài không bị hỏi lại. Vài điểm trước khi sang S01.

**Ghi vào phiếu S00 đúng như bạn nói** (ghi nguyên văn, chưa diễn giải):
- N: "nút thêm vào giỏ hàng bị lag, bấm không hiện, sau đó đã được" (ghi kèm mm:ss nếu em có).
- N: "mật khẩu hơi kỳ kỳ".
- Bạn làm theo từng bước và hoàn thành. Ghi rõ không trợ giúp hay có trợ giúp.

Một dữ kiện liên quan đã có từ HW02: `ProductDetail.jsx:21–31` bỏ qua lần bấm lẻ ở nút thêm giỏ (handoff HW02 mục 5). Nhận định đây là lỗi riêng lẻ hay vấn đề thiết kế là phần findings của em.

**Rút kinh nghiệm từ pilot cho S01–S07:**
1. **Hỏi sâu ngay khi người tham gia nói mơ hồ.** "Mật khẩu hơi kỳ kỳ" mà không hỏi lại thì không dùng được. Lần sau hỏi ngay: *"Kỳ ở chỗ nào?"* hoặc *"Bạn mong nó thế nào?"*. Riêng S00 thì nhắn hỏi lại bạn ấy luôn, khi bạn còn nhớ.
2. **Ghi mốc thời gian.** Em bảo bạn làm nhanh, nhưng plan cần số: tổng mấy phút, mốc đăng nhập và đặt hàng. Nếu có video thì lấy lại mốc từ video.
3. Kịch bản không cần sửa. Ghi vào report §5.5: "pilot: đề bài rõ, không sửa; bổ sung: hỏi lại ngay khi người tham gia nhận xét mơ hồ".

**Lưu S00:** em điền JSON phiên S00 (mã P00, SEQ/SUS lấy trong tab Responses của form, ghi chú quan sát), rồi bảo Claude Code:
```
Phiên S00 (pilot) xong: SV đã nhập HW03/usability/sessions/S00.json → chạy sus_score.py HW03/usability/sessions --check; lỗi thì báo, KHÔNG tự sửa số SV nhập. Commit `HW03[T2] 2/10: pilot S00`. Rồi "phiên mới": restart tunnel, báo link mới.
```

Xong là sang S01. Bạn tiếp theo vào Meet lúc mấy giờ?
````

**Xử lý:** [...]

---

## #135 | 22:15 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Bạn tiếp theo đã vào rồi. Mình thực hiện tiếp luôn nhé. Ghi note từng lần, còn đưa vào trong kia thì để sau nehs
```

**Output:**
```
Được, em ghi phiếu ra Notepad trước, JSON và commit để sau khi xong hết các phiên.

**Ngay bây giờ cho S01:**
1. Bảo Claude Code: **"phiên mới"**. Nó restart backend và tunnel, ra link mới. Đừng dùng link cũ: CSDL vẫn còn đơn của S00.
2. Đổi mã trong khối chat Meet thành **S01**, dán link mới.
3. Chạy theo phiếu như pilot. Nhớ hai điểm vừa rút ra: **hỏi lại ngay** khi bạn nói mơ hồ, và **ghi mm:ss** các mốc.

Sau mỗi phiên, em lưu Notepad thành file riêng (`S01.txt`, `S02.txt`, …) để khỏi ghi đè, và đổi tên video tương ứng.

Xong cả lượt thì gửi anh các file phiếu. Anh đưa lệnh cho Claude Code dựng khung JSON; em điền số SEQ/SUS từ form rồi commit từng phiên.
```

**Xử lý:** [...]

---

## #136 | 22:16 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
phiên mới
```

**Output:**
```
Link mới cho phiên này: https://golf-mechanical-involves-attorneys.trycloudflare.com
- Đã tắt tunnel cũ và chạy lại script, backend được khởi động lại (dữ liệu seed lại từ đầu).
- Trang chủ trả 200; `/api/products` có đủ 5 sản phẩm (iPhone 15 Pro Max … Keychron Q1). Lượt này em chỉ kiểm bằng curl, chưa mở bằng Playwright như lần trước. Tunnel để chạy, AI không tắt.
```

**Xử lý:** [...]

---

## #137 | 22:17 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
https://golf-mechanical-involves-attorneys.trycloudflare.com/
```

**Output:**
````
Anh không mở thử được link (trang chặn công cụ đọc web của anh), nên em tự mở nhanh trên máy hoặc điện thoại cho chắc trước khi gửi.

Khối dán vào chat Meet cho S01:

```
Link: https://golf-mechanical-involves-attorneys.trycloudflare.com/

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản: test@eshop.com / Test1234!
Xong thì nói "Xong".
```

Form sau nhiệm vụ: `https://docs.google.com/forms/d/e/1FAIpQLScZPV1xgaQLVw8nUl8wmY8EqEol7BeoMwhDjaCw1rEXGoNuqQ/viewform`, mã phiên **S01**.

Nhớ bật quay sau khi bạn đồng ý, và bấm đồng hồ khi bạn mở link.
````

**Xử lý:** [...]

---

## #138 | 22:30 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
phiên mới
```

**Output:**
```
Link mới: https://chances-tel-allow-beyond.trycloudflare.com
- Đã tắt tunnel cũ và chạy lại script; backend khởi động lại nên dữ liệu seed lại.
- Trang chủ trả 200, `/api/products` trả đủ 5 sản phẩm (chỉ kiểm bằng curl). Tunnel đang chạy, em không tự tắt.
```

**Xử lý:** [...]

---

## #139 | 22:32 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
S01: Bấm đăng nhập mà thấy chữ đăng ký.
Mình nghĩ là cần thêm hình ảnh sinh động xí
Mình tự giảm số tiền khi checkout thì sao. Đã giảm tổng giá trị xuống 300000. Và nói mình chưa hiểu chỗ này lắm
Thêm giỏ hàng ở detail thì được, còn ở list thì không được.
Bạn ấy ngồi test hơi quá đà.
Đơn hàng đang ở trạng thái chờ xác nhận.
Fact: Bạn ngồi làm khách hàng gian lận
===
MÌnh đã gõ phiên mới ở Claude Code:
Đây là link mới: https://chances-tel-allow-beyond.trycloudflare.com
```

**Output:**
````
S01 có dữ kiện tốt. Ghi phiếu tách bạch như sau:

**Ghi vào phiếu S01 (nguyên văn, không diễn giải)**
- N: "Bấm đăng nhập mà thấy chữ đăng ký".
- N: "cần thêm hình ảnh sinh động xí".
- L/N: thêm giỏ ở trang chi tiết thì được, ở danh sách thì không được.
- **Lệch nhiệm vụ:** bạn tự giảm số tiền lúc checkout, tổng còn 300.000, và nói chưa hiểu chỗ này lắm. **Ghi rõ bạn làm bằng cách nào**: sửa trên giao diện, DevTools hay sửa request? Không nhớ thì xem lại video. Chi tiết này quyết định nó là finding gì.
- Bạn trả lời trạng thái đơn: "chờ xác nhận".
- Ghi chú người điều phối: người tham gia làm vượt nhiệm vụ, thử như khách hàng gian lận.

Hai điểm cần lưu ý cho phần phân tích:
- **Tiêu chí thành công** là tổng = 5.900.000 ₫. Đơn của S01 có tổng 300.000 do bạn tự sửa, nên em phải quyết khi phân tích: hoàn thành, hoàn thành có lệch, hay không hoàn thành. Ghi lại để quyết sau, đừng sửa số.
- **Hồ sơ người tham gia:** "ngồi test quá đà" thường là người làm IT. Ghi nghề nghiệp của bạn ấy (form có cột này) để bảng 7 người và phần giới hạn nghiên cứu phản ánh đúng.

Với các phiên sau, nếu người tham gia rẽ khỏi nhiệm vụ, em có thể nói câu trung tính: *"Bạn cứ làm như một người mua bình thường nhé."* Ghi lại câu đó (T).

**Khối chat cho S02:**
```
Link: https://chances-tel-allow-beyond.trycloudflare.com

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản: test@eshop.com / Test1234!
Xong thì nói "Xong".
```
Form: mã phiên **S02**.
````

**Xử lý:** [...]

---

## #140 | 22:47 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
phiên mới
```

**Output:**
```
Link mới: https://inexpensive-runner-manufacturing-convert.trycloudflare.com
- Đã tắt tunnel cũ, restart backend (dữ liệu seed lại). Trang chủ trả 200, `/api/products` có đủ 5 sản phẩm (kiểm bằng curl). Tunnel đang chạy, em không tự tắt.
```

**Xử lý:** [...]

---

## #141 | 22:49 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
S02: Bấm nút thêm vào giỏ hàng mà mà 
Ủa kiểm tra đơn hàng ở đâu vậy
Thấy là cái web này tính năng từ việc chọn đơn hàng rồi xác nhận đơn hàng đến xác nhận mã giảm giá rất hợp lý, không có vấn đề gì. Mình nghĩ cái web rất là ổn.
===
link mới:
https://inexpensive-runner-manufacturing-convert.trycloudflare.com/
```

**Output:**
````
Ghi phiếu S02:
- **N:** "Bấm nút thêm vào giỏ hàng mà mà…". Câu bị cụt, em bổ sung từ trí nhớ hoặc video xem bạn nói gì tiếp và có bấm lại không.
- **D/N:** "Ủa kiểm tra đơn hàng ở đâu vậy". Ghi mm:ss và bạn tìm thấy bằng cách nào: tự tìm hay có trợ giúp.
- **N (nhận xét chung):** chọn hàng, xác nhận đơn, mã giảm giá đều hợp lý; web ổn.

Đây là phiên thứ hai có vấn đề ở nút thêm giỏ (S00 bị lag, S01 ở danh sách không được, S02 thì câu bị cụt nên chưa rõ). Em chỉ ghi lại, tới phần findings mới gom.

**Khối chat S03:**
```
Link: https://inexpensive-runner-manufacturing-convert.trycloudflare.com/

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản: test@eshop.com / Test1234!
Xong thì nói "Xong".
```
Form: mã phiên **S03**.
````

**Xử lý:** [...]

---

## #142 | 23:05 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
phiên mới
```

**Output:**
```
Link mới: https://imaging-knowledgestorm-bikes-ages.trycloudflare.com
- Đã tắt tunnel cũ, restart backend (dữ liệu seed lại). Trang chủ trả 200, `/api/products` có đủ 5 sản phẩm (kiểm bằng curl). Tunnel đang chạy, em không tự tắt.
```

**Xử lý:** [...]

---

## #143 | 23:06 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
S03: Chưa thấy hình của sản phẩm
Không rành, nhưng mà kiểu thấy nó nhạy hơn
Các luồng thực hiện nhanh hơn so với Shopee.
===
https://imaging-knowledgestorm-bikes-ages.trycloudflare.com/
```

**Output:**
````
Ghi phiếu S03:
- **N:** "Chưa thấy hình của sản phẩm".
- **N:** "Không rành, nhưng mà kiểu thấy nó nhạy hơn". Câu này mơ hồ: nhạy hơn cái gì, so với gì? Nếu lúc đó em đã hỏi lại thì ghi câu trả lời. Chưa hỏi thì ghi "không hỏi lại" để khỏi diễn giải hộ.
- **N:** "Các luồng thực hiện nhanh hơn so với Shopee".
- Ghi nghề nghiệp nếu bạn tự nói "không rành": đây là người non-IT, đúng hồ sơ ưu tiên.

Đã xong S00 và S01–S03, còn 4 phiên. Khoảng 15 phút mỗi phiên tính cả đổi người, nên dự kiến xong lúc 00:10.

**Khối chat S04:**
```
Link: https://imaging-knowledgestorm-bikes-ages.trycloudflare.com/

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản: test@eshop.com / Test1234!
Xong thì nói "Xong".
```
Form: mã phiên **S04**.
````

**Xử lý:** [...]

---

## #144 | 23:39 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
phiên mới
```

**Output:**
```
Link mới: https://protecting-creativity-repeat-gene.trycloudflare.com
- Đã tắt tunnel cũ, restart backend (dữ liệu seed lại). Trang chủ trả 200, `/api/products` có đủ 5 sản phẩm (kiểm bằng curl). Tunnel đang chạy, em không tự tắt.
```

**Xử lý:** [...]

---

## #145 | 23:41 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
S04: I clicked the button but it doesn't having anything. What is going on. 
It's show the AirPods Pro, doesn't have number 2 in it (picture). Oohh, look it, perfect (Description). It's already in the Cart. Oh I forgot to Sign In. Let's sign in. My account is:... Sign In. Wait a minute, how can I click put it in the Cart the outside in.
Ý là mình thậm chí còn chưa đăng nhập vào nữa sao có thể thêm vào giỏ hàng. Là mình thêm vào giỏ hàng nào á.
I got a voucher VIP100. 
Có vẻ như nút thêm vào giỏ chả làm gì cả (ở list, trang chủ).
Thử tìm có ra không.
Oke, ấn thêm vào giỏ cũng không được luôn. Aaaaaa, Oh, bấm thêm vào giỏ hàng không được nhưng nó không có tín hiệu gì cả, không có thông tin nhận biết cho thấy mình đã thêm vào giỏ hàng. Bấm xoá này cũng không xoá được luôn à. À xoá được xoá được xoá được.
Oke xoá được xoá được, tiếp tục mua hàng vẫn được. Thêm vào giỏ nhưng nó không hiện thông tin gì mình đã thêm vào giỏ cả. Còn bấm vào chi tiết bấm thêm vào giỏ hàng thì hắn thêm rồi nè.
Vấn đề làm sao để nhập voucher VIP100.
Ở đây nhiệm vụ cần nhập voucher thì mới hoàn thành, nhưng mà nó mới (ý là ở cart).
Ủa, sao tổng tiền thanh toán có thể điều chỉnh được.
Ủa mình có thể trả ít hơn tiền à. Hmmm. Lạ thế. Cái nút này là sao ta. Oke mình cứ áp mã VIP100 vào xem thử giảm được bao nhiêu tiền, ừ giảm đúng rồi đỏ.
Trả 100000 thôi được không, ok thanh toán (điều chỉnh số tiền), thanh toán thành công luôn. Mình thậm chí có thể trả ít tiền hơn.
Giờ vào mua lại với voucher VIP100, VIP1000 thì sao, à không tồn tại. Oke xác nhận thanh toán. Oke mình thanh toán thành công rồi nhưng mà kiểm tra xem đơn hàng đã được ghi nhận chưa và đang ở trạng thái nào.
Là mình về trang chủ và sau đó mình, sau đó mình xem giỏ hàng à, chỉ xem được giỏ hàng thôi. À đây đây (ở profile). A, chờ xác nhận nữa, vậy là nếu mình không trả đủ tiền thì có thể từ chối đơn à. Ngay từ đầu mình không cho khách hàng chỉnh giá thì đâu cần có trạng thái "Chờ xác nhận" đâu.
Thanh toán đơn hàng rồi mới nhập số điện thoại và địa chỉ giao hàng à.
Let's input my phone number to watch see will happen. and my adress.
I put the button, thông báo gì đây, ủa số điện thoại đủ 10 số mà...
Nhắc lại nhiệm vụ.
Điền form: nhiệm vụ vừa rồi khá là dễ, nhưng nó khá là dễ với người thông minh.
===
https://protecting-creativity-repeat-gene.trycloudflare.com/
```

**Output:**
````
S04 là phiên rất giàu dữ kiện. Khi ghi phiếu, em giữ nguyên văn (cả tiếng Anh) và tách theo loại:

- **L/N – thêm giỏ ở danh sách và trang chủ:** bấm không có phản hồi, không biết đã thêm chưa. Ở trang chi tiết thì thêm được.
- **N – giỏ khi chưa đăng nhập:** "chưa đăng nhập sao có thể thêm vào giỏ hàng, giỏ hàng nào".
- **D – nút xoá trong giỏ:** lúc đầu tưởng xoá không được, sau đó xoá được.
- **D – tìm ô voucher.**
- **L/N – tổng tiền ở checkout sửa được:** bạn tự sửa trả 100.000, thanh toán thành công, rồi đặt lại đơn với VIP100. Đây là **phiên thứ hai** (sau S01) có người tham gia sửa được số tiền.
- **N – thử mã VIP1000:** thông báo không tồn tại.
- **D – tìm đơn hàng:** về trang chủ, vào giỏ, cuối cùng thấy ở Hồ sơ. Bạn nói trạng thái "Chờ xác nhận", kèm nhận xét về trạng thái này.
- **N – thứ tự bước:** "Thanh toán đơn hàng rồi mới nhập số điện thoại và địa chỉ giao hàng à".
- **L – Hồ sơ:** SĐT đủ 10 số bị báo lỗi. Dữ kiện liên quan: Claude Code cô lập ở 5/6e rằng `Profile.jsx:43` chặn SĐT bắt đầu bằng 0, đúng chỗ BUG-73/75/78 của em.
- **T:** em nhắc lại nhiệm vụ. Ghi câu em nói và mm:ss.
- **Form:** "khá là dễ, nhưng dễ với người thông minh".

**Lưu ý giờ:** S04 kéo dài khoảng 30 phút, gấp 3 lần kế hoạch. Ghi thời gian thật vào phiếu, đây cũng là dữ kiện. Còn S05–S07, nếu mỗi phiên khoảng 15 phút thì xong lúc 00:30. Từ giờ em giữ mốc 6 phút: hết giờ thì *"Mình dừng ở đây nhé"*, trừ khi bạn đang sắp xong.

**Khối chat S05:**
```
Link: https://protecting-creativity-repeat-gene.trycloudflare.com/

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản: test@eshop.com / Test1234!
Xong thì nói "Xong".
```
Form: mã phiên **S05**.
````

**Xử lý:** [...]

---

## #146 | 23:55 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
phiên mới
```

**Output:**
```
Link mới: https://translate-clients-storage-friday.trycloudflare.com
- Đã tắt tunnel cũ, restart backend (dữ liệu seed lại). Trang chủ trả 200, `/api/products` có đủ 5 sản phẩm (kiểm bằng curl). Tunnel đang chạy, em không tự tắt.
```

**Xử lý:** [...]

---

## #147 | 00:00 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
S05: Mình nghĩ là khi ấn thêm vào giỏ thì phải hiện thông báo đơn hàng này phải thêm vào giỏ để người dùng dễ nhận biết hơn. Ví dụ thêm vào rồi thì ở cái chỗ giỏ hàng hiển thị số 1 để biết có 1 đơn hàng trong giỏ hàng.
===
https://translate-clients-storage-friday.trycloudflare.com/
```

**Output:**
````
Ghi phiếu S05:
- **N:** "khi ấn thêm vào giỏ thì phải hiện thông báo… để người dùng dễ nhận biết hơn". Bạn gợi ý: biểu tượng giỏ hiện số 1 khi có 1 món. Ghi nguyên văn, đây là đề xuất của người tham gia.
- Ghi thêm mốc thời gian, kết quả hoàn thành, trạng thái đơn bạn nói, và có lần sửa tổng tiền hay không. Thông tin này để so với S01/S04.

Hiện tại phiên thứ 4 trên 5 có nhắc tới phản hồi của nút thêm giỏ (S00, S01, S04, S05). Em chỉ ghi lại, tới phần findings mới gom.

Còn S06 và S07. Bây giờ là 00:00, deadline 10:00.

**Khối chat S06:**
```
Link: https://translate-clients-storage-friday.trycloudflare.com/

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản: test@eshop.com / Test1234!
Xong thì nói "Xong".
```
Form: mã phiên **S06**.
````

**Xử lý:** [...]

---

## #148 | 00:02 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Không làm pilot đâu nhé. Hết người rồi. Nên là nộp cả S00 đến S06 đấy nhé
```

**Output:**
```
Được. Vì kịch bản không đổi sau S00, dữ liệu S00 vẫn so sánh được với các phiên sau. Nhưng có 2 điểm phải ghi trung thực:

1. **Đề yêu cầu pilot** ("Run a pilot session with one person… refine before the real sessions"). Nếu S00 thành phiên chính thì bài **không có pilot**. Report §5.5 và §12 phải nói rõ:
   - S00 dự kiến là pilot. Do không tuyển thêm được người, em tính S00 là 1 trong 7 phiên.
   - Sau S00 không sửa kịch bản nhiệm vụ, chỉ bổ sung cách điều phối: hỏi lại ngay khi người tham gia nhận xét mơ hồ, áp dụng từ S01.
   - Phần "pilot" trong tự chấm Task 2 trừ tương ứng.

   Không được ghi là có pilot, cũng không được dùng S00 vừa làm pilot vừa tính vào 7 phiên.
2. **Khác biệt nhỏ về cách điều phối** giữa S00 và S01–S06 (S00 không hỏi lại "mật khẩu hơi kỳ kỳ") nên ghi vào phần giới hạn của nghiên cứu.

Theo kế hoạch cũ, commit pilot là `2/10` và các phiên là `3/10…9/10`. Giờ sẽ là S00–S06 tương ứng `3/10…9/10`. Anh sẽ đưa vào lệnh nhập dữ liệu sau.

**S06 (phiên cuối):** dùng khối chat vừa gửi, link `https://translate-clients-storage-friday.trycloudflare.com/`, mã phiên **S06**.

Xong S06, em làm theo thứ tự:
1. Bảo Claude Code tắt tunnel.
2. Gửi anh 7 file phiếu (`S00.txt`…`S06.txt`) và nghề nghiệp của từng bạn (không cần tên, SĐT).
3. Anh đưa lệnh dựng JSON và tính SUS. Em kiểm số rồi viết findings.
```

**Xử lý:** [...]

---

## #149 | 00:21 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
tắt tunnel
```

**Output:**
```
Đã tắt tunnel: cloudflared và Vite (:5173) không còn chạy.
- Backend :3000 vẫn chạy (script để backend lại sau mỗi phiên), dữ liệu của phiên cuối vẫn nằm trong đó. Lần restart backend tới sẽ xoá và seed lại. Muốn tắt backend luôn thì báo em.
- SUT vẫn ở nhánh `usability-tunnel`. Trước khi chạy lại checklist hoặc làm bài khác, chạy `tools\sut_main.ps1` để về `main`.
```

**Xử lý:** [...]

---

## #150 | 00:22 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Vậy S07 ngày mai thêm được không, vì giờ mọi người đi ngủ hết rồi á.
Nghề nghiệp theo thứ tự: DA, SWE, DE, Vật lý học, Tự động hoá, Dược, Thực phẩm
```
*Đính kèm:* `S00.txt`, `S01.txt`, `S02.txt`, `S03.txt`, `S04.txt`, `S05.txt`, `S06..txt`

**Output:**
````
**Không cần S07.** S00–S06 đã đủ 7 phiên, đúng số đề yêu cầu. Thêm S07 sáng mai cũng không thành pilot, vì pilot phải chạy *trước* các phiên chính. Thêm phiên nữa chỉ tốn giờ, còn sáng mai em cần thời gian cho findings, Critique và nộp bài trước 10:00.

**Hồ sơ 7 người:** DA, SWE, DE là 3 người IT; Vật lý, Tự động hoá, Dược, Thực phẩm là 4 người non-IT (Tự động hoá em tự xếp, ghi rõ trong bảng). Ghi tỉ lệ này vào phần giới hạn của nghiên cứu.

**Điểm yếu cần biết:** phiếu quan sát hiện chỉ có câu nói. Chưa có **mốc thời gian, kết quả hoàn thành (có/không trợ giúp), số lỗi, do dự, trợ giúp** của từng phiên, trong khi plan mục 8 đo những thứ này. Cách gỡ nhanh:
- Có video thì tua lại, mỗi phiên lấy **tổng thời gian + kết quả hoàn thành + có trợ giúp không**. Khoảng 3 phút một phiên.
- Không có video hoặc không kịp thì ghi theo trí nhớ, ghi rõ "theo ghi nhớ của người điều phối, không có mốc mm:ss", và đưa vào phần giới hạn. Không được bịa số.

Em gửi anh 7 dòng theo mẫu này (điền từ video hoặc trí nhớ):
```
S00: thời gian ~__ phút · hoàn thành: không trợ giúp/có trợ giúp/không · nói đúng trạng thái đơn: có/không · có sửa tổng tiền: có/không
```

Rồi tải CSV từ tab Responses của form, đặt vào `HW03\usability\evidence_raw\responses.csv`, và dán cho Claude Code:

```
NHIỆM VỤ: nhập 7 phiên usability S00–S06 (T2 3/10…9/10). SV chốt: không có pilot – S00 (dự kiến pilot) tính là phiên chính vì không tuyển thêm được người; sau S00 không sửa kịch bản, chỉ thêm "hỏi lại ngay khi nhận xét mơ hồ" từ S01. Ghi report_plan mục e. Không push, không amend.
1. Tắt tunnel. Đảm bảo HW03/usability/evidence_raw/ bị gitignore (CSV có họ tên/SĐT – KHÔNG commit, KHÔNG in ra báo cáo).
2. SV đặt phiếu ghi tay S00.txt…S06.txt vào HW03/usability/sessions/notes/ → commit nguyên văn (không sửa chữ).
3. Mỗi phiên: new_session.py tạo khung S0x; điền (nhãn "AI chép, SV duyệt"): mã P0x, nghề nghiệp theo thứ tự S00…S06 = DA, SWE, DE, Vật lý học, Tự động hoá, Dược, Thực phẩm; SEQ + 10 câu SUS chép từ responses.csv theo cột "Mã phiên" (chữ số đầu của ô); câu nói nguyên văn từ notes/S0x.txt; thời gian/kết quả = `<SV điền>`. Mã phiên trong CSV trùng/thiếu/có dòng thử ("z") → bỏ dòng thử, thiếu thì DỪNG báo.
4. sus_score.py HW03/usability/sessions --check (lỗi → báo, không tự sửa số).
5. Commit mỗi phiên 1 commit `HW03[T2] k/10: phiên S0x` (S00=3/10 … S06=9/10).
Báo cáo ≤ 10 dòng: SEQ + SUS từng phiên (đã tính), trung bình, lỗi check, hash.
```

Sau đó: em điền thời gian và kết quả vào JSON, Claude Code chạy `sus_score.py --report`, rồi em viết findings (§5.8, 5.9). Ngủ được thì ngủ vài tiếng trước khi viết findings; đầu óc tỉnh viết sẽ nhanh hơn.
````

**Xử lý:** [...]

---

## #151 | 00:30 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Mở lại tunnel
```

**Output:**
```
Tunnel đã mở lại: https://medicine-thee-flush-soldier.trycloudflare.com
- Trang chủ trả 200, `/api/products` có đủ 5 sản phẩm (kiểm bằng curl). SUT vẫn ở `usability-tunnel` @ `e33212d`.
- Lần này em không restart backend để giữ dữ liệu của phiên trước (tài khoản, đơn hàng); chỉ bật lại Vite và cloudflared bằng tay. Cần phiên sạch (seed lại) thì nói "phiên mới".
```

**Xử lý:** [...]

---

## #152 | 00:32 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
https://medicine-thee-flush-soldier.trycloudflare.com/
---
mới mở lại cho lượt 7, viết nhé
```

**Output:**
````
Khối chat cho **S07**:

```
Link: https://medicine-thee-flush-soldier.trycloudflare.com/

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản: test@eshop.com / Test1234!
Xong thì nói "Xong".
```

Form: `https://docs.google.com/forms/d/e/1FAIpQLScZPV1xgaQLVw8nUl8wmY8EqEol7BeoMwhDjaCw1rEXGoNuqQ/viewform`, mã phiên **S07**.

Nhớ bật quay sau khi bạn đồng ý, bấm đồng hồ khi bạn mở link, và hỏi lại ngay khi bạn nhận xét mơ hồ.

Có S07 thì bài có 8 người, nhiều hơn mức 7 của đề, nên cũng tốt. Nhưng S00 vẫn là phiên chính, không phải pilot. Khi dán lệnh nhập dữ liệu cho Claude Code, em sửa mấy chỗ:
- "S00–S06" thành "S00–S07".
- Thêm nghề nghiệp của S07 vào cuối danh sách.
- Commit S07 thành `HW03[T2] 10/10: phiên S07`.
````

**Xử lý:** [...]

---

## #153 | 00:41 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Xong luôn rồi, vẫn để pilot nhé. Nên là quay tới S07 là đúng nhỉ
```
*Đính kèm:* `S07.txt`

**Output:**
````
Đúng: **S00 là pilot, S01–S07 là 7 phiên chính**. Cách này hợp lệ và tốt hơn phương án lúc nãy, vì S00 thật sự chạy *trước* các phiên chính và có rút kinh nghiệm (hỏi lại ngay khi người tham gia nhận xét mơ hồ, áp dụng từ S01). Như vậy đủ cả pilot lẫn 7 phiên theo đề.

Ghi phiếu S07 (nguyên văn):
- **L/N:** "Bấm 1 đơn thành 2 đơn". Nếu em nhớ thì ghi bạn bấm nút nào, bấm mấy lần.
- **N:** "Không cần nhập địa chỉ, số điện thoại vẫn đặt được đơn".
- **N:** "Tên cũng không cần đổi vẫn đặt được".

**Cần em bổ sung:** nghề nghiệp lúc nãy em đưa 7 cái cho S00–S06. Giờ cần nghề của **S07**, và xác nhận thứ tự vẫn là S00 = DA, S01 = SWE, …, S06 = Thực phẩm.

Lệnh cho Claude Code (thay `<...>`):

```
NHIỆM VỤ: nhập pilot + 7 phiên usability. SV chốt: S00 = pilot (chạy trước, sau pilot giữ nguyên kịch bản, bổ sung "hỏi lại ngay khi nhận xét mơ hồ" từ S01); S01–S07 = 7 phiên chính. Ghi report_plan mục e + report §5.5. Còn <...> → DỪNG. Không push, không amend.
1. Tắt tunnel. Kiểm HW03/usability/evidence_raw/ bị gitignore (responses.csv có họ tên/SĐT – KHÔNG commit, KHÔNG in ra báo cáo).
2. SV đặt notes S00.txt…S07.txt vào HW03/usability/sessions/notes/ → commit nguyên văn.
3. Mỗi phiên: new_session.py tạo khung; điền (nhãn "AI chép, SV duyệt"): mã P00…P07; nghề nghiệp S00…S07 = DA, SWE, DE, Vật lý học, Tự động hoá, Dược, Thực phẩm, <nghề S07>; SEQ + 10 câu SUS từ responses.csv theo "Mã phiên" (chữ số đầu; bỏ dòng thử "z"; thiếu/trùng → DỪNG báo); câu nói nguyên văn từ notes; thời gian/kết quả/trợ giúp = `<SV điền>`. S00 đánh dấu pilot, không tính vào thống kê 7 phiên.
4. sus_score.py HW03/usability/sessions --check.
5. Commit: S00 `HW03[T2] 2/10: pilot S00`; S01…S07 `HW03[T2] 3/10…9/10: phiên S0x`.
Báo cáo ≤ 10 dòng: SEQ + SUS từng phiên, trung bình S01–S07, lỗi check, hash.
```

Trong lúc Claude Code chạy, em gửi anh dòng tóm tắt từng phiên theo mẫu: thời gian, hoàn thành có/không trợ giúp, nói đúng trạng thái đơn, có sửa tổng tiền. Em lấy từ video hoặc trí nhớ, ghi rõ nguồn nào.
````

**Xử lý:** [...]

---

## #154 | 00:43 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Vậy prompt ở trên kia có cần sử dụng không nhỉ (prompt mà có tải CSV ấy)
```
*Đính kèm:* `EShop_-_Phi_u_ng__i_tham_gia___nh_gi__HW03.csv`

**Output:**
```
Vẫn dùng prompt đó: Claude Code cần đọc CSV trên máy em để chép số SEQ/SUS vào JSON. Nhưng phải sửa 3 chỗ, và có 1 việc khai báo.

**1. Sửa trong prompt**
- **Mã "SO1" (chữ O):** dòng S01 trong form bị gõ nhầm. Thêm vào prompt: *"dòng 'SO1' (chữ O) = S01, ghi notes 'mã phiên người tham gia gõ nhầm'"*. Không thêm thì Claude Code sẽ DỪNG vì thiếu S01.
- **Nghề S07:** em chưa đưa. Lưu ý cột "Bạn là" trong form chủ yếu ghi "Năm 4" hoặc "4", không trùng danh sách nghề em gửi anh. Dùng danh sách của em, ghi nguồn "SV cung cấp".
- **S07 chọn "Không" ở câu đồng ý để TA liên hệ.** Ghi vào bảng người tham gia. Đề nói TA có thể gọi ngẫu nhiên 2 người, nên trong bảng em đánh dấu S07 "không đồng ý liên hệ" để TA chọn người khác.

**2. Khai báo quyền riêng tư**
File CSV em vừa gửi lên đây có **họ tên và SĐT thật của 8 người**. AI-01 cấm tải dữ liệu cá nhân lên AI công cộng. Đã gửi rồi thì không rút lại được, nên ở **AI-05** không tick im lặng mục này. Ghi một dòng minh bạch, ví dụ: "em đã lỡ gửi file CSV có họ tên và SĐT người tham gia cho Claude ở phiên thảo luận lúc 00:43 11/11; AI chỉ dùng cột số SEQ/SUS". Từ giờ chỉ đưa CSV cho Claude Code ở `evidence_raw/` trên máy em.

**3. Số liệu anh tính thử** (chỉ để em đối chiếu khi Claude Code báo về):

| Phiên | SEQ | SUS |
|---|---|---|
| S00 (pilot) | 6 | 85,0 |
| S01 | 6 | 55,0 |
| S02 | 7 | 90,0 |
| S03 | 7 | 97,5 |
| S04 | 4 | 52,5 |
| S05 | 7 | 90,0 |
| S06 | 6 | 75,0 |
| S07 | 7 | 85,0 |
| **TB S01–S07** | **6,29** | **77,9** |

Bảng chỉ để em kiểm. Report phải lấy số từ `sus_score.py --report`. Nếu Claude Code ra khác thì báo anh.

Một điểm cho phần findings của em: hai phiên SUS thấp nhất (S01, S04) cũng là hai phiên người tham gia sửa được tổng tiền và trả lời "không tin" ở câu tin cậy.
```

**Xử lý:** [...]

---

## #155 | 00:44 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Là dùng cả prompt trên và prompt dưới luôn sao, có thể giúp tôi gộp lại không
```

**Output:**
````
Dùng một prompt này thay cho cả hai. Em chỉ cần điền `<nghề S07>`:

```
NHIỆM VỤ: nhập pilot + 7 phiên usability. SV chốt: S00 = pilot (chạy trước; sau pilot giữ nguyên kịch bản, bổ sung "hỏi lại ngay khi nhận xét mơ hồ" từ S01); S01–S07 = 7 phiên chính. Ghi report_plan mục e + report §5.5. Còn <...> → DỪNG. Không push, không amend.
1. Tắt tunnel. SV đặt CSV form ở HW03/usability/evidence_raw/responses.csv – kiểm thư mục này bị gitignore (CSV có họ tên/SĐT: KHÔNG commit, KHÔNG in ra báo cáo/log).
2. SV đặt notes S00.txt…S07.txt vào HW03/usability/sessions/notes/ → commit nguyên văn.
3. Mỗi phiên: new_session.py tạo khung; điền (nhãn "AI chép, SV duyệt"):
   - mã P00…P07; nghề nghiệp (nguồn "SV cung cấp", không lấy cột "Bạn là" của form) S00…S07 = DA, SWE, DE, Vật lý học, Tự động hoá, Dược, Thực phẩm, <nghề S07>;
   - SEQ + 10 câu SUS từ responses.csv theo "Mã phiên" (lấy chữ số đầu ô). Dòng "SO1" (chữ O) = S01, ghi notes "người tham gia gõ nhầm mã phiên". Thiếu/trùng mã khác → DỪNG báo;
   - 3 câu đồng ý (Có/Không) – S07 "đồng ý TA liên hệ" = Không, đánh dấu rõ;
   - câu nói nguyên văn từ notes; câu trả lời 4 câu mở chép nguyên văn từ CSV;
   - thời gian / kết quả hoàn thành / trợ giúp = `<SV điền>`.
   S00 đánh dấu pilot, không tính vào thống kê.
4. sus_score.py HW03/usability/sessions --check (lỗi → báo, không tự sửa số SV).
5. report_plan mục f: AI dựng JSON từ notes + CSV. Mục g (cho AI-05): "SV đã gửi CSV có họ tên/SĐT người tham gia cho phiên thảo luận claude.ai lúc 00:43 11/11; AI chỉ dùng cột SEQ/SUS" – ghi để SV khai minh bạch.
6. Commit: notes `HW03[T2]: phiếu ghi tay S00–S07`; S00 `HW03[T2] 2/10: pilot S00`; S01…S07 `HW03[T2] 3/10…9/10: phiên S0x`.
Báo cáo ≤ 10 dòng: SEQ + SUS từng phiên, trung bình S01–S07, lỗi check, hash. (Đối chiếu: phiên thảo luận tính được S01–S07 SUS TB 77,9, SEQ TB 6,29.)
```

Trước khi dán, em làm 2 việc:
1. Đặt `responses.csv` vào `HW03\usability\evidence_raw\`.
2. Đặt 8 file `S00.txt`…`S07.txt` vào `HW03\usability\sessions\notes\`.
````

**Xử lý:** [...]

---

## #156 | 00:45 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: nhập pilot + 7 phiên usability. SV chốt: S00 = pilot (chạy trước; sau pilot giữ nguyên kịch bản, bổ sung "hỏi lại ngay khi nhận xét mơ hồ" từ S01); S01–S07 = 7 phiên chính. Ghi report_plan mục e + report §5.5. Còn <...> → DỪNG. Không push, không amend.
1. Tắt tunnel. SV đặt CSV form ở HW03/usability/evidence_raw/responses.csv – kiểm thư mục này bị gitignore (CSV có họ tên/SĐT: KHÔNG commit, KHÔNG in ra báo cáo/log).
2. SV đặt notes S00.txt…S07.txt vào HW03/usability/sessions/notes/ → commit nguyên văn.
3. Mỗi phiên: new_session.py tạo khung; điền (nhãn "AI chép, SV duyệt"):
   - mã P00…P07; nghề nghiệp (nguồn "SV cung cấp", không lấy cột "Bạn là" của form) S00…S07 = DA, SWE, DE, Vật lý học, Tự động hoá, Dược, Thực phẩm, IT;
   - SEQ + 10 câu SUS từ responses.csv theo "Mã phiên" (lấy chữ số đầu ô). Dòng "SO1" (chữ O) = S01, ghi notes "người tham gia gõ nhầm mã phiên". Thiếu/trùng mã khác → DỪNG báo;
   - 3 câu đồng ý (Có/Không) – S07 "đồng ý TA liên hệ" = Không, đánh dấu rõ;
   - câu nói nguyên văn từ notes; câu trả lời 4 câu mở chép nguyên văn từ CSV;
   - thời gian / kết quả hoàn thành / trợ giúp = `<SV điền>`.
   S00 đánh dấu pilot, không tính vào thống kê.
4. sus_score.py HW03/usability/sessions --check (lỗi → báo, không tự sửa số SV).
5. report_plan mục f: AI dựng JSON từ notes + CSV. Mục g (cho AI-05): "SV đã gửi CSV có họ tên/SĐT người tham gia cho phiên thảo luận claude.ai lúc 00:43 11/11; AI chỉ dùng cột SEQ/SUS" – ghi để SV khai minh bạch.
6. Commit: notes `HW03[T2]: phiếu ghi tay S00–S07`; S00 `HW03[T2] 2/10: pilot S00`; S01…S07 `HW03[T2] 3/10…9/10: phiên S0x`.
Báo cáo ≤ 10 dòng: SEQ + SUS từng phiên, trung bình S01–S07, lỗi check, hash. (Đối chiếu: phiên thảo luận tính được S01–S07 SUS TB 77,9, SEQ TB 6,29.)
```

**Output:**
```
Em dừng ở bước 2: chưa có file CSV và notes nên chưa nhập được phiên nào.
- Tunnel đã tắt (cloudflared và Vite :5173); backend :3000 vẫn chạy.
- `HW03/usability/evidence_raw/` lúc đầu chưa bị gitignore. Em đã thêm dòng `HW03/usability/evidence_raw/` vào `.gitignore` và kiểm lại thì `responses.csv` đã bị ignore. Thay đổi này chưa commit; em sẽ commit chung với commit notes.
- Thiếu `HW03/usability/evidence_raw/responses.csv` (cả thư mục chưa có).
- Thiếu `HW03/usability/sessions/notes/S00.txt…S07.txt` (trong `sessions/` hiện chỉ có `.gitkeep`).

SV đặt CSV và 8 file notes vào đúng đường dẫn trên rồi báo em làm tiếp từ bước 2.
```

**Xử lý:** [...]

---

## #157 | 00:46 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
đã đặt CSV và notes rồi, làm tiếp
```

**Output:**
```
Em dừng ở bước 2: CSV đã có nhưng notes vẫn chưa thấy, nên chưa tạo phiên và chưa commit gì.
- **Notes:** chưa có `HW03/usability/sessions/notes/` (thư mục chưa tồn tại). Em tìm mọi file mới trong repo cũng không thấy file `S0*.txt` nào. Có thể SV đã lưu sang chỗ khác.
- **CSV:** có 8 dòng, mã phiên S00, SO1 (chữ O, sẽ tính là S01), S02 … S07; không thiếu hay trùng mã nào khác. S07 chọn "Không" ở câu đồng ý trợ giảng liên hệ. File bị gitignore; em chỉ đọc cột mã phiên, đồng ý, SEQ, SUS, không in họ tên/SĐT.
- **Tính thử từ CSV** (chưa ghi vào file nào):

| Phiên | SEQ | SUS |
|---|---|---|
| S00 (pilot) | 6 | 85 |
| S01 | 6 | 55 |
| S02 | 7 | 90 |
| S03 | 7 | 97,5 |
| S04 | 4 | 52,5 |
| S05 | 7 | 90 |
| S06 | 6 | 75 |
| S07 | 7 | 85 |

  Trung bình S01–S07: SUS 77,86, SEQ 6,29, khớp số phiên thảo luận (77,9 và 6,29).

SV đặt `S00.txt … S07.txt` vào `HW03/usability/sessions/notes/` (hoặc báo đường dẫn đang lưu) rồi em làm tiếp từ bước 2.
```

**Xử lý:** [...]

---

## #158 | 00:47 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
đã đặt notes rồi, làm tiếp
```

**Output:**
```
Notes + CSV có đủ. Đang xem report §5 và report_plan để ghi quyết định, rồi dựng JSON phiên.

Notes đã commit. Đang viết script dựng 8 phiếu JSON từ notes + CSV.

Đã nhập pilot S00 và 7 phiên chính S01–S07: mỗi phiên một file JSON, đã commit; `--check` báo 16 lỗi, đều do các ô `<SV điền>`.

| Phiên | SEQ | SUS |
|---|---|---|
| S00 (pilot, không tính) | 6 | 85 |
| S01 | 6 | 55 |
| S02 | 7 | 90 |
| S03 | 7 | 97,5 |
| S04 | 4 | 52,5 |
| S05 | 7 | 90 |
| S06 | 6 | 75 |
| S07 | 7 | 85 |

- **Trung bình S01–S07:** SUS 77,86, SEQ 6,29, khớp số phiên thảo luận (77,9 / 6,29).
- **Kết quả `sus_score.py --check`:** 16 lỗi, đúng 2 ô mỗi phiếu (`hoan_thanh`, `ket_thuc` đang để `<SV điền>`). Vì vậy chưa phiên nào được tính vào bảng thống kê cho tới khi SV điền. Còn một số cảnh báo `t` / `reset_du_lieu` cũng do ô `<SV điền>`. Không có lỗi dữ liệu cá nhân (SĐT, email).
- **Ghi chú trong phiếu:** S01 ghi "gõ nhầm mã phiên (SO1, chữ O)"; S07 ghi `lien_he_xac_nhan` = false, kèm câu "KHÔNG đồng ý để trợ giảng liên hệ xác nhận".
- **CSV:** `HW03/usability/evidence_raw/` đã bị gitignore, không commit. Em chỉ đọc cột mã phiên, ngày, đồng ý, SEQ, SUS, 4 câu mở; không in họ tên/SĐT ra đâu.
- **Notes:** file `S06..txt` (dư dấu chấm) em đã đổi tên thành `S06.txt`, nội dung giữ nguyên văn.
- **Report:** khôi phục lại khung §5.4–5.9 trước đó, §5.5 ghi quyết định pilot; report_plan đã ghi mục e (PILOT), f (`tools/usability_fill_hw03.py` do AI viết), g (dòng CSV gửi lúc 00:43 11/11).
- **Commit:** `411c7ca` (notes), `750cfdd` (2/10 pilot S00), `8c9145d` … `52ea483` (3/10 … 9/10, S01–S07). Chưa push.
- **Còn treo:**
  - Ô `<SV điền>` (thời gian, hoàn thành, trợ giúp, nền tảng, reset dữ liệu) do SV nhập.
  - Mọi dòng notes đang để loại N (câu nói nguyên văn). Có vài dòng là ghi chú của SV chứ không phải lời người tham gia, cần đổi loại: S01 dòng 5–7, S04 dòng 17 "Nhắc lại nhiệm vụ." (có thể là một lần trợ giúp).
  - Test summary ở README/report vẫn ghi "không thực hiện phiên usability", cần sinh lại bằng `summary_hw03.py`.
```
*File AI ghi/gửi trong lượt này:* `usability_fill_hw03.py`

**Xử lý:** [...]

---

## #159 | 00:50 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
- Trung bình S01–S07: SUS 77,86, SEQ 6,29, khớp số phiên thảo luận (77,9 / 6,29).
- Kết quả sus_score.py --check: 16 lỗi, đúng 2 ô mỗi phiếu (hoan_thanh, ket_thuc đang để <SV điền>). Vì vậy chưa phiên nào được tính vào bảng thống kê cho tới khi SV điền. Còn một số cảnh báo t / reset_du_lieu cũng do ô <SV điền>. Không có lỗi dữ liệu cá nhân (SĐT, email).
- Ghi chú trong phiếu: S01 ghi "gõ nhầm mã phiên (SO1, chữ O)"; S07 ghi lien_he_xac_nhan = false, kèm câu "KHÔNG đồng ý để trợ giảng liên hệ xác nhận".
- CSV: HW03/usability/evidence_raw/ đã bị gitignore, không commit. Em chỉ đọc cột mã phiên, ngày, đồng ý, SEQ, SUS, 4 câu mở; không in họ tên/SĐT ra đâu.
- Notes: file S06..txt (dư dấu chấm) em đã đổi tên thành S06.txt, nội dung giữ nguyên văn.
- Report: khôi phục lại khung §5.4–5.9 trước đó, §5.5 ghi quyết định pilot; report_plan đã ghi mục e (PILOT), f (tools/usability_fill_hw03.py do AI viết), g (dòng CSV gửi lúc 00:43 11/11).
- Commit: 411c7ca (notes), 750cfdd (2/10 pilot S00), 8c9145d … 52ea483 (3/10 … 9/10, S01–S07). Chưa push.
- Còn treo:
  - Ô <SV điền> (thời gian, hoàn thành, trợ giúp, nền tảng, reset dữ liệu) do SV nhập.
  - Mọi dòng notes đang để loại N (câu nói nguyên văn). Có vài dòng là ghi chú của SV chứ không phải lời người tham gia, cần đổi loại: S01 dòng 5–7, S04 dòng 17 "Nhắc lạần trợ giúp).
  - Test summary ở README/report vẫn ghi "không thực hiện phiên usability", cần sinh lại bằng summary_hw03.py.
```

**Output:**
````
Số liệu đã khớp. Phần Task 2 còn phải làm như sau.

**1. Em điền JSON (khoảng 15 phút).** Mở `HW03/usability/sessions/S0x.json`, thay các ô `<SV điền>`:
- `hoan_thanh`: không trợ giúp / có trợ giúp / không hoàn thành.
- `ket_thuc` và thời gian `t`: lấy từ video hoặc trí nhớ, kèm ghi chú nguồn.
- `tro_giup`.
- `nen_tang`: trình duyệt và OS của người tham gia. Không biết thì ghi "không ghi nhận".
- `reset_du_lieu`: = true nếu phiên đó em có bảo Claude Code "phiên mới", vì script restart backend.

Sửa luôn loại dòng: S01 dòng 5–7 là ghi chú của em (chuyển sang loại ghi chú, không phải N). S04 "Nhắc lại nhiệm vụ" là **T**.
Không nhớ số thì ghi đúng như vậy, **không ước lượng cho đẹp**.

Xong thì commit `HW03[T2]: SV điền kết quả phiên S00–S07`, push, rồi dán:
```
sus_score.py HW03/usability/sessions --check phải 0 lỗi → --report vào marker REPORT:U1; chạy lại summary_hw03.py (README + report §8 hết dòng "không thực hiện phiên"). Commit `HW03[T2] 10/10: số liệu U1`. Báo ≤ 5 dòng + hash.
```

**2. Em viết findings §5.8–5.9 (🔒, khoảng 45 phút).** Gom pain point, tách lỗi riêng lẻ với vấn đề thiết kế, xếp theo severity.

**Ước thời gian còn lại (bây giờ 00:50, deadline 10:00):**

| Giờ | Việc | Ai |
|---|---|---|
| 00:50–01:10 | Điền JSON phiên | Em |
| 01:10–02:10 | Sửa 14 bug theo `bug_check.md`, commit `5/6f`, push | Em |
| 02:10–03:00 | Tạo 28 issue và chụp ảnh trang Issues (em xác nhận bảng tiêu đề, kéo ảnh) | Claude Code + em |
| 02:10–03:00 | Song song: findings §5.8–5.9, §3.4 | Em |
| 03:00–07:00 | Ngủ | |
| 07:00–09:30 | Duyệt khối 📝, Critique, verdict Audit, tự chấm, AI-05, PDF, xuất transcript `_p2`, commit log, zip | Em + Claude Code |
| Nếu còn giờ | Video skill. Không kịp thì trừ điểm skill tương ứng | Em |

Nếu phải cắt, **video là thứ cắt đầu tiên**. Thiếu bug hay thiếu Audit thì rủi ro lớn hơn nhiều.
````

**Xử lý:** [...]

---

## #160 | 00:52 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
````
```json
  "reset_du_lieu": "<SV điền>",
```

này điền gì giờ?
````

**Output:**
````
Điền `true` (boolean, **không có ngoặc kép**):

```json
  "reset_du_lieu": true,
```

Trường này hỏi: trước phiên này, backend có được khởi động lại để CSDL seed lại sạch không (xoá đơn và lượt dùng mã của người trước). Script tunnel tự restart backend mỗi lần chạy, nên:
- **S00:** `true`. Tunnel mở lần đầu lúc 21:56.
- **S01–S06:** `true` nếu trước mỗi phiên em đều gõ "phiên mới" cho Claude Code. Mỗi phiên em đều gửi link tunnel mới, link mới đồng nghĩa script đã chạy lại, nên là `true`.
- **S07:** `true`. Em đã mở lại tunnel.

Phiên nào em **không** chạy lại tunnel (dùng lại link cũ) thì ghi `false`. Theo các link em gửi anh tối nay, phiên nào cũng có link riêng.
````

**Xử lý:** [...]

---

## #161 | 00:53 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
nen_tang là Chrome hay Firefox gì đó à
```

**Output:**
````
Đúng, ghi **trình duyệt + hệ điều hành mà người tham gia dùng trong phiên**, không phải P1/P2/P3. Mẫu trong schema ghi `"P1"` là của lúc chạy checklist, còn plan mục 6 nói rõ trình duyệt và OS ở Task 2 là **của người tham gia**.

Ví dụ:
```json
  "nen_tang": "Chrome / Windows 11",
```

Cách điền:
- **Thấy được trong video** (thanh tab, logo trình duyệt, taskbar Windows/macOS) thì ghi theo video, ví dụ `"Edge / Windows 11"`, `"Safari / macOS"`.
- **Không chắc OS** thì chỉ ghi trình duyệt, ví dụ `"Chrome / không ghi nhận OS"`.
- **Không có video và không nhớ** thì ghi `"không ghi nhận"`. Đừng đoán.

Tiện thể điền luôn trường `nhom` theo nghề: DA, SWE, DE là `"IT"`; Vật lý học, Dược, Thực phẩm là `"non-IT"`; Tự động hoá do em tự quyết (đã nói là sẽ xếp và ghi rõ). S07 thì theo nghề em sẽ bổ sung.
````

**Xử lý:** [...]

---

## #162 | 00:55 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
````
```json
    "ket_thuc": "<SV điền>",
    "hoan_thanh": "<SV điền>",
```

Là sao, tưởng hỏi thời gian?
````

**Output:**
````
Có hai ô khác nhau: một ô là thời gian, một ô là kết quả.

**`ket_thuc` là thời gian**: tổng thời gian làm nhiệm vụ, tính từ lúc bạn mở link (00:00) tới lúc nói "Xong" hoặc bỏ cuộc. Định dạng bắt buộc là `mm:ss`:
```json
    "ket_thuc": "05:30",
```
Script báo lỗi nếu không đúng `mm:ss`. Nếu em không bấm giờ, lấy từ video. Không có video thì ước theo trí nhớ, nhưng ghi vào `ghi_chu` ví dụ `"ket_thuc ước theo trí nhớ, không bấm giờ"`.

**`hoan_thanh` là kết quả**, chỉ nhận đúng 1 trong 3 giá trị:

| Giá trị | Khi nào |
|---|---|
| `"khong_tro_giup"` | Bạn tự làm xong, em không nhắc gì |
| `"co_tro_giup"` | Xong nhưng em có can thiệp (ví dụ S04 em nhắc lại nhiệm vụ) |
| `"khong_hoan_thanh"` | Bỏ cuộc, hết giờ, hoặc không đạt tiêu chí thành công |

Lưu ý:
- Script kiểm chéo: có sự kiện loại **T** hoặc mục trong `tro_giup` mà lại ghi `khong_tro_giup` là báo lỗi. Vì vậy S04 phải là `co_tro_giup`.
- **S01 và S04 có sửa tổng tiền.** Tiêu chí thành công trong plan là tổng 5.900.000 ₫ và nói được trạng thái đơn. Nếu đơn cuối cùng của bạn không đúng số này, em quyết là `khong_hoan_thanh`, hay vẫn tính hoàn thành và ghi rõ lý do trong `ghi_chu`. S04 có đặt lại một đơn đúng với VIP100, nên xem đơn đó.
````

**Xử lý:** [...]

---

## #163 | 00:57 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
````
```json
      "t": "<SV điền>",
```

Mấy cái t này điền sao
````

**Output:**
````
`t` là **thời điểm** xảy ra sự kiện (hoặc lần trợ giúp), tính từ lúc bắt đầu nhiệm vụ, định dạng `mm:ss`. Mỗi dòng trong `su_kien` và `tro_giup` có một `t` riêng:

```json
"su_kien": [
  { "t": "01:20", "man_hinh": "Trang chủ", "loai": "L", "mo_ta": "Bấm thêm vào giỏ ở danh sách không có phản hồi", "bug": true }
],
"tro_giup": [
  { "t": "08:30", "ly_do": "...", "cau_noi": "..." }
]
```

Em điền như sau:
- **Có video:** tua tới đúng câu nói hoặc hành động đó, lấy số phút:giây trên video trừ đi lúc bạn mở link.
- **Không có video, nhớ đại khái thứ tự:** vẫn điền `mm:ss` ước lượng theo thứ tự trước sau, và thêm một dòng vào `ghi_chu` của phiên: `"t của su_kien ước theo trí nhớ, không có mốc thật"`.
- **Hoàn toàn không nhớ:** điền `"00:00"` cho mọi dòng, và ghi rõ trong `ghi_chu`: `"không ghi mốc thời gian; t = 00:00 chỉ để đúng định dạng"`. Như vậy script không lỗi, và người chấm biết đây không phải số đo thật.

Quan trọng nhất là **không bịa mốc chính xác** khi em không đo. Ghi chú trung thực sẽ tốt hơn số đẹp mà không có căn cứ; nếu bị vấn đáp, em giải thích được.

Tiện thể: dòng `"bug"` để `true` khi sự kiện đó trùng hoặc liên quan một bug đã biết (ví dụ nút thêm giỏ, sửa được tổng tiền, SĐT bị chặn). Đánh `true` hay `false` là em quyết, vì đó là một phần phân tích của em.
````

**Xử lý:** [...]

---

## #164 | 05:12 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đã điền xong hết rồi. làm gì tiếp nhỉ
```

**Output:**
````
Bây giờ là 05:12, còn khoảng **4 giờ 45 phút**. Trên GitHub vẫn chỉ tới `af92e6d` (20:14), tức các commit phiên usability chưa lên. Em **commit JSON và push ngay**.

**Kế hoạch tới 10:00**, theo thứ tự và chạy song song chỗ được:

| Giờ | Em | Claude Code |
|---|---|---|
| 05:15 | Commit + push JSON phiên | Số liệu U1 + chuẩn bị issue cho 14 bug sạch (lệnh 1) |
| 05:20–06:05 | Sửa 14 bug theo `bug_check.md`, commit `5/6f`, push | Tạo issue 14 bug sạch (em xác nhận bảng tiêu đề, kéo ảnh) |
| 06:05–06:50 | **Findings §5.8–5.9** (🔒) | Tạo 14 issue còn lại, chụp ảnh trang Issues |
| 06:50–07:10 | §3.4 (🔒) + duyệt khối 📝 (§3.2, §4.2, §5.5, §11) | |
| 07:10–07:40 | **Critique 200–300 từ** | |
| 07:40 | | Anh xuất transcript `_p2`, em trích prompt log, Claude Code điền #n vào AI-02/03 |
| 07:50–08:30 | Verdict + lý do Audit, tự chấm §12, ngày | |
| 08:30–09:15 | Ký | AI-05, PDF, commit log, `hw-submission-audit`, zip |
| 09:15–09:45 | Kiểm zip, nộp Moodle | |
| Dư giờ | Video skill. Không kịp thì trừ điểm skill | |

**Lệnh 1 cho Claude Code** (dán sau khi em push):
```
1. sus_score.py HW03/usability/sessions --check phải 0 lỗi (lỗi → báo, không sửa số SV) → --report vào marker REPORT:U1; summary_hw03.py chạy lại (README/report §8 có số U1). Report §5: bỏ dòng "Không thực hiện phiên…" nếu còn. Commit `HW03[T2] 10/10: số liệu U1`.
2. Chuẩn bị issue cho 14 bug "sạch" theo bug_check.md (59, 60, 61, 65, 66, 67, 68, 69, 71, 74, 77, 83, 84, 85): gh = ThachHaoo; lấy lại danh sách issue kiểm trùng lần cuối; in bảng: BUG – tiêu đề GitHub = "[HW03-C2-xx] " + Tiêu đề trong file – label bug – ảnh cần kéo (bản đã che, từ evidence/). DỪNG chờ SV xác nhận bảng. Body lấy nguyên file BUG-xx.md (--body-file), không sửa chữ.
Báo ≤ 10 dòng + bảng + hash. Không push.
```

Sau khi em xác nhận bảng, Claude Code tạo issue tuần tự. Theo quy ước HW02 có 2 điểm dừng: (1) em xác nhận bảng tiêu đề, (2) em kéo ảnh vào issue rồi báo xong. Trong lúc đó em vẫn sửa 14 bug còn lại.
````

**Xử lý:** [...]

---

## #165 | 05:13 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. sus_score.py HW03/usability/sessions --check phải 0 lỗi (lỗi → báo, không sửa số SV) → --report vào marker REPORT:U1; summary_hw03.py chạy lại (README/report §8 có số U1). Report §5: bỏ dòng "Không thực hiện phiên…" nếu còn. Commit `HW03[T2] 10/10: số liệu U1`.
2. Chuẩn bị issue cho 14 bug "sạch" theo bug_check.md (59, 60, 61, 65, 66, 67, 68, 69, 71, 74, 77, 83, 84, 85): gh = ThachHaoo; lấy lại danh sách issue kiểm trùng lần cuối; in bảng: BUG – tiêu đề GitHub = "[HW03-C2-xx] " + Tiêu đề trong file – label bug – ảnh cần kéo (bản đã che, từ evidence/). DỪNG chờ SV xác nhận bảng. Body lấy nguyên file BUG-xx.md (--body-file), không sửa chữ.
Báo ≤ 10 dòng + bảng + hash. Không push.
```

**Output:**
```
Bước 1 dừng: `tro_giup` SV ghi chuỗi `"khong_tro_giup"` thay vì danh sách `[]` → script đếm là có trợ giúp. Không sửa số SV. Làm tiếp bước 2.

Bước 1 chưa làm được vì `--check` còn 8 lỗi; em đã dừng, không sửa số SV và chưa commit `10/10`. Bước 2 đã xong và đang chờ SV xác nhận bảng.

**Bước 1**
- **Lỗi:** cả 8 phiếu S00–S07 báo "có trợ giúp nhưng `hoan_thanh = khong_tro_giup`". Nguyên nhân là trường `tro_giup` SV ghi chuỗi `"khong_tro_giup"`, trong khi schema cần danh sách: `[]` nếu không có trợ giúp, hoặc mỗi lần trợ giúp một mục. Script đếm độ dài chuỗi nên tưởng là có trợ giúp.
- Các trường khác SV đã điền đúng định dạng (`ket_thuc`, `hoan_thanh`, `nen_tang`, `reset_du_lieu` = true). SV sửa `tro_giup` (riêng S04 có dòng "Nhắc lại nhiệm vụ.", SV quyết có tính là trợ giúp không) rồi báo, em chạy lại bước 1.
- 8 file `S0*.json` SV vừa sửa vẫn chưa commit.

**Bước 2**
- **Kiểm trùng lần cuối:** `tkob-team/eshop-sut` hiện có issue tới #246; 22 issue mới (#225–#246) từ lần kiểm trước. Tất cả thuộc C1 (trang chủ, giỏ, checkout, chi tiết sản phẩm) hoặc C3 (admin), không trùng 14 bug của C2. #228–#230 cũng về thẻ h1 nhưng ở trang khác. Chưa có issue nào mang tiền tố `[HW03-C2…]`.
- **Label:** `bug` có trong repo. Ảnh lấy từ `HW03/checklist/evidence/`, cả 14 bộ ảnh đều tồn tại.

| BUG | Tiêu đề GitHub | Label | Ảnh cần kéo (`HW03/checklist/evidence/`) |
|---|---|---|---|
| 59 | [HW03-C2-59] [Tất cả màn C2] Tiêu đề tab hiển thị "frontend-web" giống hệt nhau ở mọi trang | bug | auto/P1,P2,P3_CL-13_1.png |
| 60 | [HW03-C2-60] [Tất cả màn C2] Thẻ <html> khai báo lang="en" thay vì tiếng Việt | bug | auto/P1,P2,P3_CL-14_1.png |
| 61 | [HW03-C2-61] [Đăng nhập, Quên MK, Hồ sơ] Các trang thiếu thẻ <h1> tiêu đề chính | bug | auto/P1,P2,P3_CL-02_1.png |
| 65 | [HW03-C2-65] [Đăng nhập, Hồ sơ] Bấm vào nhãn không focus vào ô nhập tương ứng | bug | auto/P1,P2,P3_CL-38_1.png |
| 66 | [HW03-C2-66] [Quên mật khẩu] Thiếu chỉ báo bước (Step Indicator) ở cả bước 1 và bước 2 | bug | P1_chrome/P1_CL-24_1, P2_firefox/P2_CL-24_1, P3_android/P3_CL-24_1 |
| 67 | [HW03-C2-67] [Quên MK B1] Không có nút hoặc liên kết 'Quay lại đăng nhập' | bug | auto/P1,P2,P3_CL-25_1.png |
| 68 | [HW03-C2-68] [Quên MK B2] Màn hình thiếu ô nhập 'Xác nhận mật khẩu mới' | bug | auto/P1,P2,P3_CL-26_1.png |
| 69 | [HW03-C2-69] [Quên MK B2] Mã OTP hiển thị 4 chữ số thay vì 6 chữ số theo SRS | bug | auto/P1,P2,P3_CL-28_1/_2.png (6 ảnh) |
| 71 | [HW03-C2-71] [Quên MK B2] Nút chính 'Đặt lại mật khẩu' và nút phụ quay lại giống nhau về hình thức | bug | P1_chrome/P1_CL-06_1, P2_firefox/P2_CL-06_1, P3_android/P3_CL-06_1 |
| 74 | [HW03-C2-74] [Navbar] Nút đăng xuất hiển thị nhãn "Thoát" thay vì "Đăng xuất" | bug | auto/P1,P2,P3_CL-42_1.png |
| 77 | [HW03-C2-77] [Tất cả màn C2] URL không tồn tại hiển thị vùng nội dung trống và thiếu link về trang chủ | bug | auto/P1,P2,P3_CL-50_1/_2.png (6 ảnh) |
| 83 | [HW03-C2-83] [Đăng nhập, Quên MK B2, Hồ sơ] Submit thất bại không tự động focus về ô nhập bị lỗi | bug | auto/P1,P2,P3_SV-03_1.png |
| 84 | [HW03-C2-84] [Đăng nhập, Hồ sơ] Độ tương phản màu sắc của chữ/nhãn so với nền không đạt tối thiểu 4.5:1 | bug | P1_chrome, P2_firefox, P3_android: SV-04_1…_4 (12 ảnh) |
| 85 | [HW03-C2-85] [Đăng nhập] Link 'Quên mật khẩu?' và 'Đăng ký ngay' có chiều cao vùng tương tác nhỏ hơn 24px | bug | auto/P1,P2,P3_SV-05_1.png |

- **Lưu ý body:** `--body-file BUG-xx.md` giữ nguyên chữ, nhưng các đường dẫn ảnh dạng `../checklist/evidence/...` trong file sẽ không mở được trên GitHub. Ảnh phải kéo tay vào issue (hoặc comment), như cột cuối bảng.
- **Commit:** chưa có commit mới; HEAD vẫn là `52ea483`.

Cần SV quyết:
1. Sửa `tro_giup` trong 8 phiếu: `[]` hoặc danh sách các lần trợ giúp.
2. Xác nhận bảng issue, hoặc sửa tiêu đề / danh sách ảnh.
```

**Xử lý:** [...]

---

## #166 | 05:15 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. Tất cả đều không có trợ giúp. 2. Xác nhận
```

**Output:**
```
Bước 1 xong (`d9919c9`). Tạo 14 issue.

Xong cả hai việc: số liệu U1 đã vào report và README, 14 issue đã tạo (#247–#260).

**1. Số liệu U1**
- Theo SV chốt, em đổi `tro_giup` của S00–S07 thành `[]`. `sus_score.py --check` chạy lại còn 0 lỗi, 7/7 phiên chính được tính.
- `--report` đã ghi bảng 7 phiên và bảng tổng hợp vào marker `REPORT:U1`; benchmark là 06:00 lấy theo plan.md (≤ 6 phút):
  - SUS trung bình 77,9 ± 17,8, SEQ trung bình 6,3 ± 1,1.
  - 7/7 phiên hoàn thành, không ai cần trợ giúp; 5/7 phiên xong trong 06:00.
- `tools/summary_hw03.py`: em sửa script cho tự tính dòng U1 từ `usability/sessions/` (pilot không tính), thay dòng cũ "không thực hiện phiên usability" đang gắn cứng. README và report §8 đã chạy lại, có số U1.
- Report §5 không còn dòng "Không thực hiện phiên…".
- Commit `d9919c9 HW03[T2] 10/10: số liệu U1`.

**2. GitHub Issues**
- Đã tạo 14 issue #247–#260 trên `tkob-team/eshop-sut` bằng tài khoản ThachHaoo, đều có label `bug`. Tiêu đề và body đúng như bảng SV đã xác nhận (body nguyên file BUG-xx.md, không sửa chữ).
- Danh sách đầy đủ để đối chiếu:

| BUG | Issue |
|---|---|
| BUG-59 | #247 |
| BUG-60 | #248 |
| BUG-61 | #249 |
| BUG-65 | #250 |
| BUG-66 | #251 |
| BUG-67 | #252 |
| BUG-68 | #253 |
| BUG-69 | #254 |
| BUG-71 | #255 |
| BUG-74 | #256 |
| BUG-77 | #257 |
| BUG-83 | #258 |
| BUG-84 | #259 |
| BUG-85 | #260 |

- Chưa push.

**Việc SV làm tiếp**
- Kéo ảnh vào từng issue theo cột ảnh trong bảng trước: đường dẫn `../checklist/...` trong body không hiện được trên GitHub.
- Muốn em ghi link issue vào mục "Link GitHub Issue" của 14 file BUG thì báo em. Ghi rồi thì chạy lại `summary_hw03.py` để dòng "đã có link GitHub Issue" lên 14/28 (hiện là 0/28).
- 14 bug còn lại (bug_check.md) chờ SV sửa xong mới tạo issue.
```

**Xử lý:** [...]

---

## #167 | 05:17 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Xong cả hai việc: số liệu U1 đã vào report và README, 14 issue đã tạo (#247–#260).

1. Số liệu U1
- Theo SV chốt, em đổi tro_giup của S00–S07 thành []. sus_score.py --check chạy lại còn 0 lỗi, 7/7 phiên chính được tính.
- --report đã ghi bảng 7 phiên và bảng tổng hợp vào marker REPORT:U1; benchmark là 06:00 lấy theo plan.md (≤ 6 phút):
  - SUS trung bình 77,9 ± 17,8, SEQ trung bình 6,3 ± 1,1.
  - 7/7 phiên hoàn thành, không ai cần trợ giúp; 5/7 phiên xong trong 06:00.
- tools/summary_hw03.py: em sửa script cho tự tính dòng U1 từ usability/sessions/ (pilot không tính), thay dòng cũ "không thực hiện phiên usability" đang gắn cứng. README và report §8 đã chạy lại, có số U1.
- Report §5 không còn dòng "Không thực hiện phiên…".
- Commit d9919c9 HW03[T2] 10/10: số liệu U1.

2. GitHub Issues
- Đã tạo 14 issue #247–#260 trên tkob-team/eshop-sut bằng tài khoản ThachHaoo, đều có label bug. Tiêu đề và body đúng như bảng SV đã xác nhận (body nguyên file BUG-xx.md, không sửa chữ).
- Danh sách đầy đủ để đối chiếu:

┌────────┬───────┐
│  BUG   │ Issue │
├────────┼───────┤
│ BUG-59 │ #247  │
├────────┼───────┤
│ BUG-60 │ #248  │
├────────┼───────┤
│ BUG-61 │ #249  │
├────────┼───────┤
│ BUG-65 │ #250  │
├────────┼───────┤
│ BUG-66 │ #251  │
├────────┼───────┤
│ BUG-68 │ #253  │
├────────┼───────┤
│ BUG-69 │ #254  │
├────────┼───────┤
│ BUG-71 │ #255  │
├────────┼───────┤
│ BUG-74 │ #256  │
├────────┼───────┤
│ BUG-77 │ #257  │
├────────┼───────┤
│ BUG-83 │ #258  │
├────────┼───────┤
│ BUG-84 │ #259  │
├────────┼───────┤
│ BUG-85 │ #260  │
└────────┴───────┘

- Chưa push.

Việc SV làm tiếp
- Kéo ảnh vào từng issue theo cột ảnh trong bảng trước: đường dẫn ../checklist/... trong body không hiện được trên GitHub.
- Muốn em ghi link issue vào mục "Link GitHub Issue" của 14 file BUG thì báo em. Ghi rồi thì chạy lại summary_hw03.py để dòng "đã có link GitHub Issue" lên 14/28 (hiện là 0/28).
- 14 bug còn lại (bug_check.md) chờ SV sửa xong mới tạo issue.
```

**Output:**
````
Hai việc đều xong. Có 2 điểm em cần kiểm:

**1. Bảng chỉ có 13 dòng, thiếu #252.** Theo thứ tự thì #252 là **BUG-67**. Bảo Claude Code xác nhận lại `#252 = BUG-67`, tiêu đề đúng, có label bug.

**2. S04 "Nhắc lại nhiệm vụ" có tính là trợ giúp không.** Phiếu ghi tay S04 (đã commit nguyên văn) có dòng "Nhắc lại nhiệm vụ", nhưng JSON giờ ghi S04 hoàn thành **không trợ giúp**, nên trong report là 7/7 không ai cần trợ giúp. Cả hai cách đều được, nhưng phải nhất quán với phiếu:
- (a) Nhắc lại **đề bài** không gợi ý giao diện, nên không tính là trợ giúp. Ghi một dòng `ghi_chu` cho S04: "nhắc lại đề bài, không gợi ý thao tác, không tính trợ giúp (SV chốt)".
- (b) Tính là trợ giúp: S04 = `co_tro_giup`, thêm mục `tro_giup`.

Plan mục 7 chỉ coi là trợ giúp khi can thiệp lúc bế tắc. Nếu S04 không bế tắc thì (a) hợp lý, nhưng phải có dòng ghi chú để người chấm khỏi thấy mâu thuẫn với phiếu.

**Việc tiếp:**
- **Em kéo ảnh** vào 14 issue theo cột ảnh, dùng bản đã che trong `evidence/`. Kiểm từng ảnh là bản che, đừng lặp lại sự cố #189/#190 ở HW02.
- Dán cho Claude Code:
```
1. Xác nhận #252 = BUG-67 (tiêu đề, label). 2. S04: SV chốt <a: ghi_chu "nhắc lại đề bài, không gợi ý thao tác, không tính trợ giúp (SV chốt)" | b: co_tro_giup + tro_giup>; chạy lại --check/--report/summary. 3. Ghi link issue vào "Link GitHub Issue" của 14 file BUG (đúng số), chạy lại summary_hw03.py. Commit từng việc. Không push. Báo ≤ 5 dòng + hash.
```
- Rồi **push**, và sửa 14 bug còn lại theo `bug_check.md`.
````

**Xử lý:** [...]

---

## #168 | 05:17 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. Xác nhận #252 = BUG-67 (tiêu đề, label). 2. S04: SV chốt <a: ghi_chu "nhắc lại đề bài, không gợi ý thao tác, không tính trợ giúp (SV chốt)" | b: co_tro_giup + tro_giup>; chạy lại --check/--report/summary. 3. Ghi link issue vào "Link GitHub Issue" của 14 file BUG (đúng số), chạy lại summary_hw03.py. Commit từng việc. Không push. Báo ≤ 5 dòng + hash.
```

**Output:**
```
Làm xong việc 1 và 3; việc 2 em dừng chờ SV chọn a hay b.

- **#252 = BUG-67:** đúng. Tiêu đề trên GitHub là `[HW03-C2-67] [Quên MK B1] Không có nút hoặc liên kết 'Quay lại đăng nhập'`, khớp tiêu đề trong file, label `bug`.
- **Link issue:** đã ghi #247–#260 vào mục "Link GitHub Issue" của 14 file BUG, chạy lại `summary_hw03.py` → "đã có link GitHub Issue: 14/28". Commit `bf715c0`.
- **S04 chưa làm:** lệnh còn để nguyên `<a … | b …>` nên em chưa sửa S04 và chưa chạy lại `--check`/`--report`/summary. SV chốt a hoặc b, em làm tiếp và commit riêng.
- Chưa push.
```

**Xử lý:** [...]

---

## #169 | 05:18 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
link để kéo ảnh đâu nhỉ?
```

**Output:**
```
Mỗi issue có link `https://github.com/tkob-team/eshop-sut/issues/<số>`:

| BUG | Issue |
|---|---|
| BUG-59 | https://github.com/tkob-team/eshop-sut/issues/247 |
| BUG-60 | https://github.com/tkob-team/eshop-sut/issues/248 |
| BUG-61 | https://github.com/tkob-team/eshop-sut/issues/249 |
| BUG-65 | https://github.com/tkob-team/eshop-sut/issues/250 |
| BUG-66 | https://github.com/tkob-team/eshop-sut/issues/251 |
| BUG-67 | https://github.com/tkob-team/eshop-sut/issues/252 (chờ xác nhận) |
| BUG-68 | https://github.com/tkob-team/eshop-sut/issues/253 |
| BUG-69 | https://github.com/tkob-team/eshop-sut/issues/254 |
| BUG-71 | https://github.com/tkob-team/eshop-sut/issues/255 |
| BUG-74 | https://github.com/tkob-team/eshop-sut/issues/256 |
| BUG-77 | https://github.com/tkob-team/eshop-sut/issues/257 |
| BUG-83 | https://github.com/tkob-team/eshop-sut/issues/258 |
| BUG-84 | https://github.com/tkob-team/eshop-sut/issues/259 |
| BUG-85 | https://github.com/tkob-team/eshop-sut/issues/260 |

**Cách kéo ảnh vào từng issue:**
1. Mở link, bấm **⋯** ở góc bài đầu (body), chọn **Edit**.
2. Tìm mục **Bằng chứng**. Chỗ đường dẫn `../checklist/evidence/…png` không hiện ảnh trên GitHub.
3. Mở thư mục `HW03\checklist\evidence\` trên máy, kéo đúng file ảnh vào ô soạn thảo, đặt ngay dưới dòng đường dẫn đó. GitHub tự upload và chèn `![tên-file](https://github.com/user-attachments/…)`.
4. Sửa phần alt thành tên file (ví dụ `![P1_CL-10_1.png](…)`) cho dễ đối chiếu.
5. Bấm **Update comment**.

Ảnh cần kéo cho từng issue nằm ở cột ảnh trong bảng mà Claude Code đã in lúc em xác nhận. Không còn bảng đó thì hỏi Claude Code: "in lại bảng BUG – issue – ảnh cần kéo".

Kéo xong cả 14 issue thì báo Claude Code "đã kéo ảnh". Nó sẽ kiểm mỗi issue có ảnh và ảnh đúng bản che.
```

**Xử lý:** [...]

---

## #170 | 05:29 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
đã kéo ảnh
```

**Output:**
```
Em đã kiểm cả 14 issue #247–#260: mỗi issue có đủ số ảnh như bảng đã chốt. #254 và #257 có 6 ảnh, #259 có 12 ảnh, 11 issue còn lại mỗi cái 3 ảnh. Ảnh nằm trong phần mô tả của issue, không ở comment.

Còn chờ SV: chọn a hay b cho S04 để em chạy lại `--check`/`--report`/summary.
```

**Xử lý:** [...]

---

## #171 | 05:30 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Em đã kiểm cả 14 issue #247–#260: mỗi issue có đủ số ảnh như bảng đã chốt. #254 và #257 có 6 ảnh, #259 có 12 ảnh, 11 issue còn lại mỗi cái 3 ảnh. Ảnh nằm trong phần mô tả của issue, không ở comment.

Còn chờ SV: chọn a hay b cho S04 để em chạy lại --check/--report/summary.
```

**Output:**
````
Ảnh đã đủ. Còn hai việc:

**1. Em chọn S04, trả lời Claude Code `S04=a` hoặc `S04=b`:**
- **a:** nhắc lại **đề bài**, không gợi ý thao tác, nên không tính trợ giúp. Thêm `ghi_chu` cho S04. Kết quả vẫn 7/7 không trợ giúp.
- **b:** tính là trợ giúp. S04 = `co_tro_giup`, kết quả thành 6/7 không trợ giúp, 1/7 có trợ giúp.

Anh khuyến nghị **a** nếu lúc đó S04 không bế tắc mà chỉ hỏi lại đề, vì plan mục 7 chỉ tính trợ giúp khi can thiệp lúc bế tắc. Nếu em nhắc vì bạn đang kẹt thì chọn **b**.

**2. Thêm một yêu cầu kiểm ảnh** trong cùng lệnh: Claude Code mới đếm số ảnh, chưa xác nhận ảnh đúng bản đã che.
```
S04=<a|b>. Sau đó: kiểm alt/tên ảnh trong 14 issue khớp file trong HW03/checklist/evidence/ (bản đã nén/che, không phải evidence_raw); lệch → báo số issue + tên ảnh. Ghi link issue vào 14 file BUG + summary_hw03.py nếu chưa làm. Commit, không push. Báo ≤ 5 dòng + hash.
```

Rồi **push** và chuyển sang sửa 14 bug còn lại theo `bug_check.md`. Đây là việc đường găng tiếp theo.
````

**Xử lý:** [...]

---

## #172 | 05:31 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Ở lần này mình không làm alt nhé, nên không cần quan tâm
```

**Output:**
````
Được, bỏ phần alt. Riêng việc ảnh là **bản đã che** thì vẫn quan trọng, vì repo và issue đều public. Không có alt thì Claude Code không đối chiếu tên được, nên em tự xác nhận một câu: **em kéo ảnh từ `HW03\checklist\evidence\`**, không phải từ `evidence_raw\`. Nếu đúng vậy thì xong.

Lệnh rút gọn:
```
S04=<a|b>. Chạy lại --check/--report/summary. Ghi link issue vào 14 file BUG + summary_hw03.py nếu chưa làm. Bỏ qua alt ảnh (SV chốt). Commit, không push. Báo ≤ 4 dòng + hash.
```

Sau đó em push rồi sửa 14 bug còn lại.
````

**Xử lý:** [...]

---

## #173 | 05:31 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
S04=a. Chạy lại --check/--report/summary. Ghi link issue vào 14 file BUG + summary_hw03.py nếu chưa làm. Bỏ qua alt ảnh (SV chốt). Commit, không push. Báo ≤ 4 dòng + hash.
```

**Output:**
```
S04 đã ghi ghi_chu theo phương án a: dòng "Nhắc lại nhiệm vụ." là nhắc lại đề bài, không gợi ý thao tác, không tính trợ giúp.
- Chạy lại `--check` 0 lỗi; `--report` và `summary_hw03.py` cho số liệu U1 không đổi (vẫn 0 trợ giúp).
- Link issue #247–#260 đã ghi vào 14 file BUG từ trước (`bf715c0`); summary hiện "đã có link GitHub Issue: 14/28". Bỏ qua alt ảnh theo SV chốt.
- Commit `c19c3ab HW03[T2]: S04 ghi chú nhắc lại nhiệm vụ (SV chốt a)`, chưa push.
```

**Xử lý:** [...]

---

## #174 | 05:32 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
S04 đã ghi ghi_chu theo phương án a: dòng "Nhắc lại nhiệm vụ." là nhắc lại đề bài, không gợi ý thao tác, không tính trợ giúp.
- Chạy lại --check 0 lỗi; --report và summary_hw03.py cho số liệu U1 không đổi (vẫn 0 trợ giúp).
- Link issue #247–#260 đã ghi vào 14 file BUG từ trước (bf715c0); summary hiện "đã có link GitHub Issue: 14/28". Bỏ qua alt ảnh theo SV chốt.
- Commit c19c3ab HW03[T2]: S04 ghi chú nhắc lại nhiệm vụ (SV chốt a), chưa push.
===
đã push rồi nhé, làm gì tiếp nhỉ
```

**Output:**
````
Việc tiếp theo là **sửa 14 bug còn lại** theo `HW03/bugs/bug_check.md`. Anh tóm tắt điểm cần xem của từng bug. Đây chỉ là dữ kiện; sửa thế nào là chữ của em.

| BUG | Cần xem |
|---|---|
| **58** | Nhận định câu 1 ("rắc rối lớn") và câu 2 ("hoàn toàn không thể truy cập Navbar" ở B2) chưa có dữ kiện. Thêm "(chưa kiểm chứng)" hoặc bỏ |
| **62** | Trang Đăng nhập nhãn thật là **"Username"**, không phải "Email". Steps làm đúng thì ô Mật khẩu trống chặn submit (0 request), nên Steps cần bước nhập mật khẩu |
| **63** | Expected nhắc ô "Xác nhận mật khẩu" ở B2, nhưng ô này **không tồn tại** (đó chính là BUG-68). Gọi "Email" ở Đăng nhập trong khi nhãn thật là "Username" |
| **64** | Hồ sơ với SĐT `123` hiện hộp thoại **"Số điện thoại không hợp lệ…"**, không phải "Cập nhật thành công!" như Actual/Nhận định đang viết |
| **70** | Câu nguyên nhân ("regex/validation… sai cấu trúc") chưa có dữ kiện. "(chưa kiểm chứng)" đang gắn sai câu. Dữ kiện có sẵn: `ForgotPassword.jsx:26` bắt buộc có khoảng trắng |
| **72** | Nhận định câu 1 ("làm sai lệch dữ liệu") chưa đánh dấu |
| **73** | Tiêu đề thiếu **Họ Tên** (cả 3 trường đều về giá trị cũ). Actual chưa nhắc hộp thoại sau khi bấm Cập nhật. **Cô lập:** web chặn ngay (0 request) vì regex không nhận SĐT bắt đầu bằng 0 (`Profile.jsx:43`); với `912345678` thì cả 3 trường lưu bền. Em quyết: giữ hiện tượng hay viết lại theo nguyên nhân |
| **75** | Actual "cập nhật sau F5" **không có trong Dữ kiện**. Làm đúng Steps (SĐT trống) thì bị chặn, không lưu. Cô lập: khi lưu được (SĐT `912345678`) thì navbar không cập nhật ngay, sau F5 mới đổi. Tiền điều kiện cần SĐT hợp lệ |
| **76** | Expected có **2 nhánh** (chuyển `/login` *hoặc* thông báo kèm link) |
| **78** | Câu "P3 bị TimeoutError do dblclick" là **lỗi của harness**, không phải SUT. Steps B2 và Hồ sơ chưa nêu giá trị nhập. Có số cô lập: Hồ sơ với `912345678` gửi 2 PUT, B2 với `Abcd efg1` gửi 2 request |
| **79** | Actual P1 "hiển thị trạng thái rỗng trước" không có trong Dữ kiện P1. Repro thì **có thấy** trạng thái rỗng, nhưng dùng trễ 3000 ms, không phải throttling thật |
| **80** | Nhận định chưa có "(chưa kiểm chứng)" |
| **81** | Làm đúng Tiền điều kiện (restart + `seed_orders.py`) thì đơn Đang giao là **#3**, không phải #10 hay #8…#12 |
| **82** | Tiêu đề nói Autofill không dùng được ở cả 3 màn, nhưng Actual P1 ghi **dùng được ở Quên MK**. Expected "Paste *hoặc* Autofill" đọc được thành 2 nhánh. Bước Autofill Playwright không chạy được, cần em tự xác nhận tay trên P1 |

**Bất thường ngoài 28 bug** (em quyết có lập bug mới không):
- `Login.jsx:24`: tiêu đề form Đăng nhập là "Đăng Ký". Đã **trùng #9** (CL-03), nên không lập.
- `Login.jsx:40`: ô Mật khẩu `type="text"`, mật khẩu hiện rõ (thấy trong ảnh P3). Chưa có trong 28 bug, chưa kiểm trùng. Nếu muốn lập thì bảo Claude Code kiểm trùng trước. Thiếu giờ thì ghi vào report là "phát hiện, chưa lập".

Sửa xong: commit `HW03[T1] 5/6f: SV sửa BUG theo kiểm dữ kiện`, push. Rồi dán:
```
Kiểm lại 14 bug SV vừa sửa (58,62,63,64,70,72,73,75,76,78,79,80,81,82) theo bug_check.md – chỉ đọc, ghi bug_check2.md; còn điểm nào chưa xử lý thì liệt kê, không sửa chữ SV. Sạch → in bảng tiêu đề [HW03-C2-xx], DỪNG chờ SV xác nhận rồi tạo issue (--body-file), ghi link vào file BUG, summary_hw03.py. Không push. Báo ≤ 8 dòng + hash.
```

Em xử lý trong khoảng **35 phút** (khoảng 2–3 phút mỗi bug). Phần lớn chỉ cần thêm "(chưa kiểm chứng)" hoặc sửa tên trường. BUG-73 và 75 lâu hơn chút vì cần em quyết.
````

**Xử lý:** [...]

---

## #175 | 05:33 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Giờ mình định đi ngủ, hiện tại khối lượng công việc tổng lại còn bao nhiêu nhỉ
```

**Output:**
```
Còn khoảng **4,5 giờ tới deadline 10:00**. Việc còn lại, nặng nhất ở trên:

**Phần em bắt buộc tự làm (🔒), khoảng 3 giờ 15 phút**

| Việc | Thời gian ước |
|---|---|
| Sửa 14 bug theo `bug_check.md` | 35–45' |
| Findings Task 2 §5.8–5.9 (gom pain point, lỗi riêng lẻ ↔ thiết kế, severity) | 40' |
| §3.4 item em bổ sung + vì sao AI bỏ sót | 15' |
| Critique 200–300 từ | 25' |
| Verdict + lý do Audit (khoảng 25 artifact) | 30' |
| Duyệt khối 📝 (§3.2, §4.2, §5.5, §11, moderator_script) | 15' |
| Tự chấm §12, ngày nộp, tick + ký AI-05/AI-02/AI-03 | 15' |
| Bảng 7 người tham gia (che 4 số giữa SĐT) | 10' |

**Phần AI làm, chạy song song, khoảng 1 giờ (cần em xác nhận vài lần)**
- Tạo 14 issue còn lại, chụp ảnh trang Issues (em xác nhận bảng tiêu đề, kéo ảnh): 20'.
- Xuất transcript `_p2`, trích prompt log, điền #n vào AI-02/AI-03: 10'.
- AI-05, PDF, commit log, `hw-submission-audit`, zip, đo dung lượng: 30'.

**Có thể cắt:** video skill (45' nếu làm). Không làm thì trừ điểm skill tương ứng khi tự chấm.

**Lời khuyên thẳng:** khối lượng của em khoảng 3 giờ 15 phút cộng 1 giờ phối hợp. Nếu ngủ tới 07:00 thì còn 3 giờ, **không đủ** cho tất cả, phải cắt bớt. Có hai cách:
- **Ngủ 1 tiếng (05:40–06:40):** còn khoảng 3h20, đủ nếu bỏ video và làm liền tay. Đặt 2 báo thức.
- **Làm 14 bug bây giờ (~40') rồi mới ngủ tới 07:15.** Trong lúc em ngủ, Claude Code tạo 14 issue (nó sẽ dừng ở bước xác nhận, sáng em xác nhận). Sáng còn khoảng 2h45 cho findings, Critique, Audit và nộp.

Anh nghiêng về **cách 2**. Bug là phần nhiều điểm nhất của Task 1 (30đ) và cần chạy qua issue, nên làm xong trước khi ngủ thì sáng chỉ còn phần viết.

Dù chọn cách nào, đừng để sát giờ: **nhắm nộp lúc 09:30**, vì zip, Moodle và PDF đều có thể trục trặc.
```

**Xử lý:** [...]

---

## #176 | 07:49 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Kiểm lại 14 bug SV vừa sửa (58,62,63,64,70,72,73,75,76,78,79,80,81,82) theo bug_check.md – chỉ đọc, ghi bug_check2.md; còn điểm nào chưa xử lý thì liệt kê, không sửa chữ SV. Sạch → in bảng tiêu đề [HW03-C2-xx], DỪNG chờ SV xác nhận rồi tạo issue (--body-file), ghi link vào file BUG, summary_hw03.py. Không push. Báo ≤ 8 dòng + hash.
```

**Output:**
```
Đang đối chiếu từng chỗ SV sửa với bug_check.md; còn xem BUG-79/81/82.

Kiểm lại xong 14 bug SV sửa: 6 bug sạch, 8 bug còn điểm. Chi tiết từng điểm trong `HW03/bugs/bug_check2.md` (commit `de6882e`). Chưa tạo issue nào, chưa push.

**8 bug còn điểm:**
- **BUG-72:** SV đã sửa dòng "Dữ kiện (AI chép)" của CL-32 P3 (bỏ đoạn "912345678 được lưu"), nên dòng này không còn khớp `checklist.json`. Ngoài ra file ghi "Tái hiện trên P1, P2, P3" trong khi lượt tái hiện chỉ chạy P1, P2.
- **BUG-64, BUG-73, BUG-75:** Actual mới ghi "Cả P1, P2 và P3", nhưng P3 chưa có dữ kiện cho điều kiện mới. BUG-64 còn thêm: Actual mới khác với mục Dữ kiện trong file.
- **BUG-75, BUG-78:** gọi SĐT `912345678` là "hợp lệ", trái với FR-04.2 và với chính BUG-72. Riêng BUG-78: Steps mới dùng giá trị lọt kiểm tra, mà làm theo thì ra 2 request, khác Actual đang ghi 0 request.
- **BUG-76:** Expected chỉ còn 1 nhánh (chuyển hướng về `/login`), hẹp hơn Expected của item CL-49; có thêm một dòng `- ` rỗng.
- **BUG-63, BUG-79:** chưa xử lý điểm cũ của `bug_check.md`. BUG-63: Địa chỉ trống bị chặn là do ô SĐT trống. BUG-79: ảnh P3 cho thấy trạng thái rỗng hiện trước bảng đơn, trái với Actual P3.

**6 bug sạch**, chờ SV xác nhận rồi em mới tạo issue (`--body-file`, label `bug`):

| BUG | Tiêu đề GitHub |
|---|---|
| 58 | [HW03-C2-58] [Đăng nhập, Quên MK] Focus nhảy ngược và bỏ qua Navbar khi nhấn Tab |
| 62 | [HW03-C2-62] [Đăng nhập, Quên MK B1] Ô Email type="text", email sai định dạng không bị chặn |
| 70 | [HW03-C2-70] [Quên MK B2] Mật khẩu hợp lệ 'Abcdef1!' bị từ chối với thông báo "Mật khẩu quá yếu!" |
| 80 | [HW03-C2-80] [Lịch sử đơn] Ngày đặt không đúng định dạng dd/mm/yyyy và không nhất quán giữa các nền tảng |
| 81 | [HW03-C2-81] [Lịch sử đơn] Nút 'Hủy đơn' vẫn hiển thị và thao tác được ở đơn hàng trạng thái 'Đang giao' |
| 82 | [HW03-C2-82] [Đăng nhập, Hồ sơ] Không sử dụng được tính năng tự động điền (Autofill) của trình duyệt |

SV quyết: tạo trước 6 issue này, hay chờ sửa xong cả 14 rồi tạo một lượt.
```
*File AI ghi/gửi trong lượt này:* `bug_check2.md`

**Xử lý:** [...]

---

## #177 | 07:51 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
10h là đl mình đặt ra thôi deadline thật là 11h30 nhé. 
Giờ đang chờ chạy prompt sau khi sửa BUG, tôi có thể làm gì thêm không
```

**Output:**
```
Deadline 11:30 thì còn khoảng **3 giờ 40 phút**, đủ để làm cả video nếu giữ nhịp.

Trong lúc Claude Code kiểm bug, em làm **findings Task 2 (§5.8–5.9, 🔒)**: việc lớn nhất, và không phụ thuộc gì nữa.

**Nguồn dữ kiện**
- `usability/sessions/notes/S00…S07.txt`: câu nói nguyên văn.
- `usability/sessions/S0x.json`: sự kiện L/D/N, thời gian, SEQ/SUS từng người.
- Bảng REPORT:U1 trong report: SUS 77,9, SEQ 6,3, 5/7 xong trong 6 phút.
- 4 câu hỏi mở trong JSON (chép từ form).
- Pilot S00 chỉ dùng như dữ kiện phụ, không tính vào thống kê.

**Khung gợi ý cho §5.8 (gom pain point):**

| Nhóm pain point | Phiên gặp (S0x) | Bằng chứng (câu nói / sự kiện) | Lỗi riêng lẻ hay vấn đề thiết kế | Liên quan bug/issue |
|---|---|---|---|---|

**Khung gợi ý cho §5.9 (xếp theo severity):**

| # | Finding | Severity | Tần suất (x/7) | Ảnh hưởng tới hoàn thành nhiệm vụ | Đề xuất |
|---|---|---|---|---|---|

Thang severity em tự chốt (plan mục 9 để 📝) và ghi ngay dưới bảng. Ví dụ: severity × tần suất, hoặc thang 4 mức blocker/major/minor/cosmetic như slide môn học.

Một số điều cần giữ khi viết:
- Tần suất chỉ đếm S01–S07, ghi kiểu "4/7".
- Tách **vấn đề usability** (người dùng bối rối) với **bug chức năng hay bảo mật** mà người tham gia vô tình lộ ra (ví dụ sửa được tổng tiền). Bug thật thì tra trùng với issue sẵn có trước khi đề xuất lập mới.
- Không khẳng định quá dữ kiện. Ví dụ SUS 77,9 với 7 người, 3 người IT, nên dùng "cho thấy", không dùng "chứng minh".

Viết xong commit `HW03[T2]: SV viết findings` rồi push, anh đọc lại dữ kiện.

**Thứ tự sau đó:** §3.4 → Critique → Audit → video (giờ đã có chỗ).

Anh cũng sẽ cập nhật handoff: deadline thật là 11:30.
```

**Xử lý:** [...]

---

## #178 | 07:55 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
mình thấy 14 bug đã oke hết rồi, tạo issues hết nhé
```

**Output:**
```
Đã tạo issue cho cả 14 bug còn lại (#261–#274), đủ 28/28 bug đều có issue trên GitHub. Chưa push.

- **Issue:** tạo trên `tkob-team/eshop-sut` bằng tài khoản ThachHaoo, label `bug`, tiêu đề dạng `[HW03-C2-xx] …`, body là nguyên file BUG. Trước khi tạo em kiểm lại thì chưa có issue mới nào sau #260.
- **Link:** đã ghi vào mục "Link GitHub Issue" của 14 file BUG, chạy lại `summary_hw03.py` → "đã có link GitHub Issue: 28/28". Commit `77a351f`.
- **Ảnh SV cần kéo vào từng issue** (thư mục `HW03/checklist/evidence/`):

| Issue | BUG | Số ảnh | Ảnh |
|---|---|---|---|
| #261 | 58 | 4 | `auto/` P1, P2 của CL-10 và CL-12 |
| #262 | 62 | 6 | `auto/` P1–P3 của CL-17 và CL-66 |
| #263 | 63 | 6 | `auto/` P1–P3 của CL-20 và CL-21 |
| #264 | 64 | 3 | `auto/` P1–P3 của CL-23 |
| #265 | 70 | 3 | `auto/` P1–P3 của CL-29 |
| #266 | 72 | 3 | `auto/` P1–P3 của CL-32 |
| #267 | 73 | 3 | `auto/` P1–P3 của CL-37 |
| #268 | 75 | 3 | `auto/` P1–P3 của CL-56 |
| #269 | 76 | 6 | `auto/` P1–P3 của CL-49, mỗi nền tảng `_1`, `_2` |
| #270 | 78 | 6 | CL-53 ở `P1_chrome`, `P2_firefox`, `P3_android` + `auto/` P1–P3 của SV-06 |
| #271 | 79 | 5 | `P1_CL-63_1`, `_2` · `P2_CL-63_1` · `P3_CL-63_1`, `_2` |
| #272 | 80 | 3 | CL-09 ở `P1_chrome`, `P2_firefox`, `P3_android` |
| #273 | 81 | 6 | `auto/` P1–P3 của CL-59, mỗi nền tảng `_1`, `_2` |
| #274 | 82 | 12 | SV-02 `_1`…`_4` ở cả ba thư mục `P1_chrome`, `P2_firefox`, `P3_android` |

- **Lưu ý:** BUG-72 lên issue #266 với dòng "Dữ kiện (AI chép)" của CL-32 P3 đã bị sửa, không còn khớp `checklist.json`. Nếu muốn sửa thì phải sửa cả file BUG lẫn body issue.
```

**Xử lý:** [...]

---

## #179 | 07:58 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đã tạo issue cho cả 14 bug còn lại (#261–#274), đủ 28/28 bug đều có issue trên GitHub. Chưa push.

- Issue: tạo trên tkob-team/eshop-sut bằng tài khoản ThachHaoo, label bug, tiêu đề dạng [HW03-C2-xx] …, body là nguyên file BUG. Trước khi tạo em kiểm lại thì chưa có issue mới nào sau #260.
- Link: đã ghi vào mục "Link GitHub Issue" của 14 file BUG, chạy lại summary_hw03.py → "đã có link GitHub Issue: 28/28". Commit 77a351f.
- Ảnh SV cần kéo vào từng issue (thư mục HW03/checklist/evidence/):

┌───────┬─────┬────────┬───────────────────────────────────────────────────────────────────┐
│ Issue │ BUG │ Số ảnh │                                Ảnh                                │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #261  │ 58  │ 4      │ auto/ P1, P2 của CL-10 và CL-12                                   │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #262  │ 62  │ 6      │ auto/ P1–P3 của CL-17 và CL-66                                    │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #263  │ 63  │ 6      │ auto/ P1–P3 của CL-20 và CL-21                                    │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #264  │ 64  │ 3      │ auto/ P1–P3 của CL-23                                             │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #265  │ 70  │ 3      │ auto/ P1–P3 của CL-29                                             │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #266  │ 72  │ 3      │ auto/ P1–P3 của CL-32                                             │
│ #267  │ 73  │ 3      │ auto/ P1–P3 của CL-37                                             │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #268  │ 75  │ 3      │ auto/ P1–P3 của CL-56                                             │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #269  │ 76  │ 6      │ auto/ P1–P3 của CL-49, mỗi nền tảng _1, _2                        │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #270  │ 78  │ 6      │ CL-53 ở P1_chrome, P2_firefox, P3_android + auto/ P1–P3 của SV-06 │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #271  │ 79  │ 5      │ P1_CL-63_1, _2 · P2_CL-63_1 · P3_CL-63_1, _2                      │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #272  │ 80  │ 3      │ CL-09 ở P1_chrome, P2_firefox, P3_android                         │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #273  │ 81  │ 6      │ auto/ P1–P3 của CL-59, mỗi nền tảng _1, _2                        │
├───────┼─────┼────────┼───────────────────────────────────────────────────────────────────┤
│ #274  │ 82  │ 12     │ SV-02 _1…_4 ở cả ba thư mục P1_chrome, P2_firefox, P3_android     │
└───────┴─────┴────────┴───────────────────────────────────────────────────────────────────┘

- Lưu ý: BUG-72 lên issue #266 với dòng "Dữ kiện (AI chép)" của CL-32 P3 đã bị sửa, không còn khớp checklist.json. Nếu muốn sửa thì phải sửa cả file BUG lẫn body issue.
===
đã push rồi nhé
```

**Output:**
````
28/28 bug đã có issue. Anh kiểm BUG-72: dòng Dữ kiện (AI chép) của CL-32 P3 bị mất đoạn đầu `Lỗi: Error: 912345678 được lưu ·` trong commit sửa của em (`496ad20`). Có lẽ em lỡ xoá khi sửa phần Actual. Phần "Dữ kiện (AI chép)" phải khớp nguyên văn `checklist.json`, nên **khôi phục lại**. Đây là sửa dữ kiện sai, AI được làm, không đụng chữ em.

**Việc của em bây giờ:** kéo ảnh cho 14 issue #261–#274 theo bảng Claude Code vừa in. Cách kéo giống lần trước, ảnh lấy từ `HW03\checklist\evidence\`. Có 81 ảnh, mất khoảng 15–20 phút.

Kéo xong thì dán cho Claude Code:
```
1. BUG-72: khôi phục dòng "Actual nguyên văn CL-32 P3 (auto)" về đúng checklist.json (bị SV lỡ xoá ở 496ad20); gh issue edit #266 sửa body tương ứng + comment đính chính 1 dòng ("Đính chính: khôi phục dòng dữ kiện CL-32 P3 chép từ checklist.json"); log trước/sau vào HW03/bugs/issue_edits.md. Commit `HW03[T1]: khôi phục dữ kiện BUG-72 (#266)`.
2. Kiểm 14 issue #261–#274 có đủ số ảnh theo bảng (ảnh trong body).
3. Ảnh trang Issues: Playwright mở https://github.com/tkob-team/eshop-sut/issues?q=is%3Aissue+%22HW03-C2%22+author%3AThachHaoo (đủ 28, chụp nhiều trang nếu cần) → HW03/bugs/issues_page_HW03-C2_<n>.png; đưa vào report §6. Commit `HW03[T1]: ảnh trang Issues`.
Không push. Báo ≤ 6 dòng + hash.
```

Trong lúc Claude Code chạy, em viết **findings §5.8–5.9** theo khung anh gửi lúc nãy.
````

**Xử lý:** [...]

---

## #180 | 08:01 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Gửi cho tôi các link cần thêm evidence nhé
```

**Output:**
```
Danh sách issue cần kéo ảnh, ảnh lấy trong `HW03\checklist\evidence\`:

| Issue | BUG | Số ảnh | Ảnh cần kéo |
|---|---|---|---|
| https://github.com/tkob-team/eshop-sut/issues/261 | 58 | 4 | `auto\`: P1, P2 của CL-10 và CL-12 |
| https://github.com/tkob-team/eshop-sut/issues/262 | 62 | 6 | `auto\`: P1–P3 của CL-17 và CL-66 |
| https://github.com/tkob-team/eshop-sut/issues/263 | 63 | 6 | `auto\`: P1–P3 của CL-20 và CL-21 |
| https://github.com/tkob-team/eshop-sut/issues/264 | 64 | 3 | `auto\`: P1–P3 của CL-23 |
| https://github.com/tkob-team/eshop-sut/issues/265 | 70 | 3 | `auto\`: P1–P3 của CL-29 |
| https://github.com/tkob-team/eshop-sut/issues/266 | 72 | 3 | `auto\`: P1–P3 của CL-32 |
| https://github.com/tkob-team/eshop-sut/issues/267 | 73 | 3 | `auto\`: P1–P3 của CL-37 |
| https://github.com/tkob-team/eshop-sut/issues/268 | 75 | 3 | `auto\`: P1–P3 của CL-56 |
| https://github.com/tkob-team/eshop-sut/issues/269 | 76 | 6 | `auto\`: P1–P3 của CL-49, mỗi nền tảng `_1`, `_2` |
| https://github.com/tkob-team/eshop-sut/issues/270 | 78 | 6 | CL-53 ở `P1_chrome\`, `P2_firefox\`, `P3_android\` + `auto\` P1–P3 của SV-06 |
| https://github.com/tkob-team/eshop-sut/issues/271 | 79 | 5 | `P1_CL-63_1`, `P1_CL-63_2`, `P2_CL-63_1`, `P3_CL-63_1`, `P3_CL-63_2` |
| https://github.com/tkob-team/eshop-sut/issues/272 | 80 | 3 | CL-09 ở `P1_chrome\`, `P2_firefox\`, `P3_android\` |
| https://github.com/tkob-team/eshop-sut/issues/273 | 81 | 6 | `auto\`: P1–P3 của CL-59, mỗi nền tảng `_1`, `_2` |
| https://github.com/tkob-team/eshop-sut/issues/274 | 82 | 12 | SV-02 `_1`…`_4` ở `P1_chrome\`, `P2_firefox\`, `P3_android\` |

Cách làm: mở link, bấm **⋯** ở body, chọn **Edit**, kéo ảnh vào mục **Bằng chứng**, rồi bấm **Update comment**.

Riêng **#266 (BUG-72)**: Claude Code sẽ sửa lại body để khôi phục dòng dữ kiện. Em kéo ảnh trước hay sau cũng được, nhưng nếu kéo trước thì nhắc Claude Code là body đã có ảnh, để nó chỉ sửa đúng dòng đó, không ghi đè cả body bằng file.
```

**Xử lý:** [...]

---

## #181 | 08:11 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. BUG-72: khôi phục dòng "Actual nguyên văn CL-32 P3 (auto)" về đúng checklist.json (bị SV lỡ xoá ở 496ad20); gh issue edit #266 sửa body tương ứng + comment đính chính 1 dòng ("Đính chính: khôi phục dòng dữ kiện CL-32 P3 chép từ checklist.json"); log trước/sau vào HW03/bugs/issue_edits.md. Commit `HW03[T1]: khôi phục dữ kiện BUG-72 (#266)`.
2. Kiểm 14 issue #261–#274 có đủ số ảnh theo bảng (ảnh trong body).
3. Ảnh trang Issues: Playwright mở https://github.com/tkob-team/eshop-sut/issues?q=is%3Aissue+%22HW03-C2%22+author%3AThachHaoo (đủ 28, chụp nhiều trang nếu cần) → HW03/bugs/issues_page_HW03-C2_<n>.png; đưa vào report §6. Commit `HW03[T1]: ảnh trang Issues`.
Không push. Báo ≤ 6 dòng + hash.
```

**Output:**
```
Ảnh đủ cả 14. Chụp trang Issues.

25 + 3 = 28. Xem ảnh trước khi commit.

Xong cả 3 việc, chưa push.

- **BUG-72 (#266):** dòng dữ kiện CL-32 P3 trong `BUG-72.md` đã khôi phục đúng `checklist.json`. Body issue #266 sửa đúng dòng đó, ảnh SV đã kéo giữ nguyên, kèm comment đính chính. Trước/sau ghi ở `HW03/bugs/issue_edits.md`. Commit `99a9e27`.
- **Ảnh trong 14 issue #261–#274:** đủ số ảnh theo bảng, tất cả nằm trong body.
- **Ảnh trang Issues:** chụp bằng Playwright, không đăng nhập. Trang tìm kiếm ra đúng 28 kết quả, chia 2 trang: `HW03/bugs/issues_page_HW03-C2_1.png` (25 issue) và `_2.png` (3 issue). Em đã xem từng ảnh, không thấy thông tin riêng. Đã chèn 2 ảnh và link tìm kiếm vào report §6. Commit `08fe5ab`.
- **Còn trống trong report §6:** dòng 📝 "bảng BUG-58…, link GitHub Issues" em để nguyên, vì bảng bug là phần SV tự viết.
```

**Xử lý:** [...]

---

## #182 | 08:25 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Xong cả 3 việc, chưa push.

- BUG-72 (#266): dòng dữ kiện CL-32 P3 trong BUG-72.md đã khôi phục đúng checklist.json. Body issue #266 sửa đúng dòng đó, ảnh SV đã kéo giữ nguyên, kèm comment đính chính. Trước/sau ghi ở HW03/bugs/issue_edits.md. Commit 99a9e27.
- Ảnh trong 14 issue #261–#274: đủ số ảnh theo bảng, tất cả nằm trong body.
- Ảnh trang Issues: chụp bằng Playwright, không đăng nhập. Trang tìm kiếm ra đúng 28 kết quả, chia 2 trang: HW03/bugs/issues_page_HW03-C2_1.png (25 issue) và _2.png (3 issue). Em đã xem từng ảnh, không thấy thông tin riêng. Đã chèn 2 ảnh và link tìm kiếm vào report §6. Commit 08fe5ab.
- Còn trống trong report §6: dòng 📝 "bảng BUG-58…, link GitHub Issues" em để nguyên, vì bảng bug là phần SV tự viết.
===
push rồi nhé, 5.8, 5.9 cũng viết xong rồi
```

**Output:**
````
Anh đã đọc §5.8–5.9. Có mấy lỗi dữ kiện nghiêm trọng, cần sửa trước khi nộp.

**Trước hết, anh hỏi thẳng một lần:** phần này em có nhờ công cụ AI khác (ChatGPT, Gemini…) viết không? Dấu hiệu: cột "Liên quan" ghi **"Đã biết – BUG-01…BUG-06"** kèm tên tiếng Anh ("Client-side price override", "Unauthenticated cart session ambiguity"…), mà các bug này **không tồn tại**. BUG-01…06 của em là bug HW02 trang Đăng ký (BUG-01 = #17 regex mật khẩu), không liên quan giỏ hàng hay checkout. Nếu có dùng AI khác thì theo AI-01 em phải khai lượt đó (vào `prompt_log_extra.toml`) và **tự viết lại** phần 🔒 này. Nếu em tự viết thì cứ nói, anh chỉ ra chỗ sai dữ kiện để em sửa.

**Lỗi dữ kiện (em sửa, anh không viết hộ)**

| # | Chỗ | Vấn đề |
|---|---|---|
| 1 | Cột "Liên quan" ở cả 6 dòng "Đã biết – BUG-0x" | Bịa mã bug. Hoặc tra issue thật trên `tkob-team/eshop-sut` (bảo Claude Code kiểm trùng cho 7 pain point), hoặc ghi "chưa kiểm trùng" |
| 2 | "Backend tin `totalAmount` từ Client" | Dữ kiện HW02 là `/api/checkout` đọc `total_amount` từ body. Tên trường sai; nếu nêu nguyên nhân thì dẫn đúng dữ kiện, không thì ghi "(chưa kiểm chứng)" |
| 3 | "hỏng API trigger ở trang danh sách", đề xuất "Sửa API handler" | Giỏ web là **state React, không gọi API** (dữ kiện HW02 B). Câu này sai |
| 4 | "Sai nhãn nút: Đăng nhập hiện 'Đăng ký'" | Đó là **tiêu đề form** "Đăng Ký" (`Login.jsx:24`), không phải nhãn nút. Đã **trùng #9** |
| 5 | Severity **"Critical (Blocker)"** cho #1, #2 nhưng ghi "không cản trở hoàn thành nhiệm vụ" | Tự mâu thuẫn. Blocker là chặn hoàn thành, mà 7/7 phiên đều hoàn thành. Em chọn thang khác hoặc bỏ chữ "Blocker" |
| 6 | Thang severity | Chưa ghi định nghĩa thang dưới bảng §5.9 (plan mục 9 để 📝) |
| 7 | "Khó tìm lịch sử đơn": 1/7 (S02) | **S04 cũng tìm** ("về trang chủ… xem giỏ hàng… À đây (ở profile)") nên ít nhất là 2/7 |
| 8 | "Thêm giỏ ở danh sách hỏng": tính S02 | Câu của S02 bị cụt ("Bấm nút thêm vào giỏ hàng mà…"), không cho biết ở trang nào. Tính vào 4/7 là khẳng định quá dữ kiện, trừ khi video xác nhận |
| 9 | "thiếu đường dẫn trực tiếp trên Header", "thiếu Debounce/Idempotency" | Nguyên nhân chưa kiểm chứng. Ghi "(chưa kiểm chứng)" hoặc bỏ |

Còn lại cấu trúc tốt: tách lỗi riêng lẻ với thiết kế, có tần suất, có đề xuất, bám câu nói thật.

Nếu cần kiểm trùng nhanh cho mục 1, dán:
```
Chỉ đọc: với 7 pain point ở report §5.8 (sửa tổng tiền checkout; thêm giỏ ở danh sách không phản hồi; đặt đơn không cần SĐT/địa chỉ; bấm 1 thành 2 đơn; giỏ khi chưa đăng nhập; khó tìm lịch sử đơn; tiêu đề form Đăng nhập "Đăng Ký" + thiếu ảnh SP) → tìm issue trùng/liên quan trên tkob-team/eshop-sut (mọi tác giả) + BUG HW02/HW03 của SV; in bảng pain point – issue (số, tiêu đề) – mức. Không sửa report. Báo ≤ 12 dòng.
```
````

**Xử lý:** [...]

---

## #183 | 08:31 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Không dùng AI, để mình sửa lại, đang buồn ngủ quá
Sửa lại rồi, commit thế nào nhỉ, commit xong mình dùng prompt kia của bạn nhé
```

**Output:**
````
Commit và push như sau:

```
git add HW03/23120255_HW03_Report.md
git commit -m "HW03[T2]: SV sửa findings theo kiểm dữ kiện"
git push
```

Rồi dán prompt kiểm trùng cho Claude Code. Khi nó trả bảng pain point ↔ issue, em điền đúng số issue vào cột "Liên quan", commit thêm một lần: `HW03[T2]: SV ghi issue liên quan vào findings`.

Em đang buồn ngủ, nên ưu tiên phần còn lại (deadline 11:30):
1. **§3.4** (15'), **Critique** (25'), **verdict Audit** (30'): bắt buộc.
2. Duyệt khối 📝, tự chấm, ký: 20'.
3. Đóng gói: Claude Code làm, khoảng 30'.
4. **Video**: chỉ làm nếu tới khoảng 10:15 vẫn còn dư giờ.

Nếu cần chợp mắt thì ngủ 20 phút ngay bây giờ (đặt báo thức) còn hơn viết Critique lúc mắt díp. Sau đó làm liền một mạch tới lúc nộp.
````

**Xử lý:** [...]

---

## #184 | 08:32 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Chỉ đọc: với 7 pain point ở report §5.8 (sửa tổng tiền checkout; thêm giỏ ở danh sách không phản hồi; đặt đơn không cần SĐT/địa chỉ; bấm 1 thành 2 đơn; giỏ khi chưa đăng nhập; khó tìm lịch sử đơn; tiêu đề form Đăng nhập "Đăng Ký" + thiếu ảnh SP) → tìm issue trùng/liên quan trên tkob-team/eshop-sut (mọi tác giả) + BUG HW02/HW03 của SV; in bảng pain point – issue (số, tiêu đề) – mức. Không sửa report. Báo ≤ 12 dòng.
```

**Output:**
```
Đã đối chiếu 7 pain point với toàn bộ issue của `tkob-team/eshop-sut` (đến #274, mọi tác giả) và BUG HW02 (BUG-01…57, #17–#30, #161–#203) + HW03 (BUG-58…85, #247–#274) của SV. Em chỉ so tiêu đề issue, chưa mở body; chưa sửa report. Còn 3 pain point (4, 6, ảnh SP ở 7) chưa có issue nào khớp đúng.

| Pain point | Issue trùng / liên quan | Mức |
|---|---|---|
| 1. Sửa được tổng tiền ở checkout | #13 [BUG-FR08-04] Ô "Tổng tiền thanh toán" trên Web sửa được · #10 [BUG-FR08-01] Backend lưu mọi `total_amount` do client gửi | **Trùng** #13 (đã biết); #10 liên quan |
| 2. Thêm giỏ ở danh sách không phản hồi | #162 [FR-07] Trang chủ: bấm 'Thêm vào giỏ' không có phản hồi trực quan (= HW02 BUG-16) · #166 Navbar thiếu badge số lượng giỏ (BUG-20, S05 gợi ý đúng ý này) · #161 nút ở trang chi tiết nuốt lượt bấm đầu (BUG-15) | **Trùng** #162 (BUG-16); #166, #161 liên quan |
| 3. Đặt đơn không cần SĐT/địa chỉ | #65 [BUG-FR08-08] Thanh toán trên Web không gửi `shipping_address` · #58 bản Mobile | **Một phần** (#65): chưa issue nào nói checkout không bắt buộc SĐT/địa chỉ |
| 4. Bấm 1 thành 2 đơn (S07) | #163 [FR-07] Thêm cùng sản phẩm nhiều lần thành nhiều dòng (BUG-17) · #270 [HW03-C2-78] nút submit không khoá (form C2, không phải checkout) | **Chưa có issue khớp**; SV cần xác định "2 đơn" là 2 đơn hàng hay 2 dòng trong giỏ (nếu là 2 dòng thì trùng #163) |
| 5. Thêm giỏ khi chưa đăng nhập (S04) | #242 [HW03-C1][FR-08] Khách truy cập trực tiếp Checkout và thấy nút xác nhận · #69 [BUG-FR20-07] Đăng xuất không xoá giỏ | **Liên quan**: chưa issue nào về việc khách thêm được vào giỏ |
| 6. Khó tìm lịch sử đơn (S02, S04) | (không có) – các issue Lịch sử đơn hiện có (#61, #271–#273) nói về màu, loading, ngày, nút huỷ | **Chưa có** |
| 7a. Form Đăng nhập có tiêu đề "Đăng Ký" (S01) | #9 [BUG-FR02-09] Form đăng nhập: tiêu đề "Đăng Ký", nhãn "Username", nút "Sign In" | **Trùng** #9 (đã biết) |
| 7b. Thiếu ảnh sản phẩm (S01, S03) | #171 [FR-07] 5 ảnh sản phẩm trang chủ có `alt=""` (BUG-25) | **Liên quan**: chưa issue nào về ảnh không hiển thị / sai hình |
```

**Xử lý:** [...]

---

## #185 | 08:33 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
buồn ngủ là nói về hiệu suất bị suy hụt, chứ không phải giờ muốn đi ngủ, tôi sẽ cố hoàn thành deadline rồi mới đi ngủ.
```
*Đính kèm:* `attachment.txt`

**Output:**
```
Hiểu rồi, ta làm liền một mạch tới lúc nộp.

**Điền cột "Liên quan" trong §5.8–5.9 theo bảng Claude Code vừa trả.** Lưu ý nó mới so **tiêu đề**, chưa mở body.

| Pain point | Ghi vào "Liên quan" |
|---|---|
| 1. Sửa tổng tiền | Trùng **#13**; liên quan **#10** |
| 2. Thêm giỏ ở danh sách | Trùng **#162** (BUG-16 của em); liên quan **#166** (badge, đúng ý S05), **#161** |
| 3. Không cần SĐT/địa chỉ | Một phần **#65**; chưa có issue riêng |
| 4. 1 thành 2 đơn (S07) | Chưa xác định. Nếu S07 nói 2 dòng trong giỏ thì trùng **#163**; 2 đơn hàng thì chưa có issue. Em xem video hoặc nhớ lại |
| 5. Giỏ khi chưa đăng nhập | Liên quan **#242**, **#69**; chưa có issue riêng |
| 6. Khó tìm lịch sử đơn | Chưa có issue (vấn đề usability, không hẳn là bug) |
| 7a. Tiêu đề "Đăng Ký" | Trùng **#9** |
| 7b. Thiếu ảnh SP | Liên quan **#171**; chưa có issue về ảnh không hiển thị |

**Bug Task 2:** plan mục 9 ghi "bug thật → GitHub Issues". Những pain point **chưa có issue** (3, 4 nếu là 2 đơn, 5, 7b) em có thể lập thêm, mỗi bug khoảng 10' (em viết, Claude Code tạo). Với thời gian còn lại, anh khuyến nghị **không lập thêm**. Thay vào đó ghi một dòng dưới §5.9: *"Pain point 3, 5, 7b (và 4 nếu là 2 đơn hàng) chưa có issue; chưa lập do giới hạn thời gian"*. Vậy là trung thực, và người chấm thấy em đã kiểm trùng. Nếu cuối giờ còn dư thì lập sau.

Commit `HW03[T2]: SV ghi issue liên quan vào findings`, push.

**Tiếp theo: §3.4 (🔒, khoảng 15').** Nội dung là item em bổ sung SV-01…06 và vì sao AI bỏ sót.
- Dữ kiện: `HW03/checklist/sv_items.md` (6 item của em) và `HW03/checklist/ai_gap_answer.md` (AI tự nhận, tách 3 loại: đã nghĩ nhưng không đưa vào / không nghĩ tới / bị gỡ theo quyết định SV).
- Mỗi item 2–3 câu: item kiểm gì, AI có nghĩ ra không (theo `ai_gap_answer`), và theo em vì sao bỏ sót (prompt, phạm vi slide, cách skill dặn). Bài học handoff mục 6 có ghi gap SV-06 là do AI chỉ đọc một phần slide, đó là dữ kiện em dùng được.

Xong §3.4 thì sang Critique.
```

**Xử lý:** [...]

---

## #186 | 08:34 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
là giờ điền cột liên quan đó à, xong đặt ở đâu nhỉ
```

**Output:**
````
Đúng vậy. Em sửa thẳng trong report `HW03/23120255_HW03_Report.md`, ở hai bảng em vừa viết:

**1. §5.8, cột cuối "Liên quan bug/issue"** (ngoài cùng bên phải). Thay nội dung đang có ở từng dòng, ví dụ:
- Dòng "Cho phép tự điều chỉnh tổng tiền…": thay thành `Trùng #13; liên quan #10`.
- Dòng "Nút Thêm vào giỏ ở trang danh sách…": thay thành `Trùng #162 (BUG-16); liên quan #166, #161`.
- …các dòng khác theo bảng anh vừa gửi.

**2. §5.9, cột "Đề xuất".** Mỗi ô đang mở đầu bằng **"Đã biết – BUG-0x:"**. Đổi phần đó thành số issue tương ứng, ví dụ `Trùng #13:` hoặc `Chưa có issue:`, phần đề xuất phía sau giữ nguyên.

**3. Thêm một dòng ngay dưới bảng §5.9:**
> Pain point 3, 5, 7b (và 4 nếu là 2 đơn hàng) chưa có issue; chưa lập do giới hạn thời gian. Đối chiếu trùng theo tiêu đề issue trên tkob-team/eshop-sut.

Em viết lại câu này theo giọng của em cũng được.

Xong thì:
```
git add HW03/23120255_HW03_Report.md
git commit -m "HW03[T2]: SV ghi issue liên quan vào findings"
git push
```
````

**Xử lý:** [...]

---

## #187 | 08:39 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Push rồi, có cần Claude Code kiểm tra lại gì không?
```

**Output:**
```
Anh đã kiểm trên repo (`afc81da`), không cần Claude Code kiểm lại:
- Mã BUG-0x bịa, `totalAmount`, "API trigger/handler", "Blocker" đều đã gỡ hết.
- Cột Liên quan có số issue thật (#9, #10, #13, #65, #69, #161, #162, #163, #166, #171, #242) và có dòng "chưa có issue".
- Tần suất đã sửa: thêm giỏ 3/7, lịch sử đơn 2/7.

**Còn thiếu 1 điểm nhỏ:** chưa có **định nghĩa thang severity** dưới bảng §5.9. Em thêm 1–2 dòng: Critical/High/Medium/Low nghĩa là gì theo em, ví dụ dựa trên ảnh hưởng tới nhiệm vụ, an toàn tiền/dữ liệu và tần suất. Vì #1 và #2 là Critical dù "không cản trở hoàn thành nhiệm vụ", thang phải giải thích được vì sao. Tối đa 3 phút. Commit chung với §3.4 cũng được.

**Tiếp theo: §3.4** theo hướng dẫn anh gửi lúc nãy, dùng `sv_items.md` và `ai_gap_answer.md`.
```

**Xử lý:** [...]

---

## #188 | 08:41 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Rồi thêm rồi nhé, push luôn rồi, xem oke chưa
```

**Output:**
```
Ổn. Thang đã giải thích được vì sao #1 và #2 là Critical dù nhiệm vụ vẫn hoàn thành, và các mức tách nhau rõ.

Chỉ một chữ nhỏ, sửa hay không tuỳ em: ở mức Critical, cụm "nhờ thao tác lách/thủ công" khớp với #1 (sửa tổng tiền) nhưng không khớp #2 (đặt đơn không cần SĐT/địa chỉ, người dùng không lách gì). Muốn chặt thì bỏ cụm đó, chỉ giữ "dù người dùng vẫn hoàn thành nhiệm vụ".

Task 2 coi như xong phần của em. **Tiếp: §3.4**, rồi Critique.
```

**Xử lý:** [...]

---

## #189 | 08:48 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
xong 3.4 rồi, commit gì đây nhỉ, bạn check hay là Claude Code check đây nhỉ, và check trước khi commit hay sau khi commit
```

**Output:**
````
**Commit trước, kiểm sau.** Quy tắc vẫn như cũ: bản em viết phải nằm trong git trước, sửa gì sau đó thì tạo commit mới.

```
git add HW03/23120255_HW03_Report.md
git commit -m "HW03[T1]: SV viết §3.4 – item bổ sung + vì sao AI bỏ sót"
git push
```

**Anh kiểm**, vì đây là phần chữ của em: anh soi dữ kiện trên repo (mã SV-xx có thật không, câu "AI không nghĩ tới / đã nghĩ nhưng không đưa vào" có khớp `ai_gap_answer.md` không, có khẳng định quá mức không). Không cần Claude Code. Push xong em báo một câu, trong lúc anh đọc thì em bắt đầu viết **Critique**.
````

**Xử lý:** [...]

---

## #190 | 08:48 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
đã push rồi nhé
```

**Output:**
```
Anh đã đọc §3.4 và đối chiếu với `ai_gap_answer.md` và bản v1. Phần lớn khớp dữ kiện. Có một điểm cần sửa và hai điểm nhỏ.

**Cần sửa: SV-05 lệch với câu trả lời của AI**
- `ai_gap_answer.md` (commit `de4c69a`, 19:29 04/11) trả lời cho **SV-05 bản cũ: "Bố cục form khi bàn phím ảo hiện trên di động"**. Sau đó em đổi SV-05 thành **Target Size** ở `d173b63` (19:46), nên **AI chưa bao giờ trả lời "vì sao bỏ sót" cho Target Size**.
- Trong §3.4, dòng "AI có nghĩ ra không: Không nghĩ tới (Nhóm 2)" của SV-05 đang trình bày như thể là câu trả lời của AI. Anh vừa grep bản v1: đúng là không có "24px", "target size", "vùng bấm", nên kết luận "không có trong v1" vẫn đúng. Nhưng em cần ghi rõ nguồn, đại ý: *AI trả lời cho SV-05 bản cũ (bàn phím ảo); sau khi em đổi SV-05 thành Target Size thì không hỏi lại AI, em tự đối chiếu v1 và không thấy item nào về kích thước vùng bấm.*
- Câu nguyên nhân SV-05 khi đó là nhận định của em, không phải của AI. Viết sao cũng được, chỉ cần đúng là của em.

**Hai điểm nhỏ**
1. Các câu "Nguyên nhân bỏ sót" của SV-01, 02, 03, 04, 06 bám rất sát phần "Nguyên nhân khả dĩ (nhận định của AI)" trong `ai_gap_answer.md`, nhưng đang viết như khẳng định của em. Thêm một câu dẫn ở đầu §3.4 (ví dụ *"Nguyên nhân dựa trên câu trả lời của AI ở `ai_gap_answer.md`, em đối chiếu với v1"*) hoặc đổi vài chữ "do…" thành "có thể do…". Như vậy khớp với chỗ AI tự ghi là "khả dĩ".
2. SV-06: câu "nằm ngoài đoạn slide AI được cấp… **dẫn đến việc** AI không mở rộng" là nguyên nhân chưa kiểm chứng. AI cũng chỉ ghi "có thể". Đổi thành "có thể dẫn đến".

Sửa xong commit `HW03[T1]: SV sửa §3.4 theo kiểm dữ kiện`, push. Rồi sang **Critique**. Lúc này là 08:50; giữ nhịp thì Critique xong khoảng 09:20, Audit khoảng 09:50, đóng gói khoảng 10:30, và còn dư cho video.
```

**Xử lý:** [...]

---

## #191 | 08:54 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Push ồi nhé, kiểm tra lần cuối trước khi mình sang Critique nhé
```

**Output:**
```
§3.4 ổn. Lệch SV-05 đã ghi rõ nguồn, câu dẫn đầu mục đúng sự thật, các câu nguyên nhân đã chuyển sang "có thể".

Còn một chi tiết, sửa hay không tuỳ em: câu nguyên nhân SV-05 (*"Do AI chỉ quét cấu trúc mã nguồn tĩnh và đọc các thuộc tính CSS mặc định…"*) là nhận định của em nhưng vẫn viết dạng khẳng định. Ý "đọc CSS mặc định" chưa có dữ kiện. Đổi "Do" thành "Có thể do" là đồng bộ với 5 mục kia. Không sửa cũng không sai dữ kiện nghiêm trọng.

**Sang Critique (§10, 🔒, 200–300 từ, đếm theo khoảng trắng)**

Đề yêu cầu đủ 3 ý: AI **sai** ở đâu, **thiên lệch** ở đâu, **thiếu** gì. Dữ kiện có sẵn trong repo để em dẫn (chỉ là nguồn, câu chữ là của em):
- **Sai:**
  - Playwright tự động lệch với lượt tay: auto ép locale vi-VN nên CL-08 P2/P3 sai; CL-11 so toạ độ sai với bố cục 2 cột; CL-15 đo viewport 375. Xem report §4.1 bảng lệch.
  - Timeout của harness ở P3 được ghi thành Blocked; BUG-78 lúc đầu có câu "TimeoutError" là lỗi harness.
  - Khung `sv_items.md` thiếu trường `loai_nguon` (L2). RUN.md M6 mâu thuẫn chính nó. Commit ảnh sót P3_M2_2.
- **Thiên lệch:**
  - v1 bám SRS (40/65 item), bỏ quy tắc slide (Golden Rule, SV-03).
  - Accessibility vắng hẳn vì prompt không nêu (SV-01, 04, 05).
- **Thiếu:**
  - AI chỉ đọc một phần slide (dòng 56–210, 401–460) nên bỏ double-submit (SV-06).
  - Hành vi chỉ thấy trên trình duyệt hoặc thiết bị thật (autofill, focus ring).
  - Task 2: AI không thay được người quan sát, mọi pain point đến từ người tham gia thật.
- **Nguyên nhân phía em:** prompt bước 1 chỉ nêu 3 nguồn; skill viết trước khi quy trình chốt (handoff mục 6).

Những điều cần giữ:
- Tách "AI không nghĩ ra item" với "hệ thống có lỗi thật".
- Không dùng item hoặc case đã bỏ làm bằng chứng.
- Không dùng "luôn", "tuyệt đối"; dùng "cho thấy" thay "chứng minh".

Viết xong commit `HW03: SV viết Critique`, push, anh đếm từ và soát dữ kiện.
```

**Xử lý:** [...]

---

## #192 | 09:03 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
push rồi, xem nhé
```

**Output:**
```
Critique có đủ 3 ý (sai, thiên lệch, thiếu) và nêu được nguyên nhân phía em. Nhưng có 2 lỗi dữ kiện và **quá số từ**.

**Số từ: 365, đề cho 200–300** (đếm theo khoảng trắng, không tính tiêu đề). Cần cắt khoảng 65–70 từ. Chỗ dễ cắt:
- Câu mở đầu ("Nhìn lại cả hành trình…"): khoảng 30 từ, không mang dữ kiện.
- Câu "Em nhận ra cần tách biệt rõ…": đây là lời nhắc anh gửi em, không phải nhận xét về AI. Bỏ được khoảng 20 từ.
- Rút gọn ví dụ trong đoạn "điểm sai".

**Lỗi dữ kiện**

| Câu | Vấn đề |
|---|---|
| "đo nhầm kích thước viewport về 375px (CL-15)" | Auto đo **đúng** ở 375 px (scrollWidth 381 > 375). Chỗ lệch là lượt tay **không** đo ở 375 px (report §4.1). Đây không phải AI sai, nên bỏ hoặc sửa |
| "AI ghi nhận nhầm timeout… thành trạng thái Blocked (BUG-78)" | Timeout của harness ghi **Blocked là đúng** (quy ước V1: timeout ≠ Failed). Chỗ sai thật là dòng "TimeoutError do dblclick" từ lượt auto đi vào Actual của BUG-78, trong khi đó là lỗi harness, không phải hành vi SUT. Viết lại cho đúng ý này hoặc bỏ |

**Khẳng định hơi quá (nhẹ)**
- "hoàn toàn vắng bóng **chỉ vì** prompt…": AI tự ghi đó là nguyên nhân *khả dĩ*. Đổi thành "có thể vì".
- "**mọi** điểm nghẽn… đều xuất phát từ người dùng thật": dữ kiện của em ủng hộ ý này, nhưng nên viết "các điểm nghẽn em thu được đều…" thay cho "mọi".

**Lỗi chính tả:** "bo qua" → "bỏ qua".

Sửa xong commit `HW03: SV sửa Critique (số từ + dữ kiện)`, push, anh đếm lại.
```

**Xử lý:** [...]

---

## #193 | 09:09 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Push rồi, xem lại giúp mình thử nhé
```

**Output:**
```
Đã đạt số từ: **283 từ**. Hai lỗi dữ kiện lần trước đã gỡ, chính tả đã sửa. Còn 2 chỗ chưa chính xác, mỗi chỗ chỉ cần sửa vài chữ:

1. **"AI cũng đưa nhầm thông báo lỗi harness `TimeoutError` trên P3 vào phần Actual của BUG-78"**
   Actual của BUG-78 là **em viết**. Phía AI là harness Playwright (do AI viết) ghi `TimeoutError` thành kết quả auto của SV-06 trên P3. Dòng đó nằm trong phần Dữ kiện, rồi em chép sang Actual. Nói "AI đưa vào Actual" là đổ lỗi chưa đúng chỗ. Gợi ý ý (câu chữ em tự viết): *harness do AI viết ghi `TimeoutError` (lỗi của chính test) thành kết quả SV-06 trên P3, nên lỗi này lọt vào BUG-78*.

2. **"do AI chỉ đọc một phần slide…, kịch bản chống gửi trùng… đã bị bỏ qua"**
   - Đây là nguyên nhân khả dĩ, AI cũng chỉ ghi "có thể". Đổi thành **"có thể do"**.
   - AI **không bỏ qua hẳn**: CL-53 có chống gửi trùng, nhưng chỉ ở màn Đăng nhập khi mạng chậm (`ai_gap_answer.md` xếp SV-06 nhóm 1, "đã nghĩ nhưng không đưa vào"). Nên viết là chỉ phủ một màn hoặc một điều kiện, không phải bỏ qua.

Sửa xong số từ vẫn trong khoảng 280–290, không lo vượt.

Sửa, commit `HW03: SV sửa Critique (2 dữ kiện)`, push. Sau đó **chưa cần anh xem lại**, sang thẳng **verdict Audit**. Anh sẽ đưa lệnh xuất transcript và điền #n để Audit có đủ cột.
```

**Xử lý:** [...]

---

## #194 | 09:11 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Push rồi, bạn xem đã oke chưa nhé
```

**Output:**
````
Hai dữ kiện đã đúng. Nhưng đoạn sửa làm Critique dài thêm: giờ là **308 từ**, vượt mức 300 khoảng 8 từ (đếm theo khoảng trắng, không tính tiêu đề).

Cắt khoảng 10–15 từ cho an toàn. Gợi ý chỗ cắt, câu chữ vẫn là của em:
- "(dẫn đến lỗi này lọt vào…)" có thể rút còn "(lọt vào BUG-78)".
- "chứ chưa mở rộng sang các điều kiện và form khác" có thể rút còn "chưa mở rộng sang form khác".
- "AI lộ hạn chế khi xử lý tự động hóa và dựng khung tài liệu" có thể rút gọn hoặc bỏ, vì các ví dụ phía sau đã nói đủ.

Sửa xong commit `HW03: SV rút gọn Critique`, push. Không cần anh xem lại nội dung nữa. Nếu muốn, em tự đếm bằng PowerShell:
```
(Get-Content HW03\23120255_HW03_Report.md -Raw -Encoding UTF8) -match '(?s)## 10\.[^\n]*\n(.*?)\n## 11\.' | Out-Null; ($Matches[1] -split '\s+' | ? {$_}).Count
```

Sau đó sang **Audit**. Lệnh chuẩn bị Audit anh gửi ngay sau đây.
````

**Xử lý:** [...]

---

## #195 | 09:12 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
285 từ rồi, kiểm tra giúp mình nhé
```

**Output:**
````
Critique đạt: **285 từ**, nằm trong khoảng 200–300, dữ kiện đã đúng. Xong.

Anh xuất transcript phiên này (`_p2`) ngay bây giờ, để Claude Code điền #n vào Audit. File sẽ tới trong giây lát.

Transcript `claude-ai_session_HW03_p2.jsonl` đã xuất. Phiên này chạy từ 18:18 10/11 tới 09:12 11/11 và không bị nén: lượt đầu trùng giờ bắt đầu.

Lúc kết thúc phiên (trước khi nộp), anh sẽ xuất lại **cùng tên `_p2`** để có thêm các lượt từ giờ tới lúc đó. Em ghi đè file cũ, rồi trích prompt log lần cuối.

**Bây giờ em làm:**
1. Đặt file vào `.transcripts\`.
2. Dán cho Claude Code:

```
NHIỆM VỤ: chuẩn bị Audit + form. Không push, không amend, KHÔNG viết verdict/lý do/Critique/tự chấm.
1. python tools/hooks/on_stop.py --manual (đã có .transcripts/claude-ai_session_HW03_p2.jsonl) → commit `HW03: prompt log thêm transcript phiên claude.ai (p2)`. Chạy --list --commits.
2. AI-02: cập nhật danh mục artifact từ git (thêm các việc AI làm từ tối 10/11: khung bug theo mẫu HW02 + script, kiểm trùng issue, bug_check/bug_check2 + tests/repro_bugs.spec.ts, issue_edits, Google Form (Apps Script, phiên thảo luận), moderator_script, usability_fill_hw03.py + JSON phiên AI chép, summary_hw03 sửa, ảnh trang Issues, AI nháp §3.2/§4.2). Điền cột #n theo prompt log (dải lượt trước commit của artifact); verdict/lý do = <SV viết>. Bảng in gọn để SV điền nhanh.
3. AI-03: cập nhật số lượt theo dòng "Tổng" (đủ model + lượt không rõ model + lý do = <SV viết> nếu notes chưa có).
4. §11 Mandatory Disclosure + report_plan f/g: thêm các việc AI mới ở trên; dòng AI-05 về CSV có họ tên/SĐT.
5. Chạy lại mọi script sinh bảng (report_t1, sus_score --report, summary_hw03, forms_hw03). Liệt kê mọi <SV viết>/<SV điền>/📝 còn lại (file:dòng).
Commit theo từng việc. Báo cáo ≤ 12 dòng + hash.
```

Trong lúc Claude Code chạy, em **duyệt các khối 📝** trong report: §3.2, §4.2 (AI nháp) và §5.5. Đọc, sửa chỗ sai, rồi xoá dòng 📝.
````
*File AI ghi/gửi trong lượt này:* `claude-ai_session_HW03_p2.jsonl`

**Xử lý:** [...]

---

## #196 | 09:13 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: chuẩn bị Audit + form. Không push, không amend, KHÔNG viết verdict/lý do/Critique/tự chấm.
1. python tools/hooks/on_stop.py --manual (đã có .transcripts/claude-ai_session_HW03_p2.jsonl) → commit `HW03: prompt log thêm transcript phiên claude.ai (p2)`. Chạy --list --commits.
2. AI-02: cập nhật danh mục artifact từ git (thêm các việc AI làm từ tối 10/11: khung bug theo mẫu HW02 + script, kiểm trùng issue, bug_check/bug_check2 + tests/repro_bugs.spec.ts, issue_edits, Google Form (Apps Script, phiên thảo luận), moderator_script, usability_fill_hw03.py + JSON phiên AI chép, summary_hw03 sửa, ảnh trang Issues, AI nháp §3.2/§4.2). Điền cột #n theo prompt log (dải lượt trước commit của artifact); verdict/lý do = <SV viết>. Bảng in gọn để SV điền nhanh.
3. AI-03: cập nhật số lượt theo dòng "Tổng" (đủ model + lượt không rõ model + lý do = <SV viết> nếu notes chưa có).
4. §11 Mandatory Disclosure + report_plan f/g: thêm các việc AI mới ở trên; dòng AI-05 về CSV có họ tên/SĐT.
5. Chạy lại mọi script sinh bảng (report_t1, sus_score --report, summary_hw03, forms_hw03). Liệt kê mọi <SV viết>/<SV điền>/📝 còn lại (file:dòng).
Commit theo từng việc. Báo cáo ≤ 12 dòng + hash.
```

**Output:**
```
Commit + list commits.

Forms generated by forms_hw03.py. Read it.

Đang sửa `forms_hw03.py` (thêm artifact mới + cột #n), sắp chạy.

Cột #n đã sinh. Sửa U6 = #184 rồi commit AI-02.

Xong AI-02, AI-03. Giờ làm §11 + report_plan f/g.

Chạy lại các script sinh bảng.

Ghi danh sách chỗ trống vào file, commit cuối.

Xong 5 việc, 6 commit, chưa push. Không đụng verdict, lý do, Critique, tự chấm.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** chuẩn bị Audit + form (bước 1–5).
- **Commit:**
  - `0c96555` prompt log thêm transcript claude.ai p2.
  - `d4fa9e4` AI-02.
  - `47b96b1` AI-03.
  - `f33f7d5` §11 + report_plan f/g.
  - `bfe1e36` chạy lại script.
  - `3b2f412` thêm `HW03/placeholders_left.md` (đánh dấu `export-ignore`, không nộp).
- **Prompt log:** 196 lượt (Sonnet 4.6: 3, Opus 5.5: 186, không rõ model: 7). `--list --commits` ghi ra `appendix/prompt_log_turns.txt`, dùng cùng `since`/`exclude` với log nên số `#n` khớp log.
- **AI-02:** từ 22 lên 34 artifact (thêm B1–B7, U3–U6, R4; R1/R4 tách phần AI nháp §3.2, §4.2).
  - Cột #n lấy lượt nằm giữa commit liền trước và commit tạo artifact. Nếu khoảng đó rỗng thì lấy lượt cuối trước commit. U6 (đối chiếu pain point) đặt tay `#184`.
  - Bảng 3.2 rút còn 4 cột: Mã | #n | Verdict | Lý do. Chạy lại script vẫn giữ ô SV đã điền.
- **AI-03:** số lượt theo dòng Tổng; 7 lượt không rõ model, mỗi lượt một dòng lý do `<SV viết>` (notes chưa có khoá).
- **§11:** thêm mục 8–12, mục 12 là dòng CSV có họ tên/SĐT (cho AI-05). report_plan f thêm 6 dòng, g điền dòng "AI tạo bản đầu".
- **Kiểm tra:** `sus_score --check` 8 phiếu, 7 phiên tính được, 0 lỗi. `report_t1`, `sus_score --report`, `summary` chạy xong, report/README không đổi. `forms_hw03.py` chạy lại xong.
- **Chỗ trống còn lại:** chi tiết từng dòng ở `HW03/placeholders_left.md`.
  - Report: 34 chỗ. Gồm §1, §2, §5.1–5.4, §6, §7, §9, §11 (2 dòng), §12 tự chấm, phụ lục D, và nhãn 📝 "AI nháp" ở §3.2, §4.2, §11.
  - README:11–15 (tự chấm).
  - AI-02: 34 × 2 ô (dòng 63–111) + §4 (dòng 115).
  - AI-03: dòng 30–36, 41, 45, 51, 57.
  - `skills/VideoLinks.md`:5–6 (link video).
- **Bất thường:**
  - `HW03/23120255_HW03_Report.md` đang có thay đổi chưa commit, không phải em sửa: bỏ nhãn "📝 AI nháp – SV duyệt/sửa" ở §3.2 hoặc §4.2. Em để nguyên, không commit.
  - Lúc 09:16 trên đĩa có dòng §2.1 sửa thành "📝Tấn Hiệp: C2 - U1; Thái Hoà: C1 - U2; Phúc Hoàng: C3 - U3", sau đó dòng này mất. Script chỉ ghi lại khối §11 nên đáng ra không đụng §2.1, nhưng em không xác định được dòng đó mất vì đâu. SV kiểm lại editor, nếu mất thì gõ lại.
  - `#196` là lượt hiện tại, đang ghi "không rõ model" vì lượt chưa kết thúc. Sau lần trích log cuối, chạy lại `python tools/forms_hw03.py` để cập nhật số lượt.
- **Cần quyết định:** không có điểm chặn.
```

**Xử lý:** [...]

---

## #197 | 09:16 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
````
Trong lúc chờ Claude Code chạy.

```markdown
## 1. Môi trường và SUT

- SUT: `tkob-team/eshop-sut` @ 📝 (commit) · backend :3000, web :5173 (`--host 127.0.0.1`).
- Nền tảng: P1 Chrome trên Windows · P2 Firefox trên Windows · P3 Chrome Android (POCO F5, `adb reverse tcp:5173` + `tcp:3000`). Phiên bản trình duyệt/OS: 📝
- Không dùng BrowserStack/LambdaTest (M11): 📝 lý do.
- Tài khoản dùng: `test@eshop.com`; backend seed lại mỗi lần khởi động.
```

Phần này mình nhớ là mình có đưa thông tin hết sao mà chưa điền nhỉ
===
GIúp mình kiểm tra trên issues phần này luôn nhé:

```markdown
### 2.1 Phân chia trong nhóm (M4)

📝Tấn Hiệp: C2 - U1; Thái Hoà: C1 - U2; Phúc Hoàng: C3 - U3
```

===
Đợi chút, hay là bạn chỉ kêu tôi duyệt các khối ở 3.2 4.2 5.5 thôi nhỉ?
````

**Output:**
````
Ba câu trả lời:

**3. Không chỉ 3.2, 4.2, 5.5.** Lúc nãy anh chỉ nêu các khối **AI nháp** cần em duyệt. Ngoài ra report còn các dòng 📝 là **chỗ trống chờ dữ kiện**, như §1 và §2.1 em vừa thấy. Trước khi nộp, **mọi 📝 phải hết**. Lệnh anh vừa đưa có bước 5 bắt Claude Code liệt kê đủ mọi 📝 còn lại (file:dòng), để em không phải tự dò.

**1. §1 Môi trường.** Đúng, em đã đưa đủ thông tin; chỉ là khung report viết từ đầu chưa được điền. Đây là dữ kiện nên Claude Code điền được. **Lưu ý:** khung đang ghi *"P1 Chrome trên Windows"* là **sai**: P1 là **Cốc Cốc** (quyết định Q1), Chrome 157 chỉ là lượt auto tham chiếu. Dữ kiện có trong repo:
- SUT: `tkob-team/eshop-sut` @ `de0f48f` (= `85af3ba` + .gitignore). Riêng Task 2 dùng nhánh local `usability-tunnel` @ `e33212d`.
- P1 Cốc Cốc 160 / Win 11 (auto tham chiếu Chrome 157, Playwright 1.48.2) · P2 Firefox 159 / Win 11 (auto Firefox 131 của Playwright) · P3 Chrome Android 156 / POCO F5 / Android 14.
- Không dùng BrowserStack/LambdaTest: trial quá ít (report_plan M11).

**2. §2.1 Phân chia nhóm.** Anh chỉ đối chiếu được một phần qua bản `issues.json` trong repo (chụp tới #224):
- **C3 = nphoang-itus**: khớp, có 21 issue `[HW03-C3-01…23]` (#204–#224).
- **C1**: Claude Code từng thấy issue **#242 `[HW03-C1][FR-08]`** lúc kiểm trùng, nhưng anh không xem được tác giả (snapshot chưa có, API từ chối). Cần kiểm xem tác giả là ai.
- **U1/U2/U3**: issue không cho biết, vì usability thường không có issue. Nguồn là tin nhắn nhóm 04/11 (report_plan M4), em tự xác nhận.
- Report nên ghi kèm tài khoản GitHub để người chấm đối chiếu được, ví dụ `Phúc Hoàng (nphoang-itus): C3 – U3`.

Gửi thêm lệnh nhỏ này cho Claude Code sau lệnh lớn (đừng chen vào giữa lúc nó đang chạy):
```
1. Report §1: điền dữ kiện (không viết thêm ý): SUT tkob-team/eshop-sut @ de0f48f (= 85af3ba + .gitignore), Task 2 nhánh local usability-tunnel @ e33212d; P1 = Cốc Cốc 160 / Windows 11 (lượt auto tham chiếu Chrome 157, Playwright 1.48.2 – Q1), P2 = Firefox 159 / Windows 11 (auto Firefox 131 của Playwright), P3 = Chrome Android 156 / POCO F5 / Android 14; lý do không dùng BrowserStack/LambdaTest lấy nguyên câu ở report_plan M11. Sửa "P1 Chrome" sai. Xoá các 📝 đã điền.
2. §2.1: gh issue list -R tkob-team/eshop-sut --state all --search "HW03-C1 in:title" và "HW03-C3 in:title" → báo tác giả (login) của issue C1, C3. KHÔNG sửa §2.1 (SV tự viết).
Commit `HW03: report §1 môi trường (dữ kiện)`. Báo ≤ 4 dòng + hash.
```

Có tên login của C1 rồi thì em tự viết lại §2.1 kèm login, và xoá 📝.
````

**Xử lý:** [...]

---

## #198 | 09:20 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. Report §1: điền dữ kiện (không viết thêm ý): SUT tkob-team/eshop-sut @ de0f48f (= 85af3ba + .gitignore), Task 2 nhánh local usability-tunnel @ e33212d; P1 = Cốc Cốc 160 / Windows 11 (lượt auto tham chiếu Chrome 157, Playwright 1.48.2 – Q1), P2 = Firefox 159 / Windows 11 (auto Firefox 131 của Playwright), P3 = Chrome Android 156 / POCO F5 / Android 14; lý do không dùng BrowserStack/LambdaTest lấy nguyên câu ở report_plan M11. Sửa "P1 Chrome" sai. Xoá các 📝 đã điền.
2. §2.1: gh issue list -R tkob-team/eshop-sut --state all --search "HW03-C1 in:title" và "HW03-C3 in:title" → báo tác giả (login) của issue C1, C3. KHÔNG sửa §2.1 (SV tự viết).
Commit `HW03: report §1 môi trường (dữ kiện)`. Báo ≤ 4 dòng + hash.
```

**Output:**
```
- Report §1 đã điền dữ kiện theo lệnh, sửa "P1 Chrome" thành Cốc Cốc 160, câu lý do M11 chép nguyên văn từ report_plan, đã bỏ 3 chỗ 📝. Commit `4c3b0b2`.
- Tác giả issue: 19 issue `[HW03-C1]` đều của `henry-banana`; 24 issue `[HW03-C3]` đều của `nphoang-itus` (gồm 3 issue `C3-T2`). Em không sửa §2.1.
- Report còn 2 chỗ xoá nhãn "📝 AI nháp" chưa commit (dòng 49, 301), em không làm nên không commit cùng. `A_prompt_log.md` vừa được hook trích lại, chưa commit.
```

**Xử lý:** [...]

---

## #199 | 09:22 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
response lệnh lớn:
Báo cáo cho phiên thảo luận

- Nhiệm vụ: chuẩn bị Audit + form (bước 1–5).
- Commit:
  - 0c96555 prompt log thêm transcript claude.ai p2.
  - d4fa9e4 AI-02.
  - 47b96b1 AI-03.
  - f33f7d5 §11 + report_plan f/g.
  - bfe1e36 chạy lại script.
  - 3b2f412 thêm HW03/placeholders_left.md (đánh dấu export-ignore, không nộp).
- Prompt log: 196 lượt (Sonnet 4.6: 3, Opus 5.5: 186, không rõ model: 7). --list --commits ghi ra appendix/prompt_log_turns.txt, dùng cùng since/exclude với log nên số #n khớp log.
- AI-02: từ 22 lên 34 artifact (thêm B1–B7, U3–U6, R4; R1/R4 tách phần AI nháp §3.2, §4.2).
  - Cột #n lấy lượt nằm giữa commit liền trước và commit tạo artifact. Nếu khoảng đó rỗng thì lấy lượt cuối trước commit. U6 (đối chiếu pain point) đặt tay #184.
  - Bảng 3.2 rút còn 4 cột: Mã | #n | Verdict | Lý do. Chạy lại script vẫn giữ ô SV đã điền.
- AI-03: số lượt theo dòng Tổng; 7 lượt không rõ model, mỗi lượt một dòng lý do <SV viết> (notes chưa có khoá).
- §11: thêm mục 8–12, mục 12 là dòng CSV có họ tên/SĐT (cho AI-05). report_plan f thêm 6 dòng, g điền dòng "AI tạo bản đầu".
- Kiểm tra: sus_score --check 8 phiếu, 7 phiên tính được, 0 lỗi. report_t1, sus_score --report, summary chạy xong, report/README không đổi. forms_hw03.py chạy lại xong.
- Chỗ trống còn lại: chi tiết từng dòng ở HW03/placeholders_left.md.
  - Report: 34 chỗ. Gồm §1, §2, §5.1–5.4, §6, §7, §9, §11 (2 dòng), §12 tự chấm, phụ lục D, và nhãn 📝 "AI nháp" ở §3.2, §4.2, §11.
  - README:11–15 (tự chấm).
  - AI-02: 34 × 2 ô (dòng 63–111) + §4 (dòng 115).
  - AI-03: dòng 30–36, 41, 45, 51, 57.
  - skills/VideoLinks.md:5–6 (link video).
- Bất thường:
  - HW03/23120255_HW03_Report.md đang có thay đổi chưa commit, không phải em sửa: bỏ nhãn "📝 AI nháp – SV duyệt/sửa" ở §3.2 hoặc §4.2. Em để nguyên, không commit.
  - Lúc 09:16 trên đĩa có dòng §2.1 sửa thành "📝Tấn Hiệp: C2 - U1; Thái Hoà: C1 - U2; Phúc Hoàng: C3 - U3", sau đó dòng này mất. Script chỉ ghi lại khối §11 nên đáng ra không đụng §2.1, nhưng em không xác định được dòng đó mất vì đâu. SV kiểm lại editor, nếu mất thì gõ lại.
  - #196 là lượt hiện tại, đang ghi "không rõ model" vì lượt chưa kết thúc. Sau lần trích log cuối, chạy lại python tools/forms_hw03.py để cập nhật số lượt.
- Cần quyết định: không có điểm chặn.
===
response lệnh nhỏ:
- Report §1 đã điền dữ kiện theo lệnh, sửa "P1 Chrome" thành Cốc Cốc 160, câu lý do M11 chép nguyên văn từ report_plan, đã bỏ 3 chỗ 📝. Commit 4c3b0b2.
- Tác giả issue: 19 issue [HW03-C1] đều của henry-banana; 24 issue [HW03-C3] đều của nphoang-itus (gồm 3 issue C3-T2). Em không sửa §2.1.
- Report còn 2 chỗ xoá nhãn "📝 AI nháp" chưa commit (dòng 49, 301), em không làm nên không commit cùng. A_prompt_log.md vừa được hook trích lại, chưa commit.
===
push rồi nhé
```

**Output:**
````
Đã có đủ dữ kiện. Bây giờ là 09:22, còn **2 giờ 08 phút** tới 11:30.

**Về dòng §2.1 bị mất:** gần như chắc chắn do em đang mở report trong editor đúng lúc script của Claude Code ghi lại file, nên một bên đã đè bên kia. Từ giờ **đừng sửa report trong lúc Claude Code đang chạy script trên report**. Lưu và commit phần của em trước, rồi mới đưa lệnh.

**Em làm ngay (5 phút):**
1. Gõ lại §2.1, kèm login cho người chấm đối chiếu. Theo issue thì C1 = henry-banana, C3 = nphoang-itus, nên Thái Hoà = henry-banana; em xác nhận lại tên. Ví dụ:
   `Tấn Hiệp (ThachHaoo): C2 – U1 · Thái Hoà (henry-banana): C1 – U2 · Phúc Hoàng (nphoang-itus): C3 – U3`
   Xoá 📝 của dòng này.
2. Commit cả phần bỏ nhãn 📝 ở §3.2 và §4.2 em đã làm, cùng prompt log:
```
git add HW03/23120255_HW03_Report.md HW03/appendix/A_prompt_log.md
git commit -m "HW03: SV duyệt §3.2, §4.2, viết §2.1"
git push
```

**Rồi dán cho Claude Code** (việc dữ kiện, trong lúc em làm Audit):
```
Không sửa phần SV, không push. Trước khi ghi report: git status phải sạch (SV đã commit).
1. Report §6: bảng bug BUG-58…85 chép NGUYÊN VĂN từ file BUG (Tiêu đề, Severity, Priority, issue #) nhãn "(AI chép)"; + ảnh trang Issues đã có. Xoá 📝 đã điền.
2. §5.1–5.4, §7, Phụ lục D: điền chỗ 📝 là dữ kiện (trỏ file, số liệu, link VideoLinks) – chỗ nào cần chữ/nhận định SV thì để `<SV viết>`.
3. Liệt kê lại chỗ trống còn lại (placeholders_left.md).
Commit `HW03: report §6 bảng bug (AI chép) + điền dữ kiện`. Báo ≤ 6 dòng + hash.
```

**Sau đó em làm Audit (35 phút):** mở `HW03/ai-forms/AI-02_Audit_Report_23120255.md`, điền 34 hàng. Mỗi hàng gồm:
- **Verdict:** VALID (dùng nguyên) · INVALID (sai, bỏ) · INCOMPLETE (đúng một phần, phải sửa).
- **Lý do:** một câu, khớp với dữ kiện ở cột (5). Ví dụ có commit "SV sửa" thì là INCOMPLETE, kèm số commit.

Sau đó viết §4 kết luận (2–3 câu): khi nào nên và không nên dùng AI.

Lưu ý: **chỉ mở AI-02 khi Claude Code không chạy `forms_hw03.py`**. Lệnh trên không đụng AI-02, nên làm song song được.

**Mốc thời gian:**
- 10:05: xong Audit.
- 10:05–10:20: tự chấm §12 và README, lý do 7 lượt không rõ model (notes), ngày.
- 10:20–10:50: Claude Code xuất transcript lần cuối, form, PDF, AI-05 (em tick và ký), commit log, `hw-submission-audit`, zip.
- 11:00: nộp.

Video: còn dư giờ sau 10:50 thì quay nhanh. Không thì trừ điểm skill.
````

**Xử lý:** [...]

---

## #200 | 09:28 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Không sửa phần SV, không push. Trước khi ghi report: git status phải sạch (SV đã commit).
1. Report §6: bảng bug BUG-58…85 chép NGUYÊN VĂN từ file BUG (Tiêu đề, Severity, Priority, issue #) nhãn "(AI chép)"; + ảnh trang Issues đã có. Xoá 📝 đã điền.
2. §5.1–5.4, §7, Phụ lục D: điền chỗ 📝 là dữ kiện (trỏ file, số liệu, link VideoLinks) – chỗ nào cần chữ/nhận định SV thì để `<SV viết>`.
3. Liệt kê lại chỗ trống còn lại (placeholders_left.md).
Commit `HW03: report §6 bảng bug (AI chép) + điền dữ kiện`. Báo ≤ 6 dòng + hash.
```

**Output:**
```
Đang dựng bảng §6 từ 28 file BUG.

Đã ghi xong, commit `3f96664`, chưa push. Trước khi ghi, working tree chỉ còn `A_prompt_log.md` (hook tự trích lại), em không commit file đó.

- **§6:** bảng 28 bug BUG-58…85, chép nguyên văn Tiêu đề / Severity / Priority / link issue #247–#274, có nhãn "(AI chép)", ảnh trang Issues giữ nguyên. Chỉ đổi cách viết dấu `<`, `>` trong 2 tiêu đề (`<html>`, `<h1>`) thành `&lt;`/`&gt;` để markdown không nuốt thẻ; chữ hiển thị không đổi.
- **§5:**
  - §5.1 và §5.4 cần chữ của SV nên để `<SV viết>`; §5.4 có thêm câu trỏ tới mã P01–P07 và nghề nghiệp trong `S0x.json`.
  - §5.2 thêm `VIP100` (K1) và mốc 06:00; §5.3 ghi SEQ/SUS, 4 câu hỏi mở, Google Form.
  - §5.6 ghi dữ kiện: Meet, `usability_session.ps1`, `moderator_script.md`, đồng ý quay màn hình 8/8 · ghi âm 8/8 · liên hệ 7/8 (S07 không), nền tảng người tham gia.
- **§7:** bảng 2 skill (thư mục, thành phần, trỏ `skills/VideoLinks.md`); phần "Cách dùng" để `<SV viết>`. Link video trong VideoLinks vẫn `<SV điền>`.
- **Phụ lục D:** cây thư mục lấy từ `git ls-files`, bỏ file `export-ignore`, chưa có PDF và `commit_log.txt` nên cần sinh lại sau khi thêm.
- **Chỗ trống còn lại** (chi tiết ở `HW03/placeholders_left.md`): report 24 chỗ, README 6, AI-02 bảng 3.2 + §4, AI-03 12, VideoLinks 2.
```

**Xử lý:** [...]

---

## #201 | 09:30 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đã ghi xong, commit 3f96664, chưa push. Trước khi ghi, working tree chỉ còn A_prompt_log.md (hook tự trích lại), em không commit file đó.

- §6: bảng 28 bug BUG-58…85, chép nguyên văn Tiêu đề / Severity / Priority / link issue #247–#274, có nhãn "(AI chép)", ảnh trang Issues giữ nguyên. Chỉ đổi cách viết dấu <, > trong 2 tiêu đề (<html>, <h1>) thành &lt;/&gt; để markdown không nuốt thẻ; chữ hiển thị không đổi.
- §5:
  - §5.1 và §5.4 cần chữ của SV nên để <SV viết>; §5.4 có thêm câu trỏ tới mã P01–P07 và nghề nghiệp trong S0x.json.
  - §5.2 thêm VIP100 (K1) và mốc 06:00; §5.3 ghi SEQ/SUS, 4 câu hỏi mở, Google Form.
  - §5.6 ghi dữ kiện: Meet, usability_session.ps1, moderator_script.md, đồng ý quay màn hình 8/8 · ghi âm 8/8 · liên hệ 7/8 (S07 không), nền tảng người tham gia.
- §7: bảng 2 skill (thư mục, thành phần, trỏ skills/VideoLinks.md); phần "Cách dùng" để <SV viết>. Link video trong VideoLinks vẫn <SV điền>.
- Phụ lục D: cây thư mục lấy từ git ls-files, bỏ file export-ignore, chưa có PDF và commit_log.txt nên cần sinh lại sau khi thêm.
- Chỗ trống còn lại (chi tiết ở HW03/placeholders_left.md): report 24 chỗ, README 6, AI-02 bảng 3.2 + §4, AI-03 12, VideoLinks 2.

===
xong chưa nhỉ
```

**Output:**
````
Phần của Claude Code đã xong. Còn lại **chỉ phần của em** (khoảng 24 chỗ trong report và form), sau đó là đóng gói. Bây giờ là 09:30, còn 2 giờ.

**Push trước** (`3f96664`) và commit luôn prompt log:
```
git add HW03/appendix/A_prompt_log.md
git commit -m "HW03: cập nhật prompt log"
git push
```

**Việc của em, theo thứ tự (danh sách đủ ở `HW03/placeholders_left.md`)**

| # | Việc | File | Ước |
|---|---|---|---|
| 1 | **Audit:** verdict + lý do 34 hàng, §4 kết luận khi nào nên/không nên dùng AI | `ai-forms/AI-02_…md` | 35' |
| 2 | §5.1 mục tiêu (2–3 câu, có thể dựa plan mục 1–2) | report | 3' |
| 3 | §5.4 bảng 7 người tham gia: mã P01–P07, nghề, IT/non-IT, SĐT **che 4 số giữa**, ngày, đồng ý liên hệ (S07 = Không) | report | 10' |
| 4 | §7 "Cách dùng" 2 skill (vài dòng mỗi skill) | report | 5' |
| 5 | Lý do 7 lượt không rõ model: ghi khoá giờ vào `prompt_log_notes.toml` | notes | 5' |
| 6 | Tự chấm: §12 report + README (Task 1 /30, Task 2 /40, Task 3 /20, Skill /10), tổng = 3 số trong tên zip | report, README | 5' |
| 7 | Video: quay, hoặc ghi rõ "chưa có video" trong VideoLinks và trừ điểm Skill | VideoLinks | 1' / 40' |
| 8 | Duyệt §11 Mandatory Disclosure (đọc, xoá 📝) | report | 3' |

Mỗi việc xong thì commit và push. Nhớ **không sửa report hay form trong lúc Claude Code đang chạy script**.

**Khi em xong cả 8 việc** (dự kiến khoảng 10:40), anh làm 3 việc:
1. Xuất lại transcript `_p2` lần cuối.
2. Đưa lệnh đóng gói cho Claude Code: trích prompt log, `forms_hw03.py`, AI-05 (em tick, ký), PDF (report, AI-02, AI-03, AI-05), commit log, `hw-submission-audit`, `git archive` zip, kiểm danh sách file và dung lượng.
3. Em nộp lên Moodle trước 11:30, mục tiêu 11:15.

Bắt đầu Audit ngay. Gặp hàng nào phân vân verdict thì hỏi anh.
````

**Xử lý:** [...]

---

## #202 | 09:32 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
chỉ viết ai-forms 02 và 03 thôi nhỉ
```

**Output:**
```
Đúng, phần **em viết** chỉ ở AI-02 và AI-03. Bài này cần 3 form:

| Form | Ai làm | Việc của em |
|---|---|---|
| **AI-02 Audit** | Claude Code dựng xong (34 artifact, #n) | Verdict + lý do 34 hàng, §4 kết luận, ký |
| **AI-03 Disclosure** | Claude Code dựng xong (số lượt, model) | 12 chỗ trống: lý do 7 lượt không rõ model, phần cách xác minh và xác nhận, ký |
| **AI-05 Privacy Checklist** | Claude Code dựng **cuối cùng**, sau khi AI-02/03 xong | Tick các mục cam kết cá nhân, ký. Có sẵn dòng minh bạch về CSV họ tên/SĐT |
| AI-04 | Không cần (đề HW03 không yêu cầu) | — |
| AI-06 | Đã nộp tuần 1 | — |

Với **7 lượt không rõ model** ở AI-03: lý do nên ghi vào `prompt_log_notes.toml` theo khoá giờ (giống HW02), để script tự đưa vào log và form. Như vậy khỏi phải gõ hai nơi. Nếu thiếu giờ thì gõ thẳng vào AI-03 cũng được.

Làm AI-02 trước (nặng nhất), rồi AI-03.
```

**Xử lý:** [...]

---

## #203 | 09:44 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
điền xong 2 form rồi commit message gì
```

**Output:**
````
```
git add HW03/ai-forms/AI-02_Audit_Report_23120255.md HW03/ai-forms/AI-03_Disclosure_Form_23120255.md
git commit -m "HW03: SV viết verdict Audit (AI-02) + điền AI-03"
git push
```

Nếu em có ghi lý do 7 lượt vào `prompt_log_notes.toml` thì add thêm file đó vào cùng commit.

Push xong em báo, anh soát nhanh một lượt. Chủ yếu kiểm verdict có khớp cột (5) không: hàng nào có commit "SV sửa" mà ghi VALID là mâu thuẫn. Trong lúc anh soát, em làm tiếp §5.1, §5.4 (bảng người tham gia), §7 và tự chấm.
````

**Xử lý:** [...]

---

## #204 | 09:45 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Push rồi, soát giúp tôi nhé
```

**Output:**
```
Anh đã soát AI-02. Cấu trúc đủ, nhưng có vấn đề lớn: **33/34 hàng ghi VALID**, mâu thuẫn với chính Critique của em và với dữ kiện git. Người chấm sẽ thấy ngay chỗ này. Verdict là của em, anh chỉ chỉ ra chỗ mâu thuẫn dữ kiện:

**Mâu thuẫn giữa VALID và lỗi em đã nêu trong Critique hoặc commit sửa**

| Hàng | Em ghi | Dữ kiện |
|---|---|---|
| **T3** khung `sv_items.md` | VALID, "đúng cấu trúc chuẩn" | Thiếu trường `loai_nguon`, check_checklist báo 12 lỗi (L2). Chính Critique em nêu lỗi này |
| **T5** Playwright | VALID, "chính xác" | Critique em nêu: ép locale vi-VN làm sai CL-08, so toạ độ sai CL-11, TimeoutError ghi nhầm SV-06 P3 |
| **T6** RUN.md | VALID | RUN.md M6 mâu thuẫn chính nó (AI sai, đã sửa) |
| **T2** checklist v1 | VALID | 20 item thuộc "Both" (AI + SV sửa) và 6 item SV bổ sung. Critique em nói v1 thiên lệch SRS |
| **T11** khung bug | VALID | Phải dựng lại theo mẫu HW02 (B2); BUG-80 thiếu P1 |

**Lý do sai dữ kiện**

| Hàng | Câu sai | Đúng là |
|---|---|---|
| **U1** | INVALID, "đã được gỡ bỏ và thay thế" | Plan, kit, phiếu quan sát **vẫn dùng**: form và kịch bản dựng từ kit, plan chỉ sửa mục 3 và 5 cho phiên 10 phút. Không bị bỏ, nên là INCOMPLETE |
| **B4** | "xác nhận các lỗi đã được xử lý triệt để" | B4 kiểm **chữ em sửa trong file bug**, không phải lỗi SUT đã được sửa. SUT không sửa gì |
| **R4** | "SV đã rà soát và điều chỉnh lại câu chữ" | Commit duyệt `eb9c78a` của em **chỉ xoá 2 dòng 📝**, không đổi chữ nào. Ghi "SV duyệt, giữ nguyên" thì VALID mới đúng |
| **S2** | "quy trình 6 thành phần của Rubin & Chisnell" | Skill dùng kế hoạch **9 phần** (Rubin & Chisnell, slide) |
| **T5, B3, B1** | "theo tiêu chí ISTQB Test Automation", "Repeatability của ISTQB", "Bug Triage" | Chỉ giữ nếu em chỉ ra được mục cụ thể trong tài liệu ISTQB của môn. Không chắc thì bỏ tên tiêu chuẩn |

**§4 Kết luận:** "hoàn toàn thiếu vắng WCAG" là quá mức, vì v1 có dùng WCAG cho `lang`, `title`, nhãn (CL-13, CL-14, CL-38). Viết "thiếu các tiêu chí WCAG về tương phản, focus, kích thước vùng bấm" là đúng.

**Gợi ý nguyên tắc chọn verdict** (em tự áp dụng):
- **VALID:** dùng nguyên, không có commit sửa vì lỗi của AI.
- **INCOMPLETE:** dùng được nhưng phải sửa. Cột (5) có commit sửa, hoặc Critique có nêu lỗi.
- **INVALID:** bỏ hẳn.

Sửa xong 5–8 hàng này mất khoảng 10 phút. Commit `HW03: SV sửa verdict Audit theo kiểm dữ kiện`, push. Rồi làm §5.1, §5.4, §7, tự chấm. Bây giờ là 09:47.
```

**Xử lý:** [...]

---

## #205 | 09:54 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đã viết lại rồi, kiểm tra cũng như đã viết xong 5.1 và 5.4 rồi nhé. Push hết rồi
```

**Output:**
```
Audit đã ổn: 26 VALID / 8 INCOMPLETE, các hàng mâu thuẫn đều đã sửa đúng dữ kiện. §5.1 cũng ổn, bám đúng plan mục 1–3.

**§5.4 có lỗi nghiêm trọng, phải sửa ngay: cột SĐT không khớp số thật.** Anh đối chiếu với CSV form (file em gửi lúc 00:43): **không số nào khớp**. Các số trong bảng có dạng `…456`, `…789`, `…321`, `…654`, `…987`, trông như số mẫu. Đề nói TA **gọi ngẫu nhiên 2 người để xác minh**, và *"Impersonation results in 0 points for Task 2"*. Số sai thì TA không liên lạc được, mất trắng Task 2.

Số đúng (đã che 4 số giữa, lấy từ CSV):

| Phiên | SĐT che |
|---|---|
| S01 | `091****280` |
| S02 | `035****689` |
| S03 | `079****218` |
| S04 | `091****230` |
| S05 | `097****074` |
| S06 | `036****273` |
| S07 | `086****517` |

(S00 pilot: `039****875`, nếu em muốn liệt kê pilot riêng.)

**Bổ sung khác cho §5.4**
- Thêm cột **"Đồng ý TA liên hệ"**: S07 = **Không**, các phiên khác = Có. TA cần biết để không gọi S07.
- Nghề và trình duyệt khớp với JSON. Riêng S07 ghi nghề là "IT", hơi chung; nếu biết cụ thể hơn thì ghi.
- Trường `nhom` trong JSON đang **trống** (null), trong khi bảng đã có IT/Non-IT. Bảo Claude Code chép `nhom` từ bảng §5.4 vào JSON rồi chạy lại `--report`, để bảng U1 tách được IT/non-IT. Không bắt buộc, nhưng chỉ mất 1 phút.

**AI-02 §4 Kết luận:** câu "hoàn toàn thiếu vắng các tiêu chuẩn khả năng truy cập" vẫn còn. Đổi thành "thiếu các tiêu chí WCAG về tương phản, focus, kích thước vùng bấm", vì v1 có dùng WCAG cho `lang`, `title`, nhãn.

Sửa 2 chỗ trên, commit `HW03: SV sửa SĐT bảng người tham gia + kết luận Audit`, push. Rồi làm §7 "Cách dùng" và tự chấm. Bây giờ là 09:56, mốc kế tiếp là 10:15 bắt đầu đóng gói.
```

**Xử lý:** [...]

---

## #206 | 09:59 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Mình đã sửa xong rồi, push rồi. 5.4 vậy mình đánh giá là xong rồi đấy (nếu bạn cần thêm cột nào khác)
```

**Output:**
```
§5.4 xong, đủ cột: SĐT khớp CSV, có cột đồng ý liên hệ (S07 = Không). Kết luận Audit cũng đã sửa.

Còn lại **3 việc của em**, sau đó là đóng gói:

1. **§7 "Cách dùng"** 2 skill: vài dòng mỗi skill (gọi thế nào, chạy bước nào, ra file gì).
2. **Video:** quay hay bỏ? Bây giờ là 10:00, quay một bản 10 phút cộng upload vẫn kịp nếu bắt đầu ngay sau bước 3. Nếu bỏ, ghi trong `skills/VideoLinks.md` câu "Chưa có video demo (không kịp thời gian)" và tự chấm Skill tương ứng.
3. **Tự chấm** ở §12 report và README: Task 1 /30, Task 2 /40, Task 3 /20, Skill /10. Mỗi mục kèm 1 dòng căn cứ. Tổng phải bằng 3 số trong tên zip.

Commit `HW03: SV viết §7, tự chấm`, push, rồi **báo anh tổng điểm**. Anh sẽ xuất transcript `_p2` lần cuối và đưa lệnh đóng gói (AI-05, PDF, commit log, `hw-submission-audit`, zip `23120255_HW03_AI_GUIUsability_<điểm>.zip`).
```

**Xử lý:** [...]

---

## #207 | 10:00 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
````
```markdown
## 7. Agent Skill

| Skill | Thư mục | Thành phần | Video |
|---|---|---|---|
| `gui-checklist-testing` | `skills/gui-checklist-testing/` | SKILL.md, 1 reference, 3 asset, 8 script | `skills/VideoLinks.md` |
| `usability-evaluation` | `skills/usability-evaluation/` | SKILL.md, 2 reference, 3 asset, 6 script | `skills/VideoLinks.md` |

Cách dùng: `<SV viết>`

```

===
Ủa phần này bạn hỗ trợ mình viết được mà nhỉ. Chỉ có video là bắt buộc mình xíu nữa phải tự demo thôi
````

**Output:**
````
Đúng, phần này anh viết nháp được: nó chỉ mô tả cách gọi skill, lấy từ SKILL.md, không thuộc phần cấm. Anh gắn nhãn 📝 để em duyệt và khai trong Audit/§11. Em dán thay dòng `Cách dùng: <SV viết>`:

```markdown
📝 AI nháp – SV duyệt/sửa

**Cách dùng**

Cả hai skill chạy trong Claude Code, **mỗi lần gọi làm một bước rồi dừng** để em review và commit. Output AI của từng bước được đóng băng (`scripts/freeze.py`) trước khi em sửa. Quy định môn học (AI-01, `CLAUDE.md`) thắng skill khi mâu thuẫn.

- **`gui-checklist-testing`** – gọi `/gui-checklist-testing <thư-mục-checklist> <bước>` (vd `HW03/checklist 1`). Toàn bộ dữ liệu của một phạm vi nằm trong một file `checklist.json`; bảng Markdown, Excel, danh sách Failed, nhóm bug đều sinh từ file này.
  - Bước 0 khảo sát control và điều khoản UI → `<scope>_inventory.md`.
  - Bước 1 AI nháp checklist từ 3 nguồn (đặc tả UI, checklist theo control, heuristic Nielsen/Norman/Shneiderman/WCAG); mỗi item có Expected quan sát được, có ngưỡng "Fail nếu…".
  - Bước 2 SV bổ sung item (AI không gợi ý, chỉ dựng khung trống) → AI trả lời vì sao bỏ sót.
  - Bước 3 phân loại item auto / manual / mixed, sinh `RUN.md`, `dom_probe.js` (tuỳ chọn Playwright, oracle khoá theo sha1 của Expected).
  - Bước 4 chạy từng nền tảng, gộp bằng `merge_runs.py` (verdict chính thức = lượt chạy tay).
  - Bước 5–6 Excel + test summary (`build_excel.py`), danh sách Failed, gom nhóm bug (`failed_list.py`, `bug_groups.py`) – SV viết bug.
- **`usability-evaluation`** – gọi `/usability-evaluation <thư-mục> <bước>` (vd `HW03/usability 4`).
  - Bước 0 kế hoạch 9 phần (Rubin & Chisnell, slide) → `plan.md`; bước 1 participant kit + phiếu quan sát (`check_kit.py`).
  - Bước 2 pilot (`S00`) → `kit_diff.py` ghi thay đổi, SV ghi lý do.
  - Bước 3 mỗi phiên `new_session.py` tạo khung JSON trống, SV nhập (mã ẩn danh P0x, không SĐT/email).
  - Bước 4 `sus_score.py --check` / `--report` tính SUS, SEQ, tỉ lệ hoàn thành, thời gian vào marker report.
  - Bước 5–6 khung findings và gom dữ kiện bug (`bug_facts.py`) – SV viết findings và bug.

Trong HW03, skill `gui-checklist-testing` được dùng cho toàn bộ Task 1 và Task 3 (C2, 3 nền tảng); `usability-evaluation` cho Task 2 (pilot S00 + 7 phiên S01–S07).
```

Một điểm cần biết khi em duyệt: skill `usability-evaluation` quy định **AI không điền JSON phiên** và **không đưa dữ liệu cá nhân cho AI**. Ở bài này cả hai đã xảy ra: Claude Code chép số từ CSV vào JSON, và em gửi CSV lên phiên thảo luận. Cả hai đã được khai ở report_plan f/g và §11, nên không cần sửa §7. Chỉ cần đúng là em biết, phòng khi vấn đáp.

Dán xong em sửa câu chữ nếu muốn, xoá dòng 📝, rồi làm tự chấm. Khi giao lệnh đóng gói, anh sẽ nhắc Claude Code thêm vào Audit và §11 một dòng "AI nháp §7 Cách dùng".
````

**Xử lý:** [...]

---

## #208 | 10:02 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
duyệt oke rồi, commit sao đây
```

**Output:**
````
```
git add HW03/23120255_HW03_Report.md
git commit -m "HW03: §7 cách dùng skill (AI nháp, SV duyệt)"
git push
```

Tiếp theo là **tự chấm** ở §12 report và README, mỗi mục kèm 1 dòng căn cứ:

| Mục | Tối đa | Căn cứ để em tự cân |
|---|---|---|
| Task 1 – GUI checklist | 30 | 74 item, 3 nền tảng, Excel, 28 bug + 28 issue, ảnh trang Issues, §3.4 |
| Task 2 – Usability | 40 | Plan 9 phần, kit, pilot S00, 7 phiên, SUS/SEQ, findings có severity, bảng người tham gia. **Chưa có:** mốc thời gian đo thật (ước theo trí nhớ, nếu đúng vậy), chưa lập bug Task 2 |
| Task 3 – Cross-platform | 20 | 3 nền tảng thật, ảnh overlay đủ, bảng khác biệt |
| Skill + video | 10 | 2 skill tự đủ. **Video:** quay được thì tính, không thì trừ phần video |

Tổng là 3 số trong tên zip. Điểm của em, em tự quyết; anh chỉ nhắc là phần nào có chỗ thiếu thì trừ tương ứng, cho trung thực.

Viết xong commit `HW03: SV tự chấm`, push, rồi báo anh **tổng điểm** và **có quay video không**. Anh đưa lệnh đóng gói ngay.
````

**Xử lý:** [...]

---

## #209 | 10:08 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
push rồi nhé. Vì mình dự định sẽ quay video nên chấm trước đó luôn nhé
```

**Output:**
````
Anh đã đọc §12 và README. Điểm là quyền của em, anh chỉ soát dữ kiện trong cột căn cứ:

**Sai dữ kiện ở README, cần sửa**
- Task 1: "74 item (65 item nháp v1 + 6 item SV bổ sung + cấu trúc chuẩn)". 65 + 6 = 71, không ra 74. Dữ kiện đúng: **74 item = AI 48 · Both 20 · SV 6**, bản v1 có 65 item.
- Task 1: "đối chiếu **137 item Failed**". 137 là số **ô** Failed (item × nền tảng); số item Failed là **47**. Từ đó ra 14 trùng, 4 trùng một phần, 28 bug mới.
- Task 2: "kịch bản 9 phần" → **kế hoạch** 9 phần (`plan.md`). Kịch bản là nhiệm vụ U1.
- Dòng đầu README: "Công cụ AI: 📝" còn trống. Ghi: Claude (Opus 5.5, Sonnet 4.6) qua claude.ai và Claude Code.

**Report §12:** xoá dòng "📝 (đồng bộ với README)", và điền tên zip `23120255_HW03_AI_GUIUsability_094.zip`.

**Lưu ý trung thực:**
- Skill 9/10 chỉ đúng **nếu có video**. Không kịp quay thì phải hạ điểm Skill và **đổi tên zip** cho khớp.
- Task 2 38/40: phần đề chấm có "analysis". Bài có findings, nhưng chưa lập bug cho các pain point chưa có issue. Mốc thời gian thì ước theo trí nhớ (nếu đúng như vậy). Em cân nhắc lại cho khớp căn cứ.

Sửa xong commit `HW03: SV sửa căn cứ tự chấm`, push.

**Kế hoạch còn lại (bây giờ 10:10, deadline 11:30):**

| Giờ | Em | Claude Code |
|---|---|---|
| 10:15–10:50 | Quay video (giọng em), upload YouTube Unlisted | Chuẩn bị đóng gói (lệnh dưới) |
| 10:50 | Dán link vào `VideoLinks.md` + §7 + README, commit, push | |
| 10:55 | | Anh xuất transcript lần cuối → trích log → form → PDF → zip |
| 11:05 | Kiểm zip, ký PDF (nếu cần) | |
| 11:15 | **Nộp** | |

**Video:** chạy lại các bước AI từ đầu sẽ không kịp. Nên quay bản **walkthrough cách em đã dùng 2 skill**, khoảng 8 phút:
- Mỗi skill: mở SKILL.md và nói các bước.
- Chỉ commit từng bước trong git log (`HW03[T1] 1/6…`, `HW03[T2] k/10…`).
- Chạy thật vài script nhanh: `check_checklist.py`, `merge_runs.py --help`, `sus_score.py --check` / `--report`.
- Mở output: Excel, report.

Video nói đúng là "cách em đã dùng skill trong bài", không phải chạy mới. Không quay token, mật khẩu hay CSV có SĐT.

**Lệnh chuẩn bị đóng gói cho Claude Code** (dán ngay, chạy trong lúc em quay):
```
NHIỆM VỤ: chuẩn bị đóng gói HW03 (chưa zip). Không push, không amend, KHÔNG sửa phần SV.
1. report_plan f + §11 + AI-02: thêm artifact "AI nháp report §7 Cách dùng skill (phiên thảo luận 10:00 11/11)" (verdict/lý do <SV viết>).
2. Dựng AI-05 (mẫu HW02/ai-forms, không chép số liệu): tick mục có bằng chứng; mục cam kết cá nhân để [ ] "(em tự xác nhận)"; dòng minh bạch CSV họ tên/SĐT gửi phiên thảo luận 00:43 11/11; số lượt AI = dòng Tổng prompt log.
3. Kiểm placeholders_left: liệt kê mọi 📝 / <SV viết> / <SV điền> / [...] còn lại (file:dòng).
4. Chạy thử: pandoc/xuất PDF cho report, AI-02, AI-03, AI-05 vào HW03/ (đúng tên đề); git archive thử → đo dung lượng + liệt kê file trong zip (không có report_plan, CLAUDE.md, evidence_raw, placeholders_left, demo_plan, CSV).
Commit từng việc. Báo ≤ 10 dòng + hash + danh sách chỗ trống còn lại.
```
````

**Xử lý:** [...]

---

## #210 | 10:13 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Mình đã sửa và push lại README cùng với report. Bạn kiểm tra xem oke chưa nhé
```

**Output:**
```
Ổn rồi. README và §12 khớp nhau: 28 + 35 + 19 + 9 = **91**, tên zip `…_091.zip` đúng. Căn cứ đã đúng dữ kiện (74 = 48 + 20 + 6; 47 item Failed; kế hoạch 9 phần), dòng công cụ AI đã điền.

Còn một lỗi định dạng nhỏ: dòng Task 2 trong README **thiếu dấu `|` ở cuối** (và dấu chấm). Đa số trình xem vẫn hiển thị được, nhưng thêm vào cho chắc, sửa lúc nào commit tiếp cũng được.

Điều kiện còn treo: **Skill 9/10 chỉ đúng nếu có video.** Không kịp quay thì hạ Skill, đổi tổng và tên zip ở cả README lẫn §12.

Giờ em **quay video** ngay. Đừng quên dán lệnh chuẩn bị đóng gói cho Claude Code trước khi quay, để nó chạy song song. Upload xong, dán link vào `skills/VideoLinks.md`, commit, push, rồi báo anh. Mốc chậm nhất là **10:50**.
```

**Xử lý:** [...]

---

## #211 | 10:14 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Phải quay 2 video demo 2 skill nhỉ.
```

**Output:**
```
Nên quay **2 video ngắn, mỗi skill một video, khoảng 4–5 phút**. Lý do:
- Đề viết "demonstration **videos**" và yêu cầu mỗi video cho thấy "end to end" cách dùng skill.
- `VideoLinks.md` đã có sẵn 2 dòng.

Tổng thời gian không hơn một video dài. Nếu gấp quá, quay **1 video có 2 phần**, ghi mốc thời gian cho từng skill trong mô tả YouTube, và dán cùng link vào cả 2 dòng kèm mốc (`?t=…`).

**Ý chính mỗi video** (em tự nói bằng lời của em):

**Video 1: `gui-checklist-testing`** (C2, Task 1 + 3)
1. Mở `HW03/skills/gui-checklist-testing/SKILL.md`: mục đích và 6 bước, mỗi lần gọi một bước rồi dừng.
2. `git log --oneline --grep "HW03\[T1\]"`: cho thấy mỗi bước một commit.
3. Bước 1–2: mở bản đóng băng v1 trong `appendix/ai-outputs/` và `sv_items.md` (6 item em tự thêm).
4. Bước 3–4: `RUN.md`, thư mục ảnh 3 nền tảng, chạy thật `python HW03/skills/gui-checklist-testing/scripts/check_checklist.py …`.
5. Bước 5–6: mở Excel, `failed_list.md`, một file BUG và issue tương ứng trên GitHub.

**Video 2: `usability-evaluation`** (U1, Task 2)
1. Mở SKILL.md: kế hoạch 9 phần, giới hạn AI (không điền phiếu, không dữ liệu cá nhân).
2. `plan.md`, `participant_kit.md`, `moderator_script.md`.
3. Chạy thật `new_session.py` (tạo khung S99 rồi xoá, không commit) để thấy khung trống.
4. Mở một `S0x.json` (mã P0x, không SĐT); chạy `sus_score.py HW03/usability/sessions --check` và `--report`.
5. Mở report §5.7–5.9: số liệu do script tính, findings do em viết.

**Lưu ý khi quay:**
- Không mở CSV form, tab Responses của Google Form, hay bảng có SĐT đầy đủ.
- Không quay token hay đường dẫn có tên người dùng nếu tránh được.
- Tải lên YouTube ở chế độ **Unlisted**.
```

**Xử lý:** [...]

---

## #212 | 10:16 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Giờ tôi muốn bạn giúp tôi lên kịch bản cả 2 video. Bật gì và nói gì.
Tôi định sử dụng mỗi Claude Opus 5.5 Medium mới hẳn (tức là mở session) ở cả 2 video nhé
```

**Output:**
````
Lưu ý trước: theo AI-01, **giọng thuyết minh phải là của em**, nên anh không viết lời thoại. Anh đưa bảng thời gian, việc cần bật, lệnh gõ vào Claude Code và **ý chính** từng đoạn; em tự nói bằng lời của mình.

---

## Chuẩn bị chung (5 phút, chưa quay)

1. Mở PowerShell tại repo, tạo nhánh tạm để demo không lẫn vào bài nộp:
   ```
   git switch -c demo-video
   ```
2. Đóng mọi cửa sổ có CSV, Google Form Responses, Gmail, mật khẩu.
3. Bật sẵn: VS Code mở repo, trình duyệt có tab GitHub Issues đã lọc `"HW03-C2" author:ThachHaoo`, Excel `23120255_HW03_Checklist.xlsx`.
4. Quay bằng **Win + Alt + R** (Game Bar), có micro.
5. Mỗi video mở **một session Claude Code mới**, chọn Opus 5.5 (Medium).

---

## Video 1: `gui-checklist-testing` (~6 phút)

Ý tưởng: **chạy thật bước 0–1 trên một màn nhỏ ngoài C2** (Đăng ký `/register`) để thấy skill hoạt động, rồi dùng các bước 2–6 đã làm trên C2 để cho thấy trọn quy trình.

| Mốc | Bật / làm gì | Ý chính em nói |
|---|---|---|
| 0:00 | VS Code mở `HW03/skills/gui-checklist-testing/SKILL.md` | Skill dùng để làm gì; 3 nguồn checklist (đặc tả UI, theo control, heuristic); mỗi lần gọi một bước rồi dừng để người review; quy tắc AI không gợi ý ở bước 2 |
| 0:45 | Session Claude Code mới, gõ **lệnh 1** (dưới) | Demo trên màn khác C2 để thấy skill dùng lại được |
| 1:30 | Mở `HW03/demo/register/register_inventory.md` vừa sinh | Bước 0: AI khảo sát control thật từ code, có file:dòng, không bịa |
| 2:00 | Gõ **lệnh 2** | Bước 1: sinh nháp theo 3 nguồn, có ngưỡng "Fail nếu…" |
| 3:00 | Mở `checklist.md` vừa sinh, chỉ 1–2 item; chỉ dòng `check_checklist` báo 0 lỗi, thư mục đóng băng | Expected lấy từ đặc tả chứ không lấy từ hành vi hiện tại; output được đóng băng trước khi người sửa |
| 3:30 | Chuyển sang bài thật: `git log --oneline --grep "HW03\[T1\]"` | Trong bài, mỗi bước là một commit |
| 4:00 | Mở `HW03/checklist/sv_items.md` | Bước 2: em tự bổ sung 6 item, sau đó mới hỏi AI vì sao bỏ sót |
| 4:20 | Mở `RUN.md`, thư mục `evidence/P1_chrome`, `P2_firefox`, `P3_android` | Bước 3–4: chạy 3 nền tảng, auto + tay, verdict chính thức là lượt tay |
| 5:00 | Mở Excel, rồi `failed_list.md`, rồi 1 file `BUG-xx.md`, rồi tab GitHub Issues | Bước 5–6: Excel và test summary; nhóm bug do skill gom, **bug do em viết**, issue tạo từ file của em |
| 5:45 | Kết | Tóm 1 câu: skill làm gì, phần nào người làm |

**Lệnh 1:**
```
/gui-checklist-testing HW03/demo/register 0
Phạm vi demo: chỉ màn Đăng ký web (/register) của ../eshop-sut. Đây là demo video trên nhánh demo-video: freeze vào HW03/demo/ai-outputs (KHÔNG vào appendix/ai-outputs), không commit.
```

**Lệnh 2:**
```
/gui-checklist-testing HW03/demo/register 1
Demo: tối thiểu 8 item, đủ IA-01…IA-04 nếu có. Chạy render → freeze (HW03/demo/ai-outputs) → check_checklist. Không commit.
```

Nếu AI chạy quá 2 phút thì em **tạm dừng quay** (Win + Alt + R), chạy xong mới quay tiếp.

---

## Video 2: `usability-evaluation` (~5 phút)

Ý tưởng: **chạy thật bước 3 (tạo khung phiên) và bước 4 (tính số liệu)** trên dữ liệu thật của U1, còn bước 0–2 và 5 cho xem kết quả đã làm.

| Mốc | Bật / làm gì | Ý chính em nói |
|---|---|---|
| 0:00 | VS Code mở `HW03/skills/usability-evaluation/SKILL.md` | Usability test moderated, kế hoạch 9 phần theo slide; **giới hạn AI**: không điền phiếu, không viết findings, không nhận dữ liệu cá nhân |
| 0:45 | Mở `usability/plan.md`, `participant_kit.md`, `moderator_script.md` | Bước 0–1: AI nháp, em chốt; nhiệm vụ chỉ nêu mục tiêu, không nêu bước |
| 1:30 | Session Claude Code mới, gõ **lệnh 3** | Bước 3: trước mỗi phiên, script tạo khung trống |
| 2:00 | Mở `S99.json` vừa tạo (mọi giá trị null), rồi mở `S04.json` thật | Khung trống so với phiếu thật; chỉ có mã P0x, không SĐT |
| 2:45 | Gõ **lệnh 4** | Bước 4: script kiểm phiếu và tính SUS, SEQ, tỉ lệ hoàn thành |
| 3:30 | Mở report §5.7 (bảng U1) | SUS 77,9, SEQ 6,3; 7/7 hoàn thành; số do script tính, không gõ tay |
| 4:00 | Mở report §5.8–5.9 | Bước 5: findings do **em** viết, gom pain point và severity, đối chiếu issue |
| 4:40 | Kết | Tóm 1 câu |

**Lệnh 3:**
```
/usability-evaluation HW03/usability 3
Demo video (nhánh demo-video): chỉ chạy new_session.py tạo khung HW03/usability/sessions/S99.json để minh hoạ, không điền gì, không commit.
```

**Lệnh 4:**
```
/usability-evaluation HW03/usability 4
Demo video: bỏ qua S99 (xoá file S99.json trước), chạy sus_score.py --check rồi --report vào marker REPORT:U1, báo kết quả. Không commit.
```

---

## Sau khi quay (3 phút)

```
git restore .
git clean -fd HW03/demo HW03/usability/sessions/S99.json
git switch main
git branch -D demo-video
```

- Upload 2 video lên YouTube, chế độ **Unlisted**. Tiêu đề gợi ý: `23120255 HW03 – Demo skill gui-checklist-testing` và `… usability-evaluation`.
- Dán 2 link vào `skills/VideoLinks.md`; thêm vào §7 report và README nếu có chỗ.
- Commit `HW03[Skill] 3/3: link video demo`, push, báo anh.
- Các lượt demo vẫn vào prompt log (D2 = a), không cần làm gì thêm: lần trích log cuối sẽ tự lấy.
````

**Xử lý:** [...]

---

## #213 | 10:22 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Skill có bước 0 đến bước 6. mà chỉ chạy bước 0 và 1 thôi sao? Vậy sao gọi là demo end to end skill nhỉ
```

**Output:**
```
Em nói đúng: chạy bước 0–1 rồi chiếu các bước 2–6 từ bài cũ là **walkthrough**, không hẳn là "end to end". Anh nói thẳng cái được và mất của từng cách:

| Cách | Làm gì | Thời gian | Rủi ro |
|---|---|---|---|
| **A. Nửa chạy, nửa chiếu** (kịch bản lúc nãy) | Chạy thật 0–1; bước 2–6 chiếu kết quả C2 đã làm | ~25' cả 2 video | Người chấm có thể cho là chưa end to end |
| **B. Chạy thật đủ 0–6, phạm vi rất nhỏ** | Một màn (`/register`), khoảng 8 item, **1 nền tảng**, mỗi bước gọi skill thật; tạm dừng quay khi AI đang chạy | ~35–40' cả 2 video | Sát giờ: xong khoảng 11:00, còn khoảng 25' đóng gói và nộp |

Còn 68 phút. Anh khuyên chọn **B**: đề chấm đúng điểm này, và nếu vấn đáp thì em cũng nói được là đã chạy thật. Điều kiện là **chốt cứng 11:00**: tới giờ đó, video nào chưa xong thì dừng ở bước đang làm, nói rõ trong video là dừng ở bước nào, và trừ điểm tương ứng.

---

## Video 1 (B): `gui-checklist-testing` trên `/register`, 1 nền tảng P1

Mọi lệnh đều thêm câu: *"Demo video trên nhánh demo-video, freeze vào HW03/demo/ai-outputs, không commit."*

| Bước | Lệnh | Em làm / nói ý chính |
|---|---|---|
| 0 | `/gui-checklist-testing HW03/demo/register 0` (phạm vi: màn Đăng ký web, nền tảng P1) | Khảo sát control có file:dòng |
| 1 | `… 1` (tối thiểu 8 item) | 3 nguồn, Expected có ngưỡng, freeze |
| 2 | **Em** gõ thêm 1 item vào `sv_items.md` (khung AI dựng), rồi gọi `… 2` | AI không gợi ý; sau đó hỏi "vì sao bỏ sót" |
| 3 | `… 3` (chỉ chế độ tay, không Playwright) | Phân loại auto/manual, `RUN.md`, `dom_probe.js` |
| 4 | **Em** chạy tay 3–4 item trên Cốc Cốc (dán `dom_probe.js` vào Console), ghi file lượt; gọi `… 4` | Verdict chính thức là lượt tay |
| 5 | `… 5` | Excel và test summary sinh từ JSON |
| 6 | `… 6` | Danh sách Failed và nhóm bug; nói rõ **bug do em viết**, không quay phần viết |

## Video 2 (B): `usability-evaluation` trên một thư mục demo

| Bước | Lệnh | Em làm / nói ý chính |
|---|---|---|
| 0 | `/usability-evaluation HW03/demo/usability 0` (flow U1 thu nhỏ) | Kế hoạch 9 phần, nhiệm vụ dạng mục tiêu |
| 1 | `… 1` | Participant kit, `check_kit` |
| 2 | Em sửa 1 dòng kit; gọi `… 2` | `kit_diff`: em ghi lý do, AI không suy diễn |
| 3 | `… 3` tạo `S01` | Khung trống. Để có số mà demo, **chép `HW03/usability/sessions/S01.json` thật vào thư mục demo**; không bịa dữ liệu |
| 4 | `… 4` | SUS, SEQ, tỉ lệ hoàn thành tính bằng script |
| 5–6 | `… 5`, `… 6` | Khung findings trống và gom dữ kiện bug; nói: **findings và bug do em viết** (chỉ ra §5.8–5.9 thật) |

---

**Mẹo giữ giờ:**
- AI chạy lâu thì **tạm dừng quay** (Win + Alt + R), xong mới quay tiếp.
- Mỗi bước nói 15–20 giây là đủ.
- Bước 4 của video 1 chỉ chạy 3–4 item, không chụp ảnh. Nói rõ là demo.

Dọn dẹp sau khi quay, upload và commit link: làm như lúc nãy. Mốc **11:00** là phải có link trong repo; nếu không, nộp với điểm Skill đã hạ.
```

**Xử lý:** [...]

---

## #214 | 10:23 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Gửi cho mình cả quy trình giống như lúc nãy nhé
```

**Output:**
````
Toàn bộ quy trình quay 2 video theo cách B (chạy thật đủ bước 0–6 trên phạm vi nhỏ). Lời thuyết minh là của em; anh chỉ ghi ý chính.

---

## 0. Chuẩn bị (5 phút, chưa quay)

1. PowerShell tại repo:
   ```
   git status --short        # phải sạch; còn A_prompt_log.md thì commit trước
   git switch -c demo-video
   ```
2. Backend + web chạy được cho màn `/register` trên Cốc Cốc. SUT đang ở nhánh `usability-tunnel`, giao diện giống main nên dùng được:
   ```
   powershell -ExecutionPolicy Bypass -File tools\restart_backend.ps1
   ```
   Web: `npm run dev -- --host 127.0.0.1` trong `..\eshop-sut\frontend-web` nếu chưa chạy.
3. Đóng mọi cửa sổ có CSV, Google Form Responses, Gmail, mật khẩu, token.
4. Mở sẵn: VS Code (repo), Cốc Cốc tab `http://localhost:5173/register`, Excel.
5. Quay bằng **Win + Alt + R**, có micro. **AI chạy lâu thì tạm dừng quay.**
6. Mỗi video mở **session Claude Code mới**, chọn **Opus 5.5 – Medium**.

**Câu thêm vào cuối mọi lệnh** (gọi là [DEMO]):
```
Demo video trên nhánh demo-video: freeze vào HW03/demo/ai-outputs (KHÔNG appendix/ai-outputs), không commit, không push.
```

---

## 1. Video 1: `gui-checklist-testing` (khoảng 15 phút thực, khoảng 7 phút sau khi cắt)

| Mốc | Lệnh / thao tác | Ý chính em nói |
|---|---|---|
| Mở đầu | Mở `HW03/skills/gui-checklist-testing/SKILL.md` | Skill làm gì; 3 nguồn; mỗi lần một bước rồi dừng; phần AI không được làm |
| **Bước 0** | `/gui-checklist-testing HW03/demo/register 0` + "Phạm vi: chỉ màn Đăng ký web /register của ../eshop-sut, nền tảng chỉ P1 (Cốc Cốc / Windows 11)." + [DEMO] → mở `register_inventory.md` | Control lấy từ code thật, có file:dòng |
| **Bước 1** | `/gui-checklist-testing HW03/demo/register 1` + "Tối thiểu 8 item." + [DEMO] → mở `checklist.md` | 3 nguồn; Expected có ngưỡng "Fail nếu…", lấy từ đặc tả, không lấy từ hành vi SUT; đã đóng băng |
| **Bước 2** | `/gui-checklist-testing HW03/demo/register 2` + "Chỉ dựng khung trống sv_items.md." + [DEMO] → **em tự gõ 1 item** vào khung → gọi lại `… 2` + "SV đã điền 1 item; kiểm cấu trúc, chép vào JSON, trả lời vì sao AI bỏ sót." + [DEMO] | AI không gợi ý; em thêm trước rồi mới hỏi AI |
| **Bước 3** | `/gui-checklist-testing HW03/demo/register 3` + "Chỉ chế độ tay, không Playwright." + [DEMO] → mở `RUN.md` | Phân loại item; quy tắc ảnh; `dom_probe.js` |
| **Bước 4** | Cốc Cốc → F12 → Console → dán `dom_probe.js` → em chấm **3–4 item**, ghi file lượt `runs/P1_manual_demo.md` theo mẫu trong RUN.md (bảng `ID | status | notes | ảnh`) → `/gui-checklist-testing HW03/demo/register 4` + "Gộp lượt tay P1 vừa ghi; demo nên bỏ yêu cầu ảnh." + [DEMO] | Verdict chính thức là lượt tay; dom_probe chỉ là dữ kiện, người chấm Pass/Fail |
| **Bước 5** | `/gui-checklist-testing HW03/demo/register 5` + [DEMO] → mở Excel vừa sinh | Excel và test summary sinh từ JSON, có công thức |
| **Bước 6** | `/gui-checklist-testing HW03/demo/register 6` + [DEMO] → mở danh sách Failed / nhóm bug | Skill gom dữ kiện; **bug do em viết** (chiếu 1 file BUG thật + issue GitHub của C2) |
| Kết | — | Tóm 1 câu: skill lo phần nào, em lo phần nào |

---

## 2. Video 2: `usability-evaluation` (khoảng 12 phút thực, khoảng 6 phút sau khi cắt)

| Mốc | Lệnh / thao tác | Ý chính em nói |
|---|---|---|
| Mở đầu | Mở `HW03/skills/usability-evaluation/SKILL.md` | Moderated usability test; kế hoạch 9 phần; giới hạn AI (không điền phiếu, không findings, không dữ liệu cá nhân) |
| **Bước 0** | `/usability-evaluation HW03/demo/usability 0` + "Flow: đăng nhập test@eshop.com → tìm tai nghe → thêm giỏ → VIP100 → xem đơn trong Hồ sơ; remote moderated; 7 người; SEQ + SUS." + [DEMO] → mở `plan.md` | Đủ 9 phần; nhiệm vụ chỉ nêu mục tiêu |
| **Bước 1** | `/usability-evaluation HW03/demo/usability 1` + [DEMO] → mở `participant_kit.md` | Lời mở đầu, xin đồng ý, SEQ, SUS, 4 câu hỏi mở; `check_kit` |
| **Bước 2** | **Em sửa 1 dòng** trong kit (ví dụ câu nhiệm vụ) → `/usability-evaluation HW03/demo/usability 2` + [DEMO] → mở `pilot_changes.md` | Pilot rồi sửa kit; **em ghi lý do**, AI không suy diễn |
| **Bước 3** | `/usability-evaluation HW03/demo/usability 3` + "Tạo khung S01." + [DEMO] → mở `S01.json` trống → **em chép** `HW03\usability\sessions\S01.json` thật đè lên (nói rõ: dữ liệu phiên thật, không bịa) | Khung trống; chỉ mã P0x, không SĐT |
| **Bước 4** | `/usability-evaluation HW03/demo/usability 4` + "Tính số liệu, in bảng (không cần ghi vào report thật)." + [DEMO] | SUS, SEQ, hoàn thành, thời gian do script tính |
| **Bước 5–6** | `/usability-evaluation HW03/demo/usability 5` + [DEMO] → mở khung findings trống; `… 6` + [DEMO] → mở dữ kiện bug | Khung trống; **findings và bug do em viết** (chiếu report §5.8–5.9 thật) |
| Kết | — | Tóm 1 câu |

---

## 3. Sau khi quay (5 phút)

1. Dọn demo, về main:
   ```
   git restore .
   git clean -fd HW03/demo
   git switch main
   git branch -D demo-video
   git status --short
   ```
   Nếu còn `A_prompt_log.md` (M) thì giữ lại, commit chung ở bước 3.
2. Upload 2 video lên YouTube, chế độ **Unlisted**:
   - `23120255 HW03 – Demo skill gui-checklist-testing`
   - `23120255 HW03 – Demo skill usability-evaluation`
3. Dán link vào `HW03/skills/VideoLinks.md`, rồi:
   ```
   git add HW03/skills/VideoLinks.md HW03/appendix/A_prompt_log.md
   git commit -m "HW03[Skill] 3/3: link video demo"
   git push
   ```
4. Báo anh, anh xuất transcript lần cuối và đưa lệnh zip.

**Mốc cứng: 11:00 phải có link trong repo.** Không kịp thì dừng ở bước đang làm, upload phần đã quay, ghi trong VideoLinks là "demo tới bước k", và hạ điểm Skill cùng tên zip.
````

**Xử lý:** [...]

---

## #215 | 10:26 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Lúc đang làm có thể bỏ qua bước con người. Để thể hiện gõ xong skill là nó tự chạy E2E từ đầu tới cuối luôn được không?
```

**Output:**
````
Được một phần, nhưng có giới hạn. Anh nói rõ để video không phản tác dụng.

**Không nên để AI "làm thay người" ở các bước của người.** Các bước đó là:
- Bước 2: item SV bổ sung.
- Bước 4: verdict chạy tay.
- Usability bước 3: phiếu phiên.
- Usability bước 5–6: findings, bug.

Nếu AI tự điền mấy chỗ này thì video cho thấy:
1. AI làm đúng những việc AI-01 và chính skill của em **cấm**: gợi ý item, bịa dữ liệu phiên, viết findings.
2. Skill bỏ qua điểm dừng để người review. Đây lại là điểm thiết kế chính mà em nói trong video và Critique.

Người chấm xem sẽ thấy mâu thuẫn, và nếu bị vấn đáp thì khó giải thích.

**Cách đạt gần như ý em (khuyến nghị):** gõ **một lệnh duy nhất**, AI tự chạy liên tiếp mọi bước của AI. Tới bước cần người thì nó **dừng, nói rõ cần em làm gì**; em làm phần đó trong khoảng 20–30 giây (hoặc chỉ gõ "bỏ qua") rồi gõ **"tiếp"**. Video vẫn liền mạch từ đầu tới cuối, mà vẫn đúng thiết kế.

**Lệnh cho Video 1** (session mới, Opus 5.5 Medium):
```
/gui-checklist-testing HW03/demo/register
Demo video E2E: chạy lần lượt bước 0 → 6, xong mỗi bước in 1 dòng tóm tắt rồi CHUYỂN NGAY sang bước kế, trừ bước cần người:
- Bước 2: dựng khung sv_items.md rồi DỪNG chờ tôi gõ "tiếp" (tôi tự điền hoặc gõ "bỏ qua" → ghi "SV bỏ qua trong demo").
- Bước 4: tạo file lượt tay trống theo RUN.md rồi DỪNG chờ tôi chấm 3–4 item và gõ "tiếp". Không tự điền verdict.
Phạm vi: chỉ màn Đăng ký /register, nền tảng P1 (Cốc Cốc/Windows 11), tối thiểu 8 item, chỉ chế độ tay, demo không cần ảnh. Nhánh demo-video: freeze vào HW03/demo/ai-outputs, không commit, không push.
```

**Lệnh cho Video 2:**
```
/usability-evaluation HW03/demo/usability
Demo video E2E: chạy lần lượt bước 0 → 6 (flow U1: đăng nhập test@eshop.com → tìm tai nghe → thêm giỏ → VIP100 → xem đơn trong Hồ sơ; remote moderated; SEQ + SUS), xong mỗi bước in 1 dòng rồi chuyển ngay bước kế, trừ bước cần người:
- Bước 2: DỪNG chờ tôi sửa 1 dòng kit và gõ "tiếp"; cột lý do để tôi ghi.
- Bước 3: tạo khung S01 rồi DỪNG; tôi chép phiếu thật HW03/usability/sessions/S01.json vào và gõ "tiếp". Không tự điền.
- Bước 5–6: chỉ dựng khung findings và gom dữ kiện, không viết nội dung.
Nhánh demo-video: không ghi vào report thật, không commit, không push.
```

Phần còn lại giữ như quy trình lúc nãy: chuẩn bị, tạm dừng quay khi AI chạy lâu, dọn nhánh, upload Unlisted, commit link, mốc 11:00.

Nếu em vẫn muốn bản "gõ một lần, không dừng" thì phải để các bước người **trống và ghi rõ "bỏ qua trong demo"**, chứ không để AI điền. Trong video, nói thẳng là những bước đó do người làm và đã làm trong bài thật.
````

**Xử lý:** [...]

---

## #216 | 10:27 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Ý là kiểu bước 2 mình sẽ không làm. Còn bước 4 thì mình sẽ nói sơ qua là cần phải kiểm tra lại chạy tay
---
Giờ lên kịch bản cho GUI trước đã
```

**Output:**
````
## Kịch bản Video 1: `gui-checklist-testing` (khoảng 6–7 phút sau khi cắt)

Nguyên tắc: **gõ một lệnh, AI tự chạy 0 → 6**. Bước 2 em **bỏ qua**. Bước 4 em chỉ **nói** là cần chạy tay rồi gõ "tiếp". Bước 5–6 trên dữ liệu demo sẽ gần như trống, nên chuyển sang chiếu **kết quả thật của C2**.

### Chuẩn bị (chưa quay)
```
git status --short          # sạch (còn A_prompt_log.md thì commit trước)
git switch -c demo-video
```
- Đóng cửa sổ có CSV, Google Form, Gmail, mật khẩu.
- Mở sẵn VS Code (repo), Excel `HW03\excel\23120255_HW03_Checklist.xlsx`, tab GitHub Issues đã lọc `"HW03-C2" author:ThachHaoo`.
- Mở **session Claude Code mới**, chọn **Opus 5.5 – Medium**.
- Win + Alt + R để quay. AI chạy lâu thì tạm dừng quay.

### Lệnh duy nhất (dán khi tới mốc 0:40)
```
/gui-checklist-testing HW03/demo/register
Demo video E2E: chạy lần lượt bước 0 → 6, xong mỗi bước in 1 dòng tóm tắt rồi chuyển ngay sang bước kế. Phạm vi: chỉ màn Đăng ký web /register của ../eshop-sut, nền tảng P1 (Cốc Cốc / Windows 11), tối thiểu 8 item, chỉ chế độ tay, demo không cần ảnh.
- Bước 2: SV bỏ qua trong demo – không dựng item, không gợi ý item; ghi meta "bước 2 bỏ qua (demo)" rồi sang bước 3.
- Bước 4: tạo file lượt tay trống theo RUN.md rồi DỪNG chờ tôi gõ "tiếp"; KHÔNG tự điền verdict; khi tôi gõ "tiếp" thì để ket_qua trống ("chưa chạy – demo") và sang bước 5.
Nhánh demo-video: freeze vào HW03/demo/ai-outputs (KHÔNG appendix/ai-outputs), không commit, không push.
```

### Dòng thời gian

| Mốc | Trên màn hình | Ý chính em nói |
|---|---|---|
| **0:00** | VS Code: `HW03/skills/gui-checklist-testing/SKILL.md` (cuộn qua "Quy tắc bắt buộc", "Các bước") | Skill dùng cho checklist GUI theo bài giảng; 3 nguồn checklist; 7 bước, mỗi bước có điểm dừng cho người; những gì AI không được làm (gợi ý item ở bước 2, lấy Expected từ hành vi SUT) |
| **0:40** | Claude Code: dán lệnh | Demo trên màn Đăng ký, ngoài phạm vi C2 của bài, để cho thấy skill dùng lại được |
| **~1:10** | Bước 0 xong: mở `HW03/demo/register/register_inventory.md` | Control lấy từ code thật, có file:dòng, kèm điều khoản SRS |
| **~1:50** | Bước 1 xong: mở `HW03/demo/register/checklist.md`, chỉ 1–2 item | Item theo 3 nguồn; Expected có ngưỡng "Fail nếu…", căn cứ là đặc tả; output đã đóng băng |
| **~2:20** | Log: "bước 2 bỏ qua" | Bước này người tự bổ sung item, AI không được gợi ý; trong bài thật em thêm 6 item (mở nhanh `HW03/checklist/sv_items.md`) |
| **~2:50** | Bước 3 xong: mở `HW03/demo/register/RUN.md` | Phân loại cách chạy; quy tắc ảnh (overlay, tên file); `dom_probe.js` hỗ trợ đọc DOM |
| **~3:20** | Claude Code dừng ở bước 4 | Verdict chính thức phải là **lượt chạy tay** trên trình duyệt thật; trong bài thật em chạy tay 3 nền tảng. Gõ **"tiếp"** |
| **~3:50** | Bước 5–6 xong: Excel và danh sách Failed demo (trống) | Hai bước này sinh từ kết quả chạy; demo không chạy tay nên trống. Chuyển sang kết quả thật |
| **~4:20** | Mở Excel thật: sheet Checklist, Test Summary | Kết quả thật 74 item × 3 nền tảng; số liệu là công thức |
| **~4:50** | Mở `HW03/bugs/failed_list.md`, rồi `bug_groups.md` | Skill gom Failed thành nhóm và kiểm trùng issue |
| **~5:20** | Mở 1 file `HW03/bugs/BUG-xx.md`, rồi tab GitHub có issue tương ứng | **Bug do em viết**; skill chỉ gom dữ kiện; issue tạo từ file của em |
| **~6:00** | Terminal: `git log --oneline --grep "HW03\[T1\]"` | Mỗi bước một commit, output AI đóng băng trước khi em sửa |
| **~6:30** | Kết | Tóm 1–2 câu: skill lo phần nào, người lo phần nào |

### Quay xong video 1
- **Chưa dọn nhánh**, để quay tiếp video 2 trên cùng nhánh `demo-video`.
- Báo anh "xong video 1", anh đưa kịch bản video 2.
````

**Xử lý:** [...]

---

## #217 | 10:31 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
/gui-checklist-testing HW03/demo/register
Demo video E2E: chạy lần lượt bước 0 → 6, xong mỗi bước in 1 dòng tóm tắt rồi chuyển ngay sang bước kế. Phạm vi: chỉ màn Đăng ký web /register của ../eshop-sut, nền tảng P1 (Cốc Cốc / Windows 11), tối thiểu 8 item, chỉ chế độ tay, demo không cần ảnh.
- Bước 2: SV bỏ qua trong demo – không dựng item, không gợi ý item; ghi meta "bước 2 bỏ qua (demo)" rồi sang bước 3.
- Bước 4: tạo file lượt tay trống theo RUN.md rồi DỪNG chờ tôi gõ "tiếp"; KHÔNG tự điền verdict; khi tôi gõ "tiếp" thì để ket_qua trống ("chưa chạy – demo") và sang bước 5.
Nhánh demo-video: freeze vào HW03/demo/ai-outputs (KHÔNG appendix/ai-outputs), không commit, không push.
```

**Output:**
```
Đã đọc SRS + Register.jsx @ de0f48f. Giờ làm bước 0.

**Bước 1:** đã đọc slide (Nielsen/Norman/Shneiderman, *From heuristics…*, *Test every control*: text box, button, hyperlink, validation). Sinh item.

**Bước 2 bỏ qua (demo):** ghi `meta.step2`, không dựng item SV.

**Bước 3 xong:** `RUN.md` (3 nhóm G1–G3, chỉ tay, không ảnh) + `dom_probe.js`, 16 item `che_do: manual`, freeze step3, check 0 lỗi.

**Bước 4 – dừng:** file lượt tay trống `HW03/demo/register/runs/P1_manual_20261111-1034.md` (16 dòng theo thứ tự nhóm G1→G3 của RUN.md, cột status/notes trống). Em không điền verdict.

Anh/chị gõ **"tiếp"** khi muốn sang bước 5. Khi đó `ket_qua` sẽ để trống, ghi "chưa chạy – demo".
```

**Xử lý:** [...]

---

## #218 | 10:37 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
tiếp
```

**Output:**
````
**Bước 4 tiếp:** `ket_qua` để trống, `meta.step4` = "chưa chạy – demo".

**Bước 5 xong:** Excel `HW03/demo/register/excel/demo_register_checklist.xlsx` + `test_summary.md` (16 thiết kế / 0 đã chạy).

Đã chạy demo trên màn Đăng ký từ bước 0 đến bước 6. Chưa có verdict nào vì lượt tay chưa chạy, nên bước 6 ra danh sách Failed rỗng. Không commit, không push.

- **Bước 0:** khảo sát được 10 control và 5 điều khoản đặc tả (FR-01, FR-21, FR-22, FR-23, SEC-04), ghi vào `register_inventory.md`. Mã không có trường "Xác nhận mật khẩu" mà FR-01 yêu cầu, và trang không có `<h1>`.
- **Bước 1:** 16 item, đủ 4 IA (IA-01: 4, IA-02: 6, IA-03: 2, IA-04: 4). Theo nguồn: SRS 11, control 3, heuristic 2. Có 4 giả định GA1–GA4. Đã freeze vào `HW03/demo/ai-outputs`, `check_checklist` 0 lỗi.
- **Bước 2:** bỏ qua, ghi `meta.step2 = "bước 2 bỏ qua (demo)"`. Không dựng item, không gợi ý.
- **Bước 3:** `RUN.md` chia 3 nhóm G1–G3, chỉ chạy tay, không ảnh; kèm `dom_probe.js`. Cả 16 item để `che_do: manual`. Đã freeze RUN.md, dom_probe và checklist.
- **Bước 4:** file lượt tay để trống, `ket_qua` không điền, ghi "chưa chạy – demo".
- **Bước 5:** Excel 3 sheet và `test_summary.md` (16 item thiết kế, 0 đã chạy).
- **Bước 6:** lấy 229 issue về `issues.json`; `failed_list.md` có 0 item. `bug_groups.py` không chạy vì không có item MỚI để gom.

`HW03/appendix/A_prompt_log.md` đang hiện modified: hook Stop tự sinh lại, em không sửa tay. Nhánh demo-video không commit nên cứ để nguyên.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: demo video gui-checklist-testing bước 0→6, màn Đăng ký web /register, P1 Cốc Cốc/Win11, chỉ tay, không ảnh (nhánh demo-video)
- File đã tạo: HW03/demo/register/{register_inventory.md, checklist.json, checklist.md, RUN.md, dom_probe.js, runs/P1_manual_20261111-1034.md, excel/demo_register_checklist.xlsx, test_summary.md, bugs/{issues.json, failed_cfg.json, failed_list.md}}; HW03/demo/ai-outputs/ (freeze step1, step3 + INDEX.md)
- Kết quả kiểm tra: check_checklist 0 lỗi 0 cảnh báo (16 item, --min 8); lượt tay P1: Not run (demo); failed_list 0 item
- Commit: không (theo lệnh); không push
- Bất thường SUT: Register.jsx:47 Email type="text"; :72 nút submit bg-red-500; :32 chỉ có <h2>, không <h1>; thiếu trường Xác nhận mật khẩu; index.html:2,7 lang="en", title "frontend-web" (chỉ là dữ kiện mã, chưa phải verdict)
- Ghi chú: SUT ../eshop-sut vẫn ở nhánh usability-tunnel; A_prompt_log.md do hook tự sinh lại (modified, chưa commit)
- Cần quyết định: không
```
````

**Xử lý:** [...]

---

## #219 | 10:43 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
xong video 1
```

**Output:**
````
## Kịch bản Video 2: `usability-evaluation` (khoảng 5–6 phút sau khi cắt)

Bây giờ là 10:43. **Quay xong trước 10:58**, rồi upload cả 2 video trong lúc Claude Code đóng gói.

### Chuẩn bị (1 phút)
- Vẫn ở nhánh `demo-video`.
- Mở **session Claude Code mới**, Opus 5.5 – Medium.
- Mở sẵn VS Code: `HW03/skills/usability-evaluation/SKILL.md`, report `HW03/23120255_HW03_Report.md` (§5.7–5.9).

### Lệnh duy nhất (dán ở mốc 0:40)
```
/usability-evaluation HW03/demo/usability
Demo video E2E: chạy lần lượt bước 0 → 6, xong mỗi bước in 1 dòng tóm tắt rồi chuyển ngay sang bước kế. Flow: đăng nhập test@eshop.com → tìm tai nghe chống ồn → thêm giỏ → mã VIP100 → xem đơn trong Hồ sơ; remote synchronous moderated (Google Meet); 7 người + 1 pilot; SEQ + SUS + 4 câu hỏi mở.
- Bước 2 (pilot): SV bỏ qua trong demo – ghi "bước 2 bỏ qua (demo)".
- Bước 3: chỉ tạo khung trống sessions/S01.json bằng new_session.py, KHÔNG điền gì.
- Bước 4: KHÔNG dùng phiếu demo; chạy sus_score.py --check và --report trên dữ liệu thật HW03/usability/sessions, chỉ IN bảng ra màn hình, không ghi vào report.
- Bước 5–6: chỉ dựng khung findings trống và gom dữ kiện bug; không viết nội dung.
Nhánh demo-video: không commit, không push, không sửa report thật.
```

### Dòng thời gian

| Mốc | Trên màn hình | Ý chính em nói |
|---|---|---|
| **0:00** | `SKILL.md` (bảng file theo bước, "Giới hạn của AI") | Skill cho usability test moderated theo bài giảng (kế hoạch 9 phần); mỗi bước một file; **AI không** tạo danh sách người tham gia, không điền phiếu, không viết findings, không nhận dữ liệu cá nhân |
| **0:40** | Claude Code: dán lệnh | Chạy cả quy trình trên một thư mục demo |
| **~1:20** | Bước 0 xong: mở `HW03/demo/usability/plan.md` | Đủ 9 phần đúng thứ tự; nhiệm vụ chỉ nêu mục tiêu, có tiêu chí thành công và benchmark |
| **~1:50** | Bước 1 xong: mở `participant_kit.md` | Lời mở đầu, xin đồng ý quay và liên hệ, SEQ, SUS, 4 câu hỏi mở; `check_kit` kiểm đủ phần |
| **~2:10** | Log: "bước 2 bỏ qua" | Pilot do người chạy; bài thật pilot S00, sau đó em bổ sung cách hỏi lại khi người tham gia nhận xét mơ hồ |
| **~2:30** | Bước 3: mở `sessions/S01.json` trống, rồi mở `HW03/usability/sessions/S04.json` thật | Khung trống; người điều phối nhập; chỉ mã ẩn danh P0x, không SĐT |
| **~3:10** | Bước 4: bảng SUS/SEQ in trong terminal | Số liệu do script tính trên 7 phiên thật: SUS 77,9, SEQ 6,3, 7/7 hoàn thành; pilot không tính |
| **~3:40** | Bước 5–6: khung findings trống | Khung do skill dựng, nội dung phải là người viết |
| **~4:00** | Report §5.8–5.9 thật | Findings em tự viết: gom pain point, tách lỗi riêng lẻ với thiết kế, severity, đối chiếu issue |
| **~4:40** | Kết | Tóm 1–2 câu |

### Quay xong (làm ngay)
1. Dọn nhánh:
   ```
   git restore .
   git clean -fd HW03/demo
   git switch main
   git branch -D demo-video
   git status --short
   ```
2. **Dán lệnh chuẩn bị đóng gói** (lệnh anh gửi lúc 10:10) cho Claude Code nếu chưa dán.
3. Upload 2 video lên YouTube, **Unlisted**. Trong lúc upload, em làm tiếp phần khác.
4. Dán 2 link vào `HW03/skills/VideoLinks.md`, commit `HW03[Skill] 3/3: link video demo` (add cả `A_prompt_log.md` nếu M), push, báo anh.
````

**Xử lý:** [...]

---

## #220 | 10:50 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
/usability-evaluation HW03/demo/usability
Demo video E2E: chạy lần lượt bước 0 → 6, xong mỗi bước in 1 dòng tóm tắt rồi chuyển ngay sang bước kế. Flow: đăng nhập test@eshop.com → tìm tai nghe chống ồn → thêm giỏ → mã VIP100 → xem đơn trong Hồ sơ; remote synchronous moderated (Google Meet); 7 người + 1 pilot; SEQ + SUS + 4 câu hỏi mở.
- Bước 2 (pilot): SV bỏ qua trong demo – ghi "bước 2 bỏ qua (demo)".
- Bước 3: chỉ tạo khung trống sessions/S01.json bằng new_session.py, KHÔNG điền gì.
- Bước 4: KHÔNG dùng phiếu demo; chạy sus_score.py --check và --report trên dữ liệu thật HW03/usability/sessions, chỉ IN bảng ra màn hình, không ghi vào report.
- Bước 5–6: chỉ dựng khung findings trống và gom dữ kiện bug; không viết nội dung.
Nhánh demo-video: không commit, không push, không sửa report thật.
```

**Output:**
````
Bước 0: plan.md đủ 9 phần, check_kit 0 lỗi, đã freeze. Bước 1: participant_kit.md, check_kit 0 lỗi, đã freeze. Bước 2 bỏ qua (demo). Giờ làm bước 3–6.

Đã chạy đủ bước 0 → 6 trên nhánh `demo-video`. Không commit, không push, report thật không sửa.

- **Bước 0:** `HW03/demo/usability/plan.md` đủ 9 phần, `check_kit` báo 0 lỗi, đã đóng băng thành `demo_usability_plan_step0_20261111-105143.md`.
- **Bước 1:** `participant_kit.md` có nhiệm vụ dạng mục tiêu, SEQ, 10 câu SUS và 4 câu hỏi mở; `check_kit` báo 0 lỗi, đã đóng băng thành `demo_usability_participant_kit_step1_20261111-105143.md`.
- **Bước 2:** bỏ qua (demo).
- **Bước 3:** `sessions/S01.json` là khung trống do `new_session.py` tạo, mọi giá trị `null`.
- **Bước 4:** `--check` trên `HW03/usability/sessions`: 8 phiếu, 7 phiên chính, 0 lỗi. Bảng chỉ in ra màn hình: SUS trung bình 77,9 ± 17,8, median 85,0; SEQ trung bình 6,3; hoàn thành không trợ giúp 7/7; trong mốc 06:00 là 5/7; thời gian median 03:10.
- **Bước 5:** `findings.md` chép nguyên khung trống, chưa có nội dung.
- **Bước 6:** `bugs/_groups_usability.md` có 0 sự kiện, vì phiếu thật chưa có sự kiện nào đánh dấu `"bug": true`. Đã liệt kê issue của nhóm để em kiểm trùng.

Hai file đóng băng nằm trong `HW03/demo/ai-outputs/`, không đụng `HW03/appendix/ai-outputs/`.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: demo video /usability-evaluation bước 0→6 trong HW03/demo/usability (nhánh demo-video)
- File đã tạo/sửa: HW03/demo/usability/{plan.md, participant_kit.md, sessions/S01.json (trống), findings.md (khung trống), bugs/_groups_usability.md (0 sự kiện)}; freeze 2 file vào HW03/demo/ai-outputs/ (+ INDEX.md)
- Kết quả kiểm tra: check_kit plan+kit 0 lỗi; sus_score --check dữ liệu thật 8 phiếu / 7 phiên / 0 lỗi; bảng chỉ in màn hình, không ghi report (Pass)
- Commit: không (nhánh demo, theo lệnh)
- Cần quyết định / câu hỏi: không có điểm chặn
- Bất thường: cả 7 phiếu thật HW03/usability/sessions/S0*.json chỉ có sự kiện loại N → cột Lỗi (L) / Do dự (D) / Trợ giúp (T) trong bảng đều bằng 0. SV xem lại: phiên đó thật sự không có L/D/T hay lúc nhập phiếu đã ghi hết thành N.
- Bước 6 trên dữ liệu thật ra 0 sự kiện vì chưa phiếu nào có "bug": true.
```
````

**Xử lý:** [...]

---

## #221 | 11:01 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Testing Software: Demo Skill GUI: https://youtu.be/2E0pcpoG7Mk
Testing Software: Demo Skill Usability: https://youtu.be/KsJLMV-y4UQ
===
Thêm vào VideoLinks rồi nhé, push luôn rồi nhé
```

**Output:**
```
Video đã có link, Skill 9/10 có căn cứ. Còn **29 phút**. Anh xuất transcript `_p2` bản cuối ngay; ngay sau đó là lệnh đóng gói. Tới đây em **không sửa repo** nữa, trừ phần ký/tick và điền ngày ở form.
```

**Xử lý:** [...]

---

## #222 | 11:04 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
claude attach a0a67d1c
```

**Output:**
```
`claude attach a0a67d1c` là lệnh shell, không phải yêu cầu gửi cho tôi. Gõ vào đây thì nó chỉ thành tin nhắn chat, nên chưa attach được.

Cách mở phiên nền "Checklist GUI màn /register HW03":
- **Xem/tương tác với phiên đó:** mở một terminal PowerShell riêng, chạy `claude attach a0a67d1c`. Đừng dùng tiền tố `!` ở đây, vì attach cần terminal tương tác.
- **Tiếp tục phiên đó ngay trong cửa sổ này:** chạy `claude stop a0a67d1c` trong ter
```

**Xử lý:** [...]

---

## #223 | 11:04 11/11/2026 | Claude (không rõ model) | [...]
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

## #224 | 11:05 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: ĐÓNG GÓI HW03 – hạn 11:30, làm nhanh, không hỏi lại trừ lỗi chặn. Không amend. KHÔNG sửa phần SV viết.
1. python tools/hooks/on_stop.py --manual (đã có _p2 bản cuối) → forms_hw03.py (số lượt AI-02/03 theo dòng Tổng) → commit `HW03: prompt log + form – lần trích cuối`.
2. AI-02 + §11 + report_plan f: thêm artifact "AI nháp §7 Cách dùng skill" và "kịch bản quay video (phiên thảo luận)" – verdict/lý do để `<SV viết>` (nếu chưa có). Video: link đã có ở VideoLinks.md, chép vào §7 report + README.
3. AI-05 (mẫu HW02/ai-forms, không chép số liệu): tick mục có bằng chứng; mục cam kết cá nhân để [ ] "(em tự xác nhận)"; dòng minh bạch "SV đã gửi CSV có họ tên/SĐT người tham gia cho phiên thảo luận claude.ai 00:43 11/11"; số lượt = dòng Tổng.
4. Chạy lại report_t1, sus_score --report, summary_hw03 (README/§8), cây thư mục Phụ lục D.
5. Xuất commit log HW03/commit_log.txt (tools/export_commit_log.ps1 hoặc git log), commit `HW03: commit log`.
6. PDF: report, AI-02, AI-03, AI-05 (cùng tên .md → .pdf), commit `HW03: PDF`.
7. hw-submission-audit: liệt kê còn `<SV viết>`/`<SV điền>`/📝/[...] (file:dòng) – chỉ báo.
8. git archive --format=zip -o 23120255_HW03_AI_GUIUsability_091.zip HEAD HW03 → đo dung lượng; liệt kê file; kiểm KHÔNG có report_plan, CLAUDE.md, evidence_raw, placeholders_left, demo_plan, CSV, transcript; mỗi file ≤ 20 MB, tổng ≤ 20 file đính kèm Moodle.
Báo ≤ 12 dòng: chỗ trống còn lại, dung lượng zip, hash cuối.
```

**Output:**
```
Lỗi: lần chạy lại `forms_hw03.py` ghi đè phần SV trong AI-02 (ngày, chữ ký) và AI-03. Khôi phục bản SV ngay.

Viết AI-05.

Bước 4: chạy lại script + cây thư mục.

Thiếu thư viện `marked` để xuất PDF; cài tạm vào HW03/tests.

Đã xong danh sách chỗ trống. Giờ tạo zip.

Đã đóng gói HW03, chưa push. Zip `23120255_HW03_AI_GUIUsability_091.zip` ở gốc repo, 19.887.726 B (≈ 19,0 MiB), dưới giới hạn 20 MB; Moodle chỉ cần 1 file. Hash cuối: `7cee321` (PDF).

- **Sự cố em gây ra:** khi chạy lại `forms_hw03.py` (commit `91adc3f`), em đã ghi đè phần SV điền: ngày + chữ ký trong AI-02, và lý do 7 lượt "không rõ model" trong AI-03. Đã khôi phục bản SV ở `35d5c32`, chỉ cập nhật số lượt. Script giờ tự dừng nếu AI-02 đã có chữ ký. SV nên xem lại AI-02, AI-03 cho chắc.
- **Số lượt:** dòng Tổng = 204 lượt (Sonnet 4.6: 3, Opus 5.5: 193, không rõ model: 8). #196 nay ghi Opus 5.5, nhưng AI-03 vẫn còn dòng lý do của #196 do SV viết; em không xoá, SV tự quyết.
- **Đã làm:**
  - AI-02 thêm S4 (kịch bản quay video + chạy demo skill) và R5 (AI nháp §7 Cách dùng); §11 thêm mục 13; report_plan f ghi thêm.
  - Link video vào §7 và README.
  - AI-05: tick 8 mục có bằng chứng, 7 mục để `[ ]` "(em tự xác nhận)", có dòng minh bạch về CSV.
  - Chạy lại các script sinh bảng: report và README không đổi; Phụ lục D cập nhật.
  - Commit log ở `appendix/commit_log.txt`; 4 PDF cùng tên với file .md.
- **Kiểm zip:** 416 file, file lớn nhất ≈ 1,2 MB. Không có report_plan, CLAUDE.md, evidence_raw, placeholders_left, demo_plan, transcript hay CSV người tham gia. Có 3 file `checklist/runs/*_manual_*.csv` là kết quả chạy checklist, không phải dữ liệu người tham gia.
- **Chỗ trống còn lại** (bảng dưới).
- **Lưu ý trước khi nộp:**
  - Commit log và PDF sinh trước khi SV điền chỗ trống. Sửa gì nữa thì phải xuất lại PDF, commit log và zip.
  - #203, #204 (lượt này) sẽ đổi model sau lần trích prompt log sau.
  - Em cài `marked@12.0.2` vào `HW03/tests` bằng `--no-save` để xuất PDF; file zip chưa được gitignore.

| File | Dòng còn trống |
|---|---|
| Report (📝) | 9 (mục lục), 31–34 (IA ↔ FR), 38, 40, 46, 276, 402, 546, 561 + 571 (nhãn "AI nháp"), 579, 581 (`<SV viết>`) |
| AI-02 | 109 (S4), 112 (R5): verdict + lý do |
| AI-03 | 37–38 (lý do #203, #204), 91 (cam đoan `[...]`) |
| AI-05 | 50–51 (ngày, chữ ký) |
```

**Xử lý:** [...]

---

## #225 | 11:20 11/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
GẤP – hạn 11:30. SV đã sửa xong, chưa commit. KHÔNG chạy forms_hw03.py, KHÔNG sửa chữ SV. KHÔNG zip.
1. Commit phần SV: `HW03: SV điền form + §11`.
2. on_stop.py --manual. AI-03: chỉ sửa tay số lượt ở dòng Tổng; dòng lý do #203, #204 GIỮ (SV ghi "chạy nhầm"); xoá dòng lý do #196 nếu #196 nay có model.
3. Xuất lại 4 PDF (report, AI-02, AI-03, AI-05) + commit log. Commit `HW03: bản nộp cuối (PDF + log)`.
4. Kiểm nội dung sẽ vào zip (git archive --format=tar HEAD HW03 | liệt kê): báo (a) file rỗng hoặc < 100 byte, (b) file không cần nộp (report_plan, CLAUDE.md, placeholders_left, demo_plan, tests/node_modules, file tạm). Đã export-ignore thì ghi "đã loại". CHỈ BÁO, không xoá, không đổi .gitattributes.
Báo ≤ 6 dòng + hash.
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

**Tổng:** 225 lượt; Claude Sonnet 4.6 3 lượt (#1, #2, #92); Claude Opus 5.5 215 lượt (#3, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #27, #28, #29, #30, #31, #32, #33, #34, #35, #36, #37, #38, #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #52, #53, #54, #55, #56, #58, #59, #60, #61, #62, #63, #64, #65, #66, #67, #68, #71, #72, #73, #74, #75, #76, #77, #78, #80, #81, #82, #83, #84, #85, #86, #87, #88, #89, #90, #91, #93, #94, #95, #96, #97, #98, #99, #100, #101, #102, #103, #104, #105, #106, #107, #108, #109, #110, #111, #112, #113, #114, #115, #116, #117, #118, #119, #120, #121, #122, #123, #124, #125, #126, #127, #128, #129, #130, #131, #132, #133, #134, #135, #136, #137, #138, #139, #140, #141, #142, #143, #144, #145, #146, #147, #148, #149, #150, #151, #152, #153, #154, #155, #156, #157, #158, #159, #160, #161, #162, #163, #164, #165, #166, #167, #168, #169, #170, #171, #172, #173, #174, #175, #176, #177, #178, #179, #180, #181, #182, #183, #184, #185, #186, #187, #188, #189, #190, #191, #192, #193, #194, #195, #196, #197, #198, #199, #200, #201, #202, #203, #204, #205, #206, #207, #208, #209, #210, #211, #212, #213, #214, #215, #216, #217, #218, #219, #220, #221, #222, #224, #225); Claude (không rõ model) 7 lượt (#4, #51, #57, #69, #70, #79, #223).

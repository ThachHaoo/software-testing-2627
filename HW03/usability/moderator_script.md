# Kịch bản điều phối phiên usability – U1 (📝 AI nháp – SV duyệt/sửa)

Dựa trên `usability/plan.md`, `participant_kit.md`, `observation_sheet.md`. Mỗi phiên **~10 phút** (mở đầu 1' · nhiệm vụ ≤ 6' · form 3'), mỗi lần 1 người.

---

## A. Tin nhắn mời (Zalo / Messenger)

> Chào [tên], mình đang làm bài tập môn Kiểm thử phần mềm, cần người thử một trang web bán hàng khoảng **10 phút** qua Google Meet. Bạn chỉ cần dùng **máy tính có Chrome/Cốc Cốc/Firefox**, làm một việc mua hàng thử (không mất tiền thật), rồi điền một phiếu ngắn. Mình đang kiểm tra trang web chứ không kiểm tra bạn nên không có đúng sai đâu.
> Trợ giảng môn học có thể gọi/nhắn để xác nhận bạn đã tham gia, nên mình sẽ xin họ tên + SĐT trong phiếu.
> Bạn rảnh khung nào tối nay: 20:00 / 20:30 / 21:00 / 21:30?

**Lọc nhanh (hỏi trước khi chốt):** Bạn đã từng mua hàng online chưa? Bạn có học lớp Kiểm thử HW03 / đã dùng trang EShop chưa? → cần: *đã mua online*, *chưa dùng EShop*, *không học HW03*.

## B. Tin nhắn chốt giờ (gửi trước ~10 phút)

> Tới giờ rồi nè. Bạn vào link Meet này: [link Meet]. Dùng **máy tính**, mở sẵn trình duyệt, tắt bớt tab có thông tin riêng vì lát mình nhờ bạn chia sẻ màn hình.

---

## C. Chuẩn bị của em (trước MỖI phiên)

- [ ] `powershell -ExecutionPolicy Bypass -File tools\usability_session.ps1` → copy link `https://….trycloudflare.com` (link đổi mỗi lần chạy; script đã restart backend).
- [ ] `python .claude/skills/usability-evaluation/scripts/new_session.py HW03/usability/sessions S0x`
- [ ] Mở `observation_sheet` (giấy hoặc file), ghi Mã phiên, ngày, tick "Backend đã restart".
- [ ] Soạn sẵn trong Notepad: link tunnel, khối nhiệm vụ (mục E), link Google Form.
- [ ] Đồng hồ bấm giờ sẵn (điện thoại).
- [ ] Đóng tab/ứng dụng riêng tư trên máy em (Game Bar quay cả màn hình em).

---

## D. Mở đầu (~1 phút – nói nhanh, gộp 4 ý)

1. **Chào + nói mục đích**
   > Cảm ơn bạn đã giúp mình. Hôm nay mình kiểm tra **trang web**, không kiểm tra bạn. Chỗ nào bạn thấy khó là chỗ trang web cần sửa, nên cứ làm tự nhiên.

2. **Xin đồng ý quay** (hỏi trước khi bật quay)
   > Mình xin phép **quay màn hình và ghi âm** phiên này để xem lại, chỉ dùng cho bài tập, không đăng công khai. Trợ giảng có thể liên hệ bạn để xác nhận. Bạn đồng ý không?
   - Đồng ý → bật **Game Bar (Win + Alt + R)**, rồi nói: *"Mình bắt đầu quay rồi nhé, bạn xác nhận lại là đồng ý quay giúp mình."* (để lời đồng ý có trong video).
   - Không đồng ý → không quay, chỉ ghi phiếu; ghi "không quay" vào observation_sheet.

3. **Nhờ chia sẻ màn hình**
   > Bạn bấm **Trình bày ngay → Toàn bộ màn hình** (hoặc một cửa sổ trình duyệt) giúp mình.

4. **Hướng dẫn nói to suy nghĩ (think-aloud)**
   > Trong lúc làm, bạn **nói to những gì đang nghĩ**: đang tìm gì, thấy gì lạ, định bấm gì. Ví dụ: *"Mình đang tìm ô tìm kiếm… à đây rồi, mà không biết bấm vào đâu…"*. Mình sẽ **không hướng dẫn** trong lúc bạn làm, bạn cứ làm như ở nhà. Bạn có thể dừng bất cứ lúc nào.

---

## E. Giao nhiệm vụ (dán vào chat Meet, rồi đọc to)

```
Link trang web: <link tunnel>

NHIỆM VỤ: Bạn muốn mua một chiếc tai nghe chống ồn cho mình trên trang EShop.
Cửa hàng đã tặng bạn mã giảm giá VIP100. Hãy đặt mua tai nghe với giá đã được giảm,
sau đó kiểm tra xem đơn hàng của bạn đã được ghi nhận chưa và đang ở trạng thái nào.

Tài khoản của bạn: test@eshop.com / Test1234!
Khi xong, bạn nói "Xong".
```

> Bạn đọc nhiệm vụ trong chat nhé. Có gì chưa rõ về **đề bài** thì hỏi mình trước khi bắt đầu. *(Chỉ giải thích lại đề, KHÔNG nói cách làm: không nói "dùng ô tìm kiếm", "vào Hồ sơ".)*
> Bạn bấm vào link để bắt đầu.

→ **Bấm đồng hồ** khi người tham gia mở link (00:00).

---

## F. Trong lúc làm (≤ 6 phút)

**Em làm:** im lặng, ghi mốc thời gian + diễn biến (L/D/N/T) vào observation_sheet; chép **nguyên văn** câu than/thắc mắc.

**Câu nhắc trung tính (chỉ dùng khi họ im lặng lâu > 20 giây):**
- "Bạn đang nghĩ gì?"
- "Bạn đang tìm gì?"
- "Bạn mong đợi điều gì sẽ xảy ra?"

**Khi họ hỏi "bấm đâu?", "đúng chưa?":** trả lời lại bằng câu hỏi
- "Nếu không có mình ở đây thì bạn sẽ làm gì?"
- "Bạn nghĩ sao?"

**Can thiệp (ghi T vào phiếu, tính "có trợ giúp")** – chỉ khi ≥ 1,5 phút không tiến triển hoặc họ xin trợ giúp:
1. Lần 1 (kẹt ≥ 1,5 phút): "Bạn thử nhìn lại toàn bộ trang xem có gì liên quan không?"
2. Lần 2 (vẫn kẹt): gợi ý **vùng** màn hình, không nói tên nút. Ghi nguyên văn câu em nói.
3. Quá **6 phút** hoặc họ muốn dừng → "Không sao, mình dừng ở đây nhé." → ghi **Không hoàn thành**.

**Không làm:** không khen/chê ("đúng rồi", "sai rồi"), không giải thích giao diện, không đọc chữ trên màn hình giúp.

**Khi họ nói "Xong":** dừng đồng hồ, hỏi
> Theo bạn, đơn hàng của bạn đang ở **trạng thái** nào?

→ ghi câu trả lời (tiêu chí thành công: đơn mới, tổng 5.900.000 ₫, nói được trạng thái).

---

## G. Sau nhiệm vụ: phiếu (~3 phút)

1. Dán link Google Form vào chat:
   > Bạn điền giúp mình phiếu này, **Mã phiên là S0x**. 4 câu cuối bạn trả lời **1 câu ngắn** là đủ.

2. **Chỉ khi còn thời gian** (người tham gia không vội): hỏi **1 câu** vào chỗ khó nhất vừa thấy, ghi lại:
   - "Lúc [mm:ss] mình thấy bạn dừng lại ở [màn hình], lúc đó bạn đang nghĩ gì?"
   - "Bạn có để ý số tiền sau khi nhập mã không? Bạn thấy nó đúng chưa?"
   - "Nếu là trang thật, chỗ nào làm bạn ngại mua nhất?"

3. Đợi họ bấm **Gửi** form.

---

## H. Kết thúc (~10 giây)

> Cảm ơn bạn nhiều, phần của bạn xong rồi. Bạn **dừng chia sẻ màn hình** giúp mình nhé.

→ Dừng quay (**Win + Alt + R**), rời Meet.

---

## I. Sau MỖI phiên (em làm ngay, ~3 phút)

- [ ] **Ctrl+C** tắt tunnel (phiên sau chạy lại script → backend tự restart, link mới).
- [ ] Đổi tên video `S0x_<ngày>.mp4` (để ngoài repo nếu > vài MB hoặc có mặt/tên người tham gia).
- [ ] Hoàn thiện observation_sheet: kết quả, số lỗi/do dự/trợ giúp.
- [ ] Nhập JSON phiên (mã **P0x**, không họ tên/SĐT; SEQ, SUS lấy từ tab Responses – chữ số đầu) → `sus_score.py HW03/usability/sessions --check`.
- [ ] Ghi họ tên + SĐT vào **bảng người tham gia riêng** (ngoài repo; bản đưa vào report che 4 số giữa SĐT).
- [ ] Commit `HW03[T2] k/10: phiên S0x` (pilot = 2/10; S01…S07 = 3/10…9/10).

---

### Ghi chú

- **Pilot (S00):** chạy đủ kịch bản với 1 người; sau pilot ghi lại chỗ cần sửa (đề bài khó hiểu? thời gian?) vào report §5.5 trước khi chạy S01.
- Không nhắc người tham gia về lỗi F5 làm mất giỏ (plan mục 6) – nếu xảy ra thì ghi vào phiếu.
- Repo public: không commit CSV form, video có mặt/giọng người tham gia, hay họ tên/SĐT đầy đủ.

# HỆ THỐNG SƠ ĐỒ CHỖ NGỒI LỄ TỐT NGHIỆP 2026 (DUE OFFICIAL EDITION)

## Quy cách ghế hiện tại: 18 ghế mỗi dãy

Mỗi dãy tân khoa có **18 ghế: 9 ghế khối trái và 9 ghế khối phải**. Giữ nguyên khung hai khối rộng 400px, hành lang, sân khấu, bảng vinh danh, bảng ghi chú và phong cách hiển thị. Ghế được phân bố đều trong khung hiện có.

Với cấu hình mặc định 4 dãy Đại biểu, Dãy 5 gồm vị trí 1–18 (trái 1–9, phải 10–18), Dãy 6 gồm vị trí 19–36. Khối phải tiếp tục đánh số từ hành lang ngoài vào giữa: khi nhìn từ trái sang phải là 18…10. Số ghế hiển thị vẫn lấy nguyên văn từ Excel, độc lập với vị trí.

Số dãy tân khoa `R = ceil(maxPos / 18)`, tối đa 20 dãy (360 vị trí). Các dãy Người thân nối tiếp ngay sau dãy tân khoa cuối. Danh sách hiện tại có 232 vị trí: Dãy 5–17, còn 2 ô trống ở Dãy 17; cấu hình Excel hiện có 4 dãy Người thân nên nằm ở Dãy 18–21. Không cần sửa vị trí hoặc số ghế trong danh sách Excel.

Khi trình chiếu trên màn hình dọc hoặc màn hình rộng, sơ đồ vẫn giữ tỷ lệ 16:9 và căn giữa. Canvas pháo hoa dùng `object-fit: contain` và căn giữa giống SVG, nên bám đúng khung vinh danh cả khi xoay màn hình hoặc bật/tắt toàn màn hình.

## Triển khai GitHub Pages

Website: https://tieuhac0109.github.io/sodochongoiTN/

Mỗi lần push vào nhánh `main`, workflow `.github/workflows/deploy-pages.yml` tự cài Python, build lại `index.html` từ `danhsach.xlsx` và triển khai lên GitHub Pages. Trong **Settings → Pages**, chọn **Source: GitHub Actions**. Có thể chạy lại bằng **Actions → Deploy GitHub Pages → Run workflow**.

Để cập nhật danh sách chung, thay `danhsach.xlsx`, commit và push lên `main`. Nhập Excel trên giao diện chỉ thay đổi dữ liệu tại trình duyệt đang dùng và lưu vào localStorage; thao tác đó không cập nhật GitHub hoặc các máy khác. Nút khôi phục danh sách mặc định sẽ bỏ danh sách nhập tại trình duyệt.

Build trên máy tính: `python -m pip install -r requirements.txt`, sau đó `python build_due_html.py` (hoặc chạy `Cap_Nhat_Danh_Sach.bat`). Bản HTML đã nhúng cả ảnh, font và thư viện đọc Excel; chỉ cần sao chép `index.html` để chạy offline.

Gói website triển khai chỉ chứa `index.html` và `.nojekyll`. Repo công khai vẫn cho phép xem mã nguồn và Excel; danh sách tân khoa mặc định được nhúng trong HTML và có thể đọc công khai.

## Kiểm thử khi sửa mã nguồn

Chạy `python -m pip install -r requirements-test.txt`, `python build_due_html.py`, rồi `python -m unittest discover -s tests -v`. Bộ kiểm thử dùng Microsoft Edge đã cài trên Windows. Với máy không có Edge, chạy `python -m playwright install chromium` và đặt biến môi trường `BROWSER_CHANNEL=chromium` trước khi chạy kiểm thử. Ảnh kiểm tra xuất PNG được lưu tại `test-results/export.png` (không đưa vào Git).

Kiểm thử bao gồm dữ liệu Excel không hợp lệ, nội dung có ký tự HTML, nhãn ghế đặc biệt, giới hạn sức chứa, dãy thiếu, giữ vị trí vinh danh khi đổi cấu hình, xuất PNG và tắt hiệu ứng canvas.

**TRƯỜNG ĐẠI HỌC KINH TẾ — ĐẠI HỌC ĐÀ NẴNG (DUE)**
**LỄ TRAO BẰNG TỐT NGHIỆP TIẾN SĨ, THẠC SĨ, CỬ NHÂN ĐỢT 3 NĂM 2026**
Thiết kế Digital Signage chuẩn Full HD 16:9 (1920 × 1080) dành cho **TV 43 inch trước sảnh** và **Màn hình LED trong hội trường**.

---

## 🌟 1. Điểm nổi bật & Cải tiến mới nhất theo Brand Guidelines của DUE

1. **Đồng bộ 100% Hệ thống Nhận diện Thương hiệu DUE:**
   - **Logo DUE chính thức:** Đặt trang trọng, sắc nét tại góc trên bên trái header (`sources/logo.png`).
   - **Bộ font chữ thương hiệu:** Tích hợp trực tiếp bộ font chuẩn **SVN-Gilroy** (Bold, SemiBold, Medium, Regular) cho toàn bộ tiêu đề, nhãn ghế và văn bản, hiển thị tiếng Việt hoàn hảo.
   - **Bảng màu chuẩn thương hiệu DUE:**
     - Xanh dương chủ đạo: `DUE Blue #005EA3` (PANTONE 3015C)
     - Xanh lá khu Đại biểu: `DUE Green #058E47` (PANTONE 355C)
     - Cam khu Tân Cử nhân: `DUE Orange #EE6323` (PANTONE 165C)
     - Vàng khu Khen thưởng: `DUE Yellow #FFB612` (PANTONE 1235C)
     - Tím khu Tân Thạc sĩ: `#7C1FA3`
     - Đỏ khu Tân Tiến sĩ / NCS: `#B90C1A`

2. **Căn giữa tuyệt đối & Khung nền trắng mở rộng cân bằng 3 lề (28px):**
   - Trục hành lang giữa và Sân khấu được căn chỉnh chính xác tại tâm màn hình 1920×1080.
   - Khung nền trắng nội trường (`innerCardBg`) được mở rộng ngang với tọa độ `X = 28` đến `X = 1892` (chiều rộng 1864px).
   - Canh lề đối xứng 3 chiều: **Cách lề trái = Cách lề phải = Cách lề dưới = 28px**.
   - Ôm trọn 100% cả **Bảng Vinh Danh Tân Khoa** bên trái và **Bảng Ghi Chú** bên phải vào trọn vẹn bên trong lòng khung viền vàng kim, xóa bỏ hoàn toàn tình trạng rơi rớt mép ngoài.

3. **Cụm WC và "Lối vào ➔" siêu nhỏ gọn (Không viền đen):**
   - Đã tái cấu trúc 100% bằng code SVG vector thuần, loại bỏ hoàn toàn ảnh crop và hiệu ứng shadow tối gây viền đen.
   - Thu nhỏ kích thước xuống footprint mini (WC: 42×42px, Lối vào: 64×26px) và dời sát vào mép đường mũi tên dọc (`X = 390`, khoảng cách chỉ 10px), giải phóng hoàn toàn không gian rộng lớn bên cánh trái.

4. **Bảng GHI CHÚ nhỏ gọn, tinh tế:**
   - Đặt ở bên phải, thu hẹp kích thước thanh thoát, tạo sự cân bằng thị giác hoàn mỹ với Bảng Vinh Danh bên trái.
   - Đổi chính xác câu chữ hướng dẫn di chuyển:
     **"Hướng di chuyển của Tân Thạc sĩ, Tân Cử nhân khi lên nhận bằng"**.
   - Cập nhật mục phân loại ghế người thân:
     **"Ghế ngồi người thân \n Tân TS/ThS/ĐH"**.
   - Cập nhật mục phân loại khen thưởng:
     **"Ghế ngồi Cá nhân được \n tuyên dương, khen thưởng"**.

5. **Đồ họa chất lượng cao tích hợp từ thư mục `background/`:**
   - **`Ảnh 1.png` (Tòa nhà trường đại học & Cây xanh & Dải lụa đáy):** Tách nền trong suốt cao cấp, tăng kích thước gấp 3 lần, đặt ở góc dưới bên phải màn hình (dưới bảng Ghi chú), không che khuất mũi tên.
   - **`Congratulations.png` (Chữ nghệ thuật "Congratulations, Graduates!"):** Chữ thư pháp 3D vàng kim kèm dải lụa hoàng gia xanh - vàng kim uốn lượn được đặt trang trọng tại góc dưới, hỗ trợ tinh chỉnh tọa độ (`x`, `y`, `width`, `height`) linh hoạt.
   - **`Ảnh 2.png` (Mũ cử nhân 3D & Cuộn bằng thắt nơ đỏ):** Tách nền trong suốt tinh xảo, đặt cạnh Logo DUE ở góc trên bên trái header.
   - **`Ảnh 3.png` (Chùm pháo hoa vàng kim & Dải lụa hoàng gia):** Đặt ở lớp hiển thị trên cùng (Z-Order ưu tiên), bung nở trọn vẹn ở góc trên bên phải màn hình mà không bị thanh header che khuất.
   - Toàn bộ được mã hóa Base64 Data URI nhúng trực tiếp vào `index.html`, đảm bảo **100% Single-File Offline**, mang sang bất kỳ máy tính nào không có mạng đều hiển thị sắc nét tức thì.

6. **Thảm đỏ danh dự trung tâm (Central Red Carpet):**
   - Trải dọc lối đi giữa từ **Dãy 1 (VIP)** kéo dài xuyên suốt đến hết **Dãy 23 (Người thân Tân TS/ThS/ĐH)**.
   - Thiết kế vân nhung đỏ chuyển sắc (`#8a040f` đến `#db1c2b`) với viền chỉ vàng kim đứt đoạn tinh xảo, tôn vinh lối đi trang trọng nhất của buổi lễ.

7. **Tối ưu hóa luồng di chuyển & Mũi tên một chiều:**
   - **Mũi tên thoát ngang Dãy 5:** Chiều dài mũi tên sang hai bên được tinh chỉnh dừng trước mép hành lang dọc (cách 9px), triệt tiêu hoàn toàn sự đè lấn lên luồng di chuyển chính.
   - **Liền mạch hành lang phải:** Luồng di chuyển từ Cánh gà phải chạy liền mạch 100% xuống đáy hội trường, xóa bỏ hoàn toàn khoảng hở đứt đoạn trước đây.
   - **Tối giản đầu mũi tên:** Mỗi tuyến đường (hành lang trái, hành lang phải, hành lang đáy) chỉ duy nhất 1 đầu mũi tên định hướng và 1 đầu mũi tên chỉ vào Cánh gà trái, giúp sơ đồ thanh thoát, không bị rối mắt.
   - **Mặt sân khấu trung tâm:** Đã loại bỏ hoàn toàn 2 mũi tên trên sàn sân khấu để giữ tính uy nghiêm, tôn nghiêm tối đa.

8. **Chuẩn hóa nhãn các dãy Người thân (số dãy tự động theo dữ liệu):**
   - Cập nhật chính xác nhãn 2 khối ghế cuối hội trường thành **`Người thân Tân TS/ThS/ĐH`**, chữ đậm nổi bật trên nền xám xanh thanh lịch.

9. **BẢNG VINH DANH TÂN KHOA THEO 3 TRÌNH ĐỘ (PURE DIGITAL SIGNAGE DESIGN):**
   - **Tích hợp 3 khung nền đồ họa hoàng gia cao cấp (`Khungvinhdanh/`):**
     - **Tiến sĩ:** Khung `TanTiensi.png` ("Chúc mừng Tân Tiến sĩ").
     - **Thạc sĩ:** Khung `TanThacsi.png` ("Chúc mừng Tân Thạc sĩ").
     - **Đại học:** Khung `TanCunhan.png` ("Chúc mừng Tân Cử nhân").
     - Hệ thống tự động chuyển đổi khung nền mượt mà theo đúng trình độ của từng người học được gọi tên.
   - **Cố định 100% Cỡ chữ To Chuẩn (20.5px):**
     - Mở rộng biên độ hiển thị tên tiệm cận khung viền vàng kim (~305px).
     - Mọi tên trên 1 hàng (lên tới 27 ký tự như *Dương Thị Thu Hường*, *Nguyễn Hoàng Minh Phương*, *Công Tằng Tôn Nữ Bích Ngọc*) đều được **giữ nguyên 100% cỡ chữ lớn chuẩn `20.5px`**, tuyệt đối không bị co nhỏ.
     - Khi tên có đè lên cành nguyệt quế 2 bên, chữ vẫn nổi hoàn toàn lên trên vòng nguyệt quế với bóng đổ đen sâu (`nameGlowDrop`).
   - **Đồng nhất 100% Cỡ chữ khi Xuống hàng:**
     - Với các tên đặc biệt dài (> 27 ký tự) buộc phải xuống 2 hàng, cả Dòng 1 và Dòng 2 đều được **khóa chặt ở cùng một cỡ chữ lớn `19.5px` bằng nhau tuyệt đối** (không còn tình trạng dòng 2 bé hơn dòng 1).
   - **Thẻ Tên & Khung Vinh Danh Lớp Trên Cùng (`z-index: 20`):**
     - Toàn bộ Khung vinh danh, tên người học (`#honorsPlaqueName1`), huy hiệu khen thưởng và thẻ số ghế được đưa lên lớp SVG trên cùng (`#topHonorsSvg`), nổi hoàn toàn lên trên Canvas pháo hoa (`z-index: 10`). Tên của tân khoa luôn sáng rõ 100%, không bị rocket hay hạt lửa che khuất.
   - **UI/UX Khen thưởng Hoàng gia Đẳng cấp:**
     - **Trực tiếp trên Khung Vinh Danh:** Xuất hiện huy hiệu vàng kim dập nổi `★ KHEN THƯỞNG ★` (được thu gọn 136px vừa khít nội dung) ngay phía dưới tên người học.
     - **Dải Ruy Băng 3D Hoàng gia (Royal Swallowtail Ribbon):** Thiết kế dải lụa vàng kim 3D với 2 đuôi nơ én vát nhọn, kẹp giữa là 2 huy chương ngôi sao vàng và dòng chữ dập nổi `CÁ NHÂN ĐƯỢC KHEN THƯỞNG` kèm hiệu ứng nhịp thở hào quang vàng óng (`awardRibbonGlow`). Tích hợp động cơ **tự động co chỉnh tỉ lệ đa màn hình (Auto-Fit Engine)**: tự động đo kích thước render thực tế của font chữ trên từng thiết bị/màn hình để tự động co tỉ lệ (auto-scale), đảm bảo dòng chữ luôn giữ khoảng cách an toàn tối thiểu $\ge 17.5\text{px}$ và không bao giờ chạm hay đè lên 2 ngôi sao.
     - **Huy hiệu Số ghế:** Đổi sang màu vàng hoàng kim rực rỡ với viền đôi kim loại phát sáng.
   - **Hiệu ứng Pháo hoa Hạt Vật lý bằng CODE THẬT 100% (Pure Canvas Physics Fireworks Engine):**
     - Rocket phóng từ đỉnh khung vinh danh lên bầu trời phát nổ thành các chùm hạt photon vàng kim bung tỏa và rơi xuống tự nhiên với trọng lực (`gravity = 0.058`), lực cản không khí (`drag = 0.965`) kèm vệt đuôi ánh sáng lấp lánh (sparkling trails).
     - Loại bỏ hoàn toàn ảnh crop, tâm đa giác kim cương, 24 nan hoa xoay và các ngôi sao nhân tạo.
     - Tự động kích hoạt chùm pháo hoa 3 tầng khi xướng danh Tân Tiến sĩ hoặc Cá nhân khen thưởng.
   - **Hiệu ứng xướng danh Tân Tiến sĩ (`TS1`):** Tự động phát hào quang vàng kim vào toàn bộ hàng ghế NCS, GVHD & Gia đình (Dãy 4 phải).
   - **Tùy chọn 4 Tốc độ chuyển người:** Bổ sung đầy đủ 4 mức: **`1s` • `2s` • `3s` • `5s`** linh hoạt theo nhịp xướng danh của MC.
   - **Giao diện trình chiếu tinh gọn, sạch sẽ:**
     - Tập trung công cụ `📥 Nhập Excel` và `📄 Tải mẫu Excel` duy nhất trên thanh **Toolbar ngang** trên cùng.
     - Đã xóa bỏ 2 nút trùng lặp này khỏi bảng **Cài đặt (phím E)** để bảng cài đặt trở nên gọn gàng, thanh thoát.
     - Bảng Cài đặt chuyên trách: Chỉnh tốc độ (`1s/2s/3s/5s`), Cụm điều khiển vinh danh (`Trước/Dừng/Sau/Về đầu` + **Ô nhập số chuyển trực tiếp `🎯 Đi tới`**), Thống kê thực tế từ Excel (Khen thưởng, Thạc sĩ, Cử nhân), Hộp kiểm tra lỗi/cảnh báo dữ liệu (`#importIssues`) và Khôi phục danh sách mặc định.
   - **Tương tác trực tiếp trên Sơ đồ Ghế (Click ô ghế để vinh danh):**
     - Nhấp chuột trực tiếp vào bất kỳ ô ghế nào của tân khoa trên sơ đồ hội trường, bảng vinh danh lập tức chuyển đến đúng người đó, đồng thời kích hoạt luồng phát sáng spotlight tại vị trí ghế và hiển thị thông báo.
     - Nhấp vào hàng ghế NCS (Dãy 4 phải hoặc dãy chỉ định) sẽ lập tức vinh danh Tân Tiến sĩ (`TS1`).
   - **Kiến trúc Hình học Động Thống Nhất (tự co giãn theo tổng số dãy):**
     - **Giải quyết triệt để sự đè lấn:** Tự động tính toán phân bổ chính xác 3 phân khu trong khung cố định Full HD `Y = 258 .. 892` (chiều cao 634px), triệt tiêu hoàn toàn hiện tượng khối Người thân đè lên Dãy 18.
     - **Đồng bộ nhịp bước hàng:** Chiều cao hàng $h$ và bước hàng $step$ được chuẩn hóa đồng nhất cho cả dãy Đại biểu (Dãy 1–4), Tân khoa và Người thân, loại bỏ hoàn toàn sự chênh lệch (không còn tình trạng hàng 1–4 bị thưa).
     - **2 khoảng cách phân khu cân xứng ($G_1 = G_2 \ge \frac{1}{3} h$):**
       - Khoảng cách 1: Giữa hàng cuối Đại biểu và hàng 1 Tân khoa.
       - Khoảng cách 2: Giữa hàng cuối Tân khoa và hàng 1 Người thân (bằng đúng khoảng cách 1).
       - Khoảng cách luôn đảm bảo tối thiểu $\ge \frac{1}{3} h$ và tự điều chỉnh theo tổng số dãy, để tạo sự phân khu rõ ràng trong khung hiện có.
     - **Cột số dãy 2 bên đồng bộ hoàn hảo:** Đánh số liên tục từ Dãy 1 đến Dãy $T$, với `T = số dãy Đại biểu + R + số dãy Người thân`; các khoảng ngắt phân khu tương ứng giúp người tham dự định vị tức thì.
   - **Sơ đồ Ghế Động 100% theo Dữ liệu Excel (Tách bạch Vị trí ghế & Số ghế hiển thị):**
     - **Phân biệt rõ `Vị trí ghế` và `Số ghế`:**
       - `Vị trí ghế` (`1..N`): Quyết định ghế được vẽ ở ô thứ mấy trên lưới hội trường (Dãy 5: vị trí 1–18, Dãy 6: vị trí 19–36...). Tân Tiến sĩ (`TS1`) để trống cột này.
       - `Số ghế`: Nhãn số ghế thực tế in lên ô ghế và bảng vinh danh (không bắt buộc liên tục 1–280; ví dụ có thể là `1, 3, 4, 5, 7, 8...`).
     - **Màu ghế theo từng cá nhân (`Loại ghế`):** Hỗ trợ cột `Loại ghế` (`Khen thưởng` / `Thạc sĩ` / `Cử nhân` / `Tiến sĩ`) hoặc tự động suy ra theo thứ tự ưu tiên: `Tiến sĩ (Đỏ) > Khen thưởng (Vàng) > Thạc sĩ (Tím) > Cử nhân (Cam)`.
     - **Tự động co giãn số dãy ghế & đôn dãy Người thân:** Số dãy ghế `R = ceil(maxPos / 18)` bắt đầu từ Dãy 5 (`5 .. 5 + R - 1`), và mặc định 5 dãy `Người thân Tân TS/ThS/ĐH` tự động đánh số nối tiếp ngay sau đó (`5 + R .. 5 + R + 4`). Ví dụ: nạp 280 vị trí → Ghế Dãy 5–20, Người thân Dãy 21–25; nạp 260 vị trí → Ghế Dãy 5–19, Người thân Dãy 20–24. Số dãy Đại biểu và Người thân có thể điều chỉnh từ Excel hoặc Cài đặt.
     - **Ô trống mờ (`seat-empty`):** Nếu dãy cuối không đủ 18 ghế hoặc có vị trí bị bỏ trống trong khoảng `1..maxPos`, hệ thống tự động vẽ ô nét đứt mờ thanh lịch để giữ nguyên bố cục đối xứng của hội trường.
   - **Động cơ Dữ liệu Excel Đa Tầng Siêu Tốc:**
     - *Tải mẫu tức thì (0ms):* Tải về file mẫu `Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx` (kèm sheet `HuongDan`) ngay lập tức từ gói nhị phân Base64 nhúng sẵn, không cần mạng.
     - *Nhập file ngoại tuyến:* Nhúng đầy đủ thư viện SheetJS nội bộ, hỗ trợ đọc file `.xlsx`, `.xls`, `.csv` hoàn toàn offline.
     - *Tự động nhúng vĩnh viễn:* Khi chạy `python build_due_html.py`, script tự động quét và nhúng danh sách thật vào lõi file `index.html`.
     - *Chống mất dữ liệu tại hiện trường:* Tự động lưu danh sách nạp mới từ giao diện vào `localStorage` của trình duyệt máy chiếu (kèm cơ chế đối chiếu dấu vân tay `honorsFingerprint` để bản build mới luôn tự động cập nhật).

---

## 💡 2. Cách nạp vĩnh viễn danh sách Excel chính thức vào duy nhất 1 file `index.html`

Nếu bạn muốn **chỉ copy duy nhất 1 file `index.html` mang đi cắm vào TV hoặc máy chiếu**, mà khi mở lên là **chạy ngay 100% danh sách tân khoa thật** (không cần nạp lại file Excel):

### 🌟 Cách 1: Tiện ích 1-Click tự động (Khuyên dùng - Không cần gõ lệnh)
Hệ thống đã tích hợp sẵn công cụ tự động **`Cap_Nhat_Danh_Sach.bat`**:
1. Chuẩn bị file Excel danh sách tân khoa chính thức.
2. Thực hiện 1 trong 2 cách:
   - **Kéo - Thả:** Kéo file Excel của bạn thả trực tiếp lên tệp **`Cap_Nhat_Danh_Sach.bat`**.
   - **Hoặc Đặt tên:** Đổi tên file Excel thành `danhsach.xlsx` (hoặc chép đè vào `Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx`) trong cùng thư mục rồi **nhấp đúp chuột vào `Cap_Nhat_Danh_Sach.bat`**.
3. Hệ thống sẽ tự động quét và nhúng vĩnh viễn toàn bộ danh sách mới vào lõi tệp **`index.html`** làm danh sách gốc (`DEFAULT_HONORS_ROWS`) chỉ trong 2 giây!
4. Giờ đây bạn chỉ việc copy duy nhất file **`index.html`** sang máy tính/TV hội trường, mở lên là vinh danh ngay lập tức mà không cần mạng Internet hay file Excel đi kèm.

### 💻 Cách 2: Biên dịch bằng lệnh Python (Dành cho Quản trị viên)
1. Điền danh sách tốt nghiệp thực tế vào file **`Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx`** *(hoặc tạo file `danhsach.xlsx` trong cùng thư mục)*.
2. Mở Terminal và chạy lệnh:
   ```bash
   python build_due_html.py
   ```
3. Hệ thống sẽ **tự động đọc file Excel và nhúng trực tiếp danh sách thật vào lõi của file `index.html`**.

---

### 📋 Cấu trúc các cột trong file Excel danh sách chuẩn:
   - **3 dòng cấu hình đầu bảng (tùy chỉnh quy mô hội trường):**
     * `Số dãy Đại biểu`: Nhập số dãy VIP (ví dụ: `4`, `3`, `2`).
     * `Vị trí dãy NCS`: Nhập mã vị trí (ví dụ: `4-R`, `4-L`, `4`, `3, 4-R`, `3-R, 4-R`).
     * `Số dãy Người thân`: Nhập số dãy người thân (ví dụ: `5`, `6`, `3`).
   - **Các dòng tân khoa & tiến sĩ:**
   - Cột `Vị trí ghế`: Số nguyên `1, 2, 3...` chỉ vị trí ô ghế trên sơ đồ (Dãy 5 gồm vị trí 1–18, Dãy 6 gồm vị trí 19–36...). **Để trống** đối với Tân Tiến sĩ (`TS1`).
   - Cột `Số ghế`: Nhãn số ghế thực tế hiển thị trên ô ghế và bảng vinh danh (ví dụ: `TS1`, hoặc `1, 3, 4, 5, 7, 8...` không cần liên tục).
   - Cột `Họ tên`: Họ và tên đầy đủ của người học.
   - Cột `Trình độ`: Chọn 1 trong 3 giá trị `Tiến sĩ`, `Thạc sĩ`, `Đại học` (tự động đổi khung vinh danh tương ứng).
   - Cột `Loại ghế` *(tùy chọn)*: Ghi `Khen thưởng`, `Thạc sĩ`, `Cử nhân`, hoặc `Tiến sĩ` nếu muốn chỉ định trực tiếp màu ô ghế. Nếu để trống, hệ thống tự động tô màu theo `Tiến sĩ > Khen thưởng > Thạc sĩ > Cử nhân`.
   - Cột `Khen thưởng`: Đánh dấu `x` hoặc `Có` (hoặc để trống nếu không khen thưởng).
   - Cột `Ghi chú` *(tùy chọn)*: Ngành học hoặc thông tin bổ sung.
2. Mở Terminal và chạy lệnh:
   ```bash
   python build_due_html.py
   ```
3. Hệ thống sẽ **tự động đọc file Excel và nhúng trực tiếp danh sách thật vào lõi của file `index.html`**.
4. Giờ đây bạn chỉ việc copy duy nhất file **`index.html`** sang máy tính/TV hội trường, mở lên là vinh danh ngay lập tức!

---

## 🚀 3. Hướng dẫn sử dụng & Phím tắt

- **Mở giao diện:** Nhấp đúp chuột vào file `index.html` để mở trên bất kỳ trình duyệt nào (Microsoft Edge, Google Chrome, Cốc Cốc, Firefox).
- **Phím `F` hoặc nút `⛶ Trình chiếu`:** Bật chế độ toàn màn hình 1920 × 1080 (tự động ẩn thanh công cụ điều khiển để hiển thị sơ đồ trang trọng trên TV 43 inch hoặc màn hình LED). Nhấn lại `F` hoặc `ESC` để thoát.
- **Phím `E` hoặc nút `⚙ Cấu hình`:** Mở bảng điều khiển trượt để chỉnh tốc độ vinh danh và tùy chỉnh số lượng ghế phân bổ.
- **Phím tắt điều khiển vinh danh (Hỗ trợ Bút Clicker MC):**
  - `Phím Space`: Tạm dừng / Tiếp tục chạy vinh danh.
  - `Phím mũi tên phải` hoặc `PageDown`: Sang người kế tiếp (đồng bộ với MC xướng tên).
  - `Phím mũi tên trái` hoặc `PageUp`: Quay lại người trước.
  - `Phím Home`: Quay về người đầu tiên trong danh sách.
  - `Phím End`: Đến người cuối cùng trong danh sách.
  - `Phím 1`, `2`, `3`, `5`: Đổi nhanh tốc độ chạy `1s`, `2s`, `3s`, `5s`.
  - Kéo thả (Drag & Drop) trực tiếp file `.xlsx` hoặc `.csv` vào cửa sổ để nạp dữ liệu tức thì.
- **Tìm kiếm ghế nhanh:** Gõ nhãn **Số ghế** hiển thị trên sơ đồ (ví dụ: `1`, `3`, `7`, `235`...) vào ô **Ghế số:** trên thanh công cụ → Ghế được tìm sẽ phóng to 1.35x và nhấp nháy phát sáng vàng rực rỡ kèm thông báo dãy, khối và khu vực ghế.
- **Nút `✦ Hiệu ứng`:** Bật / Tắt pháo hoa canvas và dòng ánh sáng chuyển động khi cần.
- **Nút `📷 Xuất PNG`:** Xuất file ảnh sơ đồ độ phân giải siêu nét 1920 × 1080 về máy tính.

---

## ⚙ 4. Vị trí điều chỉnh cấu hình trong mã nguồn (`build_due_html.py`)

Nếu bạn muốn tùy biến mã nguồn thủ công trước khi biên dịch:

1. **Điều chỉnh tọa độ & kích thước cụm đồ họa `Congratulations.png`:**
   ```html
   <image href="{b64_congrats}" x="-60" y="915" width="570" height="190" preserveAspectRatio="xMidYMid meet" filter="url(#goldGlow)" pointer-events="none"/>
   ```
   - Tọa độ `x`: `0` là mép cực trái màn hình; điền số âm (vd: `-60`) để dịch lùi tiếp sang bên trái tràn nhẹ viền; điền số dương lớn (vd: `1560`) để chuyển sang góc phải.
   - Tọa độ `y`: `0` là mép trên; `915` là sát mép đáy.
   - Tỷ lệ kích thước chuẩn: `width / height ≈ 3 : 1`.

2. **Cấu hình quy mô lưới ghế động (`SEATS_PER_ROW`, `SEATS_PER_SIDE`, `MAX_SEAT_ROWS`, `APP_STATE.config`):**
   - Toàn bộ số lượng ghế, nhãn số ghế và màu từng ghế được quyết định tự động 100% từ file Excel.
   - Các hằng số hình học lưới ghế nằm trong `<script>`:
     ```javascript
     const SEATS_PER_ROW = 18;     // 9 ghế Khối Trái + 9 ghế Khối Phải mỗi dãy
     const SEATS_PER_SIDE = SEATS_PER_ROW / 2;
     const MAX_SEAT_ROWS = 20;     // Tối đa 20 dãy ghế (360 vị trí)
     // APP_STATE.config.vipRows: mặc định 4; dãy tân khoa đầu = vipRows + 1
     // APP_STATE.config.familyRows: mặc định 5; nối tiếp sau dãy tân khoa cuối
     ```

3. **Điều chỉnh tốc độ ánh sáng chạy trên mũi tên:**
   - Tìm class `.flow-stream` trong `<style>`:
     ```css
     animation: streamAnim 1.6s linear infinite; /* Thay đổi 1.6s để chạy nhanh hơn hoặc chậm hơn */
     ```

---

## 📌 5. Cấu trúc Repository sau khi dọn dẹp

```text
SodoGra/
├── background/                     # Đồ họa nghệ thuật gốc (Ảnh 1, Ảnh 2, Ảnh 3, Congratulations)
├── Khungvinhdanh/                  # 3 khung nền vinh danh gốc (Tiến sĩ, Thạc sĩ, Cử nhân)
├── sources/                        # Logo DUE, bảng màu, fonts SVN-Gilroy, thư viện xlsx
├── index.html                      # Ứng dụng chính thức (100% Single-File Offline độc lập)
├── build_due_html.py               # Master Compiler script đóng gói ứng dụng
├── capture_fw_shots.py             # Script xuất ảnh Full HD 1920x1080 tự động
├── Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx  # File mẫu Excel chuẩn
├── preview_1920x1080.png           # Ảnh chụp giao diện tổng thể mới nhất
├── preview_cunhan_award.png        # Ảnh chụp trạng thái vinh danh & khen thưởng mới nhất
├── so-do-cho-ngoi-2026.png         # Mockup cấu trúc chuẩn được đối chiếu xác nhận 100%
├── readme.md                       # Tài liệu hướng dẫn sử dụng & phím tắt (đã cập nhật)
├── AGENTS.md                       # Nhật ký kỹ thuật & vai trò chuyên gia (đã cập nhật)
└── *.b64.txt                       # 9 gói dữ liệu nhị phân cần thiết cho build_due_html.py
```

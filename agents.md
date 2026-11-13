# AGENTS ASSIGNMENT & ROLES: DỰ ÁN SƠ ĐỒ CHỖ NGỒI LỄ TỐT NGHIỆP 2026

## 1. Vai trò chuyên gia (Agents & Specialized Personas)
Dự án được tối ưu toàn diện dựa trên sự kết hợp của 3 vai trò chuyên môn cao cấp:

### 1.1. Senior Frontend Architect & SVG Specialist
- **Kiến trúc giải pháp:** Xây dựng ứng dụng đơn tệp (Single-File Offline) chuẩn HTML5/CSS3/SVG thuần, không phụ thuộc bất kỳ thư viện ngoài (CDN, Google Fonts, npm), đảm bảo khả năng chạy độc lập 100% trên mọi máy tính không có Internet.
- **Tối ưu hiển thị Digital Signage 16:9:** Thiết lập tỷ lệ ViewBox chuẩn `1920 × 1080` pixel (Full HD), không sinh thanh cuộn ngang/dọc, tự động co giãn thông minh (Responsive Proportional Scaling) khi thay đổi kích thước cửa sổ.
- **Tách bạch Vị trí ghế (`pos`) và Số ghế hiển thị (`seat`) — Sơ đồ Động theo Excel:**
  - `Vị trí ghế` (`1..N`): Quyết định vị trí ô ghế trên lưới hội trường (`20 ghế/dãy`, bắt đầu từ Dãy 5). Để trống đối với Tân Tiến sĩ (`TS1`).
  - `Số ghế`: Nhãn thực tế in lên ô ghế và bảng vinh danh, lấy nguyên văn từ Excel (không bắt buộc liên tục `1–280`; ví dụ `1, 3, 4, 5, 7, 8...`).
  - `Loại ghế`: Cột tùy chọn chỉ định màu ghế trực tiếp (`Khen thưởng` / `Thạc sĩ` / `Cử nhân` / `Tiến sĩ`), hoặc tự động suy ra theo thứ tự ưu tiên `Tiến sĩ > Khen thưởng > Thạc sĩ > Cử nhân`.
  - **Tự động tính số dãy ghế & đôn dãy Người thân:** Số dãy ghế `R = ceil(maxPos / 20)` (`Dãy 5 .. 5+R-1`), và 5 dãy `Người thân Tân TS/ThS/ĐH` tự động dịch nhãn nối tiếp (`5+R .. 5+R+4`), ví dụ 260 ghế → Ghế Dãy 5–17, Người thân Dãy 18–22 (tự động bỏ Dãy 23). Các vị trí thiếu hoặc dãy cuối chưa đủ 20 ghế được vẽ thành ô trống nét đứt mờ (`seat-empty`).
- **Động cơ Dữ liệu Excel Đa Tầng (Dual-Engine Data System):**
  - *Tải mẫu siêu tốc (0ms):* Nhúng trực tiếp tệp nhị phân Base64 vào HTML, tạo Blob tải về tức thì không phụ thuộc thư viện ngoài.
  - *Bộ phân tích ngoại tuyến (SheetJS Offline):* Nhúng trọn vẹn thư viện SheetJS vào tệp, hỗ trợ đọc file `.xlsx`, `.xls`, `.csv` tự động phân loại trình độ và khen thưởng.
  - *Tự động nhúng vĩnh viễn vào mã nguồn:* `build_due_html.py` tự động quét và nhúng danh sách tân khoa từ file Excel vào thẳng lõi file `index.html` khi biên dịch (chỉ cần copy duy nhất 1 file `index.html` mang đi trình chiếu).
  - *Bảo vệ dữ liệu tại hiện trường:* Tự động lưu danh sách nạp mới vào `localStorage` của trình duyệt máy chiếu để chống mất dữ liệu khi F5 hoặc sự cố điện.
- **Chế độ Trình chiếu TV 43" & LED:** Tích hợp phím tắt `F` / F11 kích hoạt chế độ toàn màn hình Native Fullscreen, tự động ẩn toolbar quản trị để biến màn hình thành bảng thông tin số trang trọng.

### 1.2. UI/UX Designer (Academic Ceremony & Digital Signage)
- **Định hướng phong cách:** *“Elegant Academic Ceremony / Premium Graduation Event Display”*.
- **Hệ thống màu sắc nhận diện thương hiệu DUE:**
  - Nền không gian: Xanh navy sâu thẳm (`#020a1c` đến `#0a2556`) phối dải lụa vàng kim uốn lượn phong cách hoàng gia.
  - Sân khấu: Xanh lam đậm viền kép kim loại vàng (`#ffea9f`), kẹp giữa là 2 bục "Cánh gà trái" và "Cánh gà phải" phân định rõ ràng.
  - Phân khu ghế: Xanh lá (Đại biểu), Đỏ đô (Tiến sĩ & NCS/GVHD), Vàng hoàng kim (Khen thưởng), Tím hoàng gia (Thạc sĩ), Cam tươi sáng (Cử nhân), Xám xanh thanh lịch (Người thân).
- **Tuân thủ 100% Mockup đã duyệt (`so-do-cho-ngoi-2026.png`):** Giữ nguyên hai khối ghế đối xứng, cột số dãy 1 đến 23 ở cả 2 bên, khu vực Đại biểu dãy 1–4, bảng Ghi chú chuẩn bên phải.
- **Chuẩn hóa nhãn khu vực Dãy 19–23:** Đổi chính xác thành **`Người thân Tân TS/ThS/ĐH`** (tại sơ đồ) và **`Ghế ngồi người thân \n Tân TS/ThS/ĐH`** (tại bảng Ghi chú).
- **Tối ưu hóa Bảng Vinh Danh Tân Khoa (Honors Plaque):**
  - Tự động thay đổi 3 khung nền đồ họa hoàng gia theo trình độ: `TanTiensi.png`, `TanThacsi.png`, `TanCunhan.png`.
  - Mở rộng biên độ 1 hàng tiệm cận khung viền vàng kim (~305px).
  - Cố định 100% cỡ chữ to chuẩn `20.5px` cho mọi tên hiển thị 1 hàng (lên tới 27 ký tự như *Dương Thị Thu Hường*, *Nguyễn Hoàng Minh Phương*).
  - Đồng nhất 100% cỡ chữ 2 dòng (`19.5px`) khi tên đặc biệt dài (> 27 ký tự) buộc phải xuống dòng.
  - Thẻ tên nằm ở lớp hiển thị trên cùng (`#topHonorsSvg`, `z-index: 20`) kèm bóng đổ đen sâu (`nameGlowDrop`), nổi hoàn toàn lên trên cành nguyệt quế và pháo hoa canvas.
- **UI/UX Khen thưởng Hoàng gia:** Dải ruy băng 3D đuôi én vàng kim, huy chương ngôi sao vàng, huy hiệu khắc nổi `★ KHEN THƯỞNG ★` (chiều rộng 136px tinh gọn vừa khít dưới tên) và hiệu ứng nhịp thở hào quang.
- **Đồ họa Chúc mừng Tốt nghiệp:** Chữ thư pháp 3D vàng kim kèm dải lụa hoàng gia `Congratulations.png` tại góc dưới, hỗ trợ tinh chỉnh tọa độ và kích thước linh hoạt.
- **Cụm WC và Lối vào tối giản:** Thiết kế mini SVG vector (không viền đen), đặt sát tuyến luồng mũi tên dọc tại `X = 390`.

### 1.3. Motion Graphics Designer
- **Hệ thống luồng di chuyển một chiều (Closed-Loop Circulation):**
  - Khối trái: Di chuyển ngang ra hành lang ngoài bên trái → đi dọc hành lang lên cánh gà bên trái → bước lên sân khấu nhận bằng.
  - Khối phải: Di chuyển ngang ra hành lang ngoài bên phải → đi dọc xuống phía cuối hội trường → vòng ngang qua phía cuối hội trường sang hành lang bên trái → tiến lên cánh gà bên trái nhận bằng.
  - Rời sân khấu: Sau khi nhận bằng, di chuyển sang cánh gà bên phải → rời sân khấu theo hành lang bên phải trở về chỗ ngồi.
  - Dòng hạt photon ánh sáng dạ quang (`flow-stream`) chuyển động liên tục dọc theo các tuyến đường theo đúng chiều di chuyển.
- **Động cơ Pháo hoa Hạt Vật lý Canvas thuần túy (100% Code):**
  - Rocket vàng kim phóng từ đỉnh khung vinh danh lên bầu trời phát nổ thành chùm hạt ánh sáng vàng kim (`#ffffff`, `#ffe082`, `#ffb300`, `#ffd700`).
  - Chuyển động vật lý thực tế: trọng lực (`gravity = 0.058`), lực cản không khí (`drag = 0.965`) kèm vệt đuôi ánh sáng lấp lánh (sparkling trails).
  - Loại bỏ hoàn toàn ảnh crop, nan hoa giả hay họa tiết nhân tạo; tên tân khoa luôn nổi lên trên pháo hoa.
- **Hiệu ứng xướng danh Tân Tiến sĩ (`TS1`):** Tự động phát hào quang vàng kim vào toàn bộ hàng ghế NCS, GVHD & Gia đình (Dãy 4 phải).

---

## 2. Nhật ký công việc hoàn thành
| Nhiệm vụ | Trạng thái | Ghi chú kỹ thuật |
|---|:---:|---|
| Khảo sát & Phân tích Mockup | ✅ Hoàn thành | Đối chiếu `so-do-cho-ngoi-2026.png` & `Mauthamkhao.png` |
| Tích hợp Brand Assets DUE | ✅ Hoàn thành | Logo DUE chính hãng, màu chuẩn PANTONE (Xanh dương, Xanh lá, Cam, Vàng), font SVN-Gilroy |
| Tái cấu trúc Viewport 1920×1080 | ✅ Hoàn thành | Căn giữa tuyệt đối trục X = 960 cho Sân khấu & 2 Khối ghế 280 chỗ |
| Chuẩn hóa WC & Lối vào (100% SVG) | ✅ Hoàn thành | Thiết kế mã SVG thuần mini, đặt sát mép hành lang X=390, loại bỏ viền đen và marker "Bạn đang ở đây" |
| Tinh gọn Bảng Ghi chú | ✅ Hoàn thành | Thu nhỏ thanh thoát ở góc phải, đổi câu chữ chuẩn: "Tân Thạc sĩ, Tân Cử nhân" |
| Cân bằng mũi tên Dãy 5 | ✅ Hoàn thành | Chiều dài mũi tên thoát ngang từ Dãy 5 sang 2 hành lang bằng nhau tuyệt đối (64px mỗi bên) |
| Làm sạch Sân khấu trung tâm | ✅ Hoàn thành | Loại bỏ hoàn toàn 2 mũi tên trên mặt sân khấu trung tâm để bảo đảm tính tôn nghiêm |
| Thảm đỏ danh dự trung tâm | ✅ Hoàn thành | Trải thảm đỏ nhung viền vàng kim kéo dài từ Dãy 1 (VIP) đến hết Dãy 23 (Người thân) |
| Tối ưu hiển thị 3 ảnh nghệ thuật | ✅ Hoàn thành | Sắp xếp Z-Order chuẩn: Pháo hoa (`Ảnh 3`), Mũ cử nhân (`Ảnh 2`), Giảng đường (`Ảnh 1`) hiển thị 100% trọn vẹn, không bị đè lấn |
| Tối ưu khoảng hở mũi tên Dãy 5 | ✅ Hoàn thành | Mũi tên ngang dãy 5 dừng trước mép hành lang dọc (cách 9px), triệt tiêu hoàn toàn sự đè lấn |
| Liền mạch luồng hành lang phải | ✅ Hoàn thành | Nối liền mạch dòng chảy từ Cánh gà phải xuống cuối hội trường, loại bỏ hoàn toàn khoảng hở đứt đoạn |
| Tối giản mũi tên định hướng | ✅ Hoàn thành | Mỗi tuyến chỉ duy nhất 1 đầu mũi tên định hướng (trái, phải, đáy) và 1 mũi tên vào Cánh gà trái |
| Tăng kích thước Background trường học | ✅ Hoàn thành | Tăng kích thước tòa nhà lên gấp 3, kéo sát đáy viền sơ đồ tạo điểm nhấn học thuật trang trọng |
| Bảng Vinh Danh Tân Khoa (Khung trái) | ✅ Hoàn thành | Tích hợp 3 khung nền TanTiensi.png, TanThacsi.png, TanCunhan.png tự động đổi theo trình độ |
| Cơ chế Nhập Excel Offline (SheetJS) | ✅ Hoàn thành | Nhúng trực tiếp SheetJS vào HTML, hỗ trợ đọc file .xlsx, .xls, .csv hoàn toàn offline không cần Internet |
| Auto-Play Spotlight Carousel | ✅ Hoàn thành | Tự động chạy tuần tự danh sách vinh danh (1s, 2s, 3s, 5s), phóng to và phát hào quang vào số ghế tương ứng |
| Quy tắc đặc biệt Tân Tiến sĩ (TS1) | ✅ Hoàn thành | Khi vinh danh TS1, tự động kích hoạt hiệu ứng phát sáng toàn bộ hàng ghế NCS, GVHD & Gia đình (Dãy 4 phải) |
| Mở rộng Khung nền trắng (Cân bằng lề 28px) | ✅ Hoàn thành | Mở rộng ngang (X=28..1892), lề trái = lề phải = lề dưới = 28px, ôm trọn Bảng Vinh Danh |
| Nâng cấp UI/UX Khen thưởng Hoàng gia | ✅ Hoàn thành | Dải ruy băng 3D đuôi én vàng kim, huy chương sao vàng, huy hiệu khắc nổi trên khung bằng, hiệu ứng hào quang |
| Hiệu ứng Pháo hoa đỉnh Khung Vinh Danh (100% Code) | ✅ Hoàn thành | Xóa bỏ ảnh crop và các họa tiết sao xoay/nan hoa, CHỈ GIỮ động cơ hạt Canvas vật lý thực tế (bắn lên & rớt xuống tự nhiên) |
| Thẻ Tên & Khung Vinh Danh Lớp Trên Cùng (Z-Index 20) | ✅ Hoàn thành | Đưa toàn bộ Khung vinh danh, tên người học và thẻ ghế lên lớp trên cùng (`#topHonorsSvg`, z-index: 20), nổi lên trên pháo hoa Canvas; rocket phóng từ đỉnh vòm (Y:230..250), đảm bảo tên tân khoa luôn sáng rõ 100% không bị che lấp |
| Cân bằng Tiêu đề & Dải lụa Header Liền mạch | ✅ Hoàn thành | Hạ dòng "SƠ ĐỒ CHỖ NGỒI" & nguyệt quế xuống Y=68, subtitle xuống Y=112 cân xứng; tái cấu trúc dải lụa vàng kim thành 100% vector SVG liền mạch (14px, viền kép, đổ bóng 3D), triệt tiêu hoàn toàn hiện tượng vỡ hình/đứt đoạn |
| Tối ưu Z-Order Pháo Hoa & Căn Giữa Tên Tân Khoa | ✅ Hoàn thành | Đưa chùm pháo hoa góc phải nổi lên trên dải lụa viền vàng; nâng họ tên người học trong khung vinh danh lên cao (Y=342/332), căn giữa tuyệt đối theo trục dọc |
| Chuẩn hóa Cấu trúc Excel & Khen thưởng | ✅ Hoàn thành | Tách riêng cột Trình độ (Tiến sĩ/Thạc sĩ/Đại học) & Khen thưởng (tick/x/có), tự động đồng bộ màu ghế |
| Hỗ trợ Bút Trình Chiếu MC (Clicker) | ✅ Hoàn thành | Tích hợp phím Space, PageDown/► (Next), PageUp/◄ (Prev), Home, End, 1/2/3/5 và kéo-thả Excel trực tiếp |
| Đồ họa Chúc mừng Tốt nghiệp (Congratulations.png) | ✅ Hoàn thành | Tích hợp chữ thư pháp 3D vàng kim và dải lụa hoàng gia, hỗ trợ tinh chỉnh tọa độ và kích thước linh hoạt |
| Khắc phục & Hoàn thiện Tải mẫu & Nhập Excel | ✅ Hoàn thành | Tải mẫu siêu tốc 0ms từ gói nhị phân Base64 nhúng sẵn, nhúng hoàn chỉnh SheetJS offline vào HTML |
| Tự động Nhúng Excel Vĩnh viễn vào index.html | ✅ Hoàn thành | `build_due_html.py` tự động đọc file Excel và nhúng danh sách thật vào lõi file HTML (chỉ cần copy duy nhất 1 file index.html mang đi) |
| Bộ nhớ Đệm Trình duyệt Chống Mất Dữ liệu | ✅ Hoàn thành | Tự động lưu danh sách nạp từ giao diện vào `localStorage`, tải lại trang không bị mất dữ liệu |
| Nâng cấp 4 Tốc độ Vinh Danh | ✅ Hoàn thành | Bổ sung đầy đủ 4 tùy chọn tốc độ: `1s` • `2s` • `3s` • `5s` kèm phím tắt số `1`, `2`, `3`, `5` |
| Tinh giản Bảng Cài đặt (Drawer) | ✅ Hoàn thành | Xóa bỏ 2 nút trùng lặp Nhập/Tải mẫu Excel khỏi Drawer, tập trung trên thanh Toolbar ngang trên cùng |
| Chuẩn hóa Tên gọi Người thân | ✅ Hoàn thành | Cập nhật nhãn Dãy 19–23 thành `Người thân Tân TS/ThS/ĐH` và Bảng Ghi chú thành `Ghế ngồi người thân \n Tân TS/ThS/ĐH` |
| Cố định 100% Cỡ chữ Tên Tân Khoa Chuẩn (20.5px) | ✅ Hoàn thành | Giữ nguyên 100% cỡ chữ lớn `20.5px` cho toàn bộ tên trên 1 hàng (lên tới 27 ký tự); đồng nhất 100% cỡ chữ 2 dòng (`19.5px`) nếu xuống hàng |
| Dọn dẹp & Tối ưu Repository | ✅ Hoàn thành | Xóa bỏ 16 tệp rác, code tạm, ảnh trùng lặp và ảnh test cũ (~10.5 MB), tối ưu hóa cây thư mục sạch sẽ |
| Tách bạch `Vị trí ghế` & `Số ghế` hiển thị | ✅ Hoàn thành | Cấu trúc Excel 7 cột (`Vị trí ghế`, `Số ghế`, `Họ tên`, `Trình độ`, `Loại ghế`, `Khen thưởng`, `Ghi chú`); hiển thị số ghế thực tế không cần liên tục (`1, 3, 4, 5, 7...`) |
| Tự động Co giãn Dãy ghế & Đôn Dãy Người thân | ✅ Hoàn thành | Tự tính `R = ceil(maxPos / 20)` dãy ghế (`Dãy 5 .. 5+R-1`) và tự dịch 5 dãy Người thân (`5+R .. 5+R+4`), bỏ dãy thừa (vd: 260 ghế → Ghế 5–17, Người thân 18–22) |
| Ô trống mờ (`seat-empty`) & Kiểm tra Dữ liệu | ✅ Hoàn thành | Vẽ ô nét đứt mờ cho các vị trí thiếu hoặc dãy cuối chưa đủ 20 ghế; hiển thị cảnh báo trùng/thiếu vị trí trong bảng Cài đặt (`#importIssues`) |
| Kiểm tra trực quan bằng Edge Headless & Playwright | ✅ Hoàn thành | Kiểm thử tự động kịch bản 280 ghế, 260 ghế, 255 ghế (lẻ dãy + thiếu vị trí), tìm kiếm theo nhãn số ghế và chụp ảnh Full HD 1920×1080 |
| Kiến trúc Sơ Đồ Ghế Động Thống Nhất | ✅ Hoàn thành | Tự động phân bổ co giãn 3 phân khu (Đại biểu, Tân khoa, Người thân) trong khung cố định Y=258..892 |
| Tùy chỉnh Dãy Đại biểu & Dãy Người thân | ✅ Hoàn thành | Nhập số dãy Đại biểu (1..6) và số dãy Người thân (1..10) từ Excel hoặc Drawer, tự động đôn số dãy nối tiếp |
| Cấu hình Dãy NCS Đa Dãy / Đa Phía (Multi-Slot) | ✅ Hoàn thành | Hỗ trợ 4-R, 4-L, 4 hoặc kết hợp nhiều dãy/bên (3, 4-R; 3-R, 4-R; 3, 4); phát hào quang vào toàn bộ vị trí khi vinh danh TS1 |
| Khối Thẻ Người thân Liền khối Tinh gọn | ✅ Hoàn thành | Loại bỏ hoàn toàn các vạch nét đứt phân tầng theo yêu cầu; khối thẻ Người thân xám xanh liền mạch thanh thoát, đồng bộ nhãn số dãy 2 bên |
| Tự động Căn giữa Mũi tên Thoát Ngang & Thảm đỏ | ✅ Hoàn thành | Mũi tên đỏ tự động căn giữa theo hàng tân khoa đầu tiên; thảm đỏ tự động chạm khít mép đáy khối Người thân |
| Nâng cấp Độ tương phản Drawer Cài đặt (E) | ✅ Hoàn thành | Đổi nhãn số dãy đại biểu & người thân sang chữ trắng sáng (#ffffff, font 800) kèm khung viền mờ tương phản cao |
| Quy hoạch Hình học Động Tối Đa 25 Dãy | ✅ Hoàn thành | Tự động phân bổ đồng đều nhịp bước hàng (h, step) cho cả 3 phân khu; 2 khoảng cách phân khu (Gap 1 = Gap 2 >= h/3) triệt tiêu hoàn toàn sự đè lấn giữa Dãy 18 và Người thân |
| Tinh Gọn Thẻ Khen Thưởng Bảng Vinh Danh | ✅ Hoàn thành | Đổi nội dung thành "KHEN THƯỞNG" (kèm 2 sao vàng ★), thu gọn chiều rộng từ 190px xuống 136px ôm khít vừa vặn dưới tên |
| Click Ô Ghế Chuyển Bảng Vinh Danh | ✅ Hoàn thành | Nhấp trực tiếp vào ô ghế bất kỳ trên sơ đồ (hoặc hàng NCS) để bảng vinh danh lập tức hiển thị chính xác tân khoa đó kèm hào quang spotlight |
| Nhập Số Di Chuyển Vinh Danh trong Cài Đặt (E) | ✅ Hoàn thành | Bổ sung ô nhập số ghế / số thứ tự / mã TS kèm nút '🎯 Đi tới' (hỗ trợ phím Enter) trong cụm điều khiển vinh danh của Drawer Cài đặt |
| Tiện Ích Cập Nhật Danh Sách Gốc (1-Click .bat) | ✅ Hoàn thành | Tạo tệp Cap_Nhat_Danh_Sach.bat hỗ trợ kéo-thả hoặc tự nhận danhsach.xlsx, biên dịch vĩnh viễn vào lõi index.html |
| Dọn Dẹp Toàn Diện Repository (3.0+ MB) | ✅ Hoàn thành | Xóa bỏ 5 tệp rác & bản backup lỗi thời (MASTER_PROJECT.md, ảnh test preview, script test cũ, txt tạm), tối ưu hóa repo sạch sẽ 100% |
| Tinh Chỉnh Tốc Độ & Bảng Ghi Chú | ✅ Hoàn thành | Đổi tốc độ vinh danh mặc định thành 3s (từ 5s); đổi nhãn Bảng Ghi chú thành 'Ghế ngồi Cá nhân được tuyên dương, khen thưởng' |
| Auto-Fit Ruy Băng Khen Thưởng Đa Màn Hình | ✅ Hoàn thành | Nới rộng khoảng cách giữa 2 ngôi sao (cx=32/266), tinh chỉnh font 11.2px/letter-spacing 0.3; tích hợp động cơ JS tự động co tỉ lệ (auto-scale) khi mở trên màn hình hoặc font khác, triệt tiêu hoàn toàn lỗi đè chữ |

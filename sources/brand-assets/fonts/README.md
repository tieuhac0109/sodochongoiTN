# DUE Brand Fonts

## Mục đích

Thư mục này lưu bộ font thương hiệu tham chiếu dùng cho public UI của dự án `Chuyentruong`.

Hiện đã phát hiện bộ font:

- `SVN-Gilroy Regular.otf`
- `SVN-Gilroy Medium.otf`
- `SVN-Gilroy SemiBold.otf`
- `SVN-Gilroy Bold.otf`
- `SVN-Gilroy XBold.otf`
- `SVN-Gilroy Heavy.otf`
- `SVN-Gilroy Black.otf`
- các biến thể `Thin`, `Light`, `Xlight`
- các biến thể `Italic`

Ngoài ra có 1 tệp:

- `Tải nhiều font Việt hóa khác tại đây.url`

Tệp `.url` không phải là font runtime của dự án, chỉ là liên kết tham khảo.

## Quy ước sử dụng đề xuất

Cho public UI, ưu tiên dùng ít weight để giữ giao diện sạch và ổn định:

- **Body text**: `SVN-Gilroy Regular`
- **UI emphasis / label / button**: `SVN-Gilroy Medium`
- **Section heading / card title**: `SVN-Gilroy SemiBold`
- **Hero heading / branding emphasis**: `SVN-Gilroy Bold` hoặc `SVN-Gilroy XBold`

Không nên dùng quá nhiều weight trong cùng một màn hình.

## Ghi chú triển khai

- Chỉ dùng bộ font này khi đã xác nhận quyền nhúng web/app là phù hợp.
- Nếu áp dụng vào frontend, nên tạo một sprint riêng để:
  1. import font có chọn lọc;
  2. map weight rõ ràng;
  3. kiểm tra hiển thị tiếng Việt;
  4. đo ảnh hưởng tới kích thước tải trang.

## Trạng thái hiện tại

Thư mục này đang đóng vai trò **nguồn brand asset tham chiếu**.
Chưa mặc định có nghĩa là toàn bộ public UI đã dùng `SVN-Gilroy`.

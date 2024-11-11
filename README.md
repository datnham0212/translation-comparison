### Tóm tắt quá trình phát triển project

#### Mô tả Project:
- Đánh giá mức độ tương đồng của 2 bản dịch tiếng Việt.
- Mục tiêu: Xác định mức độ giống nhau giữa hai văn bản.
- Ví dụ: So sánh hai tệp phụ đề srt của một bộ phim (en & vn), dịch bản en bằng Google Dịch rồi đối chiếu với bản vn.

#### Cài đặt các thư viện cần thiết:
- Sử dụng các thư viện như Flask, python-dotenv, nltk, scikit-learn, transformers, torch.

#### Cấu hình ứng dụng:
- Tạo file config.py để cấu hình các biến môi trường và thư mục upload.

#### Tạo ứng dụng Flask:
- Tạo file run.py để khởi chạy ứng dụng Flask.

#### Xử lý và tính toán tương đồng văn bản:
- Tạo file utils.py để xử lý văn bản và tính toán độ tương đồng cosine giữa hai đoạn văn bản.

#### Xây dựng các route cho ứng dụng:
- Tạo file route.py để xử lý các yêu cầu từ người dùng, upload file và tính toán độ tương đồng.

### Cách thức chạy chương trình

#### Cài đặt các thư viện cần thiết:
- Thiết lập biến môi trường:<br/>
    - Tạo file .env và thêm các biến môi trường cần thiết (ví dụ: SECRET_KEY).

#### Chạy ứng dụng Flask:
- Truy cập ứng dụng:<br/>
    - Mở trình duyệt và truy cập http://127.0.0.1:5000/ để sử dụng ứng dụng.



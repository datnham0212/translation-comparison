### Tóm tắt quá trình phát triển project

#### Mô tả Project:
- Đánh giá mức độ tương đồng của 2 phụ đề En - Vn từ 1 bộ phim.
- Input: 2 tệp srt (phụ đề tiếng Anh và tiếng Việt).
- Output: Độ tương đồng cosine giữa các đoạn văn bản.

#### Cài đặt các thư viện cần thiết:
Các thư viện được sử dụng trong dự án này bao gồm:

- **Flask**: Flask là một micro-framework Python cho phép xây dựng ứng dụng web một cách nhanh chóng và dễ dàng. Trong dự án này, Flask được sử dụng để xây dựng một API cho phép người dùng tải lên các tệp phụ đề và nhận về độ tương đồng giữa chúng.

- **python-dotenv**: Thư viện này giúp quản lý các biến môi trường trong dự án. Các thông tin như API keys hoặc cấu hình cần thiết có thể được lưu trữ trong file .env và truy cập qua thư viện này.

- **nltk (Natural Language Toolkit)**: NLTK là một thư viện mạnh mẽ giúp xử lý ngôn ngữ tự nhiên, cung cấp các công cụ để phân tích cú pháp, tách từ (tokenize), gán nhãn từ loại và các nhiệm vụ khác. Trong dự án này, NLTK giúp xử lý và làm sạch các văn bản từ phụ đề.

- **scikit-learn**: Thư viện này cung cấp các thuật toán học máy và công cụ phân tích dữ liệu, đặc biệt là các phương pháp tính toán độ tương đồng giữa các đối tượng. Dự án sử dụng scikit-learn để tính toán độ tương đồng cosine giữa các đặc trưng văn bản đã được mã hóa.

- **transformers**: mBERT (Multilingual BERT) là một mô hình học sâu được huấn luyện trên dữ liệu đa ngôn ngữ, bao gồm cả tiếng Anh và tiếng Việt. Thư viện transformers của Hugging Face cho phép sử dụng mBERT để trích xuất các đặc trưng ngữ nghĩa từ văn bản mà không cần phải dịch các phụ đề từ tiếng Anh sang tiếng Việt (hoặc ngược lại). Đây là một bước quan trọng để so sánh các phụ đề của 2 ngôn ngữ khác nhau mà không làm mất thông tin ngữ nghĩa.

- **torch (PyTorch)**: PyTorch là một thư viện học sâu phổ biến, hỗ trợ các mô hình học máy và học sâu. Trong dự án này, PyTorch hỗ trợ việc sử dụng mBERT để tính toán các đặc trưng từ văn bản và hỗ trợ các mô hình học sâu khác nếu cần.

#### Cấu hình ứng dụng:
- Tạo file config.py để cấu hình các biến môi trường và thư mục upload tệp phụ đề.

#### Tạo ứng dụng Flask:
- Tạo file run.py để khởi chạy ứng dụng Flask, cho phép người dùng tải tệp phụ đề và nhận kết quả tính toán độ tương đồng.

#### Xử lý và tính toán tương đồng văn bản:
- Tạo file utils.py để xử lý các văn bản phụ đề, chuyển đổi chúng thành các vector đặc trưng sử dụng mBERT, và tính toán độ tương đồng cosine giữa hai đoạn văn bản.

#### Xây dựng các route cho ứng dụng:
- Tạo file route.py để xử lý các yêu cầu từ người dùng, bao gồm việc tải lên các tệp phụ đề và tính toán độ tương đồng giữa chúng.

### Các bước thực hiện dự án

#### Tiền xử lý dữ liệu:
- Đọc và phân tích các tệp phụ đề .srt.
- Làm sạch dữ liệu bằng cách loại bỏ các thông tin không cần thiết (chẳng hạn như các mốc thời gian và chỉ mục).

#### Mã hóa văn bản:
- Sử dụng mBERT (Multilingual BERT) để chuyển đổi các câu trong phụ đề thành các vector đặc trưng.
- mBERT sẽ giúp đồng bộ hóa các đặc trưng từ cả tiếng Anh và tiếng Việt mà không cần phải dịch giữa hai ngôn ngữ.

#### Tính toán độ tương đồng:
- Sau khi có các vector đặc trưng, sử dụng cosine similarity từ thư viện scikit-learn để tính toán độ tương đồng giữa các câu trong phụ đề.
- Độ tương đồng cosine sẽ cho biết mức độ tương đồng ngữ nghĩa giữa hai câu, giúp đánh giá mức độ giống nhau giữa các phụ đề tiếng Anh và tiếng Việt.

#### Xây dựng API với Flask:
- Tạo một API đơn giản cho phép người dùng tải lên hai tệp phụ đề.
- Xử lý và trả về kết quả độ tương đồng cosine giữa các câu của hai phụ đề.

#### Hiển thị kết quả:
- Người dùng sẽ nhận được kết quả dưới dạng điểm số tương đồng, từ đó có thể đánh giá mức độ khớp giữa hai phụ đề.

### Cách thức chạy chương trình

#### Cài đặt các thư viện cần thiết:
- Thiết lập các biến môi trường:
    - Tạo file .env và thêm các biến môi trường cần thiết (ví dụ: SECRET_KEY).

- Cài đặt các thư viện:
    - Sử dụng pip để cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```

#### Chạy ứng dụng Flask:
- Truy cập ứng dụng:
    - Mở terminal và chạy ứng dụng Flask:
    ```bash
    python run.py
    ```
    - Sau khi ứng dụng chạy, mở trình duyệt và truy cập http://127.0.0.1:5000/ hoặc localhost:5000 để sử dụng ứng dụng, tải lên các tệp phụ đề và nhận kết quả độ tương đồng giữa chúng.
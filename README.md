Đánh giá mức độ tương đồng của 2 bản dịch tiếng việt <br />
Mục tiêu: Xác định mức độ giống nhau giữa hai văn bản. <br />
Ví dụ Input: Hai tệp phụ đề 1 bộ phim (en & vn), dịch bản en bằng google dịch rồi đối chiếu với bản vn <br />
Ví dụ Output: Điểm số thể hiện mức độ tương đồng giữa 2 bản dịch tiếng việt - 1 do người dịch, 1 do từ google dịch (ví dụ: 80%). <br />

Kế hoạch: <br />
1. Sử dụng thư viện python googletrans để dịch phụ đề tiếng anh
2. So sánh sự tương đồng giữa bản dịch ở bước 1 với bản phụ đề tiếng việt đã có sẵn (sử dụng 1 trong số các phương pháp <br />
   như là khoảng cách Levenshtein hoặc BLEU hoặc tương đồng Cosine

Đánh giá mức độ tương đồng của 2 bản dịch tiếng việt <br />
Mục tiêu: Xác định mức độ giống nhau giữa hai văn bản. <br />
Ví dụ Input: Hai tệp phụ đề 1 bộ phim (en & vn), dịch bản en bằng google dịch rồi đối chiếu với bản vn <br />
Ví dụ Output: Điểm số thể hiện mức độ tương đồng giữa 2 bản dịch tiếng việt - 1 do người dịch, 1 do từ google dịch (ví dụ: 80%). <br />

Kế hoạch: <br />
1. Sử dụng thư viện python googletrans để dịch phụ đề tiếng anh sang tiếng việt
2. Sử dụng thư viện underthesea hoặc pyvi để áp dụng lemmatization hoặc stemming cho cả 2 bản dịch tiếng việt
3. So sánh sự tương đồng giữa 2 bản dịch tiếng việt (sử dụng 1 trong số các phương pháp <br />
   như là khoảng cách Levenshtein hoặc BLEU hoặc tương đồng Cosine <br />

ChatGPT hướng dẫn: https://chatgpt.com/share/670b3afa-163c-800c-9563-b6568d58bd3a

from transformers import pipeline
from nltk.tokenize import sent_tokenize

# Hàm để xử lý văn bản sau khi dịch 
def post_processing(text):
    try:
        # Dịch văn bản sử dụng pipeline của Hugging Face
        translated_text = transformer(text, max_length=40)[0]['translation_text']
    except Exception as e:
        print(f"Dịch thất bại: {e}")
        return text  # Trả về văn bản gốc nếu dịch thất bại
    
    return translated_text

# Hàm để chia đoạn văn thành các câu
def split_paragraph(paragraph):
    return sent_tokenize(paragraph)

# Hàm để loại bỏ "vi" ở đầu câu, nếu có
def remove_vi_at_beginning(translated_text):
    if translated_text.startswith("vi"):
        return ' '.join(translated_text.split()[1:])
    return translated_text

if __name__ == '__main__':
    # Tải mô hình dịch từ Hugging Face
    transformer = pipeline("translation", model="VietAI/envit5-translation")

    # Đoạn văn mẫu
    sample_paragraph = "I (19M) was going home from university, and to get home, I have to use the train."

    # Chia đoạn văn mẫu thành các câu
    sentences = split_paragraph(sample_paragraph)

    for sentence in sentences:
        # Dịch và xử lý sau khi dịch
        translated_text = post_processing(sentence)
        print(f"Gốc: {sentence}\nĐã dịch: {translated_text}\n")

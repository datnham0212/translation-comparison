from transformers import pipeline
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

# Hàm để xử lý văn bản sau khi dịch 
def post_processing(text):
    try:
        # Dịch văn bản sử dụng pipeline của Hugging Face
        translated_text = transformer(text, max_length=40)[0]['translation_text']
    except Exception as e:
        print(f"Dịch thất bại: {e}")
        return text  # Trả về văn bản gốc nếu dịch thất bại
    
    return translated_text

    # Loại bỏ từ lặp lại và "vi" ở đầu câu nếu có
    # translated_text = avoid_repetition(translated_text)
    # return remove_vi_at_beginning(translated_text)

# Hàm để chia đoạn văn thành các câu
def split_paragraph(paragraph):
    return sent_tokenize(paragraph)

# Hàm để xác định các động từ
# def get_verbs(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    verbs = [word for word, tag in tagged_words if tag.startswith('VB')]
    return verbs

# Hàm để tránh lặp lại từ
# def avoid_repetition(translated_text):
    # Sử dụng từ duy nhất trong bối cảnh thay vì từ lặp lại
    words = translated_text.split()
    seen_words = set()
    result = []

    # Lấy danh sách các động từ từ văn bản đã dịch
    verbs = get_verbs(translated_text)

    for word in words:
        if word not in seen_words:
            seen_words.add(word)
            result.append(word)
        # Nếu từ là động từ, giữ lại ngay cả khi nó đã xuất hiện
        elif word in verbs:
            result.append(word)

    # Nối các từ lại thành một câu
    return ' '.join(result)

# Hàm để loại bỏ "vi" ở đầu câu, nếu có
def remove_vi_at_beginning(translated_text):
    if translated_text.startswith("vi"):
        return ' '.join(translated_text.split()[1:])
    return translated_text

if __name__ == '__main__':
    # Tải mô hình dịch từ Hugging Face
    transformer = pipeline("translation", model="VietAI/envit5-translation")

    # Đoạn văn mẫu
    sample_paragraph = "I (19M) was going home from university, and to  get home, I have to use the train."

    # Chia đoạn văn mẫu thành các câu
    sentences = split_paragraph(sample_paragraph)

    for sentence in sentences:
        # Dịch và xử lý sau khi dịch
        translated_text = post_processing(sentence)

        print(f"Gốc: {sentence}\nĐã dịch: {translated_text}\n")

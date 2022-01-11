from transformers import pipeline
from nltk.tokenize import sent_tokenize

def split_paragraph(paragraph):
    sentences = sent_tokenize(paragraph)
    return sentences

def avoid_repetition(text):
    translated_text = transformer(text, max_length=40)[0]['translation_text']
    
    # Tách câu thành các từ
    words = translated_text.split()

    # Tạo 1 set để lưu các từ đã xuất hiện
    seen_words = set()

    # Tạo 1 list chứa kết quả không lặp lại từ để trả về
    result = []

    # Duyệt qua các từ trong câu
    for word in words:
        if word not in seen_words:
            seen_words.add(word)
            result.append(word)
    
    return ' '.join(result)

def remove_vi_at_beginning(translated_text):
    return ' '.join(translated_text.split()[1:])
    

if __name__ == '__main__':
    # Tải model phiên dịch từ Hugging Face
    transformer = pipeline("translation", model="VietAI/envit5-translation")

    paragraph = "This happened last week, and while she didn't seem malicious, the things she said was creepy. I (19M) was going home from university, and to get home, I have to use the train."

    for sentence in split_paragraph(paragraph):
        translated_text = avoid_repetition(sentence)
        translated_text = remove_vi_at_beginning(translated_text)
        print(f"Original: {sentence}\nTranslated: {translated_text}\n")

            

from transformers import pipeline

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

    sentences = [
        # "It's never too late to learn something new.",
        # "Knowledge is power.",
        # "Every day is a new beginning.",
        # "The journey of a thousand miles begins with a single step.",
        # "Believe in yourself and all that you are."
        # "It's never too late to do the right thing.",
        # "The only way to do great work is to love what you do.",
        # "The only limit to our realization of tomorrow will be our doubts of today.",
        # "The best way to predict the future is to create it.",
        # "The only thing we have to fear is fear itself.",
        # "Doing the right thing is never easy."
        "Hello world",
        "Greetings fellow travellers",
        "What are you talking about?",
        "That's just pure balooney"
    ]

    for sentence in sentences:
        translated_text = avoid_repetition(sentence)
        translated_text = remove_vi_at_beginning(translated_text)
        print(f"Original: {sentence}\nTranslated: {translated_text}\n")

            

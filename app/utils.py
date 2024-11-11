import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch

# Tải dữ liệu cần thiết của NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    """
    Làm sạch văn bản đầu vào bằng cách loại bỏ các thẻ HTML, dấu thời gian, số và khoảng trắng thừa.
    Chuyển văn bản thành chữ thường.
    """
    text = re.sub(r'<.*?>', '', text)  # Loại bỏ các thẻ HTML
    text = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', text)  # Loại bỏ dấu thời gian
    text = re.sub(r'\d+', '', text)  # Loại bỏ các số (chỉ mục)
    text = text.lower()  # Chuyển thành chữ thường
    text = re.sub(r'\s+', ' ', text)  # Loại bỏ khoảng trắng thừa
    return text

def process_subtitles(file_path):
    """
    Xử lý tệp phụ đề bằng cách làm sạch văn bản, tách thành các câu,
    và lemmatize các từ trong khi loại bỏ các từ dừng.
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
    
    text = clean_text(text)  # Làm sạch văn bản
    sentences = sent_tokenize(text)  # Tách thành các câu
    lemmatizer = WordNetLemmatizer()
    processed_sentences = []
    
    for sentence in sentences:
        words = word_tokenize(sentence)  # Tách thành các từ
        # Lemmatize các từ và loại bỏ các từ dừng
        words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
        processed_sentences.append(' '.join(words))  # Ghép các từ lại thành câu
    
    return processed_sentences

def calculate_similarity(paragraph1, paragraph2):
    """
    Tính toán độ tương đồng cosine giữa hai đoạn văn bản sử dụng BERT embeddings.
    """
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    model = AutoModel.from_pretrained("bert-base-multilingual-cased")

    def get_embeddings(text):
        """
        Lấy BERT embeddings cho văn bản đầu vào.
        """
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        outputs = model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).detach().numpy()

    embedding1 = get_embeddings(paragraph1)  # Lấy embeddings cho đoạn văn bản thứ nhất
    embedding2 = get_embeddings(paragraph2)  # Lấy embeddings cho đoạn văn bản thứ hai

    # Tính toán độ tương đồng cosine giữa hai embeddings
    cosine_similarities = cosine_similarity(embedding1, embedding2)
    
    return cosine_similarities[0][0]

def get_paragraphs(sentences):
    """
    Kết hợp danh sách các câu thành một đoạn văn bản.
    """
    return ' '.join(sentences)
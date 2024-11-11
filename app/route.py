from flask import Blueprint, request, render_template, redirect, url_for
from app.utils import process_subtitles, calculate_similarity, get_paragraphs
import os
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)

def allowed_file(filename):
    """
    Kiểm tra xem tệp có phần mở rộng hợp lệ hay không.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'srt', 'sub', 'txt'}

@main.route('/', methods=['GET', 'POST'])
def index():
    """
    Xử lý yêu cầu GET và POST cho trang chủ.
    """
    if request.method == 'POST':
        # Lấy các tệp được tải lên từ form
        file1 = request.files['file1']
        file2 = request.files['file2']
        
        # Kiểm tra xem các tệp có hợp lệ không
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            # Bảo mật tên tệp và lưu vào thư mục uploads
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            file1_path = os.path.join('uploads', filename1)
            file2_path = os.path.join('uploads', filename2)
            file1.save(file1_path)
            file2.save(file2_path)
            
            print(f"File 1 saved to: {file1_path}")
            print(f"File 2 saved to: {file2_path}")
            
            # Xử lý các tệp phụ đề
            subtitles1 = process_subtitles(file1_path)
            subtitles2 = process_subtitles(file2_path)
            
            print(f"Processed subtitles 1: {subtitles1[:5]}")  # In ra 5 câu đầu tiên để debug
            print(f"Processed subtitles 2: {subtitles2[:5]}")  # In ra 5 câu đầu tiên để debug
            
            # Kết hợp các câu thành đoạn văn bản
            paragraph1 = get_paragraphs(subtitles1)
            paragraph2 = get_paragraphs(subtitles2)
            
            print(f"Paragraph 1: {paragraph1[:100]}")  # In ra 100 ký tự đầu tiên để debug
            print(f"Paragraph 2: {paragraph2[:100]}")  # In ra 100 ký tự đầu tiên để debug
            
            # Tính toán độ tương đồng giữa hai đoạn văn bản
            similarity = calculate_similarity(paragraph1, paragraph2)
            
            print(f"Cosine Similarity: {similarity}")
            
            # Trả về kết quả và hiển thị trên trang web
            return render_template('index.html', similarity=similarity, paragraph1=paragraph1, paragraph2=paragraph2)
    
    # Hiển thị trang chủ
    return render_template('index.html')
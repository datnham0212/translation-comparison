from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle file uploads
        first_file = request.files.get("first_file")
        second_file = request.files.get("second_file")

        if first_file and second_file:
            first_file_path = os.path.join(app.config['UPLOAD_FOLDER'], first_file.filename)
            second_file_path = os.path.join(app.config['UPLOAD_FOLDER'], second_file.filename)
            
            # Save the files
            first_file.save(first_file_path)
            second_file.save(second_file_path)
            
            # Redirect to a comparison route (to be implemented)
            return redirect(url_for('compare', first=first_file.filename, second=second_file.filename))

    return render_template("index.html")

@app.route("/compare")
def compare():
    # For now, just return a basic message
    return "Comparison feature to be implemented"

if __name__ == "__main__":
    app.run(debug=True)

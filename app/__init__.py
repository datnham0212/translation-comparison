from flask import Flask

# Create the Flask app inside a function to avoid circular imports
def create_app():
    app = Flask(__name__)
    
    # Import routes after creating the app to prevent circular imports
    from app.route import main
    app.register_blueprint(main)

    # Other app configurations (e.g., database, extensions)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    
    return app

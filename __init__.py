from flask import Flask

def create_app():
    app = Flask(__name__)

    # Secret key dibutuhkan untuk session
    app.secret_key = 'tubes_rahasiakan_ini'  # Ganti ke string acak yang lebih aman di produksi

    # Import dan register blueprint
    from .routes import main
    app.register_blueprint(main)

    return app

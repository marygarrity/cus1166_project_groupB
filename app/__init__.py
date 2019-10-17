from flask import Flask, current_app
from config import Config
from flask_sqlalchemy import SQLAchemy

def create_app():
    app = Flask(__name__)
    from app.models import db
    app.config.from_object(Config)
#Create DB everytime "flask run" entered

    with app.test_request_context():
        db.init_app(app)
        db.create_all()

    from app.main import bp as main_routes_bp
    app.register_blueprint(main_routes_bp)
    return app

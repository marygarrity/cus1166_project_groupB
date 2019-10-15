from app import create_app
app = create_app()

import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy #pip install Flask-SQLAlchemy
from config import Config #ModuleNotFoundError: No module named 'config'
#do we need a config.py ?
from models import * #ModuleNotFoundError: No module named 'models'
#do we need a models.py ?

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    cars = db.execute("SELECT * from courses")
    return render_template('index.html', cars = cars)

def main():
    if (len(sys.argv) == 2):
        print(sys.argv)
        if sys.argv[1] == 'createdb':
            db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'p dcz'")

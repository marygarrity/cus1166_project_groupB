from flask import blueprint
from app.auth import routes

bp = Blueprint('auth',__name__)

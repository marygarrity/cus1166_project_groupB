from app.main import bp
from flask import render_template


@bp.route('/', methods=['GET','POST'])
def index():
    return render_template("<insert template_name.html>")

@bp.route('/2ndPage', methods=['GET','POST'])
def index():
    return render_template("<insert template_name2.html>")    

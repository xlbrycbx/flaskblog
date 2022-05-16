from flask import Blueprint, render_template

user_bp1 = Blueprint('user1',__name__,url_prefix='/user')

@user_bp1.route('/')
def index():
    return render_template('base.html')
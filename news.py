from flask import Blueprint
news_bp = Blueprint('news', __name__,url_prefix='/news')

@news_bp.route('/')
def news():
    return "<p> **** This is the news ****</p>"

@news_bp.route('/global')
def news_global():
    return "<p> **** This is the global news ****</p>"
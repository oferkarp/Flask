from flask import Blueprint , render_template
news_bp = Blueprint('news', __name__,url_prefix='/news')

@news_bp.route('/')
def news():
    return render_template("news.html")
    # return "<p> **** This is the news ****</p>"

@news_bp.route('/global')
def news_global():
    return "<p> **** This is the global news ****</p>"
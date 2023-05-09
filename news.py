from flask import Blueprint , render_template
news_bp = Blueprint('news', __name__,url_prefix='/news')

@news_bp.route('/')
def news():
    new_arr = [1,2,3,4,5,6,7,8,9,10]
    return render_template("news.html",my_array = new_arr)
    # return "<p> **** This is the news ****</p>"

@news_bp.route('/global')
def news_global():
    return "<p> **** This is the global news ****</p>"
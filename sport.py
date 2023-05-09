from flask import Blueprint
sport_bp = Blueprint('sport', __name__,url_prefix='/sport')

@sport_bp.route('/')
def sport():
    return "<p> **** This is the sport ****</p>"

@sport_bp.route('/global')
def sport_global():
    return "<p> **** This is the global sport ****</p>"
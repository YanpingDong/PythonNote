from flask import Blueprint

user_bt = Blueprint('user', __name__, url_prefix='/u')

@user_bt.route('/profile/')
def Profile():
    return '个人中心'

@user_bt.route('/settings/')
def settings():
    return '设置页面'
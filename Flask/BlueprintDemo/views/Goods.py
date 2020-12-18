from flask import Blueprint

goods_bt = Blueprint('goods', __name__, url_prefix='/g')

@goods_bt.route('/detail/')
def Profile():
    return '详情页面'

from flask import Flask
from views import User,Goods

app = Flask(__name__)

app.register_blueprint(User.user_bt)
app.register_blueprint(Goods.goods_bt)


@app.route('/')
def index():
    return '首页'

if __name__ == '__main__':
    app.run()
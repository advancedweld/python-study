# https://flask.github.net.cn/quickstart.html
# https://flask.palletsprojects.com/en/stable/quickstart/
# Run: 1. $env:FLASK_APP="src/flask/hello.py" 
#     2. flask run
#  设置调试模式，方便自动更新：. flask run --debug
from flask import Flask

from flask import request

app = Flask(__name__)

print('hello, world', __name__)
@app.route('/')
def hello_world():
    return 'Hello, Xiangshangzhi!'



from markupsafe import escape

@app.route("/<name>")
def hello(name):
    print('@@@rquest:', request)
    return f"Hello, name {escape(name)}!"


# 转换器： int-接受正整数
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


# 指定HTTP方法
@app.post('/login')
def login_post():
    return do_the_login()


def do_the_login():
    return 'login'
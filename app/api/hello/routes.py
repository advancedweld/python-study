from flask import Blueprint, request, jsonify
from markupsafe import escape
from .services.auth_service import login_user

hello_bp = Blueprint('hello', __name__)


@hello_bp.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, Xiangshangzhi!'})



@hello_bp.route("/<name>")
def helloNmae(name):
    print('@@@rquest:', request)
    return f"Hello, name {escape(name)}!"




@hello_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    token = login_user(email, password)
    return jsonify({'token': token})
from flask import Blueprint, request, jsonify

hello_bp = Blueprint('hello', __name__)


@hello_bp.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, Xiangshangzhi!'})
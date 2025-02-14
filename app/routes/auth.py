from flask import Blueprint, request, jsonify
from app.services.auth_service import login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    token = login_user(email, password)
    return jsonify({'token': token})


@auth_bp.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})
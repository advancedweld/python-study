from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

from markupsafe import escape
from .services.auth_service import login_user
from .services.user_service import Register



hello_bp = Blueprint('hello', __name__)

api = Api(hello_bp)

class Hello(Resource):
    def get(self):
        return {'message': 'Hello,  my Xiangshangzhi!'}

api.add_resource(Hello, '/')

api.add_resource(Register, '/register')


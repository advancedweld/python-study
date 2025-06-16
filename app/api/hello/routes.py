from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

from markupsafe import escape
# from .services.auth_service import login_user
from .services.user_register_service import Register

from .services.user_login_service import Login
from .services.user_list_service import UserList

from .services.file_upload import FileUpload


hello_bp = Blueprint('hello', __name__)

api = Api(hello_bp)

class Hello(Resource):
    def get(self):
        return {'message': 'Hello,  my Xiangshangzhi!'}

api.add_resource(Hello, '/')

api.add_resource(Register, '/user/register')

api.add_resource(Login, '/auth/login', '/auth/refreshToken')

api.add_resource(UserList, '/user/all')


api.add_resource(FileUpload, '/file/upload')
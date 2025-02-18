import uuid

from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from ..models.user import UserModel


class Register(Resource):
  def post(self):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, location='json')
    parser.add_argument('password', type=str, dest='pwd', location='json')
    data = parser.parse_args()
    print('@@@@row data',   data)
    if UserModel.find_by_username(data['username']):
      return {
        'success': False,
        'message': "用户名已存在",
        'data': None,
       }, 400
    else: 
      try:
        # 创建用户对象
        user = UserModel(username=data['username'])
        user.set_password(data['pwd'])  # 设置密码
        user.addUser()
        return {
          'success': True,
          'message': "Register succeed!",
          'data': None,
         }, 200
      except Exception as e:
        return {
          'success': False,
          'message': "Error: {}".format(e),
          'data': None,
         }, 500


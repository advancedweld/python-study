from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

from ..models.user import UserModel
from ....utils.common import res_common


class Login(Resource):
  def post(self):
    # 初始化解析器
    parser = reqparse.RequestParser()
    # 添加请求参数校验
    parser.add_argument('userName', type=str, location='json')
    parser.add_argument('password', type=str, dest='pwd', location='json')
    data = parser.parse_args()
    username = data['userName']
    user_all = UserModel.query.all()
    
    # 打印所有用户名
    print("所有用户列表:")
    for user in user_all:
        print(f"用户名: {user.username}")
    
    print("@@@@user_all",user_all)
    user_tuple = UserModel.find_by_username(username)
    print("@@@@user_tuple",user_tuple)
    if user_tuple:
      try:
        (user,) = user_tuple
        pwd_row = data['pwd']
        valid = user.check_password(pwd_row)
        if valid:
          # 生成 token 
          response_data = generateToken(username)
          # 添加用户角色信息到返回数据中
          response_data['userInfo'] = {
            'username': user.username,
            'role': user.role
          }
          return res_common(response_data)
        else:
          raise ValueError('Invalid password!')
      except Exception as e:
        return res_common(success=False, message='Error: {}'.format(e), code=500)
    else:
      return res_common(success=False, message='用户命不存在!', code=400)


  def get(self):
    # access_token 过期后 需要用 refresh_token 来换取新的 token
    # 先从 refresh_token 中取出用户信息
    current_username = get_jwt_identity()
    print('@@@@@current_username', current_username)
    # 再生成新的 token
    access_token = create_access_token(identity=current_username)
    
    # 获取用户信息
    user_tuple = UserModel.find_by_username(current_username)
    if user_tuple:
      (user,) = user_tuple
      return res_common(data={
        'accessToken': 'Bearer ' + access_token,
        'userInfo': {
          'username': user.username,
          'role': user.role
        }
      })
    return res_common(data={'accessToken': access_token})

# 生成token
def generateToken(id):
  access_token = create_access_token(identity=id)
  refresh_token = create_refresh_token(identity=id)
  return {
    'accessToken':  access_token,
    'refreshToken':  refresh_token,
   }

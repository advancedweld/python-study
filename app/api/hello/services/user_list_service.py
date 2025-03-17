from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.user import UserModel
from ....utils.common import res_common

class UserList(Resource):
    @jwt_required()
    def get(self):
        # 获取当前用户身份
        current_username = get_jwt_identity()
        
        # 查找当前用户
        user_tuple = UserModel.find_by_username(current_username)
        if not user_tuple:
            return res_common(success=False, message='用户不存在', code=404)
        
        (current_user,) = user_tuple
        
        # 检查用户角色是否为管理员
        if current_user.role != 'admin':
            return res_common(success=False, message='权限不足', code=403)
        
        # 获取所有用户
        users = UserModel.query.all()
        user_list = []
        
        # 构建用户列表数据
        for user in users:
            user_data = {
                'id': user.id,
                'username': user.username,
                'role': user.role
            }
            user_list.append(user_data)
        
        return res_common(data={
            'total': len(user_list),
            'items': user_list
        }) 
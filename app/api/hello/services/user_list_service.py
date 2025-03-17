from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.user import UserModel
from ....utils.common import res_common

class UserList(Resource):
    @jwt_required()
    def get(self):
        # 获取当前用户身份
        current_username = get_jwt_identity()
        print("@@@@current_username",current_username)
        # 查找当前用户
        user_tuple = UserModel.find_by_username(current_username)
        if not user_tuple:
            return res_common(success=False, message='用户不存在', code=404)
        
        (current_user,) = user_tuple
        print("@@@@current_user",current_user)
        # 检查用户角色是否为管理员
        if current_user.role != 'admin':
            return res_common(success=False, message='权限不足', code=403)
        
        # 获取所有用户
        users = UserModel.query.all()
        user_list = []
        
        # 使用 UserModel.dict() 方法构建用户列表数据
        for user in users:
            user_data = user.dict()
            # 添加角色信息，因为原始的 dict() 方法中没有包含角色
            user_data['role'] = user.role
            # 将 datetime 对象转换为字符串
            if 'created_at' in user_data and user_data['created_at']:
                user_data['created_at'] = user_data['created_at'].strftime('%Y-%m-%d %H:%M:%S')
            if 'updated_at' in user_data and user_data['updated_at']:
                user_data['updated_at'] = user_data['updated_at'].strftime('%Y-%m-%d %H:%M:%S')
            user_list.append(user_data)
        
        return res_common(data={
            'total': len(user_list),
            'items': user_list
        }) 
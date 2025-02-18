from ..models.user import UserModel
from app.utils.jwt_utils import JWTUtils

def login_user(email, password):
    user = UserModel.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return JWTUtils.reate_tokens(user.id)
    return None
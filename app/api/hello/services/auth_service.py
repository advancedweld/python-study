from ..models.user import User
from app.utils.jwt_utils import JWTUtils

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return JWTUtils.reate_tokens(user.id)
    return None
from app.models.user import User
from app.utils.jwt_utils import generate_token

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return generate_token(user.id)
    return None
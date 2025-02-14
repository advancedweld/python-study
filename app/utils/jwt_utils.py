from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from flask_jwt_extended.exceptions import JWTExtendedException

class JWTUtils:
    @staticmethod
    def create_tokens(identity, additional_claims=None):
        """
        生成 JWT Token（Access Token 和 Refresh Token）

        :param identity: 用户标识（通常是用户 ID 或用户名）
        :param additional_claims: 额外的声明（字典形式）
        :return: 包含 access_token 和 refresh_token 的字典
        """
        access_token = create_access_token(
            identity=identity,
            expires_delta=timedelta(hours=1),  # Access Token 过期时间
            additional_claims=additional_claims
        )
        refresh_token = create_refresh_token(
            identity=identity,
            expires_delta=timedelta(days=7)  # Refresh Token 过期时间
        )
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    @staticmethod
    def decode_token(token):
        """
        解码 JWT Token

        :param token: JWT Token
        :return: 解码后的 Token 数据
        """
        try:
            return decode_token(token)
        except JWTExtendedException as e:
            raise ValueError(f"Invalid token: {str(e)}")

    @staticmethod
    def get_current_user():
        """
        获取当前用户标识（从 JWT Token 中提取）

        :return: 用户标识（通常是用户 ID 或用户名）
        """
        try:
            verify_jwt_in_request()  # 验证请求中是否包含有效的 JWT
            return get_jwt_identity()
        except JWTExtendedException as e:
            raise ValueError(f"Invalid token: {str(e)}")

    @staticmethod
    def refresh_access_token():
        """
        刷新 Access Token（使用 Refresh Token）

        :return: 新的 Access Token
        """
        try:
            identity = get_jwt_identity()
            return create_access_token(identity=identity, expires_delta=timedelta(hours=1))
        except JWTExtendedException as e:
            raise ValueError(f"Invalid token: {str(e)}")
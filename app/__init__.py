from flask import Flask
from flask_cors import CORS
from app.config import config
from app.api import init_api
from flask_jwt_extended import JWTManager

from app.database import db, migrate 

def create_app(config_name):
    # print('@__name__', __name__)
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    print('@@@app:',config[config_name])
    print('@@@appconfig:',app.config)
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, supports_credentials=True)
    # 注册API路由
    init_api(app)

     # 初始化 JWT
    jwt = JWTManager(app)

    return app
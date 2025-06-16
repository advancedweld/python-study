import os
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
    # 设置上传目录为项目根目录下的 uploads 文件夹
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads-content')

    app.config['MAX_CONTENT_LENGTH'] = 2000 * 1024 * 1024  # 2000MB
    # 可选：限制最大上传文件大小，比如5MB
    # app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

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
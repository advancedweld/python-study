from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config
from app.api import init_api

db = SQLAlchemy()
# 初始化数据库迁移工具
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # 注册蓝图

    # from app.routes.user import user_bp
    # 注册API路由
    init_api(app)
    # app.register_blueprint(user_bp)

    return app
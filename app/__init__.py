from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

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
    from app.routes.auth import auth_bp
    # from app.routes.user import user_bp
    app.register_blueprint(auth_bp)
    # app.register_blueprint(user_bp)

    return app
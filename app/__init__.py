from flask import Flask
from flask_cors import CORS
from app.config import config
from app.api import init_api


from app.database import db, migrate  # 从 extensions 导入 db 和 migrate

# print('@@@Config:', config)

def create_app(config_name):
    # print('@__name__', __name__)
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    print('@@@app:',config[config_name])
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
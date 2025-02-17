from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 初始化扩展
db = SQLAlchemy()
migrate = Migrate()
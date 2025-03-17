from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

from datetime import datetime
class UserModel(db.Model):
  """
   用户表
   """
  __tablename__ = 'users'

  # 主键 id
  id = db.Column(db.Integer(), primary_key=True, nullable=False, autoincrement=True, comment='主键ID')
  # 用户名
  username = db.Column(db.String(80), unique=True, nullable=False, comment='用户姓名')
  # 密码 可能会比较长，这里最大长度设置255
  pwd = db.Column(db.String(255), comment='密码')
  # salt
  salt = db.Column(db.String(32), comment='salt')
  # 创建时间
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now, comment='创建时间')
  # 更新时间
  updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')
  # 添加角色字段，默认为'user'，管理员为'admin'
  role = db.Column(db.String(20), default='user', nullable=False)

  # 新增用户
  def addUser(self):
    db.session.add(self)
    db.session.commit()

  # 用户字典
  def dict(self):
    return {
      "id": self.id,
      "username": self.username,
      "created_at": self.created_at,
      "updated_at": self.updated_at,
     }
  
  # 按 username 查找用户 返回一个元组(user,)
  @classmethod
  def find_by_username(cls, username):
    return db.session.execute(db.select(cls).filter_by(username=username)).first()

   # 返回所有用户
  @classmethod
  def get_all_user(cls):
    return db.session.query(cls).all()


   # 密码设置：加盐并加密
  def set_password(self, password):
      self.salt = uuid.uuid4().hex  # 生成一个新的盐值
      self.pwd = generate_password_hash(f'{self.salt}{password}')  # 使用盐值加密密码

    # 密码校验
  def check_password(self, password):
      return check_password_hash(self.pwd, f'{self.salt}{password}')


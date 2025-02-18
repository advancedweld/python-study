from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128))

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
    


from datetime import datetime
class UserModel(db.Model):
  """
   用户表
   """
  __tablename__ = 'user'

  # 主键 id
  id = db.Column(db.Integer(), primary_key=True, nullable=False, autoincrement=True, comment='主键ID')
  # 用户名
  username = db.Column(db.String(40), nullable=False, default='', comment='用户姓名')
  # 密码
  pwd = db.Column(db.String(102), comment='密码')
  # salt
  salt = db.Column(db.String(32), comment='salt')
  # 创建时间
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now, comment='创建时间')
  # 更新时间
  updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')

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
  
  # 获取密码和 salt
  def getPwd(self):
    return {
      "pwd": self.pwd,
      "salt": self.salt,
     }

  # 按 username 查找用户
  @classmethod
  def find_by_username(cls, username):
    return db.session.execute(db.select(cls).filter_by(username=username)).first()

   # 返回所有用户
  @classmethod
  def get_all_user(cls):
    return db.session.query(cls).all()




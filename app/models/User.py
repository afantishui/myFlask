from flask_login import UserMixin
from .. import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True)  # 用户名
    password = db.Column(db.String(50))  # 密码
    nickname = db.Column(db.String(50))  # 昵称
    email = db.Column(db.String(50))  # e-mail
    birthday = db.Column(db.DateTime)  # 生日
    gender = db.Column(db.Integer)  # 性别
    moblie = db.Column(db.Integer)  # 手机
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))  # 外键指向roles表中的id列

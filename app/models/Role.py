from .. import db


class Role(db.Model):  # 需继承模型
    __tablename__ = 'roles'  # db中表明，如果不设置，则会与class同的默认名
    id = db.Column(db.Integer, primary_key=True)  # SQLAlchemy要求必须有主键，一般命名为id即可
    name = db.Column(db.String(50), unique=True)  # 表示name为字符串，不重复
    users = db.relationship("User", backref='role')  # 关联user模型，并在user中添加反向引用(backref)

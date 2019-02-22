# _*_ coding:utf-8 _*_
from flask import Flask, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_script import Manager
import pymysql
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Afanti!@#$824144294@47.107.208.146:3306/myFlask?charset=utf8mb4'  # 配置链接字符串
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 配置请求结束后更改自动提交
db = SQLAlchemy(app)
manager = Manager(app)
pymysql.install_as_MySQLdb()
migrate = Migrate(app, db)  # 配置迁移
manager.add_command('db', MigrateCommand)  # 配置迁移命令


@app.route('/hello/')
@app.route('/hello/<name>')
def show_user(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    return render_template('index.html', site_name='肥肥')


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def loginPost():
    username = request.form.get("username", type=str, default=None)
    password = request.form.get("password", type=str, default=None)
    user = User.query.filter_by(username=username, password=password).first()  # 数据查询
    if user is not None:
        session['user'] = username
        print(username)
        print(password)
        session["user"] = username
        return render_template("/index.html", name=username, site_name='肥肥')
    else:
        print(username)
        print(password)
        flash("您输入的用户名或密码错误")
        return render_template("login.html")  # 返回的仍为登录页


class Role(db.Model):  # 需继承模型
    __tablename__ = 'roles'  # db中表明，如果不设置，则会与class同的默认名
    id = db.Column(db.Integer, primary_key=True)  # SQLAlchemy要求必须有主键，一般命名为id即可
    name = db.Column(db.String(50), unique=True)  # 表示name为字符串，不重复
    users = db.relationship("User", backref='role')  # 关联user模型，并在user中添加反向引用(backref)


class User(db.Model):
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


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    manager.run()

# @app.route('/login', methods=['GET'])
# def login():
#     html = "<form method='post'>" \
#            "<table>" \
#            "<tr><td>请输入用户名</td><td><input type='text' name='username'/></td></tr>" \
#            "<tr><td>请输入密码</td><td><input type='password' name='password'/></td></tr>" \
#            "<tr><td><input type='submit' value='登录'/></td></tr>" \
#            "</table>" \
#            "</post>"
#     return html

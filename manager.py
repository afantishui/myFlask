# _*_ coding:utf-8 _*_
from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_script import Manager
import pymysql
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask_login import UserMixin
from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, DateField, TextAreaField
from wtforms.validators import Length,DataRequired,Optional, EqualTo, Email


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

login_manager = LoginManager()
login_manager.session_protection = 'strong'  # 可设置为None，basic，strong已提供不同的安全等级
login_manager.login_view = 'login'  # 设置登录页
login_manager.init_app(app)  # flask-login初始化配置 注入current_user


# 登录表单
class LoginForm(FlaskForm):
    username = StringField("请输入用户名", validators=[DataRequired()])
    password = PasswordField("请输入密码")
    remember_me = BooleanField("记住我")  # BooleanField默认为多选按钮
    submit = SubmitField("登录")


# 注册表单
class RegisterForm(FlaskForm):
    username = StringField("请输入用户名", validators=[DataRequired()])
    password = PasswordField("请输入密码", validators=[DataRequired()])
    repassword = PasswordField("确认密码", validators=[EqualTo("password")])
    nickname = StringField("昵称")
    birthday = DateField("出生日期")
    email = StringField("邮箱地址", validators=[Email()])
    gender = RadioField("性别", choices=[("0", "男"), ("1", "女")], default=0)
    mobile = StringField("手机号")
    submit = SubmitField("提交")

@app.route('/hello/')
@app.route('/hello/<name>')
def show_user(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    return render_template('index.html', site_name='肥肥')


# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username, password=password).first()
        if user is not None:
            session["user"] = username
            login_user(user, form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash("您输入的用户名或密码错误")
            return render_template('login.html', form=form)  # 返回首页
    return render_template('login.html', form=form)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


# @app.route("/login", methods=['POST'])
# def loginPost():
#     username = request.form.get("username", type=str, default=None)
#     password = request.form.get("password", type=str, default=None)
#     user = User.query.filter_by(username=username, password=password).first()  # 数据查询
#     if user is not None:
#         session['user'] = username
#         print(username)
#         print(password)
#         session["user"] = username
#         return render_template("/index.html", name=username, site_name='肥肥')
#     else:
#         print(username)
#         print(password)
#         flash("您输入的用户名或密码错误")
#         return render_template("login.html")  # 返回的仍为登录页

# 注册路由
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.password = form.password.data
        user.birthday = form.birthday.data
        user.email = form.email.data
        user.gender = form.gender.data
        user.nickname = form.nickname.data
        user.moblie = form.mobile.data
        user.role_id = 1  # 暂时约定公开用户角色为1
        db.session.add(user)
    return render_template("register.html", form=form)
    # # 判断,其中用户名,密码,昵称不能为空
    # if(len(user.username.strip()) == 0):
    #     flash("用户名不能为空")
    #     return render_template("/register.html")
    # if (len(user.password.strip()) == 0):
    #     flash("用户密码不能为空")
    #     return render_template("/register.html")
    # if (len(user.nickname.strip()) == 0):
    #     flash("用户昵称不能为空")
    #     return render_template("/register.html")
    # if (len(user.moblie.strip()) == 0):
    #     flash("用户手机不能为空")
    #     return render_template("/register.html")
    # flash("您已注册成功")



# 回调函数，使用指定的标识符加载用户
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):  # 需继承模型
    __tablename__ = 'roles'  # db中表明，如果不设置，则会与class同的默认名
    id = db.Column(db.Integer, primary_key=True)  # SQLAlchemy要求必须有主键，一般命名为id即可
    name = db.Column(db.String(50), unique=True)  # 表示name为字符串，不重复
    users = db.relationship("User", backref='role')  # 关联user模型，并在user中添加反向引用(backref)


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

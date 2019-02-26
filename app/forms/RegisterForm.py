from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, DateField
from wtforms.validators import DataRequired, EqualTo, Email


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

# _*_ coding:utf-8 _*_
from flask import Flask, render_template, request, session, flash

from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123456'


@app.route('/hello/')
@app.route('/hello/<name>')
def show_user(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    return render_template('index.html', site_name='肥肥')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def loginPost():
    username = request.form.get("username", type=str, default=None)
    password = request.form.get("password", type=str, default=None)

    if username == "test" and password == "123456":
        print(username)
        print(password)
        session["user"] = username
        return render_template("/index.html", name=username, site_name='肥肥')
    else:
        print(username)
        print(password)
        flash("您输入的用户名或密码错误")
        return render_template("login.html")  # 返回的仍为登录页


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

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
from . import auth
from .. import db, login_manager
from ..forms.LoginForm import LoginForm
from ..models.User import User
from flask_login import login_user, logout_user
from flask import render_template, flash, redirect, url_for


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print(url_for("main.index"))
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(User)
        user = User.query.filter_by(username=username, password=password).first()
        if user is not None:
            login_user(user, form.remember_me.data)
            print(url_for("main.index"))
            return redirect(url_for("main.index"))
        else:
            flash("您输入的用户名或密码错误")
            return render_template("/auth/login.html", form=form)  # 返回的仍为登录页
        return redirect(url_for("main.index"))
    return render_template("/auth/login.html", form=form)


@auth.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

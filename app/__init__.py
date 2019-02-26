# _*_ coding:utf-8 _*_
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymysql
pymysql.install_as_MySQLdb()
from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = Config.LOGIN_PROTECTION
    login_manager.login_view = Config.LOGIN_VIEW
    db.init_app(app)
    # 蓝本进行注册
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)  # 无url前缀
    app.register_blueprint(auth_blueprint, url_prefix="/auth")  # url前缀为/auth
    return app

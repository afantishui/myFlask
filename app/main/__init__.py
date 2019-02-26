# _*_ coding:utf-8 _*_
from flask import Blueprint

main = Blueprint("main", __name__)  # 创建蓝本
from . import errors, views

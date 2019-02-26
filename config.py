# _*_ coding:utf-8 _*_
class Config:
    SECRET_KEY = "123456"  # 密钥
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Afanti!@#$824144294@47.107.208.146:3306/myFlask?charset=utf8mb4'  # 配置链接字符串
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 配置请求结束后更改自动提交
    LOGIN_PROTECTION = 'strong'  # 可设置为None，basic，strong已提供不同的安全等级
    LOGIN_VIEW = 'login'  # 设置登录页

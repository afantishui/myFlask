# myFlask
自学--一个基于flask的web应用诞生<br>
<br>
## 环境
系统:linux<br>
语言:python<br>
框架:flask<br>
模块:flask-bootstrap <br>
### 连接数据库
使用模块:<br>
flask-sqlalchemy SQLAlchemy数据库框架的flask集成包<br>
flask-script flask命令行脚本扩展 <br>
PyMySQL库<br>
flask-migrate   数据库迁移插件<br>
mysql连接字符串  ‘mysql://[user]:[password]@[domain]:[por]/[dbname]’
<br>
## 安装
```python
pip install Flask  # 安装flask
```
```python
pip install flask-bootstrap  #安装flask-bootstrap模块
```
## 运行
```python
# python manager.py
python manager.py runserver
```
登录页http://47.107.208.146:5000/login<br>
### 问题小记
1.RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.<br>
解决：
加入  app.config['SECRET_KEY'] = '123456'<br>

2.liunx上有两个python 一个2.7 一个3.5，安装pip install flask-bootstrap 时会默认安装到2.7上，用3.5版本运行时报错
解决：
方法一: 未安装前切换python的版本
先查看当前python版本  
python --version<br>
如果是2.7执行
alias python='/usr/bin/python3'<br>
然后再安装
pip install flask-bootstrap<br>

方法二：已经安装在2.7上面，重新再安装一个<br>
执行pip3 install flask-bootstrap<br>
如果没有pip3执行 apt install python3-pip进行安装<br>

3.使用shell建立数据库表OperationalError: (pymysql.err.OperationalError) (2003, "Can't connect to MySQL server on 'localhost' ([WinError 10061] 由于目标计算机积极拒绝，无法连接。)
") (Background on this error at: http://sqlalche.me/e/e3q8)<br>
解决：服务器上面没有mysql  <br>
重新安装一个https://blog.csdn.net/Erice_s/article/details/80021718<br>

4.使用flask-script模块让flask支持命令行脚本使用manager.run代替app.run()；本地执行python default.py runserver时正常，上传到linux就会访问不了<br>
解决：<br>
cd /usr/local/lib/python3.5/dist-packages/flask_script<br>
vim commands.py<br>
把host='127.0.0.1'改成'0.0.0.0'(使用/host搜索)<br>


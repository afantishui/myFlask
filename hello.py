# _*_ coding:utf-8 _*_
from flask import Flask, url_for
app=Flask(__name__)


# @app.route('/')
# def hello_world():
#     return "Hello World"
#
#
# @app.route('/user/<name>')
# def show_user(name):
#     return "user is %s" % name
@app.route('/')
def index():pass


@app.route('/login')
def login():pass


@app.route('/user/<username>')
def profile(username):pass


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__=='__main__':
    
    app.run(host='0.0.0.0',port=5000)

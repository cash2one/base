# -*- coding:utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

# 路由
#@app.route('/')
@app.route('/index/')
def hello1():
    return "Hello World!"
# URL 变量
@app.route('/user/<username>')
def show_user_profile(username):
    return "User %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id
# 唯一 URLs 重定向行为
@app.route('/projects/')
def projects():
    return "The project page"

@app.route('/about') # 访问时如果url后带‘/’,则返回404 “Not Found” 错误
def about():
    return "The about page"

# 构建url

# HTTP 方法
@app.route('/login1',methods=['GET','POST'])
def login1():
    if request.method == 'POST':
        return 'POST!'
    else:
        return 'GET!'

# 静态文件
from flask import url_for
#url_for('static', filename='style.css')

# 渲染模板
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

# 请求对象
@app.route('/login2',methods=['GET','POST'])
def login2():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            return log_the_uer_in(request.form['username'])
        else:
            error = "Invalid username/password"
    return render_template('login.html',error=error)

# 文件上传
from werkzeug import secure_filename
@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('./'+secure_filename(f.filename))

# 重定向和错误
from flask import abort, redirect, url_for
@app.route('/')
def re_index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(404)
    this_is_never_executed()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

# -*- coding:utf-8 -*-

from flask.ext.wtf import Form
from wtforms import IntegerField, HiddenField, PasswordField, TextField, ValidationError, SubmitField
from wtforms.validators import required

class LoginForm(Form):
    username = TextField(validators=[required(u"用户名不能为空")])
    password = PasswordField(validators=[required(u"密码不能为空")])

    remember = TextField()
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    username = TextField(validators=[required(u"用户名不能为空")])
    password = PasswordField(validators=[required(u"密码不能为空")])

    remember = TextField()
    submit = SubmitField('Register')
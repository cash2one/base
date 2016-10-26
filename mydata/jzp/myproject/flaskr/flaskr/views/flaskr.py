# -*- coding:utf-8 -*-
from flask import request, session, redirect, url_for, \
     abort, render_template, flash, Module

from . import instance
import sys
from colander import SchemaNode, MappingSchema, SequenceSchema
from colander import Int,Float, Date, String, Bool, DateTime
from ..models.models import Entries,Users
from ..extensions import db
from ..authutil import login
from ..froms import LoginForm, RegistrationForm
from flask.ext.login import login_user

@instance.route('/')
def show_entries():

    entries = Entries.query.order_by('title').all()
    return render_template("show_entries.html", entries=entries)
    #return "".join(sys.path)


@instance.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    title = request.form['title']
    text = request.form['text']

    entries = Entries(
        title=title,
        text=text
    )
    db.session.add(entries)
    db.session.commit()
    db.session.flush()
    #db.execute('insert into entries (title, text) values (?, ?)',[request.form['title'],request.form['text']])
    #db.commit()
    flash('New entry was sucessfully posted')
    return redirect(url_for('instance.show_entries'))

################ 登录 ######################
class UserLoginSchema(MappingSchema):

    username = SchemaNode(String())
    password = SchemaNode(String())

@instance.route('/login', methods=['GET','POST'])
def login():
    '''
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error = "Invalid username"
        elif request.form['password'] != 'admin':
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash("You were logged in")
            return redirect(url_for("instance.show_entries"))
    return render_template('login.html',error=error)
    '''

    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        #user = Users.query.filter_by(username=request.form['username'])
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(url_for("instance.show_entries"))
        flash('Invalid username or password.')
    return render_template('login.html',form=form)


    '''
    data = UserLoginSchema().deserialize(request.values.to_dict())
    username = str(data['username'])
    password = data['password']
    ua, auth = Users.auth(username, password)
    if not auth:
        flash('ERROR')
        return redirect(url_for('instance.login'))
    user = Users.query.get_or_404(ua.id)
    login(user)
    return redirect(url_for("instance.show_entries"))
    '''

@instance.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('instance.login'))
    return render_template('register.html', form=form)


@instance.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('instance.show_entries'))








#if __name__== "__main__":
#    app.debug = True
#    app.run()



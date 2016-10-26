# -*- coding:utf-8 -*-
import os
import sys

curr_path = os.path.normpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
sys.path.insert(0, curr_path)


from flask.ext.script import Manager, prompt_bool # flask-scipt 扩展包，可以 ## python manager.py --help #有选项
from flask.ext.script import Server
from flaskr import create_app
from flaskr.extensions import db
from flaskr.configs import APP_CONFIG
from flaskr.models.models import Users

app = create_app(APP_CONFIG)


manager = Manager(app)


@manager.command
def create_all():
    if prompt_bool("Are you sure? You will init your database"):
        db.create_all()
        user = Users(
            username = 'jia',
            password = 'jiazhipeng'
        )
        db.session.add(user)
        db.session.commit()


manager.add_command('runserver', Server())
if __name__ == "__main__":
    app.debug = True
    app.use_debugger = True
    manager.run()
    print sys.path
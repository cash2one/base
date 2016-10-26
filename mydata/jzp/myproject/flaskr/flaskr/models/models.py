from sqlalchemy import func
from sqlalchemy import Column, Text, String, Integer
from werkzeug.security import check_password_hash
from flaskr.extensions import db


class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=100)
    title = db.Column(db.String(100))
    text = db.Column(db.String(500))


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=100)
    username = db.Column(db.Unicode(50), unique=True, nullable=False)
    password = db.Column(db.String(100))

    @staticmethod
    def auth(username, password):
        ua = db.session.query(Users).filter(Users.username==username).first()
        if ua:
            auth = True if check_password_hash(ua.password, password) else False
        else:
            auth = False
        return ua, auth

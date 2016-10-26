from flask import session


def login(user):
    session['curr_id'] = user.id
    session['name'] = user.username

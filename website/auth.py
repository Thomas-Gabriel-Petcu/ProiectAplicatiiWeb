from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/signup')
def signup():
    return "<p>signup</p>"

@auth.route('/signin')
def signin():
    return "<p>signin</p>"

@auth.route('/signout')
def signout():
    return "<p>signout</p>"
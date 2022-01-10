from flask import Blueprint, render_template, request

auth = Blueprint('auth',__name__)

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('floatingUsername')
        email = request.form.get('floatingEmail')
        password1 = request.form.get('floatingPassword1')
        password2 = request.form.get('floatingPassword2')

        if len(username) <2:
            print("Username was too short")
        elif password1 != password2:
            print("passwords did not match")
        else:
            print("Added user to database")

    return render_template("signup.html")

@auth.route('/signin', methods=['GET','POST'])
def signin():
    return render_template("login.html")

@auth.route('/signout', methods=['GET','POST'])
def signout():
    return "<p>signout</p>"
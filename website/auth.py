from flask import Blueprint, render_template, request, redirect

auth = Blueprint('auth',__name__)
from website.functions import get_db_conn, db, create_user, get_user_credentials, get_user_profile_info

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        form = request.form
        conn = get_db_conn(db)
        create_user(conn, form)
        conn.close()
        #username = request.form.get('floatingUsername')
        #email = request.form.get('floatingEmail')
        #password1 = request.form.get('floatingPassword1')
        #password2 = request.form.get('floatingPassword2')
        #weight = request.form.get('floatingWeight')
        #height = request.form.get('floatingHeight')
        #age = request.form.get('floatingAge')

        #if len(username) <2:
        #    print("Username was too short")
        #elif password1 != password2:
        #    print("passwords did not match")
        #elif weight == 0:
        #    print("Weight cannot be 0")
        #elif age < 14:
        #    ("You need to be older than 14")
        #else:
        #    print("Added user to database")

    return render_template("signup.html")

@auth.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        form = request.form
        email = form.get("floatingEmail")
        password = form.get("floatingPassword")
        conn = get_db_conn(db)
        user = get_user_credentials(conn, email)
        conn.close()
        if user[1] == password:
            print("logged in")
            destination = "http://127.0.0.1:5000/profile/" + f"{user[0]}"
            return redirect(destination)
        else:
            raise Exception("Failed to log in, passwords did not match")
    return render_template("login.html")


@auth.route("/profile/<email>", methods=["GET", "PUT"])
def profile(email=None):
    if request.method == "GET":
        conn = get_db_conn(db)
        user = get_user_profile_info(conn, email)
       
        return render_template("profile.html", Email = f"{user[0]}", Username = f"{user[2]}", Weight = f"{user[3]}",Height = f"{user[4]}", Age = f"{user[5]}")

    if request.method == "PUT":
        return f"Updating {email}", 200

@auth.route("/bmi", methods = ["GET","POST"])
def bmi():
    return render_template("bmi.html")

@auth.route('/signout', methods=['GET','POST'])
def signout():
    return "<p>signout</p>"
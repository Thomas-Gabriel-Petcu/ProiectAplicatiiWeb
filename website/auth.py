from flask import Blueprint, render_template, request, redirect, url_for
auth = Blueprint('auth',__name__)
from website.functions import get_db_conn, db, create_user, get_user_credentials, get_user_profile_info

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        try:
            #reference to request.form
            form = request.form
            #get database connection
            conn = get_db_conn(db)
            #pass form and connection as parameter to function for creating user
            if form.get("password1") == form.get("password2"):
                create_user(conn, form)
            #close database connection
            conn.close()
        except Exception as e:
            error = {
                "error": f"Failed to create user. {e}"
            }
            return error
    return render_template("signup.html")



@auth.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        form = request.form
        email = form.get("floatingEmail")
        password = form.get("floatingPassword")
        conn = get_db_conn(db)
        user = get_user_credentials(conn, email)
        if user[1] == password:
            print("logged in")
            destination = "http://127.0.0.1:5000/profile/" + f"{user[0]}"
            return redirect(destination)
        else:
            raise Exception("Failed to log in, passwords did not match")
        conn.close()
    return render_template("login.html")


@auth.route("/profile/<email>", methods=["GET", "PUT"])
def profile(email=None):
    if request.method == "GET":
        conn = get_db_conn(db)
        user = get_user_profile_info(conn, email)
        return render_template("profile.html", Email = user[0], Password = user[1], Username = user[2], Age = user[3])

    if request.method == "PUT":
        return f"Updating {email}", 200




@auth.route('/signout', methods=['GET','POST'])
def signout():
    return "<p>signout</p>"



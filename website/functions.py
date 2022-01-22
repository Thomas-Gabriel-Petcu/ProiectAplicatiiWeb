import sqlite3

db = "/Users/thoma/source/repos/Thomas-Gabriel-Petcu/ProiectAplicatiiWeb/Databases/database.db"

def get_db_conn(path_to_db):
    conn = sqlite3.connect(path_to_db)
    return conn

def create_user(conn, form):
    query = """INSERT INTO Users (Username, Email, Password, Weight, Height, Age)
    values (?,?,?,?,?,?)"""

    user_info = [
    form.get('floatingUsername'),
    form.get('floatingEmail'),
    form.get('floatingPassword1'),
    form.get('floatingWeight'),
    form.get('floatingHeight'),
    form.get('floatingAge')
    ]
    for x in user_info:
        if x == "":
            raise Exception(f"User information is missing {x}")

    if len(user_info[0]) < 2:
        raise Exception("Username too short")
    elif user_info[3] == 0:
        raise Exception("Weight cannot be 0")
    elif int(user_info[5]) < 14:
        raise Exception("Must be at least 14 years old to user services")
    else:
        print("Added user to database")
        cursor = conn.cursor()
        cursor.execute(query, user_info)
        conn.commit()

def get_user_credentials(conn, email):
    query = f"""SELECT Email, Password FROM Users WHERE Email='{email}'"""
    cursor = conn.cursor()
    user = list(cursor.execute(query))
    if user:
        return user[0]
    else:
        return user

def get_user_profile_info(conn, email):
    query = f"""SELECT Email, Password, Username, Weight, Height, Age FROM Users WHERE Email='{email}'"""
    cursor = conn.cursor()
    user = list(cursor.execute(query))
    if user:
        return user[0]
    else:
        return user
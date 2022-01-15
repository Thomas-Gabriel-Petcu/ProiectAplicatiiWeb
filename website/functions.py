import sqlite3

db = "/Users/thoma/source/repos/Thomas-Gabriel-Petcu/ProiectAplicatiiWeb/Databases/database.db"

def get_db_conn(path_to_db):
    conn = sqlite3.connect(path_to_db)
    return conn

def create_user(conn, form):
    query = """INSERT INTO Users (Username, Email, Password)
    values (?,?,?)"""

    user_info = [
    form.get('floatingUsername'),
    form.get('floatingEmail'),
    form.get('floatingPassword1'),
    ]

    if user_info[0] == "" or user_info[1] == "" or user_info[2] == "":
        raise Exception("User information is missing.")
    elif len(user_info[0]) < 2:
        raise Exception("Username too short")
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
from flask import Flask, request
from flask_cors import CORS
import sqlite3  

app = Flask(__name__)
CORS(app)

database = r"C:\Users\thoma\source\repos\Thomas-Gabriel-Petcu\ProiectAplicatiiWeb\Databases\database.db"

@app.route("/", methods=["POST"])
def signUp():
    try:
        body = request.json
        username = body.get("username")
        email = body.get("email")
        password = body.get("password")
        age = body.get("age")
        return '', 204
    except Exception as e:
        error = {
            "error": f"Failed to create new user because {e}"
        }
        return error, 500

@app.route("/", methods=["POST"])
def signIn():
    return '', 204

if __name__ == "__main__":
    app.run(debug=True, port=3011)

def conn_to_db(path):
    conn = sqlite3.connect(path)
    return conn
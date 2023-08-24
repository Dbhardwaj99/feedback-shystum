#lecture feedback system

import jwt, datetime, os
from flask import Flask, request, render_template, redirect, url_for, make_response
from flask_mysqldb import MySQL
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

server = Flask(__name__)
mysql = MySQL(server)

server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = int(os.environ.get("MYSQL_PORT"))
JWT_SECRET = "humpetohhaihino"

print(os.environ.get("MYSQL_DB"))

@server.route("/login", methods=["GET"])
def show_login():
    return render_template("/views/login.html")


@server.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    
    if username == "":
        return "Missing credentials", 401
    
    #check for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM teacher WHERE email=%s", (username,)
    )

    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if username != email or password != password:
            return "Invalid credentials", 401
        else:
            jwt_token = createJWT(username, JWT_SECRET, True)
            response = make_response(redirect(url_for("dashboard")))
            response.set_cookie("jwt_token", jwt_token)
            return response  
    else:
        return "User not found", 401


@server.route("/", methods=["GET"])
def dashboard():
    token = request.cookies.get("jwt_token")
    print("JWT Token from Cookie:", token)
    # validate token from validate() function and redirect to dashboard
    if token == "":
        return "Missing token", 401
    else:
        # validate
        decoded, status = validate(token)
        if status == 200:
            return render_template("/views/dashboard.html", username=decoded["username"])
        else:
            return decoded, 401
    

def validate(token):
    # token = request.headers.get("Authorization")
    if token == "":
        return "Missing token", 401

    try:
        decoded = jwt.decode(
            token, JWT_SECRET, algorithms=["HS256"]
        )
        return decoded, 200
    except:
        return "Invalid token", 401


def createJWT(username, secrect, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)+ datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secrect,
        algorithm="HS256",
    )

if __name__ == "__main__":
    print(__name__)
    server.run(host="0.0.0.0", port=9000)
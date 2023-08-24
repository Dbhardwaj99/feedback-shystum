#lecture feedback system

import jwt, datetime, os
from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

print(os.environ.get("MYSQL_DB"))

@server.route("/login", methods=["GET"])
def show_login():
    return render_template("client/views/login.html")


@server.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    print(username, password)
    if(username == "t1" and password == "1"):
        return createJWT(username, os.environ.get("JWT_SECRET"), True), render_template("/client/views/dashboard.html", username=auth.username)

    auth = request.authorization
    if not auth:
        return "Missing credentials", 401
    
    #check for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username,)
    )

    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if auth.username != email or auth.password != password:
            return "Invalid credentials", 401
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True), render_template("/client/views/dashboard.html", username=auth.username)
    else:
        return "User not found", 401


@server.route("/", methods=["GET"])
def dashboard():
    token = request.headers.get("Authorization")
    # validate token from validate() function and redirect to dashboard
    if not token:
        return "Missing token", 401
    else:
        # validate
        decoded = validate()
        if decoded[1] == 200:
            return render_template("/client/views/dashboard.html", username=decoded[0]["username"])
        else:
            return decoded[0], 401
    

def validate():
    token = request.headers.get("Authorization")
    if not token:
        return "Missing token", 401

    encodedJwt = token.split(" ")[1]

    try:
        decoded = jwt.decode(
            encodedJwt, os.environ.get("JWT_SECRET"), algorithms=["HS256"]
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
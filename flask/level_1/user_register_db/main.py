from flask import Flask, render_template, flash, session, redirect, request, url_for
import sqlite3

app = Flask(__name__)

app.secret_key = "Hello123"


def connectDB():
    db_connect = sqlite3.connect("users.db")
    db_connect.execute(""" CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT, password TEXT) """)
    curs = db_connect.cursor()
    return curs, db_connect


def addUser(db_con, cur, name, email, password):
    data = cur.execute("select * from users where email=?", (email,))
    user_data = data.fetchall()
    if user_data:
        return 0
    else:
        cur.execute("insert into users (name, email, password) values (?,?,?)", (name, email, password))
        db_con.commit()
        return 1


def checkUser(name, password):
    curs, db_con = connectDB()
    data = curs.execute("select * from users where name=? and password=?",(name, password))
    if data.fetchall():
        return 1
    else:
        return 0


@app.route("/")
def index():
    if "uName" in session:
        flash("you are already logged in :-D ")
        return redirect(url_for("userPage"))
    else:
        flash("Welcome: ")
        return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def rgstr():
    if request.method == "GET":
        return render_template("registerPage.html")
    else:

        nam = request.form["fullName"]
        eml = request.form["emailID"]
        passwrd = request.form["passwd"]
        if nam and eml and passwrd:
            curs, db_con = connectDB()
            if addUser(db_con, curs, nam, eml, passwrd):
                flash("successfully registered")
                session['uName'] = nam
                return redirect(url_for('userPage'))
            else:
                flash("Email already exists, try logging in")
                return redirect(url_for('rgstr'))

        else:
            return "Error in details submitted"


@app.route("/lgn", methods=["GET", "POST"])
def loginPage():
    if request.method == "GET":
        if "uName" in session:
            flash("you are already logged in :-D ")
            return redirect(url_for("userPage"))
        else:
            flash("please enter details:")
            return render_template("loginForm.html")
    if request.method == "POST":
        nam = request.form["userName"]
        passwd = request.form["pswd"]
        if checkUser(nam, passwd):
            flash("new login successful ")
            session['uName'] = request.form["userName"]
            return redirect(url_for("userPage"))
        else:
            flash("login details incorrect", "danger")
            return render_template("loginForm.html")

@app.route("/usr")
def userPage():
    if "uName" in session:
        return render_template("userPage.html", usrName=session["uName"])
    else:
        return redirect(url_for("index"))


@app.route("/lgot")
def userLogout():
    if "uName" in session:
        session.pop("uName")
        flash("successfully logged out")
        return render_template("index.html")
    return redirect("/")


if __name__ == "__main__":
    app.run(port=5001, debug=True)

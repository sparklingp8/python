from flask import Flask, render_template, redirect, url_for, flash, request, session

app = Flask(__name__)

app.secret_key = "hello123"


@app.route("/")
def index():
    # flash("Welcomei", "info")
    # flash("Welcomee", "error")
    return render_template("index.html")


@app.route("/lgin", methods=["POST", "GET"])
def login():
    if "uName" in session:
        flash("You are already logged in")
        return redirect(url_for("userPage"))
    if request.method == "GET":
        flash("please login", "info")
        return render_template("login.html")
    else:
        session["uName"] = request.form["usrName"]
        name = session["uName"]
        flash("you are logged in successfully :D")
        return redirect(url_for("userPage"))


@app.errorhandler(404)
def errorPagehere(err):
    return "<h1>URL NOT Correct </h1>"


@app.route("/ussr")
def userPage():
    if "uName" in session:
        return render_template("user.html", usrName=session["uName"])
    else:
        flash("Welocme")
        return redirect(url_for("index"))


@app.route("/lgt")
def logouter():
    flash(f"{session['uName']} you are now logged Out")

    session.pop('uName')
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=5001, debug=True)

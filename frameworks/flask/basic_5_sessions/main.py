from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "hellox123"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def logins():
    if request.method == "GET":
        return render_template("login.html")
    else:
        dat = request.form
        session["userName"] = dat["userName"]
        return redirect(url_for("users"))


@app.route("/user")
def users():
    if "userName" in session:
        usrn = session["userName"]
        return render_template("user.html", userName=usrn)
    else:
        return redirect(url_for("logins"))


@app.route("/logout")
def loggedOut():
    session.pop("userName")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=5001, debug=True)

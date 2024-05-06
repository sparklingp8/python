from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1><a href=login>login</a></h1>"


@app.route("/login", methods=["GET", "POST"])
def lgn():
    if request.method == "POST":
        user = request.form
        nam = user['nm']
        # print(user)
        if nam:
            return redirect(url_for("userLog", usr=nam))
    return render_template("login.html")


@app.route("/user/<usr>")
def userLog(usr):
    return render_template("usrLgn.html", usrNm=usr)


if __name__ == "__main__":
    app.run(port=5001, debug=True)

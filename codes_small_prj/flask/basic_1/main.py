from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<user>/<dept>")
def user(user, dept):
    return f"<h3>hi person: {user}<h3> \nfrom department: {dept}"


@app.route("/<name>")
@app.route("/<name>/")
def special_user(name, dept="NA"):
    return redirect(url_for("user", user=name, dept=dept))


@app.route("/admin")
@app.route("/admin/")
@app.route("/admin/<anyval>")
def admin(anyval):
    return redirect(url_for("user", user="admin!", dept="all"))


if __name__ == "__main__":
    app.run()

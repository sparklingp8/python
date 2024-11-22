from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "hello page"


@app.route("/<anyText>")
def anything(anyText):
    return redirect(url_for("index"))


@app.route("/head")
def head():
    return render_template("head.html")


if __name__ == "__main__":
    app.run(port=5001)

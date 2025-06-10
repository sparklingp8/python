from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/")
@app.route("/ok")
def index():
    return render_template("index.html")


@app.route("/bootstrap")
def bootStrapPage():
    return render_template("addBootstrap.html")


@app.errorhandler(404)
def page_n_found(cump):
    return "<title>error</title><h1 style='color:red'>Wrong URL</h1>"


if __name__ == "__main__":
    app.run(port=5001,debug=True)

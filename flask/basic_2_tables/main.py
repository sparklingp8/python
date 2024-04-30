from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "index page"


@app.route("/tables/<num>")
def tables(num):
    try:
        number = int(num)
        return render_template("tables.html", number=int(num))
    except ValueError:
        return "<h1 color='red'>enter only numbers xxx in tables/xxx,</h1>"


# Define a route to handle undefined URLs
@app.errorhandler(404)
def page_not_found(error):
    # Redirect the user to a specific page
    return "<h1 color='red'>enter only numbers xxx in tables/xxx,</h1>"


@app.route("/<any>")
def anything(any):
    return redirect(url_for("tables", num=999))


if __name__ == "__main__":
    app.run(port=5002)

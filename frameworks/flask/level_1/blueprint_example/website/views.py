from flask import Blueprint

views = Blueprint('views', __name__)


@views.route("/")
def viewHome():
    return "view home"

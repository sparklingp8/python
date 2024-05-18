from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key ="Shhh123"
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/v/")
    app.register_blueprint(auth, url_prefix="/a/")
    return app

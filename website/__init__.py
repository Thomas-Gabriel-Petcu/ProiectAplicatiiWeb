from flask import Flask

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY'] = "secret key for testing"

    from .views import routes
    from .auth import auth

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
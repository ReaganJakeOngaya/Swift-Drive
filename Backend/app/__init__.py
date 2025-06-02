from flask import Flask
from .extensions import db, jwt, cors, migrate
from .routes.auth import auth_bp
from .routes.cars import cars_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(cars_bp, url_prefix="/api/cars")

    return app

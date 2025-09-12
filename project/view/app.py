from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from model.db import db

migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(environment='Development'):

    app = Flask(__name__, instance_relative_config=True)
    print(f"Loading {environment.title()}Config")
    app.config.from_object(f'view.config.{environment.title()}Config')

    from view.routes import app as app_blueprint

    app.register_blueprint(app_blueprint)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    return app
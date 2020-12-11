from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

db = SQLAlchemy()

def create_app(config_name):
    # print(config_name)
    app = Flask(__name__)
    # print(config_name)
    # app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app


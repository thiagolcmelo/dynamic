# python standard
import os

# python third-party
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

# locals
from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    Bootstrap(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    from .laboratory import laboratory as laboratory_blueprint
    app.register_blueprint(laboratory_blueprint)

    from .warehouse import warehouse as warehouse_blueprint
    app.register_blueprint(warehouse_blueprint)
    
    return app
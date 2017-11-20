from flask import Flask, render_template
from jobplus.config import configs
from jobplus.models import db

def register_blueprints(app):
    from .handlers import front
    app.register_blueprint(front)
    

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)

    return app


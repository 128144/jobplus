from flask import Flask, render_template
from jobplus.config import configs
from jobplus.models import db
from flask_migrate import Migrate

def register_blueprints(app):
    from .handlers import front, admin, company, job, user
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(company)
    app.register_blueprint(job)
    app.register_blueprint(user)
    

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app, db)
    register_blueprints(app)

    return app


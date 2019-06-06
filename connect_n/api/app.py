"""API for Connect-N game"""

# Flask module(s) and it's extentions
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Environment variable(s)
from env import API_DB_NAME

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """App factory function which runs setup for Flask app"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + API_DB_NAME
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)
    return app


app = create_app()

# pylint: disable=unused-wildcard-import
from auth import *
from routes import *
from tokens import *
from db_model import *

# Helpful when using flask shell command
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User}

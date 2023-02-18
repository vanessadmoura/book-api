from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .model import configure as config_db
from .serealizer import configure as config_ma
import pymysql
from .model import db

pymysql.install_as_MySQLdb()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/books'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .books import bp_books
    app.register_blueprint(bp_books)

    return app
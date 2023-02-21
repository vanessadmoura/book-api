from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_restx import Api

from controller.book_controller import BookItemResource, BookResource
from .model import configure as config_db
from .serealizer import configure as config_ma
import pymysql
from .utils.namespaces import book_ns

pymysql.install_as_MySQLdb()

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
          version='1.0',
          title='Book API',
          description='API - Book',
          doc='/docs')

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/books'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    app.register_blueprint(blueprint)
    book_ns.add_resource(BookResource, '/book')
    book_ns.add_resource(BookItemResource, '/book/<int:id>')
    api.add_namespace(book_ns)

    return app

from flask_restx import Namespace

book_ns = Namespace(name='Book',
                      description='Manage book',
                      path='/')
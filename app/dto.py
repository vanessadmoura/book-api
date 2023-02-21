from datetime import datetime, timedelta
from flask_restx import fields
from .utils.namespaces import book_ns


book_dto = book_ns.model('Book', { 
       'livro': fields.String(
        description='livro',
        pattern=r'^[a-zA-Z0-9]+$',
        min_length=1, max_length=255, required=True),
        
        'escritor': fields.String(
        description='escritor',
        pattern=r'^[a-zA-Z]+$',
        min_length=1, max_length=255, required=True)})
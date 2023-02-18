from flask import Blueprint, current_app, request, jsonify
from .model import Book
from .serealizer import BookSchema

bp_books = Blueprint('books', __name__)

@bp_books.route('/mostrar', methods=['GET'])
def mostrar():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200

@bp_books.route('/deletar/<id>', methods=['DELETE'])
def deletar(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!')


@bp_books.route('/modificar/<id>', methods=['PUT'])
def modificar(id):
    bs = BookSchema()
    query = Book.query.filter(Book.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_books.route('/cadastrar', methods=['POST'])
def cadastrar():
    bs = BookSchema()
    book = bs.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    return bs.jsonify(book), 201
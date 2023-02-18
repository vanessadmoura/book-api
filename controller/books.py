from flask import Blueprint, current_app, request, jsonify
from app.model import Book
from app.serealizer import BookSchema

bp_books = Blueprint('books', __name__)

@bp_books.route('/book', methods=['GET'])
def get_all_book():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200


@bp_books.route('/book/<id>', methods=['GET'])
def get_book_by_id(id):
    bs = BookSchema(many=False)
    result = Book.query.filter(Book.id == id)
    return bs.jsonify(result), 200


@bp_books.route('/book', methods=['POST'])
def register_book():
    bs = BookSchema()
    book = bs.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    return bs.jsonify(book), 201


@bp_books.route('/book/<id>', methods=['PUT'])
def modify_book(id):
    bs = BookSchema()
    query = Book.query.filter(Book.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first()), 200


@bp_books.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!'), 200

from flask import Blueprint, current_app, request, jsonify
from app.model import Book
from app.serealizer import BookSchema
from service.book_service import delete_book, get_all_book, get_book_by_id, modify_book, register_book

bp_books = Blueprint('books', __name__)
bs_list = BookSchema(many=True)
bs = BookSchema(many=False)

@bp_books.route('/book', methods=['GET'])
def get_all():
    books = get_all_book()
    return bs_list.jsonify(books), 200


@bp_books.route('/book/<id>', methods=['GET'])
def get_by_id(id):
    book = get_book_by_id(id)
    return bs_list.jsonify(book), 200


@bp_books.route('/book', methods=['POST'])
def register():
    book = bs.load(request.json)
    register_book(book)
    return bs.jsonify(book), 201


@bp_books.route('/book/<id>', methods=['PUT'])
def modify(id):
    book_to_be_saved = request.json
    query = modify_book(id, book_to_be_saved)
    return bs.jsonify(query.first()), 200


@bp_books.route('/book/<id>', methods=['DELETE'])
def delete(id):
    delete_book(id)
    return jsonify({"mensagem": "Deletado."}), 200

from flask import current_app, request
from app.model import Book
from app.serealizer import BookSchema


def get_all_book():
    return Book.query.all()


def get_book_by_id(id):
    return Book.query.filter(Book.id == id)

def register_book(book):
    current_app.db.session.add(book)
    current_app.db.session.commit()


def modify_book(id, book_to_be_saved):
    query = Book.query.filter(Book.id == id)
    query.update(book_to_be_saved)
    current_app.db.session.commit()
    return query

def delete_book(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
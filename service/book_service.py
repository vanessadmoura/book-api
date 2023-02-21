from flask import current_app, request
from app.model import Book
from app.serealizer import BookSchema
from app.model import db


def get_all_book():
    return Book.query.all()


def get_book_by_id(id):
    return Book.query.filter(Book.id == id).first()


def register_book(book):
    current_app.db.session.add(book)
    current_app.db.session.commit()


def modify_book(id, book_to_be_saved):
    book_to_update = Book.query.filter(Book.id == id).first()

    book_to_update.livro = book_to_be_saved.livro
    book_to_update.escritor = book_to_be_saved.escritor

    current_app.db.session.add(book_to_update)
    current_app.db.session.commit()
    
    return book_to_update

def delete_book(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
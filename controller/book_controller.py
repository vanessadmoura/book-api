from flask import request
from flask_restx import Resource
from app.serealizer import BookSchema
from service.book_service import delete_book, get_all_book, get_book_by_id, modify_book, register_book
from app.utils.namespaces import book_ns
from app.dto import book_dto

bs_list = BookSchema(many=True)
bs = BookSchema(many=False)

class BookResource(Resource):   

    def get(self):
        books = get_all_book()
        return bs_list.dump(books), 200
    
    
    @book_ns.expect(book_dto, validate=True)
    def post(self):
        book = bs.load(request.json)
        register_book(book)
        return bs.dump(book), 201
    
class BookItemResource(Resource):
    def get(self, id):
        book = get_book_by_id(id)
        return bs.dump(book), 200
    
    
    def put(self, id):
        book_json = request.get_json()
        book = bs.load(book_json)
        updated_book = modify_book(id, book)
        return bs.dump(updated_book), 200


    def delete(self, id):
        delete_book(id)
        return {"mensagem": "Deletado."}, 200



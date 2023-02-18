from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db
    

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro = db.Column(db.String(300))
    escritor = db.Column(db.String(255))

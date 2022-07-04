"""
Author: Phuc Tran
App Name: APIs
Purpose: Create APIs for Web
"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book_data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    book_name = db.Column(db.String(100),
                          unique=True,
                          nullable=False)
    author = db.Column(db.String(50),
                       nullable=False)
    publisher = db.Column(db.String(50),
                          nullable=False)

    def __repr__(self):
        return f"{self.book_name} by {self.author}, published by {self.publisher}"

def init_db():
    db.create_all()
    book = Book(book_name="name", author="author", publisher="publisher")
    db.session.add(book)
    db.session.commit()

@app.route("/")
def welcome():
    return "Website Provide Book's Information!!!"

@app.route("/books")
def get_books():
    books = Book.query.all()
    output = []

    for book in books:
        book_info = {"name": book.book_name,
                     "author": book.author,
                     "publisher": book.publisher}
        output.append(book_info)

    return {"books": output}

@app.route("/books/<id>")
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.book_name,
            "author": book.author,
            "publisher": book.publisher}

@app.route("/books", methods=["POST"])
def add_book():
    book = Book(book_name=request.json["name"],
                author=request.json["author"],
                publisher=request.json["publisher"])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id}

@app.route("/books/<id>", methods=["DELETE"])
def del_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Completed!!!"}


if __name__ == "__main__":
    init_db()

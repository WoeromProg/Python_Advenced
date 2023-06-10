from dataclasses import asdict
import json
from marshmallow import ValidationError
from flask import Flask, request
from schemas import BookSchema
from flask_restful import Api, Resource
from models import (
    DATA,
    get_all_books,
    init_db,
    add_book, Book,
)

app = Flask(__name__)
api = Api(app)


class BookList(Resource):
    def get(self):

        schema = BookSchema()
        return schema.dump(get_all_books(), many=True) #{'data': [asdict(book) for book in get_all_books()]}

    def post(self):
        data = request.json

        schema = BookSchema()

        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201
        # book = add_book(Book(**data))
        # return asdict(book), 201


api.add_resource(BookList, '/api/books')

if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)



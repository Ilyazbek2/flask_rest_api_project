from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models import (
    DATA,
    get_all_books,
    init_db,
    add_book,
)
from app.schemas import BookSchema


class BookList(Resource):
    def get(self):
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    def post(self):
        data = request.json
        schema = BookSchema()
        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201

from marshmallow import Schema, fields, validates, ValidationError, post_load
from models import get_book_by_title, Book

class BookSchema(Schema):
    id = fields.Int()  # dump_only=True)
    title = fields.Str()  # dump_only=True)
    author = fields.Str()#dump_only=True)

    @validates('title')
    def validate_title(self, title: str) -> None:
        if get_book_by_title(title) is not None:
            raise ValidationError(
                'Book with title "{title}" already exists,'
                'please use a different title'.format(title=title)
            )

    @post_load
    def create_book(self, data, **kwargs) -> Book:
        return Book(**data)





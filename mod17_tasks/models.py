import sqlite3
from dataclasses import dataclass
from typing import List, Dict, Optional

DATA = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]

BOOKS_TABLE_NAME = 'books'
AUTHORS_TABLE_NAME = 'authors'


@dataclass
class Author:
    id: int
    first_name: str
    last_name: str
    middle_name: Optional[str] = None

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Book:
    id: Optional[int]
    title: str
    author_id: int

    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records: List[Dict]):
    with sqlite3.connect('table_books_and_authors.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(f"CREATE TABLE IF NOT EXISTS {AUTHORS_TABLE_NAME} "
                             "(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, middle_name TEXT)")
        cursor.executescript(f"CREATE TABLE IF NOT EXISTS {BOOKS_TABLE_NAME} "
                             "(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author_id INTEGER, "
                             f"FOREIGN KEY(author_id) REFERENCES {AUTHORS_TABLE_NAME}(id))")

        for book in initial_records:
            author_data = book['author'].split()
            if len(author_data) == 2:
                first_name, last_name = author_data
                middle_name = None
            else:
                first_name, middle_name, last_name = author_data[0], ' '.join(author_data[1:-1]), author_data[-1]

            cursor.execute(f"INSERT INTO {AUTHORS_TABLE_NAME} (first_name, last_name, middle_name) "
                           "VALUES (?, ?, ?)", (first_name, last_name, middle_name))
            author_id = cursor.lastrowid

            cursor.execute(f"INSERT INTO {BOOKS_TABLE_NAME} (title, author_id) "
                           "VALUES (?, ?)", (book['title'], author_id))

        conn.commit()


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books_and_authors.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT {BOOKS_TABLE_NAME}.id, {BOOKS_TABLE_NAME}.title, {BOOKS_TABLE_NAME}.author_id, "
                       f"{AUTHORS_TABLE_NAME}.first_name, {AUTHORS_TABLE_NAME}.last_name, {AUTHORS_TABLE_NAME}.middle_name "
                       f"FROM {BOOKS_TABLE_NAME} "
                       f"JOIN {AUTHORS_TABLE_NAME} ON {AUTHORS_TABLE_NAME}.id = {BOOKS_TABLE_NAME}.author_id")
        all_books = cursor.fetchall()

        books = []
        for book_row in all_books:
            author = Author(id=book_row[2], first_name=book_row[3], last_name=book_row[4], middle_name=book_row[5])
            book = Book(id=book_row[0], title=book_row[1], author_id=book_row[2])
            books.append(book)
            book.author = author

        return books
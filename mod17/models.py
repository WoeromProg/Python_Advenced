from dataclasses import dataclass
import sqlite3
from flask import Flask
from typing import List, Dict, Optional

DATA = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]

BOOKS_TABLE_NAME = 'books'


# @dataclass
# class Author:
#     first_name: str
#     last_name: str
#     middle_name: Optional[str] = None
#     id: Optional[int] = None
#
#     def __getitem__(self, item):
#         return getattr(self, item)
#

@dataclass
class Book:
    title: str
    author: str
    id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records: List[Dict]):
    with sqlite3.connect('table_books2.db') as conn:
        cursor = conn.cursor()
        # cursor.execute(
        #     "SELECT name FROM sqlite_master "
        #     "WHERE type = 'table' AND name = 'authors'"
        # )
        cursor.execute(
            "SELECT name FROM sqlite_master "
            f"WHERE type='table' AND name='books';"
        )

        exists = cursor.fetchone()
        if not exists:
            # cursor.executescript(
            #     f"CREATE TABLE 'authors' "
            #     '(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name, last_name)'
            # )
            cursor.executescript(
                f"CREATE TABLE 'books' "
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author)'
            )
            cursor.executemany(
                f"INSERT INTO 'books'"
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
            )



def _get_book_obj_from_row(row) -> Book:
    return Book(id=row[0], title=row[1], author=row[2])


def get_all_books() -> List[Book]:  # Вывод всех книг
    with sqlite3.connect('table_books2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM 'books'")
        all_books = cursor.fetchall()
        return [_get_book_obj_from_row(row) for row in all_books]


def add_book(book: Book) -> Book:  # Добавление книги
    with sqlite3.connect('table_books2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO 'books'
            (title, author) VALUES (?, ?)
            """,
            (book.title, book.author)
        )
        book.id = cursor.lastrowid
        return book


def get_book_by_id(book_id: int) -> Optional[Book]:  # Поиск по книги по айди
    with sqlite3.connect('table_books2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM 'books' WHERE id = '%s'" % book_id)
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def update_book_by_id(book: Book):  # Обновление информации об книге
    with sqlite3.connect('table_books2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            UPDATE 'books'
            SET title =?,
                author = ?
            WHERE id = ?
            """, (book.title, book.author, book.id)
        )
        conn.commit()


def delete_book_by_id(book_id):  # Удаление книги по айди
    with sqlite3.connect('table_books2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            DELETE 'books'
            WHERE id = ?""", (book_id,)
        )
        conn.commit()

def get_book_by_title(book_title: str) -> Optional[Book]:
    with sqlite3.connect('table_books2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM 'books' WHERE title = '%s' "% book_title
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)
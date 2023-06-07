import sqlite3

from flask import Flask
from typing import List, Dict


DATA = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]


class Book:
    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author

    def __getitem__(self, item):
        return getattr(self, item)

def init_db(initial_records: List[Dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='table_books';"
        )
        exists = cursor.fetchone()

        #Если таблицы нет, создаем ее и заполняем
        if not exists:
            exists = cursor.executescript(
                "CREATE TABLE 'table_books'"
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author)'
            )
            cursor.executemany(
                'INSERT INTO table_books'
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
                #Делаем записи
            )
# def add_row_in_db(x ,y):
#     with sqlite3.connect('table_books.db') as conn:
#         cursor = conn.cursor()
#         cursor.execute(
#             'INSERT INTO table_books (title, author) VALUES (?, ?)', (x, y)
#         )
#         conn.commit()
#         conn.close()

def get_all_books() -> List[Dict]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * from table_books')
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]
        #Объединяем данные из БД, создаем из кортежа объект нашего класса

if __name__ == '__main__':
    init_db(DATA)


import re
import sqlite3
from forms import MyForm
from flask import Flask, render_template, request, redirect, url_for
from typing import List, Dict

from mod14.models import init_db, DATA, get_all_books, Book

app = Flask(__name__)

BOOKS = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]


def _get_hmtl_table_for_books(books: List[Dict]) -> str:
    table = """
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Author</th>
                </tr>
            </thead>
                <tbody>
                    {books_rows}
                </tbody>
        </table>
    """
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    return render_template('pred_index.html', books=get_all_books())


# Task1
# @app.route('/book/form')
# def get_books_form():
#     return render_template('add_book.html')

# @app.route('/book/form', methods=['GET', 'POST'])
# def get_books_form():
#     if request.method == 'POST':
#         title = request.form.get('field1')
#         author = request.form.get('field2')
#         with sqlite3.connect('table_books.db') as conn:
#             cursor = conn.cursor()
#             cursor.execute(
#                 'INSERT INTO table_books (title, author) VALUES (?, ?)', (title, author)
#             )
#     return render_template('add_book.html')


# Task2
@app.route('/book/form', methods=['GET', 'POST'])
def get_books_form():
    form = MyForm(request.form)
    if request.method == 'POST':
        title = form.title.data
        author = form.author.data
        with sqlite3.connect('table_books.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO table_books (title, author) VALUES (?, ?)', (title, author)
            )
    return render_template('add_book.html', form=form)


# Task3
@app.route('/book/search', methods=['GET', 'POST'])
def search_author():
    form = MyForm(request.form)
    if request.method == 'POST':
        author = form.author.data
        with sqlite3.connect('table_books.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM table_books WHERE author LIKE (?)", (author,))
            books = cursor.fetchall()
            x = [str(elem).replace("(", '') for elem in books]
            x = [elem.replace(")", '') for elem in x]
            x = [elem.replace("'", '') for elem in x]
            x = [elem.replace(",", '') for elem in x]
    return render_template('books_by_author.html', form=form, books=x, aut=author)


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

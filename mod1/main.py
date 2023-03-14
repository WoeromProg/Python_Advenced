import datetime
import os
import random
import re

from flask import Flask


def car():
    return ["Chevrolet", "Renault", "Ford", "Lada"]

def cat():
    return ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

def text():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, r"Толстой.txt")

    book = open(BOOK_FILE, 'r')
    text = book.read()
    text = " ".join(text.split()).split(' ')
    text = list(filter(None, text))
    word = re.sub("[^А-Яа-я]", " ", random.choice(text))
    while len(word) <= 1:
        word = re.sub("[^А-Яа-я]", " ", random.choice(text))
    return word


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/cars')
def cars():
    return ', '.join(car())


@app.route('/cats')
def cats():
    return random.choice(cat())


@app.route('/get_time/now')
def time_mow():
    now = datetime.datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return formatted_now


@app.route('/get_time/future')
def time_future():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"Точное время через час будет: {current_time_after_hour}"


@app.route('/get_random_word')
def get_random_word():
    word = text()
    return word


if __name__ == "__main__":
    app.run(debug=True)
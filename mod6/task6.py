import datetime
from flask import Flask, url_for
import random

app = Flask(__name__)
cars_names = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats_names = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
count = 0


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    global cars_names
    return ', '.join(cars_names)


@app.route('/cats')
def cats():
    global cats_names
    return random.choice(cats_names)


@app.route('/get_time/now')
def now():
    time = datetime.datetime.now()
    return f'Точное время: {time}'


@app.route('/get_time/future')
def future():
    time_after_hour = datetime.datetime.now() + datetime.timedelta(seconds=3600)
    return f'Точное время через час: {time_after_hour}'


@app.route('/counter')
def counter():
    global count
    count += 1
    return str(count)


def has_no_empty_params(rule):
    # if rule.defaults is not None:
    #     defaults = rule.defaults
    # else:
    #     default = ()
    #
    # if rule.arguments is not None:
    #     arguments = rule.arguments
    # else:
    #     arguments = ()

    defaults = rule.defaults or () #if rule.defaults is not None else ()
    arguments = rule.arguments or () #if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.errorhandler(404)
def list_routes(err):
    result = ''
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((f'http://127.0.0.1:5000{url}', rule.endpoint))
    for link, name in links:
        result += f'</br><a href="{link}">{link}<a>'
    return f"Данного адреса не существует, список других страниц: {result}"


if __name__ == '__main__':
    app.run()

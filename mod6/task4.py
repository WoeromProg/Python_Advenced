import itertools
import json
import operator
import os
import re
from collections import Counter


def read_book(filename) -> list[dict]:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, filename)
    with open(BOOK_FILE) as book:
        logs = book.readlines()
        logs = [json.loads(log) for log in logs]
    return logs


logs = read_book('skillbox_json_messages.log')


def grouping_by_levels(logs):
    for level, logs_list in itertools.groupby(logs, key=lambda d: d['level']):
        print(f'Сообщений уровня: {level}: {len(list(logs_list))}')


def grouping_time_maxLogs(logs):
    logs_in_time = {}
    for time, logs_list in itertools.groupby(logs, key=lambda d: d['time'][:2]):
        logs_in_time[time] = len(list(logs_list))
    max_hour = max(logs_in_time.items(), key=operator.itemgetter(1))[0]
    print(f'Больше всего логов было в {max_hour} часов')


def logsLevel_in_period(logs, level):
    result = [log for log in logs if log['level'] == level and bool(re.search('05:[0-1]', log['time']))]
    print(f'Кол-во логов уровня {level} в период с 05:00:00 по 05:20:00 было: {len(result)}')


def logs_count_contains_the_word(logs, word):
    result = [log for log in logs if word in str(log)]
    print(f'Кол-во сообщений, в которых встречается слово: "{word}": {len(result)}')


def popular_word(logs, search_level):
    filter_levels_logs = [log for log in logs if log['level'] == search_level]
    words = [log['message'].split() for log in filter_levels_logs]
    if len(words) > 0:
        counter = Counter([item for sublist in words for item in sublist]).most_common()[0]
        print(
            f'Самое популярное на уровне {search_level}: "{counter[0]}", встречается {counter[1]} раз')


if __name__ == '__main__':
    print('Task1:')
    grouping_by_levels(logs)
    print('Task2:')
    grouping_time_maxLogs(logs)
    print('Task3:')
    logsLevel_in_period(logs, 'CRITICAL')
    print('Task4:')
    logs_count_contains_the_word(logs, 'dog')
    print('Task5:')
    popular_word(logs, "WARNING")

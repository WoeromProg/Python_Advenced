import os.path
import os
from datetime import datetime
import sys
from flask import Flask
"""
Задание 1
"""

def get_summary_rss(x):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, f"{x}")
    file = open(BOOK_FILE, 'r')
    text = file.read()
    rss = []
    for i in text.split('\n'):
        i = i.split()
        if len(i) > 5:
            rss.append(i[5])
    rss.pop(0)
    rss = [int(x) for x in rss]
    designations = {'B': 1024, 'KiB': 1024 ** 2, 'MiB': 1024 ** 3}
    rss_bytes = []
    for key, value in designations.items():
        rss_bytes.append(key + ": " + str(float('{:.3f}'.format((sum(rss) / value)))))
    return rss_bytes


print('\n'.join((get_summary_rss("output_file.txt"))))

"""
Задание 3
"""
def decoder(cipher):
    result = []

    for i in cipher:
        result.append(i)

        if len(result) > 2 and result[-1] == '.' and result[-2] == '.':
            result.pop()
            result.pop()
            if len(result) > 0:
                result.pop()

    result = ''.join(x for x in result if x != '.')
    return result

print("абра.." + " -> " + decoder("абра.."))


"""
4 Задание
"""


app = Flask(__name__)
@app.route("/hello-world/<username>")
def hello(username) -> str:
    weekday = datetime.today().weekday()
    print(weekday)
    day_tuple = ('Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы','Субботы', 'Воскресенья')
    day_list = ['Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы', 'Субботы', 'Воскресенья']
    day_dict = {1: 'Понедельника', 2: 'Вторника', 3: 'Среды', 4: 'Четверга', 5: 'Пятницы', 6: 'Субботы', 7: 'Воскресенья'}

    print(sys.getsizeof(day_tuple)) #(96)
    print(sys.getsizeof(day_list)) #(120)
    print(sys.getsizeof(day_dict)) #(360)
    print(day_tuple[weekday])
    if weekday == 0 or weekday == 1 or weekday == 3 or weekday == 6:
        return f"Привет {username}, хорошего {day_tuple[weekday]}!"
    else:
        return f"Привет {username}, хорошей {day_tuple[weekday]}!"


@app.route("/even/<int:number>")
def even(number)->str:
    if number % 2 ==0:
        result = "чётное"
    else:
        result = "Нечётное"
    return f"Число {number} <b>{result}</b>"

"""
Задача 5
"""
@app.route("/max_number/<path:numbers>")
def max_number(numbers) -> str:
    numbers = "".join(x for x in numbers if not x.isalpha())
    numbers = numbers.split('/')
    numbers = [int(x) for x in numbers]
    print(numbers)
    maxNumber = max(numbers)
    return f"Максимальное число: <em>{maxNumber}</em>"


if __name__ == "__main__":
    app.run(debug=True)

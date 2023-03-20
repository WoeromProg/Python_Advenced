import os.path
import os
from datetime import datetime
import sys
from flask import Flask


app = Flask(__name__)
@app.route("/hello-world/<username>")
def hello(username) -> str:
    weekday = datetime.today().weekday()
    day_tuple = ('Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы','Субботы', 'Воскресенья')
    if weekday == 0 or weekday == 1 or weekday == 3 or weekday == 6:
        return f"Привет {username}, хорошего {day_tuple[weekday]}!"
    else:
        return f"Привет {username}, хорошей {day_tuple[weekday]}!"

if __name__ == "__main__":
    app.run(debug=True)
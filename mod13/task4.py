import sqlite3


sql_request_add = """
INSERT INTO table_with_birds (bird_name, date_when_added) VALUES (?,?)
"""
sql_request_exists = """
SELECT EXISTS (SELECT bird_name
               FROM table_with_birds
               WHERE bird_name = ?
               LIMIT 1)
"""
def log_bird(
        c: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    c.execute(sql_request_add, (bird_name, date_time))

def check_if_such_bird_already_seen(
        c: sqlite3.Cursor,
        bird_name: str
) -> bool:
    result = c.execute(sql_request_exists, (bird_name,)).fetchone()[0]
    return bool(result)
if __name__ == '__main__':
    bird_name = input("Введите название птицы\n>")
    time = input("Введите время когда увидели птицу\n>")

    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        if check_if_such_bird_already_seen(cursor, bird_name):
            print("Эту птицу мы уже видели")
        else:
            log_bird(cursor, bird_name, time)
            print("Птица добавлена в таблицу")



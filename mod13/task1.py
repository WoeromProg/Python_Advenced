import sqlite3

sqr_request = """
SELECT COUNT(*)
    FROM (SELECT *
    FROM table_truck_with_vaccine
    WHERE truck_number = ? AND temperature_in_celsius NOT BETWEEN 16 and 20)
"""

def check_vaccine_in_truck(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    c.execute(sqr_request, (truck_number, ))
    request_result, *_ = c.fetchone()
    return request_result >= 3

if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()

        name = input("Введите номер грузовика \n> ")

        print(
            "Вакцина в целостности?: ", check_vaccine_in_truck(cursor, truck_number=name)
            )
  
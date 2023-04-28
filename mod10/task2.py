import sqlite3

if __name__ == '__main__':
    with sqlite3.connect("hw_2_database.db") as conn:

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count DESC")
        result = cursor.fetchall()
        print("Какие телефоны чаще всего покупают?", (', '.join(str(y) for y in result[0:3])))

        result = cursor.execute("SELECT * FROM table_checkout WHERE phone_color IN ('Blue', 'Red') ORDER BY sold_count DESC").fetchall()[0:3]

        if result[0][1] == result[1][1]:
            print("Синие и красные телефоны покупают одинаковое кол-во")
        else: print(f"Чаще покупают телефоны такого цвета: {result[0][0]}")

        result = cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count").fetchall()[0:3]
        print(f"Телефоны цвета {', '.join(str(y) for y in result)} покупают меньше всего")
import sqlite3

if __name__ == '__main__':
    with sqlite3.connect("hw_3_database.db") as conn:

        cursor = conn.cursor()
        for number in range(1,4):
            print(f"Записей в table_{number} -", cursor.execute(f"SELECT COUNT(id) FROM table_{number}").fetchall()[0][0])

        print("Уникальных записей в таблице table_1:", cursor.execute("SELECT COUNT(DISTINCT value) FROM table_1").fetchall()[0][0])

        print("Такое кол-во записей из table_1 встречается в table_2:",
              cursor.execute("SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2)").fetchall()[0][0])
        print("Такое кол-во записей из table_1 встречается в table_2 и table_3:",
              cursor.execute("SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2) AND value IN (SELECT value FROM table_3)").fetchall()[0][0])


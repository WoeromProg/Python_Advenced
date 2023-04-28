import sqlite3

if __name__ == '__main__':
    with sqlite3.connect("hw_4_database.db") as conn:

        cursor = conn.cursor()
        print("Человек за чертой бедности:", cursor.execute(f"SELECT COUNT(*) FROM (SELECT salary FROM salaries WHERE salary < 5000)").fetchall()[0][0])
        print("Средняя зарплата населения:", cursor.execute("SELECT AVG(salary) FROM salaries").fetchone()[0])

        median = cursor.execute("SELECT salary FROM salaries ORDER BY salary DESC").fetchall()
        print(f"Медианная зарплата на острове:", median[((len(median)) - 1) // 2][0])

        count = cursor.execute("SELECT COUNT(salary) FROM salaries").fetchone()[0]
        total = cursor.execute("SELECT SUM(salary) FROM salaries").fetchone()[0]
        top10 = cursor.execute(f"SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {count})").fetchone()[0]
        inequality = round(top10 / (total - top10) * 100, 2)
        print(f"Соц неравенство: {inequality}%")

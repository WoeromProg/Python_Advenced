import sqlite3
import csv

sqr_request = """
DELETE FROM table_fees
    WHERE truck_number = ? AND timestamp = ?
"""

def delete_false_penalties(
        c: sqlite3.Cursor,
        wrong_fees_file: str
) -> None:
    with open(wrong_fees_file, 'r') as f:
        file = csv.reader(f)
        wrong_feel = list(file)
        wrong_feel.pop(0)
        #print(wrong_feel)
        for truck_and_number in wrong_feel:
            c.execute(sqr_request, (truck_and_number[0], truck_and_number[1]))


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        delete_false_penalties(cursor, "wrong_fees.csv")
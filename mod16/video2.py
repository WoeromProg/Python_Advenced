import sqlite3

CRATE_TABLE_1 = """
DROP TABLE IF EXISTS 'table_1';
CREATE TABLE 'table_1' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL,
    born_city VARCHAR(255) NOT NULL
)
"""

CRATE_TABLE_2 = """
DROP TABLE IF EXISTS 'table_2';
CREATE TABLE 'table_2' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL,
    born_city VARCHAR(255) NOT NULL
)
"""

TABLE_1_DATA = [
    ('Jonh', 'Smith', 20, 'Beijing'),
    ('Jonh', 'Ivanovich', 50, 'Rhaden'),
    ('Miles', 'Lang', 20, 'Moskow'),
    ('Bertran', 'Haley', 37, 'Warsaw'),
    ('Kmane', 'Petty', 23, 'Paris'),
    ('Simrah', 'Valenzuela', 26, 'London')
]

TABLE_2_DATA = [
    ('Jonh', 'Smith', 20, 'Beijing'),
    ('Jonh', 'Ivanovich', 50, 'Rhaden'),
    ('Miles', 'Lang', 20, 'Moskow'),
    ('Bertran', 'Haley', 37, 'Warsaw'),
    ('Kmane', 'Petty', 23, 'Paris'),
    ('Simrah', 'Valenzuela', 26, 'London')
]
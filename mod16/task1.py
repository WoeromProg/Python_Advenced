import sqlite3


if __name__ == "__main__":
    ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"
    with sqlite3.connect('mod16_task1.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS actors(
        act_id INTEGER PRIMARY KEY AUTOINCREMENT,
        act_first_name VARCAR(50) NOT NULL,
        act_last_name VARCHAR(50) NOT NULL,
        act_gender VARCHAR(1) NOT NULL);
        
        CREATE TABLE IF NOT EXISTS movie(
        mov_id INTEGER PRIMARY KEY AUTOINCREMENT,
        mov_title VARCAR(50) NOT NULL);
        
        CREATE TABLE IF NOT EXISTS director(
        dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
        dir_first_name VARCAR(50) NOT NULL,
        dir_last_name VARCHAR(50) NOT NULL);
        
        CREATE TABLE IF NOT EXISTS movie_cast(
            act_id INTEGER NOT NULL REFERENCES actors(act_id) ON DELETE CASCADE,
            mov_id INTEGER NOT NULL REFERENCES movie(mov_id) ON DELETE CASCADE,
            role VARCHAR(50) NOT NULL);
            
        CREATE TABLE IF NOT EXISTS oscar_awarded(
            award_id INTEGER PRIMARY KEY AUTOINCREMENT,
            mov_id INTEGER NOT NULL REFERENCES movie(mov_id) ON DELETE CASCADE);
            
        CREATE TABLE IF NOT EXISTS movie_direction(
            dir_id INTEGER NOT NULL REFERENCES director(dir_id) ON DELETE CASCADE,
            mov_id INTEGER NOT NULL REFERENCES movie(mov_id) ON DELETE CASCADE);
        """)
        conn.commit()
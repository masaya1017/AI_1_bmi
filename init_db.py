import sqlite3

db_path = "./hw.sqlite3"

sql = '''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        height NUMBER,
        weight NUMBER,
        typeNo INTEGER
    )
    '''
with sqlite3.connect(db_path) as conn:
    conn.execute(sql)

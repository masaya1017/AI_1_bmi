import sqlite3
import random

db_path = "./hw.sqlite3"


def insert_db(conn):
    height = random.randint(130, 180)
    weight = random.randint(30, 100)

    bmi = weight/(height/100)**2
    type_no = 1

    if bmi < 18.5:
        type_no = 0
    elif bmi < 25:
        type_no = 1
    elif bmi < 30:
        type_no = 2
    elif bmi < 35:
        type_no = 3
    elif bmi < 40:
        type_no = 4
    else:
        type_no = 5

    sql = '''
        INSERT INTO person(height,weight,typeNo) VALUES (?,?,?)
    '''
    values = (height, weight, type_no)
    print(values)
    conn.executemany(sql, [values])


with sqlite3.connect(db_path) as conn:

    for i in range(3000):
        insert_db(conn)

    count = conn.execute('SELECT count(*) FROM person')
    cnt = count.fetchone()
    print(cnt[0])
    '''
    for row in conn.execute("SELECT * FROM person"):
        print(row)
        '''

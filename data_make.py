import sqlite3
import random

db_path = "./hw.sqlite3"


def insert_db(conn):
    #身長と体重それぞれについてランダム生成を行う。
    height = random.randint(130, 180)
    weight = random.randint(30, 100)
    #BMIの算出
    bmi = weight/(height/100)**2
    type_no = 1
    #BMIの数値によって、カテゴリ分類を実行する。
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
    #sqlの発行(データの挿入処理,クエリパラメータ)
    sql = '''
        INSERT INTO person(height,weight,typeNo) VALUES (?,?,?)
    '''
    #タプルの生成
    values = (height, weight, type_no)
    print(values)
    #DB実行時は、リストに格納すること注意する。
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

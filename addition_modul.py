import sqlite3
import datetime

conn = sqlite3.connect('taxi_drivers.db', check_same_thread=False)
cur = conn.cursor()

id_count = 0


def find_max_id():
    global id_count
    cur.execute("SELECT userid FROM drivers;")
    all_results = cur.fetchall()
    for i in all_results:
        if id_count < i[0]:
            id_count = i[0]
    id_count += 1


def add_driver(data_list):
    global id_count
    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M")
    find_max_id()
    data_list.insert(0, id_count)
    data_list.append(time)
    cur.execute("""INSERT INTO drivers VALUES(?, ?, ?, ?, ?, ?, ?, ? );""", data_list)
    conn.commit()
    id_count += 1
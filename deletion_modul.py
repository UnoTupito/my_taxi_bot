import sqlite3
conn = sqlite3.connect('taxi_drivers.db', check_same_thread=False)
cur = conn.cursor()


def del_driver(user_id):
    cur.execute(f"""DELETE FROM drivers WHERE userid={user_id};""")
    conn.commit()
#
# add_driver('10')

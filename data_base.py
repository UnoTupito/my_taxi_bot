import sqlite3
conn = sqlite3.connect('taxi_drivers.db')
cur = conn.cursor()

# Создание БД
# cur.execute("""CREATE TABLE drivers(
#    userid INT PRIMARY KEY,
#    full_name TEXT,
#    identification_number TEXT,
#    rating TEXT,
#    auto TEXT,
#    fines TEXT,
#    telefon TEXT,
#    last_modified TEXT);
# """)
# conn.commit()
#
# drivers = [
#   ('0', 'Name', '№ auto ','Rate','Model auto','Penalties', 'Tel number', ''),
#   ('1', 'Stephanie Stewart', '35659','4,8','Mazda','True', '252435432', ''),
#   ('2', 'Sincere Sherman', '30819','3,9','Lada','False', '65245423532', ''),
#   ('3', 'Sidney Horn', '39798','4,5','Hyundai','False', '654325432', ''),
#   ('4', 'Litzy Yates', '33899','4,4','Lada','False', '3425423', ''),
#   ('5', 'Jaxon Mills', '31220','4,3','Ford','False', '25356423', ''),
#   ('6', 'Paul Richard', '33565','4,7','Honda','True', '65253532452', ''),
#   ('7', 'Kamari Holden', '35612','4,2','Ford','True', '43252423', ''),
#   ('8', 'Gaige Summers', '38515','4,9','Mazda','True', '43432t432', ''),
#   ('9', 'Andrea Snow', '37086','4,8','Kia','False', '432t432t432', '')
# ]
# cur.executemany("INSERT INTO drivers VALUES(?, ?, ?, ?, ?, ?, ?, ?);", drivers)
# conn.commit()
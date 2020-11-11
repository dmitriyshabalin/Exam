#! BD

import sys
import sqlite3

connection = sqlite3.connect('sqlite_bd.db')

cursor = connection.cursor()

cursor.execute('SELECT * FROM Pacient')

results = cursor.fetchall()

print(results)

connection.commit()

connection.close()

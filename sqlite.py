import sqlite3

conn = sqlite3.connect('new_db.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM USER")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
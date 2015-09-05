import sqlite3
CONN = sqlite3.connect('pw.db')
CURSOR = CONN.cursor()

CURSOR.execute('''CREATE TABLE plain_passwords (site text, username text, password text)''')
CONN.commit()
CONN.close()
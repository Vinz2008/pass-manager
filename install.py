import sqlite3
conn = sqlite3.connect('passwordmanager.db')
c = conn.cursor()
c.execute('''CREATE TABLE PASSWORD
             ([name] text,[url] text, [hash] text)''')
c.execute('''CREATE TABLE NUMBERPASSWORD
             ([numberpassword] integer)''')

conn.commit()

import sqlite3
from tqdm import tqdm
import time
conn = sqlite3.connect('passwordmanager.db')
c = conn.cursor()
c.execute('''CREATE TABLE PASSWORD
             ([id] text,[name] text,[url] text, [password] text)''')
c.execute('''CREATE TABLE NUMBERPASSWORD
             ([numberpassword] integer)''')

c.execute('''INSERT INTO NUMBERPASSWORD(numberpassword) VALUES (0)   ''')
conn.commit()

  
for i in tqdm (range (101), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)
      
print("Complete.")

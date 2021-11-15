import sqlite3
from tqdm import tqdm
import time
import os
directory = ".password"
parent_dir = os.path.expanduser('~')
path = os.path.join(parent_dir, directory)
if os.path.isdir(path) == False:
    os.mkdir(path)
conn = sqlite3.connect(path + '/passwordmanager.db')
c = conn.cursor()
c.execute('''CREATE TABLE PASSWORD
             ([id] text,[name] text,[url] text, [password] text)''')
c.execute('''CREATE TABLE NUMBERPASSWORD
             ([numberpassword] integer, [id] text)''')

c.execute('''INSERT INTO NUMBERPASSWORD(numberpassword, id) VALUES (0, "abc")   ''')
conn.commit()

  
for i in tqdm (range (101), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)
      
print("Complete.")

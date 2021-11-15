import sqlite3 #import library for database
import os
directory = ".password"
parent_dir = os.path.expanduser('~')
path = os.path.join(parent_dir, directory)
conn = sqlite3.connect(path + '/passwordmanager.db') #c>
c = conn.cursor()
numberpass = c.execute('''SELECT * FROM NUMBERPASSWORD''')
for thing in numberpass:
    print(thing)
thing = str(thing)
print(thing)
thing2 = thing[:-2]
print(thing2)
thing3 = thing2[1:]
print(thing3)
thing4 = thing3[:-2]
print(thing4)
thing5 = thing4[:-1]
print(thing5)
numberfinal = int(thing5)
print(numberfinal)

import sqlite3 #import library for database
import os
directory = ".password"
parent_dir = os.path.expanduser('~')
path = os.path.join(parent_dir, directory)
conn = sqlite3.connect(path + '/passwordmanager.db') #connect to database
c = conn.cursor()
number_password = 0

def add_password():		
<<<<<<< HEAD
=======
    name = input("Give a name to this password : ")
    url = input("What is the url for the password : ")
    password = input("What is  the password : ")
    c.execute('''INSERT INTO PASSWORD(name,url,password)VALUES (?,?,?)''',(name,url,password))
>>>>>>> 51e4cd53e2740566770f5ffe359fa0a02224d063
    numberpass = c.execute('''SELECT * FROM NUMBERPASSWORD''')
    for thing in numberpass:
        thing = thing
    
    thing = str(thing)
    thing2 = thing[:-2]
    thing3 = thing2[1:]
<<<<<<< HEAD
    thing4 = thing3[:-2]
    thing5 = thing4[:-1]
    thing6 = thing5[:1]
    numberfinal = int(thing6)
    name = input("Give a name to this password : ")
    url = input("What is the url for the password : ")
    password = input("What is  the password : ")
    id = numberfinal + 1
    c.execute('''INSERT INTO PASSWORD(id,name,url,password)VALUES (?,?,?,?)''',(id,name,url,password))
    numberpass = c.execute('''SELECT * FROM NUMBERPASSWORD''')
    c.execute('''UPDATE NUMBERPASSWORD SET numberpassword = ? WHERE id = "abc"''',(str(id)))
=======
    numberfinal = int(thing3)
    numberfinal = numberfinal + 1
    c.execute('''INSERT INTO PASSWORD(numberpassword) VALUES (?)''',(numberfinal))
>>>>>>> 51e4cd53e2740566770f5ffe359fa0a02224d063
    conn.commit()
def list_passwords():
	#for row in c.execute('SELECT * FROM PASSWORD ORDER BY name'):
		#print(row)
    print('\nPasswords:')
    data=c.execute('''SELECT * FROM PASSWORD''')
    for column in data.description:
        print(column[0], end = ",")
    print()
    data=c.execute('''SELECT * FROM PASSWORD''')
    for row in data:
        print(row)

def print_home():
	print(" 1.list of passwords \n 2.add a password \n 3.modify a password")
	user_input = int(input(" : "))
	if user_input == 1:
		list_passwords()
	elif user_input == 2:
		add_password()
	elif user_input == 3:
		print("not done yet")
print_home()


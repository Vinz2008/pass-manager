import sqlite3 #import library for database
conn = sqlite3.connect('passwordmanager.db') #connect to database
c = conn.cursor()
number_password = 0

def add_password():		
    name = input("Give a name to this password : ")
    url = input("What is the url for the password : ")
    password = input("What is  the password : ")
    c.execute('''INSERT INTO PASSWORD(name,url,password)VALUES (?,?,?)''',(name,url,password))
    numberpass = c.execute('''SELECT * FROM NUMBERPASSWORD''')
    for thing in numberpass:
        thing = thing
    
    thing = str(thing)
    thing2 = thing[:-2]
    thing3 = thing2[1:]
    numberfinal = int(thing3)
    numberfinal = numberfinal + 1
    c.execute('''INSERT INTO PASSWORD(numberpassword) VALUES (?)''',(numberfinal))
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


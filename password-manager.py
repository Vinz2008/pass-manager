import hashlib #import library for the hash
import sqlite3 #import library for database
import desktop_file
conn = sqlite3.connect('passwordmanager.db') #connect to database
c = conn.cursor()

number_password = 0

def add_password():		
	name = input("Give a name to this password : ")
	url = input("What is the url for the password : ")
	temp_password =  input("What is  the password : ")
	hash_object = hashlib.sha256(temp_password.encode())
	hex_dig = hash_object.hexdigest()
	password_hash = hex_dig
	c.execute('''INSERT INTO PASSWORD(name,url,hash) 
	             VALUES (?,?,?)''',(name,url,password_hash))
	conn.commit()
def list_passwords():
	for row in c.execute('SELECT * FROM PASSWORD ORDER BY name'):
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


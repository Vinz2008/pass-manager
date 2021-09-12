# Pass-manager
## Description
Pass-manager is a command-line application which can manage passwords written in python. It uses [sqlite3](https://docs.python.org/3/library/sqlite3.html) to keep the passwords in the storage.
### Features
- list passwords
- add passwords

## Installation
Create a .pass-manager directory :
```
mkdir ~/.pass-manager
```

Clone the git repository in the folder :
```
git clone https://github.com/Vinz2008/pass-manager.git . 
```

Run the install python script which create the database : 
```
python3 install.py  
```

Create in the folder a bash script named launch.sh :
```
touch launch.sh
```

And put in the file :
```
cd ~/.pass-manager
python3 password-manager.py
```

Add this line in your shell config file (~/.bashrc for bash and ~/.zshrc for zsh) to create an alias.
```
alias pass-manager="~/.pass-manager/launch.sh"
```
# Password Generator and Storage

## Summary
A password generator that will create a random unique password with no reoccuring characters within the password all done through a graphical user interface, using TKinter. There is an option that allows you to ommit special characters by default they are included. Once the password is generated, the password will be salted with another random password, encrypted and stored inside a database. The database will hold you the username you set for the password, and all the information needed for the password. 

## Setup:
- create a virtual enviornment: 
	Linux: python3 -m venv venv
	Windows: python -m venv venv
- activate the virtual enviornment:
	Linux: source venv/bin/activate
	Windows: venv\scripts\activate 
- install requirements text:
	Linux: pip3 install -r Requirements.txt 
	Windows: pip install -r Requirements.txt
- run the program
	Linux: python3 main.py
	Windows: python main.py
 

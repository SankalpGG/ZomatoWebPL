#ZomatoXBlinkit
import getpass
id={'user':123456}

def login():
    k=input("Enter your username: ")
    v=getpass.getpass("Enter Your Pass: ")
    if id[k]==v:
        print("Login Successful")
    else:
        print("Invalid Entry")


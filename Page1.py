id={'user':"123456"}

def login():
    k=input("Enter your username: ")
    v=input("Enter Your Pass: ")
    if id[k]==v:
        print("Login Successful")
    else:
        print("Invalid Entry")

def new_user():
    k=input("Enter your desired username: ")
    v=input("Enter your password: ")
    id[k]=v
    print("New Id Successfully Created")

print("""
###----WELCOME--TO--ZOMATO----###
Enter:
1 for login to an existing account
2 for creating a new account

""")

n=int(input(">>>"))
if n==1:
    login()
if n==2:
    new_user()

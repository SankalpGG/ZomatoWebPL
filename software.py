#ZomatoXBlinkit

id={'user':123456}

def login():
    k=input("Enter your username: ")
    v=input("Enter Your Pass: ")
    if k in id and id[k]==v:
        print("Login Successful")
    else:
        print("Invalid Credentials")

login()

def register():
    k=input("enter user name ")
    if k in id:
        print("username already exists")
        register()
    else:
        v=input("enter your password ")
        v1=input("enter your password again ")
        if v==v1:
            id[k]=v
            print("registered succesfully")
        else:
            print("password mismatch")
            register()

register()

def home():
    print("Welcome to Home Page")
    print('''
1. To order Food
2.  To DineIn
3.  
4.  To View Cart
5.  To Edit Dilevery Address
6.  To View Popular Today
7.  
8. 
9.  To Delete Your Account
10.  To Logout
''')
    n=int(input('>'))
    if n==1:
        print("Order Food")
    if n==2:
        print("DineIn")
    if n==3:
        print('Viewing Discount Codes')
    if n==4:
        print('Your Cart')
    if n==5:
        print('Edit Delivery Address')
    if n==6:
        print('Popular Today')
    if n==7:
        print('Order History')
    if n==8:
        print('Edit Payment Options')
    if n==9:
        print('To Delete Your Account')
    if n==10:
        print('You have been logged out')

home()

     

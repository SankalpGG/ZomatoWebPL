#Zomato WebPlatform
import random
import mysql.connector as c

con=c.connect(host="localhost",user="root",passwd="SANKALP_4141",database="zomato")
cur=con.cursor()

id={'user':123456}

def login():
    k=input("Enter your username: ")
    v=input("Enter Your Pass: ")
    if k in id and id[k]==v:
        print("Login Successful")
    else:
        print("Invalid Credentials")



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



def home():
    print("Welcome to Home Page")
    print('''
1.  To order Food by search
2.
3.  To View Cart
4.  To Edit Dilevery Address
5.  To View Popular cuisine Today
6.  To Delete Your Account
7.  To Logout
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



     
def trial():
    try:
        cur.execute("SELECT * FROM popular;")
        d = cur.fetchall()
        for i in d:
            print(i)
        print("end")
    except Exception as e:
        print("Error:", e)

trial()

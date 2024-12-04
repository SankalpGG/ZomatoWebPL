#Zomato WebPlatform
import random
import mysql.connector as c

con=c.connect(host="localhost",user="root",passwd="SANKALP_4141",database="zomato")
cur=con.cursor()

id={'user':"123456"}
key=""
def login():
    k=input("Enter your username: ")
    v=input("Enter Your Pass: ")
    if k in id and id[k]==v:
        print("Login Successful")
        global key
        key=k
        home()
    else:
        print("Invalid Credentials")

cart=[]
add=""

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
            login()
        else:
            print("password mismatch")
            register()


def home():
    print("Welcome to Home Page")
    print('''
1.  To order Food by search
2.  To View Cart
3.  To Enter Delivery Address
4.  To View Popular cuisine
5.  To Place Your Order
6.  To Delete Your Account
7.  To Logout
''')
    n=int(input('>'))
    if n==1:
        print("Order Food")
        order()
    if n==2:
        print("View Cart")
        view_cart()
    if n==3:
        print('Enter Delivery Address')
        address()
    if n==4:
        print('View Popular Cusine')
        popular()
    if n==5:
        print("Place Order")
        placeo()
    if n==6:
        print('To delete your Account')
        acc_del()
    if n==7:
        print('To Logout')
        logout()


def logout():
    print("Logging Out")
    ch='n'
    print("Logged Out Successfully")

def acc_del():
    x="t"
    while x in "tT":
        n=input("enter account to be deleted: ")
        k=input("enter account password: ")
        if n in id:
            del id[n]
            x="f"
        else:
            print("invalid user id")
            x="t"

def popular():
    q1="select * from popular;"
    cur.execute(q1)
    d=cur.fetchall()
    for i in d:
        print(str(i[0])+"\t"+i[1])
    cho='y'
    while cho in 'Yy':
        c= int(input("enter sno of item to be added into cart: "))
        global cart
        cart.append(d[c-1])
        cho=input("Do you want to enter another item? (y/n)")
    home()

def address():
    ad=input("Enter Your Address: ")
    global add
    add=add+ad
    print("Your entered address is:")
    print(add)
    home()

def view_cart():
    global cart
    t=0
    if len(cart)==0:
        print("Cart is empty")
        home()
        
    else:
        for i in cart:
            print(i[1],"\t",i[-1])
            t=t+i[-1]
        print("Total amount: ","\t",t)
        home()


def order():
    q1="select * from menu;"
    cur.execute(q1)
    d=cur.fetchall()
    for i in d:
        print(i[0],"  ",i[1],"  ",i[2],"  ",i[3])
    cho='y'
    while cho in 'Yy':
        c= int(input("enter sno of item to be added into cart: "))
        global cart
        cart.append(d[c-1])
        cho=input("Do you want to enter another item? (y/n) ")
    view_cart()

    
def feedback():
    global key
    fb=input("Enter Feedback: ")
    query = "INSERT INTO feedback (id, content) VALUES (%s, %s);"
    cur.execute(query, (key, fb))
    print("Thank You for Your Feedback")
    home()

def placeo():
    global cart
    print("Your Order for the items in your cart has been placed")
    r=random.randint(25,45)
    print("Your order will bw delivered in approximately",str(r),"minutes")
    print("Items you ordered are:")
    for i in cart:
        print(i[1])
    feedback()

print("*********WELCOME TO ZOMATO WEB PLATFORM*********")
print("Enter your choice:")
print("""
1. For login
2. For registering as a new user
""")
dk=int(input(">"))
if dk==1:
    login()
if dk==2:
    register()

cur.close()
con.commit()


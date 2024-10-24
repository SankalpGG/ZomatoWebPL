import random
import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="mysystem",database="bhoomika")
cur=con.cursor()

def quer1():
    q1="select * from customer;"
    cur.execute(q1)
    d=cur.fetchall()
    for i in d:
        print(i)

def quer2():
    r=random.randint(101,104)
    q2="select * from customer where custid="+str(r)
    cur.execute(q2)
    d=cur.fetchall()
    for i in d:
        print(i)
        
def quer3():
    r1=random.randint(101,102)
    r2=random.randint(105,107)
    q3="SELECT * FROM customer WHERE custid BETWEEN '{}' AND '{}' ".format(r1,r2)
    cur.execute(q3)
    d=cur.fetchall()
    for i in d:
        print(i)
n=int(input("""Enter
1 for q1
2 for q2
3 for q3
"""))
if n==1:
      quer1()
if n==2:
      quer2()
if n==3:
      quer3()

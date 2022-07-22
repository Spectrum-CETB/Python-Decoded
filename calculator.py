import math
n1=int(input("Enter 1st number :"))
n2=int(input("Enter 2nd number :"))
c=input("Enter operation to be performed :")
def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
def exp(a,b):
    return (a**b)
def log(a):
    return math.log(a)
if(c=="add"):
    r=add(n1,n2)
    print(r)
elif(c=="sub"):
    r=sub(n1,n2)
    print(r)   
elif(c=="mul"):
    r=mul(n1,n2)
    print(r) 
elif(c=="div"):
    r=div(n1,n2)
    print(r) 
elif(c=="log"):
    n=(int)(input("log of 1 or 2?"))
    if(n==1):
        r=log(n1)
        print(r)
    elif(n==2):
        r=log(n2)
        print(r) 
elif(c=="exp"):
    r=exp(n1,n2)
    print(r)      
    





print("SMART CALCULATOR")
def addition(a,b):
    return a+b
def subraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if a==0:
        return 'cannot divide by zero'
    else:
        return a/b
while True:
    print('1.addition')
    print('2.subtraction')
    print('3.multiplication')
    print('4.division')
    print('5.exit')
    
    
    
   
    ch=int(input("enter choice:"))
    if ch==5:
        break
    a=float(input("enter the 1st number:"))
    b=float(input("enter the 2nd number:"))
    if ch==1:
        print(addition(a,b))
    elif ch==2:
        print(subtraction(a,b))
    elif ch==3:
        print(multiplication(a,b))
    elif ch==4:
        print(division(a,b))
    else:
        print('invalid input')

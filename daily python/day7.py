#check even or odd 
num=int(input("enter a number"))
if num%2==0:
    print("even")
elif num==0:
    print("zeroes also  is an integer number")
else:
    print("odd")
    
    
#find largest in threee numbers
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a==b==c:
    print("all numbers are equal")
elif a>=b and a>=c:
    if a==b: 
     print("a and b are largest")
    elif a==c:
     print("a and c are largest ")
    else :
        print("a is largest")
elif b>=a and b>=c:
    if b==a:
        print("b and a are largest")
    elif b==c:
        print("b and c largest")
    else:
        print("b is largest")
else:
    print("c is largest")
    
    

#positive , negative and zero
a=int(input("enter a number"))
if a>0:
    print("positive")
elif a==0:
    print("zero")
else:
    print("negative")
    



#simple calculator (+,-,*,%)
a= int (input("enter  number"))
b=int (input("enter a number")) 
choice=input("enter a choice +,-,*,%")
if choice =="+":
    print("add ",a+b)
elif choice =="-":
    print("subtract",a-b)   
elif choice =="*":
    print("multiply",a*b)
elif choice =="%": # remainder/ module
    print("module",a%b)
else:
    print("invalid choice")
    
    
    
    
# leap year check
year=int(input("enter a year"))
if (year%4==0 and year%100!=0 )or (year%400==0):
    print("leap year")
else:
    print("normal year")
    
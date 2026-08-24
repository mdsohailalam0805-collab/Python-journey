
print("===== simple calculator=====")

while True:

    choices=input("enter a choice(+,-,*,/,%, original, percentage, square, power,exit)")
#original:- find original number from percentage 

    if choices== "exit":
        print("calculator closed")
        break
    
    n=float(input("enter 1st number"))

    if choices=="+":
        n2=float(input("enter  2nd nummber"))
        result=n+n2
        print("result",result)

    elif choices=="-":
        n2=float(input("enter a 2nd nummber"))
        result=n-n2
        print("result", result)
    
    elif choices=="*":
        n2=float(input("enter a 2nd nummber"))
        result=n*n2
        print("result",result)
        
    elif choices=="/":
        n2=float(input("enter a 2nd nummber"))
        if n2!=0:
            result=n/n2
            print("result",result)
        else :
            print("devision by zero not allowed")
            
    elif choices=="%":
    #n ka n2%
        n2=float(input("enter a 2nd nummber"))
        result=(n*n2)/100
        print("result", result)
        
    elif choices=="percentage": 
    # n2 how many percent of n
        n2=float(input("enter a 2nd number"))
        result=n*100/n2
        print("result",result)
        
    elif choices=="original":  
    # if n2% = value hoto original number
        n2=float(input("enter a 2nd number"))
        result=n*100/n2
        print("result", result)

    elif choices=="square":
        result=n**2
        print("result", result)
    elif choices=="power":
        
        n2=float(input("enter a 2nd number"))  
        result=n**n2
        print("result", result)  
        
    else:
        print("invalid operator")
    
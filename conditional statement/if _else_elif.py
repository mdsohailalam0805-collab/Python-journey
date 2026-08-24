num1=float(input('enter a number: '))
num2=float(input('enter a number: '))

choice=input('enter your choice +,-,*')
if choice=='+':
    print('addition',{num1+num2})
elif choice=='-':
    print('subtraction',{num1-num2})

elif choice=='*':
    print('multiplication : ',{num1*num2})
else:
    print('invalid choice')
    
           



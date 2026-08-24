#check  palindrome number
n=int(input("enter a number"))
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if original==rev:
    print("palindrome number") 
else:
    print(" not palindrome number")
    
 
 
#fibonacci number (sum  of previous two numbers)
n=int (input("how many turm"))
a=0
b=1
for i in range(n):
    print(a)
    next=a+b
    a=b
    b=next
    
    
#armstrong number
n=int(input("enter a number"))
original=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if original==sum:
    print("armstrong number")
else:
    print("not armstrong number")
    
    


#right triangle pattern (reverse triangle)
n= int (input('enter a number'))
for i in range (n,0,-1): #outer loop
    for j in range(i): #inner loop
        print("*",end=" ")
    print()
    
#right triangle 
n= int (input('enter a number'))
for i in range (1,n+1): #outer loop
    for j in range(i): #inner loop
        print("*",end=" ")
    print()
    
    
#inverted triangle
n=int(input("enter a number"))
for i in range(n): 
    for j in range(i): #spaces
        print(" ",end=" ")
    for k in range(n-i): #stars
        print("*",end=" ")
    print()
    
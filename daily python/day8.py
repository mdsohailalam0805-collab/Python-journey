# 1 se n tak  sum nikalo
n=int(input("enter a number"))
total=0
for i in range (1,n+1):
    total+=i
print('sum',total)
    
    
#using while loop
n=int(input("enter a number"))
total=0
i=1
while i<=n:
    total+=i
    i+=1
print("sum=",total)
    


#factorial questions
n=int(input("enter a number"))
if n<0: # for nagative numbers
    print("error message")
else:
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("factorial=",fact)
    

#while loop version
n=int(input("enter a number"))
if n<0:
    print("error message")
else:
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    print(fact)
    
    
#multiplication table
n=int(input("enter a number"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    
#while loop version
n=int(input("enter a number"))
i=1
while i<11:

    print(n,"x",i,"=",n*i)
    i+=1
  
#(arbitrary) table print
n=int(input("enter a number"))
limit=int(input("print table till"))
i=1
while (i<limit+1):
    print(n,"x",i,"=",n*i)
    i+=1
    
    
    
#prime number check (devid by 1 and itself)
n=int(input("enter a number"))
if n<=1:
    print("not prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print ("not prime number")
            break
    else:
        print("prime number")
        
        
        
# 1-100 tak even numbers
for i in range(1,101):
    if i%2==0:
        print(i)



#reverse a nummers
n=int(input("enter a number"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reversed number=",rev)

#for loop version
n=int(input("enter a number"))
rev=0
for i in range(len(str(n))):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reversed number=",rev)
#loops and patterns

#print 1-100
for i in range(1,101,1):
    print (i)

#print even numbers 
a=int (input("enter a number"))
if a %2==0:
    print ("even")
else:
    print ("odd")


#multiplication table
a=int (input("enter a number"))
for i in range(1,20,1):
    print(a,"x",i, "=" ,a*i)
    
#factorial
a=int(input("enter a number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
    print(fact)


#fibonacci series:- every next number sum of previous two numbers
s=int (input("enter a number"))
a,b=0,1
for i in range(s):
    print(a)
    a,b=b,a+b


#star pattern (triangle)
for i in range (1,6):
    print("*" *i)
#pattern me jitni baar print chahiye= utni rows



#reverse loop
for i in range(5,3,-1):
  print(i)


#count vowels in string
text= 'today i feel tired'
count=0
vowels='aeiouAEIOU'
for ch in text:
  if ch in vowels:
    count+=1
print(count)


#sum of digits
a=int (input("enter a number"))
b=int (input("enter a number"))
print ("sum" ,a+b)


#prime number check
n=int(input("enter a number"))
if n<=1:
    print ("not prime")
else:
    for i in range (2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime number")
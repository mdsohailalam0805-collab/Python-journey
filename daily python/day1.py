#print hello sohail

print("hello sohail")

#add two numbers 
a=int(input("enter a number"))
b=int (input("enter a number"))
result=a+b
print(result)

#check even /odd
a=int (input("enter a number"))
if a%2==0:
    print("even")
else:
    print("odd")

#find maximum of two numbers
num1=int(input("enter a number"))
num2=int(input("enter a number"))
if num1>num2:
    print("maximum")
elif num1<num2:
    print("minimum")
else:
    print("please enter a valid number")#optional

#check positive negative
a=10
if a>=0:
    print("positive")
else:
    print("negative")
    

#print 1-10 using loop
for i in range(1,11,1):
 print(i)

 #while loop

a=1
while a<=10:
    print(a)
    a+=1


#sum of 1-n numbers
n=int(input("enter n:"))
total=0
sum = n * (n+1)//2
print("sum=",sum)

#2nd method
n= int (input(" enter a number n: "))
total=0
for i in range(1,n+1):
    total=total+i
    print(total) 



#count digits in number
num=int (input("enter a number n:"))
count=0
while num>0:
    count+=1
    num//=10
    print("digit",count)
    
#2nd method
n=input("enter n:")
print("digit", len(n))



#print reverse
num=int (input("enter a number"))
rev=0
while num>0:
    rev= rev * 10 + num % 10
    num//=10
print("reverse=",rev)


#check palindrome number
num=int (input("enter a number n:"))
temporary=num #original number save
rev=0
while num>0:
    rev=rev*10+num%10
    num//=10
if temporary==rev:
    print("palindrome number")
else:
    print("not palindrome number")

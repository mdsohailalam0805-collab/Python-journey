#largest element
e=[9,6,5,3,7,2]
print(max(e))
print(min(e))
print(sum(e))


#sum of list
a=[10,50,60]
b=[20,30,40]
result=a+b
print(result)

#remove duplicate
e=[10,2,0,1,0,10,10]
new=list(set(e))
print(new)

#count even numbers 
lst=[20,17,3,6,9,13]
count=0
for even in lst:
    if even%2==0:
        count+=1
print(count)

#sort list
lst=[50,10,5,0]
lst.sort()
print(lst)

#reverse list
numbers=[20,30,40,5,6,9]
numbers.reverse()
print(numbers)


#merge two list
sohail=[5,6,2,5]
waseem=[7,8,9,4]
result=sohail+waseem
print(result)

#list comprehension- square of each number
n=[2,4,8,10]
squares=[n*n for n in n]
print(squares)

#2nd method
squares=[i**2 for i in range(1,10)]
print(squares)

#second largest element
n=[5,8,9,10]
n=list(set(n))#remove duplicate value
n.sort() #arrange orders
print(n[-2])
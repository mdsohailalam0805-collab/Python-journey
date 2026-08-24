'''
[expression for item in iterrable if cindition]
expression=x*2
item=[1,1,2,3]
iterable=range(1,50)
condition - optional
'''
#simple code
squares=[]
for i in range(1,100,1):
    squares.append(i**2)
print(squares)

#in short comprehension method
squares=[i**2 for i in range(1,10,)]
print(squares)
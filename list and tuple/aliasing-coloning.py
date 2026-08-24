#aliasig method
x=[1,2,3]
y=x
y[1]=10
print(x,y)
#no new object is created



#coloning(copying)
x=[1,2,3]
y=x
y=x.copy()
y[0]=100
print(x,y)
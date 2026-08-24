#return statements-return sends a value back from the function

def college( name , dist):
    return(name,dist)
name= college("sandip university" ,"madhubani")
print (name)


#local and global
#local variable
def add(a,b):
    return(a+b)
x=add(10,20)
print(x)

#global variable
def add(a,b):
    print(a+b,x)
    
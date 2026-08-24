def greet():
    print("good morning")
greet()


#parameters & arguiments
def greet(name):  #name is parameters (sohail)
    print("good morning",name)
greet("sohail")


#arguiments
def greet(name):
    print("hi",name)
greet('sohail')     #sohail is arguiments( values)


'''there are three types of arguiments
positional arguiments
keyword arguiments
default arguiments 
'''
#positional arguimments-order matter
def greet(name,city):
    print("welcome",name, "to the", city)
greet("sohail","kolkata")

#keyword arguiments - order does not matter
def greet(name,city):
    print("welcome",name, "to the", city)
greet(city='kolkata',name='sohail')


#default arguiments - use when  no  arguiments is given.
def greet(name='waseem',city='purniya'):
    print("welcome",name, "to the", city)
greet(name='sohail',city='kolkata')

#lambda function:- is a small anonymous function
#lambda arguimments :expressions condition
devide=lambda x:x*10 
print(devide(20))
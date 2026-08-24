#simple function
def greet():
    print('hi')
greet()

#functions with arguiments
def greet(name):
    print('assalamualaikum', name)
greet('sohail')#arguiments

#return value
def multiply(s,w):
    return(s*w)
print((multiply(10,20)))


#default arguiments
def greet (name='sohail',city='kolkata'):
    print('welcome', name ,'to the ' ,city)
greet(name='waseem',city='delhi')#default arguiments


#keywords arguimentss
def greet(name,prn):
    print(name,'PRN', prn, 'please come to the HOD office')
greet('sohail',240205241001)#positional arguiments
greet(name='waseem',prn=240205241014)#keywords arguments
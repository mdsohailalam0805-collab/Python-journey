
# without constructor

class Pen: 
        def set_details(self,color,price):
                self.color=color
                self.price=price
pen1=Pen()
pen1.set_details('black',50)
print(pen1.color)
print(pen1.price)



#with constructor

class pen:
        def __init__(self,color,price):
                self.color=color
                self.price=price
p1=pen('blue', '10')  #values automatially set
print(p1.color,p1.price)

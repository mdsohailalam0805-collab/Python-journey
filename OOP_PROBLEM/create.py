class cricket:
         def add_details__(self, player_name, team_name, specialist):
                 self.player_name=player_name
                 self.team_name=team_name
                 self.specialist=specialist
cricket=cricket()
cricket.add_details__('sohail', 'ACC akhta','allrownder')
print(cricket.player_name,cricket.team_name, cricket.specialist,"young risinng player")
                 
#bicycle(class)
class bicycle:
        def set_details__(self, brand,price,color):
                self.brand=brand
                self.price=price
                self.color=color
bicycle=bicycle()
bicycle.set_details__('hero','5000', 'black')
print("i baught bicycle", bicycle.brand,"brand","in price",bicycle.price,"with",bicycle.color,"color")                
                


# class pen (with constructor)
class pen:
        def __init__(self,color,price):
                self.color=color
                self.price=price
p1=pen('blue', '10')  #values automatially set
p2=pen('black', '20') #values automatially set
print(p1.color,p2.price)
print(p2.color,p2.price)

#without constructor
class Pen:
        def __init__(self,color,price):
                self.color=color
                self.price=price
pen1=pen('red', '100')
print(pen1.color)
print(pen1.price)


#student class
class student:
        def __init__(self,name,branch,prn):
                self.name=name
                self.branch=branch
                self.prn=prn
# creating object
s1=student('sohail', 'b.tech cse (ai & ml)', 240205241001)
print('my name is ',s1.name,'currently minding',s1.branch, 'my prn is',s1.prn)
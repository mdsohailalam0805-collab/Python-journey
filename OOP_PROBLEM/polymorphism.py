#polimorphism with classes
class human_being:
    def speak(self):
        print('human being speaks')
class man:
    def speak(self):
        print('man speaks lovingly')
class women:
    def speak(self):
        print('women speaks loudly')
class transgender:
    def speak(self):
        print('transgender(waseem) speaks a dena re baba de de')

human_being1=man()
human_being2=women()
human_being3=transgender()

human_being1.speak()
human_being2.speak()
human_being3.speak()
 

#polymorphism with operators
print(5+5)
print("hi"+"sohail")
print([1,3]+[4,6])


#method overloading
class phone:
   def call(self,number, video='false', record='false'):
       if video and record:
           print(f"video calling {number} with recording")
       elif video:
           print(f"video calling {number}")
       elif record:
           print(f"record calling{number}")
       else:
           print(f"calling {number}")

p=phone()
p.call("8873232380")
p.call("8873232310", "video=false")
p.call("8873232360", "record=false")
p.call("8873232350", "video=false","record=false")



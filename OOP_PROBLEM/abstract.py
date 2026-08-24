#abstract method

from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

#this class gives a rule
# you cannot create an object of an abstract class

# CHILD CLASS IMPLEMENTATION

class car(vehicle):
    def start(self):
        print("car start with key")

class bike(vehicle):
    def start(self):
        print("bike start with kick")

#using object
c=car()
b=bike()

c.start()
b.start()
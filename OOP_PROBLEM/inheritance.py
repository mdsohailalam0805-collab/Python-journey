
#inheritance example
class shamim:   #parent class
    def talk(self):
        print("shamim (uncle) talks")

class altamash(shamim):  #child class
    def talk(self):
        super().talk()
        print("altamash barks")

class faisal(shamim):  #child class
    def talk(self):
        super().talk()
        print("faisal sends positive vibes before talking")

gay=altamash()
gay.talk()

good_person=faisal()
good_person.talk()



#syntax
class shamim:   #parent class
    def talk(self):
        print("shamim (uncle) talks")

class altamash(shamim):  #child class
    pass

gay=altamash()
gay.talk()
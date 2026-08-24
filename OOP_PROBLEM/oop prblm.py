worrior_name='sohail'
worrior_health='60'
worrior_attack='40'


mage_name='waseem'
mage_health='70'
mage_attack='50'

def attack_worrior():
    print(f'worrior attacks with power',worrior_attack)
def attack_mage():
    print(f'mage attack with power',mage_attack)


attack_worrior()
attack_mage()

# IN OBJECT ORIENTED PROGRAMMING

class character:
    #method
    def __init__(self, name, health, attack): 
        self.name=name
        self.health=health
        self.attack=attack
    #method
    def attack_enemy(self):
        print(f'{self.name} attack with power {self.attack}')

worrior=character('waseem',50, 20)
mage=character('sohail',70, 40)
worrior.attack_enemy()
mage.attack_enemy()

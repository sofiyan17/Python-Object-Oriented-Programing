import os
os.system("cls")

class hero:
    def __init__(self,input_name, input_health, input_power, input_armor): # fungsi __init__ adalah ketika class ini di panggil, yang pertama kali akan muncul adalah __init__ ini
        self.name = input_name
        self.health = input_health
        self.power = input_power
        self.armor = input_armor

hero1 = hero('Sniper',100,10,4)
hero2 = hero('Mirana',100,15,1)
hero3 = hero('Sofiyan',1000,100,0)
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)



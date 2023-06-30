import os
os.system("cls")

class hero:
    # class variable
    jumlah = 0
    def __init__(self,input_name, input_health, input_power, input_armor):
        # Intance variable
        self.name = input_name
        self.health = input_health
        self.power = input_power
        self.armor = input_armor
        hero.jumlah += 1
        print("Membuat hero dengan nama ", input_name)

hero1 = hero('Sniper',100,10,4)
print(hero.jumlah)
hero2 = hero('Mirana',100,15,1)
print(hero.jumlah)
hero3 = hero('Sofiyan',1000,100,0)
print(hero.jumlah)




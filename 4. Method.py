import os
os.system("cls")

class hero:
    # class variable 
    jumlah_hero = 0
    
    def __init__(self, input_name, input_health, input_power, input_armor):
        # instance variable
        self.name = input_name
        self.health = input_health
        self.power = input_power
        self.armor = input_armor
        hero.jumlah_hero += 1
        
    # void function atau methond tanpa return, tanpa argument
    def siapa(self):
        print("Namaku adalah ", self.name)
        
    # method dengan argument tanpa return
    def healthup(self, up):
        self.health += up
        
    # method dengan return
    def gethealth(self):
        return self.health
        

hero1 = hero('Sniper', 100, 10, 5)
hero2 = hero('Mario bross', 90, 5, 10)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()

hero1.healthup(10)
print(hero1.health)

print(hero1.gethealth())

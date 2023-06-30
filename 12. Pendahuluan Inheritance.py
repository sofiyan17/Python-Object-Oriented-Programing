import os
os.system("cls")


class hero:
    def __init__(self, name, helth):
        self.name = name
        self.helth = helth
        
class heroInteligent(hero):# cara membuat class inheritance
    pass        

class heroStength(hero):
    pass
        

lina = hero('Lina', 100)
techies = heroInteligent('Techies', 100)
axe = heroStength("Axe",100)


print(lina.name)
print(techies.name)
print(axe.name)
print(help(techies)) #--> untuk melihat apakah ia adlah clas atau tidak
        

import os
os.system("cls")

class hero:
    def __init__(self, name, health, attackpower): 
        self.__name = name
        self.__health = health
        self.__attpower = attackpower
        
    # getter
    def getname(self):
        return self.__name
    
    def gethelath(self):
        return self.__health
    
    # setter
    def diserang(self,serangpower):
        self.__health -= serangpower
        
    def setattackpower(self,nilaibaru):
        self.__attpower = nilaibaru

# awal dari game 
earthShaker = hero("EarthShaker", 50, 5)
        
# game berjalan

print(earthShaker.getname())
print(earthShaker.gethelath())

earthShaker.diserang(5)
print(earthShaker.gethelath())


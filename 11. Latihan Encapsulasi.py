import os
os.system("cls")

class hero:
    # private class
    __jumlah = 0
    
    def __init__(self, name, health, attpower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attpowerStandar = attpower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthStandar * self.__level
        self.__attpower = self.__attpowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        
        self.__health = self.__healthMax
        
        hero.__jumlah += 1
        
    @property
    def info(self):
        return "{} Level {}: \n\thealth = {} / {} \n\tattack = {} \n\tarmor = {}\n".format(self.__name,self.__level,  self.__health,self.__healthMax, self.__attpower, self.__armor)
    
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'Level Up')
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthStandar * self.__level
            self.__attpower = self.__attpowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            
    def attack(self, musuh):
        self.gainExp = 50
            
            
    
slardar = hero("Slardar", 100,5,10)
axe = hero("Axe", 100,5,10)
print(slardar.info)
print(axe.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
print(slardar.info)

axe.attack(slardar)
axe.attack(slardar)
axe.attack(slardar)
print(axe.info)
        

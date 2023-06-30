import os
os.system("cls")

class hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def ShowInfo(self):
        print("\nShowInfo di SuperClass")
        print("{} health {}".format(self.name,self.health))
        
class heroInteligent(hero):
    def __init__(self, name):
        super().__init__(name,100)
    
    # overide   (Mwnimpa fungsi yang ada di superclass)
    def ShowInfo(self):
        print("\nShowInfo di SubClass")
        print("{}\n\tType : Inteligent\n\thealth {}".format(self.name,self.health))
        
class heroStrength(hero):
    def __init__(self, name):
        super().__init__(name,200)
           
lina = heroInteligent("Lina")
axe = heroStrength("Axe")

axe.ShowInfo()
lina.ShowInfo()

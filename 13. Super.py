import os
os.system("cls")


class hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def ShowInfo(self):
        print("{} dengan heatlh {}".format(self.name,self.health))
        
        
class heroInteligent(hero):
    def __init__(self, name):
        ## cara yang kurang efektif
        # self.name = name
        # self.health = 100
        
        ## cara yang lebih efektif
        # hero.__init__(self, name,100)
        
        ## cara menggunaka super 
        super().__init__(name,100)
        super().ShowInfo()
        
class heroStrength(hero):
    def __init__(self, name):
        # hero.__init__(self, name,200)
        super().__init__(name,200)
        super().ShowInfo()
        
    
lina = heroInteligent("Lina")
axe = heroStrength("Axe")
        
    
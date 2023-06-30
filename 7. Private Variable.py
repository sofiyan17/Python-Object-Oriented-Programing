import os
os.system("cls")

class hero:
    # class variable
    jumlah = 0
    __private_jumlah = 0
    
    def __init__(self,name, health):
        self.name = name
        self.health = health
        
        # variable instance private
        self.__private = "private"
        
        # variable instance protected
        self._protected = 'Protected'
        
sniper = hero("Sniper",100)

print(sniper.__dict__)
print(hero.__dict__)
print(hero.__private_jumlah)

        

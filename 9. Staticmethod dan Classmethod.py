import os
os.system("cls")

class hero:
    
    # private class variable
    __jumlah = 0
    
    def __init__(self, name):
        self.name = name
        hero.__jumlah += 1
    
    # method ini hanya berlaku untuk object
    def getjumlah(self):
        return hero.__jumlah
    # method ini tidak berlaku untuk object tapi berlaku untuk class
    def getjumlah1():
        return hero.__jumlah
    
    # method stataic (decorator) --> nempel ke object dan classnya
    @staticmethod
    def getjumlah2():
        return hero.__jumlah
    
    @classmethod
    def getjumlah3(cls):
        return cls.__jumlah
    
    
        
sniper = hero('Sniper')
print(hero.getjumlah2())
rikimaru = hero('Rikimaru')
print(rikimaru.getjumlah2())
drowranger = hero('Drawranger')
print(drowranger.getjumlah3())




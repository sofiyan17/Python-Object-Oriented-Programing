import os
os.system("cls")

class hero:
    def __init__(self, name, health, attackpower, armornumber):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.armornumber = armornumber
        
    def serang (self, lawan):
        print(self.name + ' Menyerang ', lawan.name)
        lawan.diserang(self, self.attackpower)
        
    def diserang(self, lawan, attackpower_lawan):
        print(self.name + ' Diserang', lawan.name)
        
        attack_diterima = attackpower_lawan / self.armornumber
        print("Serangan terasa : ", attack_diterima)
        
        self.health -= attack_diterima
        print("Darah ", self.name, " tersisa : ", self.health)
        
sniper = hero("Sniper", 100, 10, 5)
rikimaru = hero("Rikimaru", 100, 20, 10)

sniper.serang(rikimaru)
print("")
rikimaru.serang(sniper)


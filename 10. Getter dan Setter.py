import os
os.system("cls")

class hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "Name {}: \n\tHealth : {}".format(self.__name, self.__health)
        
    # def gethealth(self):
    #     return self.__health
    
    @property # kita bisa merubah method menjadi berlaku seperti variable, dan bisa diupdate
    def info(self):
        return "Name {}: \n\tHealth : {}".format(self.name, self.__health)
    
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, masukan):
        self.__armor = masukan
    
    @armor.deleter
    def armor(self):
        print("Armor di delete")
        self.__armor = None

sniper = hero('Sniper', 100, 10)

print("Merubah info :\n")

print(sniper.info)
sniper.name = 'Sofiyan'
print(sniper.info)

print("\n\nGetter dan setter untuk __armor :")

print(sniper.armor)
sniper.armor = 20
print(sniper.armor)

print("\n\nDellete armor :")
del sniper.armor
print(sniper.__dict__)

import os
os.system("cls")

class hero:# Template
    pass

hero1 = hero() # Object/ intance
hero2 = hero()
hero3 = hero()

hero1.name = "Sniper"
hero1.health = 100

hero2.name = "Sven"
hero2.health = 100

hero3.name = "Sofiyan"
hero3.health = 300

print(hero1) # untuk mengecek apakah dia object atau bukan
print(hero1.__dict__) # untuk mengetahui atribut apa yang ada di dalam objevt
print(hero1.name) # untuk mengeluarkan object berdasarkan atributnya



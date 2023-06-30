import os
os.system("cls")

class Mangga:
    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah
        
    def __repr__(self): # ketika program masih dalam proses debug
        return "Debug - Mangga : {} dengan jumlah {}".format(self.nama,self.jumlah)
    
    def __str__(self): # ketika program sudah jadi
        return "Mangga : {} dengan jumlah {}".format(self.nama,self.jumlah)
        
    def __add__(self, objek):
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self): # harus mempunya @property jika ingin menampilakn isi dari method ini
        return "objek ini mempunya nama dan jumlah"
        

belanja1 = Mangga("Arumanis", 10)
print(repr(belanja1)) # untuk menampilkan repr jika ada magic method __str__ di dalamnya
belanja2 = Mangga("Manalagi", 5)
print(belanja2)
print(belanja1 + belanja2)

print(belanja1.__dict__)


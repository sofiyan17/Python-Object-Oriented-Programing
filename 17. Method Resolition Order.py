# method resolition order// multiple inheritance
import os
os.system("cls")
class A:
    def show(self):
        print("ini adalah Show A")
class B:
    def show(self):
        print("ini adalah Show B")
class C(B,A):
    # def show(self):
    #     print("ini adalah Show C")
    pass

objek = C()

objek.show()
# help(objek) # untuk melihat urutan


import os
os.system("cls")

# Diamond problem

class A:
    def show(self):
        print("Ini adalah show A")
    # pass

class B(A):
    # def show(self):
    #     print("Ini adalah show B")
    pass

class C(A):
    def show(self):
        print("Ini adalah show C")
    # pass
        
class D(B,C):
    pass

objek = D()

objek.show()
help(objek)
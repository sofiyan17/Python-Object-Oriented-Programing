import os
os.system("cls")

#  membuat class abstract

# abc = abstract base class

from abc import ABC,abstractmethod

class Button(ABC):
    
    @abstractmethod
    def click(self):
        pass

class PushButton(Button):
    def click(self):
        print("Push button click")

class RadioButton(Button):
    def click(self):
        print("Radio button click")
        
tombol1 = PushButton()
tombol1.click()
# help(tombol1)
        
tombol2 = RadioButton()
tombol2.click()
# help(tombol2)


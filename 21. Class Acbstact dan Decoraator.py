import os
os.system("cls")

from abc import ABC, abstractmethod

class Button(ABC):
    
    def __init__(self,set_link):
        self.link = set_link
    
    @abstractmethod
    def click(self):
        pass
    
    @property
    @abstractmethod
    def link(self):
        pass
    
class PushButton(Button):
    def click(self):
        print("Go to : {}".format(self.link))
        
    @Button.link.setter
    def link(self, input):
        self.__input = input
    
    @link.getter
    def link(self):
        return self.__input


tombol1 = PushButton("www.klasterbuka.id")
tombol1.click()
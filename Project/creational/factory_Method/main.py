from abc import ABC, abstractmethod

# Product
class IPadkrapow(ABC):
    @abstractmethod
    def prepare(self):
        '''Interface method'''
    def cook(self):
        '''Interface method'''
    def serve(self):
        '''Interface method'''

class Pork(IPadkrapow):
    def __init__(self) -> None:
        self.name = "Padkrapow Pork"
    def prepare(self):
        return "prepare Padkrapow Pork\n"
    def cook(self):
        return "cook Padkrapow Pork\n"
    def serve(self):
        return "serve Padkrapow Pork"

class Chicken(IPadkrapow):
    def __init__(self) -> None:
        self.name = "Padkrapow Chicken"
    def prepare(self):
        return "prepare Padkrapow Chicken\n"
    def cook(self):
        return "cook Padkrapow Chicken\n"
    def serve(self):
        return "serve Padkrapow Chicken"

# Factory
class Shop(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def getFood(self) ->str :
        result = ''
        product = self.factory_method()
        print(f"Menu : {product.name}")
        result += product.prepare()
        result += product.cook()
        result += product.serve()
        return result

class PadkrapowPork(Shop):
    def factory_method(self) -> IPadkrapow:
        return Pork()
    
class PadkrapowChicken(Shop):
    def factory_method(self) -> IPadkrapow:
        return Chicken()
    
# Client
def client_code(shop : Shop):
    print(f'{shop.getFood()}\n')

if __name__ == '__main__':
    client_code(PadkrapowPork())
    client_code(PadkrapowChicken())
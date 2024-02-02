class Coffee :
    def getDetail(self) :
        pass
    
class BasicCoffee(Coffee) :
    def getDetail(self) :
        print('Basic Coffee', end="")
        
class CoffeeDecorator() :
    def __init__(self, coffee) -> None:
        self.__coffee = coffee
        
    # @property
    def getDetail(self):
        self.__coffee.getDetail()
  
class MilkDecorator(CoffeeDecorator):
    def getDetail(self) :
        CoffeeDecorator.getDetail(self)
        print(', with milk', end="")

class SugarDecorator(CoffeeDecorator):
    def getDetail(self) :
        CoffeeDecorator.getDetail(self)
        print(' , with sugur', end="")      

def clientCode( basicCoffee: BasicCoffee):
    basicCoffee.getDetail()

if __name__ == '__main__' :
    coffee : Coffee() =  BasicCoffee()
    clientCode(coffee) ; print()
    
    coffeeWithMilk : Coffee() = MilkDecorator(coffee)
    clientCode(coffeeWithMilk) ; print()
    
    coffeeWithMilkWithSugar : Coffee() = SugarDecorator(coffeeWithMilk)
    clientCode(coffeeWithMilkWithSugar) ; print()
    
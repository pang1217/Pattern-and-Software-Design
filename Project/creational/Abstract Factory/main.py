from __future__ import annotations
from abc import ABC, abstractmethod

#  Abstract Factory
class ClothesFactory(ABC):
    @abstractmethod
    def createMale(self) -> Male:
        pass

    @abstractmethod
    def createFemale(self) -> Female:
        pass
     
    @abstractmethod
    def createChild(self) -> Child:
        pass

# ConF
class Shirt(ClothesFactory):
    def createMale(self) -> Male:
        return MaleShirt()
    def createFemale(self) -> Female:
        return FemaleShirt()
    def createChild(self) -> Child:
        return ChildShirt()
# ConF
class Pants(ClothesFactory):
    def createMale(self) -> Male:
        return MalePants()

    def createFemale(self) -> Female:
        return FemalePants()
    
    def createChild(self) -> Child:
        return ChildPants()

#AP
class Male(ABC):
    @abstractmethod
    def getSize(self) -> str:
        pass
    def getPrice(self) -> str:
        pass
    def getColor(self) -> str:
        pass

#CP
class MaleShirt(Male):
    def getSize(self) -> str:
        return "Male Shirt Size M"
    def getPrice(self) -> str:
        return "Price 1000฿"
    def getColor(self) -> str:
        return "Color : Black"

#CP
class MalePants(Male):
    def getSize(self) -> str:
        return "Male Pants Size L"
    def getPrice(self) -> str:
        return "Price 1250฿"    
    def getColor(self) -> str:
        return "Color : Black"

# AP
class Female(ABC):
    @abstractmethod
    def getSize(self) -> str:
        pass
    def getPrice(self) -> str:
        pass
    def getColor(self) -> str:
        pass
    
# CP
class FemalePants(Female):
    def getSize(self) -> str:
        return "Female Pants Size M"
    def getPrice(self) -> str:
        return "Price 1500฿"    
    def getColor(self) -> str:
        return "Color : Cream"
  
# CP
class FemaleShirt(Female):
    def getSize(self) -> str:
        return "Female Shirt Size S"
    def getPrice(self) -> str:
        return "Price 1000฿"
    def getColor(self) -> str:
        return "Color : Black"

# AP
class Child(ABC):
    @abstractmethod
    def getSize(self) -> str:
        pass
    def getPrice(self) -> str:
        pass
    def getColor(self) -> str:
        pass

# CP
class ChildShirt(Child):
    def getSize(self) -> str:
        return "Child Shirt Size S"
    def getPrice(self) -> str:
        return "Price 750฿"
    def getColor(self) -> str:
        return "Color : White"

# CP
class ChildPants(Child):
    def getSize(self) -> str:
        return "Child Pants Size S"
    def getPrice(self) -> str:
        return "Price 500฿"    
    def getColor(self) -> str:
        return "Color : White"

# Client
def client_code(factory: ClothesFactory) -> None:
    male = factory.createMale()
    female = factory.createFemale()
    child = factory.createChild()

    print("----- Male -----")
    print(f"{male.getSize()}")
    print(f"{male.getPrice()}")
    print(f"{male.getColor()}")
    
    print("----- Female -----")
    print(f"{female.getSize()}")
    print(f"{female.getPrice()}")
    print(f"{female.getColor()}")
    
    print("----- Child -----")
    print(f"{child.getSize()}")
    print(f"{child.getPrice()}")
    print(f"{child.getColor()}")


if __name__ == "__main__":
    print("Shirt Factory")
    client_code(Shirt())
    
    print("\n")

    print("Pants Factory")
    client_code(Pants())
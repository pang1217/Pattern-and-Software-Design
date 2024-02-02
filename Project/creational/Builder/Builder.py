from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class ComputerBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    def buildCPU(self) -> None:
        pass
    
    def buildGPU(self) -> None:
        pass

    def buildRam(self) -> None:
        pass
    
    def buildStorage(self) -> None:
        pass
    
    def buildDisplay(self) -> None:
        pass

class PCBuilder(ComputerBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PersonalComputer()

    @property
    def product(self) -> PersonalComputer:
        product = self._product
        self.reset()
        return product

    def buildCPU(self, cpu) -> None:
        self._product.add("CPU : " + cpu)

    def buildGPU(self, gpu) -> None:
        self._product.add("GPU : " + gpu)

    def buildRam(self, ram) -> None:
        self._product.add("Ram : " + ram)
        
    def buildStorage(self, storage) -> None:
        self._product.add("Storage : " + storage)
        
    def buildDisplay(self, display) -> None:
        self._product.add("Diaplay : " + display)
        
class LaptopBuilder(ComputerBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Laptop()

    @property
    def product(self) -> Laptop:
        product = self._product
        self.reset()
        return product

    def buildCPU(self, cpu) -> None:
        self._product.add("CPU : " + cpu)

    def buildGPU(self, gpu) -> None:
        self._product.add("GPU : " + gpu)

    def buildRam(self, ram) -> None:
        self._product.add("Ram : " + ram)
        
    def buildStorage(self, storage) -> None:
        self._product.add("Storage : " + storage)
        
    def buildDisplay(self, display) -> None:
        self._product.add("Diaplay : " + display)
        
# Product
class PersonalComputer:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def showDetail(self) :
        for index in range(len(self.parts)):
            print(self.parts[index])

class Laptop:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def showDetail(self) :
        for index in range(len(self.parts)):
            print(self.parts[index])

# Editor
class Director:
   def makeGeneralComputer(self, builder : ComputerBuilder) : 
       builder.buildCPU("Intel® Core i5-1235U (12 MB Cache,10 Core, 12 Threads, up to 4.40 GHz, 15 W)")
       builder.buildDisplay("1920 x 1080")
       builder.buildRam("16GB, 1x16GB, DDR4 Non-ECC,3200 MHz")
       builder.buildStorage("M.2 512GB PCIe NVMe Class 35 Solid State Drive")
       return builder.product 
   
   def makeGamingComputer(self, builder : ComputerBuilder) : 
       builder.buildCPU("Intel Core Ultra 9 185H (3.80 GHz, 24 MB L3 Cache up to 5.10 Ghz)")
       builder.buildDisplay("2560 x 1600")
       builder.buildRam("32 GB DDR5 5200Mhz")
       builder.buildStorage("2TB SSD PCIe M.2 Gen 4")
       builder.buildGPU("NVIDIA GeForce RTX 4070 (8GB GDDR6) 105 Watt TGP")
       return builder.product 

if __name__ == "__main__":
    director = Director()
    
    print(f'{'='*10} LAPTOP {'='*10}')
    laptopBuilder = LaptopBuilder()
    print(f'{'-' * 5} General Laptop')
    generalLaptop : Laptop = director.makeGeneralComputer(laptopBuilder)
    generalLaptop.showDetail()
    
    print(f'{'-' * 5} Gaming Laptop')
    gamingLaptop : Laptop = director.makeGamingComputer(laptopBuilder)
    gamingLaptop.showDetail()
    
    print(f'\n\n{'='*10} Personal Computer {'='*10}')
    pcBuilder = PCBuilder()
    print(f'{'-' * 5} General PC')
    generalPersonalComputer : PersonalComputer = director.makeGeneralComputer(pcBuilder)
    generalPersonalComputer.showDetail()
    
    print(f'{'-' * 5} Gaming PC')
    gamingPersonalComputer : PersonalComputer = director.makeGamingComputer(pcBuilder)
    generalPersonalComputer.showDetail()
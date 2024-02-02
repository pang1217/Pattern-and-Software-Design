from __future__ import annotations

class ComputerFacade() :
    def __init__(self) -> None:
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def startComputer(self):
        print("start computer...")
        self.cpu.process_data()
        self.memory.load_data()
        self.hard_drive.read_data()
        print("Computer started successfully")
    
class CPU :
    def process_data(self):
        print("CPU processing data")

class Memory :
    def load_data(self):
        print("Memory load data")

class HardDrive:
    def read_data(self):
        print("Hard Drive read data")
        
if __name__ == "__main__":
    computerFacade = ComputerFacade()
    computerFacade.startComputer()
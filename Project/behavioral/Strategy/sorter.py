class SortingStrategy :
    def pay(self, amount) :
        pass
    
class Sorter():
    def __init__(self) -> None:
        self.strategy = None
    
    def setStrategy(self, s):
        self.strategy = s
        
    def sortData(self, data) :
       self.strategy.sort(data)
        
class BubbleSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using bubble sort")
        print(sorted(data))
        
class QuickSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using quick sort")
        print(sorted(data))
        
if __name__ == "__main__":
    data = [5, 2, 7, 1, 9]
    print(f'Data : {data}')
    sorter = Sorter()
    
    sorter.setStrategy(BubbleSort())
    sorter.sortData(data)
    
    
    print()
    print(f'Data : {data}')
    sorter.setStrategy(QuickSort())
    sorter.sortData(data)
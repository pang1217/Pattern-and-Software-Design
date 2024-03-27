class Bread :
    def make(self):
        self.mixIngredients()
        self.bake()
        self.slice()
        
    def mixIngredients(self):
        pass
    
    def bake(self):
        pass
    
    def slice(self) :
        print(f'Slicing the {self.__class__.__name__}')
        
class WhiteBread(Bread):
    def mixIngredients(self):
        print('Gathering ingredients for white bread.')
    
    def bake(self):
        print('Baking the white bread for 15 minutes.')
        
class WholeWheatBread(Bread):
    def mixIngredients(self):
        print('Gathering ingredients for whole wheat bread.')
    
    def bake(self):
        print('Baking the whole wheat bread for 20 minutes.')
        
if __name__ == '__main__':
    print('---- WhiteBread')
    whiteBread = WhiteBread()
    whiteBread.make()
    
    print('='*20)
    print('---- WholeWheatBread')
    wholeWheatBread = WholeWheatBread()
    wholeWheatBread.make()
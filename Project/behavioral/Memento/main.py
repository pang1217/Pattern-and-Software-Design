class Memento :
    def show() :
        pass
    
class GameMemento(Memento):
    def __init__(self, level, score) -> None:
        self.level = level
        self.score = score
        
    def getLevel(self):
        return self.level
    
    def getScore(self):
        return self.score
    
    def showMemento(self) :
        print(f'Game level : {self.level} Score : {self.score}')

class Originator :
    def saveProgress() :
        pass
    def restoreProgress(p):
        pass
    
class Game(Originator):
    def play(self, level, score) :
        self.level = level
        self.score = score
        print(f'Play at level {self.level} score : {self.score}')
        
    def showGame(self) :
        print(f'Game level : {self.level} Score : {self.score}')
    
    def saveProgress(self):
        print(f'Save Progress')
        return GameMemento(self.level, self.score)
    
    def restoreProgress(self, p):
        gp = p # g = game ; p = progress
        self.level = gp.getLevel()
        self.score = gp.getScore()
        print(f'Restore Progress at level {gp.getLevel()} score : {gp.getScore()}')
        
class Caretaker:
    def __init__(self, o) -> None:
        self.history = []
        self.originator = o
        
    def addHistory(self):
        self.history.append(self.originator.saveProgress())
        
    def undo(self):
        if self.history:
            memento = self.history.pop()
            self.originator.restoreProgress(memento)
        else:
            print("Nothing to undo.")
       
    def showHistory(self):
        print('History')
        for h in self.history:
            h.showMemento()  

if __name__ == '__main__':
    game = Game()
    caretaker = Caretaker(game)
    game.play(level=1, score=50)
    caretaker.addHistory()
    game.play(level=5, score=450)
    caretaker.addHistory()
    game.play(level=9, score=1200)
    
    print()
    caretaker.showHistory()
    
    print('Undo')
    caretaker.undo()
    game.showGame()
    
    print()
    caretaker.showHistory()
    
    caretaker.undo()
    game.showGame()
    
    caretaker.undo()
    game.showGame()
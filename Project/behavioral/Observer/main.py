class Observer:
    def update(msg):
        pass

class Publisher :
    def subscribe(self, s : Observer):
        pass
    
    def unsubscribe(self, s : Observer):
        pass

    def notify(self, msg):
        pass
    
class NetflixPublisher(Publisher):
    def __init__(self) -> None:
        self.observers = []
        
    def subscribe(self, s : Observer):
        print(f'{s.name} Subscribe Netflix')
        self.observers.append(s)
    
    def unsubscribe(self, s : Observer):
        print(f'{s.name} Unsubscribe Netflix')
        self.observers.remove(s)
        
    def notify(self):
        for observer in self.observers:
            observer.update(self.message, "Netflix")
            
    def setMessage(self, msg):
        self.message = msg
        self.notify()
        
class HBOPublisher(Publisher):
    def __init__(self) -> None:
        self.observers = []
        
    def subscribe(self, s : Observer):
        print(f'{s.name} Subscribe HBO')
        self.observers.append(s)
    
    def unsubscribe(self, s : Observer):
        print(f'{s.name} Unsubscribe HBO')
        self.observers.remove(s)
        
    def notify(self):
        for observer in self.observers:
            observer.update(self.message, "HBO")
            
    def setMessage(self, msg):
        self.message = msg
        self.notify()
        
class SpotifyPublisher(Publisher):
    def __init__(self) -> None:
        self.observers = []
        
    def subscribe(self, s : Observer):
        print(f'{s.name} Subscribe Spotify')
        self.observers.append(s)
    
    def unsubscribe(self, s : Observer):
        print(f'{s.name} Unsubscribe Spotify')
        self.observers.remove(s)
        
    def notify(self):
        for observer in self.observers:
            observer.update(self.message, "Spotify")
            
    def setMessage(self, msg):
        self.message = msg
        self.notify()

class Family(Observer):
    def __init__(self, name) -> None:
        self.name = name
        self.messageFromPublisher = ""
        self.publisher = ""
        
    def update(self, msg, publisher):
        self.messageFromPublisher = msg
        self.publisher = publisher
        self.showMessage()
        
    def showMessage(self):
        print(f'{self.name} Family from {self.publisher} => {self.messageFromPublisher}')
    
class Personal(Observer):
    def __init__(self, name) -> None:
        self.name = name
        self.messageFromPublisher = ""
        self.publisher = ""
        
    def update(self, msg, publisher):
        self.messageFromPublisher = msg
        self.publisher = publisher
        self.showMessage()
        
    def showMessage(self):
        print(f'{self.name} Personal from {self.publisher} => {self.messageFromPublisher}')
            
if __name__ == '__main__' :
    # Publisher
    netflix = NetflixPublisher()
    hbo = HBOPublisher()
    spotify = SpotifyPublisher()
    
    # Family
    potterFamily = Family("Potter")
    grangerFamily = Family("Granger")
    
    # Personal
    tom = Personal('Tom')
    jane = Personal('Jane')
    john = Personal('John')
    
    netflix.subscribe(potterFamily)
    netflix.subscribe(grangerFamily)
    netflix.subscribe(jane)
    netflix.subscribe(tom)
    netflix.subscribe(john)
    
    print()
    netflix.setMessage('New content avaliable!')
    
    print()
    netflix.unsubscribe(jane)
    netflix.unsubscribe(grangerFamily)
    
    print()
    netflix.setMessage('New content avaliable!')
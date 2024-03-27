class State :
    def start(self):
        pass
    def stop(self):
        pass
    def pause(self):
        pass
    def open(self):
        pass
    
class WorkingState(State):
    def start(self):
        print('Microwave is working already')
        
    def stop(self):
        print('Microwave is stopped.')
        return WaitingState()
    
    def pause(self):
        print('Microwave is paused.')
        return PausedState()
    
    def open(self):
        print('Microwave is open')
        return PausedState()
    
class WaitingState(State):
    def start(self):
        print('Microwave is working, Please wait .....')
        return WorkingState()
        
    def stop(self):
        print('The Microwave is not working already')
        
    def pause(self):
        print('The Microwave is not working already')

    def open(self):
        print('Microwave is open')
    
class PausedState(State):
    def start(self):
        print('Microwave is resumed.')
        return WorkingState()
        
    def stop(self):
        print('Microwave is stopped.')
        return WaitingState()
        
    def pause(self):
        print('Microwave is already paused')
    
    def open(self):
        print('Open Microwave is already paused')
        
    
class Microwave:
    def __init__(self) -> None:
        self.state = WaitingState()
        
    def changeState(self, s) :
        if s != None :
            self.state = s
    
    def start(self):
        self.changeState(self.state.start())
        
    def stop(self):
        self.changeState(self.state.stop())
        
    def pause(self):
        self.changeState(self.state.pause())
        
    def open(self):
        self.changeState(self.state.open())
    
if __name__ == '__main__' :
    microwave = Microwave()
    microwave.start()
    microwave.pause()
    microwave.stop()
    microwave.open()
    
    print()
    microwave.stop()
    microwave.open()
		
    print()
    microwave.start()
    microwave.open()
    
    print()
    microwave.start()
    microwave.open()
    
    print()
    microwave.stop()
    
    print()
    microwave.start()
    microwave.pause()
    microwave.open()
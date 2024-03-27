class Journey : 
    def __init__(self) -> None:
        self.thingToDo = []
          
    def takeATrip(self):
        self.thingToDo.append(self.buyAFight())
        self.thingToDo.append(self.takePlane())
        self.thingToDo.append(self.hook1())
        self.thingToDo.append(self.enjoyVacation())
        self.thingToDo.append(self.buyGift())
    
    def enjoyVacation(self):
        pass
    
    def buyGift(self):
        pass
    
    def hook1(self):
        pass
    
    def buyAFight(self):
        return 'Buy a flight ticket'
    
    def takePlane(self):
        return 'Taking the plane'
    
    def getThingToDo(self):
        for msg in self.thingToDo :
            print(msg)
    
class BeachJourney(Journey):
    def enjoyVacation(self):
        return "Swimming and sun-bathing"
    def buyGift(self):
        return ''
    
class CityJourney(Journey):
    def enjoyVacation(self):
        return "Eat, drink, take photos and sleep" 

    def buyGift(self):
        return "Buy a gift"
    
class MountainJourney(Journey):
    def enjoyVacation(self):
        return "Mountain climbing" 

    def buyGift(self):
        return "Buy a gift"
    
    def hook1(self):
        return "rent car"
    
if __name__ == '__main__' :
    print('---- BeachJourney')
    beachJourney = BeachJourney()
    beachJourney.takeATrip()
    beachJourney.getThingToDo()
    
    print(f'{'='*25} \n---- CityJourney')
    cityJourney = CityJourney()
    cityJourney.takeATrip()
    cityJourney.getThingToDo()
    
    print(f'{'='*25} \n---- MountainJourney')
    mountainJourney = MountainJourney()
    mountainJourney.takeATrip()
    mountainJourney.getThingToDo()
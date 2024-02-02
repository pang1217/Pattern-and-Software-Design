class Booking :
    def calculatePrice(self) :
        pass
    def getDetail(self) :
        pass
    
class DoubleRoom(Booking) :
    def calculatePrice(self) :
        return 40
    
    def getDetail(self) :
        print('DoubleRoom', end="")
        
class BookingDecorator() :
    def __init__(self, booking) -> None:
        self.__booking = booking
        
    def calculatePrice(self):
        return self.__booking.calculatePrice()
    
    def getDetail(self):
        self.__booking.getDetail()
  
class WifiDecorator(BookingDecorator):
    def calculatePrice(self) :
        return BookingDecorator.calculatePrice(self) + 2
    
    def getDetail(self) :
        BookingDecorator.getDetail(self)
        print(', with wifi', end="")

class DoubleBedDecorator(BookingDecorator):
    def calculatePrice(self) :
        return BookingDecorator.calculatePrice(self) + 20
    
    def getDetail(self) :
        BookingDecorator.getDetail(self)
        print(' , with extra bed', end="")      

def clientCode( room: BookingDecorator):
    room.getDetail(); print()
    print(f'Price {room.calculatePrice()} $')

if __name__ == '__main__' :
    room : Booking() =  DoubleRoom()
    clientCode(room) ; print()
    
    roomwithWifi : Booking() = WifiDecorator(room)
    clientCode(roomwithWifi) ; print()
    
    roomwithWifiWithExtraBed : Booking() = DoubleBedDecorator(roomwithWifi)
    clientCode(roomwithWifiWithExtraBed) ; print()
    
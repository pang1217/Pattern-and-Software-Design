class ATMHandler :
    def setNext(self, atm ) :
        pass
    
    def handle(self, request):
        pass
    
class ATM(ATMHandler) :
    def setNext(self, atm: ATMHandler):
        self.nextHandler = atm
        
    def handle(self, request) :
        if self.nextHandler :
            self.nextHandler.handle(request)
            
class CardReader (ATM) :
    def handle(self, request) :
        print('-- Card Handle')
        if request[0]:
            print('card active')
            self.nextHandler.handle(request)
        else :
            print('card not active')

class Pin(ATM) :
    def handle(self, request) :
        print('-- Pin handle')
        if str(request[1]) == '1234':
            print("Pin Correct")
            self.nextHandler.handle(request)
        else :
            print("Pin not Correct")

class WithDraw(ATM):
    def handle(self, request) :
        print('-- With Draw handle')
        print('Balance : 10000')
        if request[2] < 10000 :
            print('Withdraw Success')
            print(f'Withdraw : {request[2]}\nCurrent Balance : {10000 - request[2]}')
            self.nextHandler.handle(request)
        else :
            print('Withdraw Fail')

class Bill(ATM) :
    def handle(self, request) :
        print('-- Bill handle')
        if request[3] :
            print("print bill\nthank you!")
        else :
            print('thank you!')

if __name__ == '__main__' :
    h1 = CardReader()
    h2 = Pin()
    h3 = WithDraw()
    h4 = Bill()
    
    h1.setNext(h2)
    h2.setNext(h3)
    h3.setNext(h4)
    
    #  card, pin, withdraw, bill
    h1.handle([True, 1234, 500, True])
    print()
    h1.handle([False, '1234', 500, True])
    print()
    h1.handle([True, 3241, 500, True])
    print()
    h1.handle([True, 1234, 11000, True])
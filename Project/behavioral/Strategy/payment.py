class PaymentStrategy :
    def pay(self, amount) :
        pass
    
class PaymentProcessor():
    def __init__(self) -> None:
        self.strategy = None
    
    def setStrategy(self, s):
        self.strategy = s
        
    def processPayment(self, amount) :
       self.strategy.pay(amount)
        
class CreditCardPayment(PaymentStrategy):
    def __init__(self, cardNumber, expirationDate, cvv) -> None:
        self.cardNumber = cardNumber
        self.expirationDate = expirationDate
        self.cvv = cvv
      
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}")
        
class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}")

if __name__ == "__main__":
    credit_card = CreditCardPayment("1234 5678 9012 3456", "12/24", "123")
    paypal = PayPalPayment("example@example.com", "password")

    payment_processor = PaymentProcessor()
    payment_processor.setStrategy(credit_card)
    payment_processor.processPayment(100)

    payment_processor.setStrategy(paypal)
    payment_processor.processPayment(50)
from __future__ import annotations
from abc import ABC, abstractmethod

# Implement
class MessagingPlatform(ABC) :
    @abstractmethod
    def sendMessage(self, message, recipient):
        pass
    
    @abstractmethod
    def receiveMessage(self, message, sender):
        pass

class SMSService(MessagingPlatform) :
    def sendMessage(self, message, recipient):
        print( f'Sending SMS : "{message}" to {recipient} ')
    
    def receiveMessage(self, message, sender):
        print( f'Receiving SMS : "{message}" from {sender} ')

class EmailMessagingPlatform(MessagingPlatform) :
    def sendMessage(self, message, recipient):
        print( f'Sending Email : "{message}" to {recipient} ')
    
    def receiveMessage(self, message, sender):
        print( f'Receiving Email : "{message}" from {sender} ')

# Abstract
class Message(ABC) :
    def __init__(self, MessagingPlatform) -> None:
        self.messagingPlatform = MessagingPlatform
        
    @abstractmethod
    def send(self, message, recipient) :
        pass
    
    @abstractmethod
    def receive(self, message, recipient) :
        pass
    
class MultimediaMessage(Message) :
    def send(self, message, recipient):
        self.messagingPlatform.sendMessage(message, recipient)
    
    def receive(self, message, sender):
        self.messagingPlatform.receiveMessage(message, sender)

class TextMessage(Message) :
    def send(self, message, recipient):
        self.messagingPlatform.sendMessage(message, recipient)
    
    def receive(self, message, sender):
        self.messagingPlatform.receiveMessage(message, sender)
    
if __name__ == "__main__":
    email_platform = EmailMessagingPlatform()
    sms_platform = SMSService()

    text_message1 = TextMessage(email_platform)
    text_message2 = TextMessage(sms_platform)

    text_message1.send("Hello!", "user@example.com")
    text_message2.receive("Hi there!", "1234567890")

    # ------------------------------------
    print('='*20)
    multimedia_message1 = MultimediaMessage(email_platform)
    multimedia_message2 = MultimediaMessage(sms_platform)

    multimedia_message1.send("Check out this website.", "user@example.com")
    multimedia_message2.receive("New video available.", "9876543210")
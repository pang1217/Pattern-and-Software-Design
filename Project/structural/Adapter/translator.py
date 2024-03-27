from translate import Translator

class English :
    def __init__(self, message) -> None:
        self.message = message
        
    def getMessage(self) -> str :
        return self.message
    
    def canTranslate(translator) :
        return translator.getMessage()
    
class Translator :
    def translate (self):
        pass

class ThaiAdapter : 
    def __init__(self, adaptee) -> None:
        self.adaptee = adaptee
        
    def translate(self):
        return self.adaptee.translate()

class ThaiAdaptee :
    def __init__(self, thaiMessage) -> None:
        self.thaiMessage = thaiMessage
        
    def translate(self):
        return self.thaiMessage

if __name__ == '__main__':
    eng = English('Hello')
    
    thaiAdaptee = ThaiAdaptee()
    thai = ThaiAdapter(thaiAdaptee)
    print(thai.translate())


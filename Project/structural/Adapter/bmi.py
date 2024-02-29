class Calculator :
    def bmi(self, weight, height) :
        pass
    
# Adapter
class BMICalculator (Calculator):
    def __init__(self, service) -> None:
        self.service = service
        
    def bmi(self, weight, height) :
        print(f'weight : {weight} height : {height} bmi = ', self.service.calculate(weight, height))
        
    def meterToInches(self, height):
        return self.meterToCm(height) / 2.54
    
    def meterToCm(self, height):
        return height * 100
    
    def kgToPound(self, weight) :
        return weight * 2.2
        
# Adaptee
class BMIService :
    def calculate (self, weight, height) :
        return weight / (height ** 2)
        
if __name__ == '__main__' :
    service = BMIService()
    bmiCalculator = BMICalculator(service)
    
    bmiCalculator.bmi(65, 1.55) # input weight (KG), and height (Meter)
    
    print(f'1.55 meter = {bmiCalculator.meterToInches(1.55)} inches')
    print(f'1.55 meter = bmiCalculator.meterToCm(1.55) cm.')
    print(f'65 kg. = {bmiCalculator.kgToPound(65)} pound')
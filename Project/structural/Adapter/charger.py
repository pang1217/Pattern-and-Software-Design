# Target interface
class Charger:
    def charge(self):
        pass

# Adaptee - US charger
class USCharger:
    def __init__(self):
        self.voltage = 120
    
    def chargeWithUsPlug(self):
        print(f"Charging with {self.voltage}V")

# Adapter - US to EU charger adapter
class EUAdapter(Charger):
    def __init__(self, usCharger):
        self.usCharger = usCharger

    def charge(self):
        print("Adapting US charger to EU charger...")
        self.usCharger.chargeWithUsPlug()

# Adaptee - EU charger
class EUCharger:
    def __init__(self):
        self.voltage = 220
    
    def chargeWithEuPlug(self):
        print(f"Charging with {self.voltage}V")

# Adapter - EU to US charger adapter
class USAdapter(Charger):
    def __init__(self, euCharger):
        self.euCharger = euCharger

    def charge(self):
        print("Adapting EU charger to US charger...")
        self.euCharger.chargeWithEuPlug()

if __name__ == '__main__':
    eu_charger = EUCharger()
    us_adapter = USAdapter(eu_charger)
    us_adapter.charge()

    print()
    us_charger = USCharger()
    eu_adapter = EUAdapter(us_charger)
    eu_adapter.charge()


class Kilometer:
    def __init__(self, km):
        self.km = km

    def getKM(self):
        return self.km

class Meter:
  def __init__(self, meter):
    self.meter = meter

  def getKM(self):
    return self.meter / 1000  # Conversion from meters to kilometers

# Interface for Distance Measurement
class Distance:
    def getKM(self):
        pass

class Mile:
    def __init__(self, mile):
        self.mile = mile

class MileAdapter(Distance):
    def __init__(self, mile):
        self.mile = mile.mile  # Access the actual mile value

    def getKM(self):
        return self.mile * 1.60934 

class MeterAdapter(Distance):
    def __init__(self, meter):
        self.meter = meter

    def getKM(self):
        return Meter(self.meter).getKM()  # Leverage Meter class for conversion

# Usage
km_distance = Kilometer(5)
meter_distance = Meter(2000)
mile_distance = Mile(2)

print(f"Kilometer distance: {km_distance.getKM()} km")
print(f"Meter distance (converted to KM): {meter_distance.getKM()} km")

# Using adapters for Miles
mile_adapter = MileAdapter(mile_distance)
print(f"Mile distance (converted to KM using adapter): {mile_adapter.getKM()} km")

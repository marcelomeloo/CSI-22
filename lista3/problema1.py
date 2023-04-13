class Vehicle:
  def __init__(self, name, mileage, capacity):
    self.name = name
    self.mileage = mileage
    self.capacity = capacity

  def fare(self):
    return self.capacity * 100

class Bus(Vehicle):
  def __init__(self, name, mileage, capacity):
    super().__init__(name, mileage, capacity)

  def fare(self):
    return super().fare() * 110 / 100

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
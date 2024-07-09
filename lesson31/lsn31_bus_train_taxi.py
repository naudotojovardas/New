# Create a Bus, Taxi, and Train child class that inherits from the Vehicle class.
# Implement at least five methods in a superclass that would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100. If the Vehicle is a Bus instance, we need to add an extra 10% on the full fare as a maintenance charge.

class Vehicle:
    def __init__(self, name, seating_capacity, fare_charge):
        self.name = name
        self.seating_capacity = seating_capacity
        self.fare_charge = seating_capacity * 100

    def display_vehicle(self):
        return f"Vehicle: {self.name}, Seating Capacity: {self.seating_capacity}, Fare Charge: {self.fare_charge}"

    def start_engine(self):
        return f"{self.name} is starting the engine."

    def stop_engine(self):
        return f"{self.name} is stopping the engine."

    def accelerate(self):
        return f"{self.name} is accelerating."

    def brake(self):
        return f"{self.name} is braking."
    
class Bus(Vehicle):
    def __init__(self, name, seating_capacity, fare_charge):
        super().__init__(name, seating_capacity, fare_charge)
        self.fare_charge = self.fare_charge + (self.fare_charge * 0.10)

    def display_vehicle(self):
        return f"Vehicle: {self.name}, Seating Capacity: {self.seating_capacity}, Fare Charge: {self.fare_charge}"
    
class Taxi(Vehicle):
    def __init__(self, name, seating_capacity, fare_charge):
        super().__init__(name, seating_capacity, fare_charge)

class Train(Vehicle):
    def __init__(self, name, seating_capacity, fare_charge):
        super().__init__(name, seating_capacity, fare_charge)

bus = Bus("Bus", 50, 0)
taxi = Taxi("Taxi", 4, 0)
train = Train("Train", 200, 0)


print(bus.display_vehicle())
print(bus.start_engine())
print(bus.accelerate())
print(bus.brake())
print(bus.stop_engine())

print(taxi.display_vehicle())
print(taxi.start_engine())
print(taxi.accelerate())
print(taxi.brake())
print(taxi.stop_engine())

print(train.display_vehicle())
print(train.start_engine())
print(train.accelerate())
print(train.brake())
print(train.stop_engine())

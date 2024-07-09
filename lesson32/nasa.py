# NASA needs to calculate expenses for the new mission: using OOP principles to implement Base and SpaceShuttle classes. Create a simple calculator with:
# Base class should give functionality to know info about spacecraft (age, cost, year built, weight, etc.)
# Through the main class, you should be able to calculate the mission cost which includes:
#  fuel cost (FUEL_COST x BURN_RATE (kg/mile) * BURN_RATE_VARIABLE (2500 / orbit_height(in miles))), average personals expenditures ( people x base_salary )
# Prepare the final report in the file document and on-screen with the method get_full_report with all gathered and calculated data

import datetime

class Base:
    def __init__(self, name, year_built, weight, cost, burn_rate, fuel_cost):
        self.name = name
        self.year_built = year_built
        self.weight = weight
        self.cost = cost
        self.burn_rate = burn_rate
        self.fuel_cost = fuel_cost

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year_built

    def get_info(self):
        return f"Name: {self.name}, Year built: {self.year_built}, Weight: {self.weight}, Cost: {self.cost}, Burn rate: {self.burn_rate}, Fuel cost: {self.fuel_cost}"
    
class SpaceShuttle(Base):
    def __init__(self, name, year_built, weight, cost, burn_rate, fuel_cost, people, base_salary, orbit_height):
        super().__init__(name, year_built, weight, cost, burn_rate, fuel_cost)
        self.people = people
        self.base_salary = base_salary
        self.orbit_height = orbit_height

    def get_fuel_cost(self):
        return self.fuel_cost * self.burn_rate * (2500 / self.orbit_height)

    def get_personals_cost(self):
        return self.people * self.base_salary

    def get_full_report(self):
        return f"Spacecraft: {self.name}, Age: {self.get_age()}, Weight: {self.weight}, Cost: {self.cost}, Burn rate: {self.burn_rate}, Fuel cost: {self.get_fuel_cost()}, Personals cost: {self.get_personals_cost()}"
    

base = Base("SpaceX", 2000, 100000, 1000000, 100, 10)
shuttle = SpaceShuttle("SpaceX", 2000, 100000, 1000000, 100, 10, 10, 1000, 1000)
print(base.get_info())
print(shuttle.get_full_report())

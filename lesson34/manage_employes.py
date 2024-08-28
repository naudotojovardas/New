# Create a complex system to manage employee records, including salaries, roles, and performance reviews using a combination of instance, static, and class methods.
# Specifications
# Base Class - Employee:
# Instance Variables: name, id, salary.
# Instance Methods: give_raise(percentage).
# Class Method: set_raise_amt(percentage): Adjust raise amounts company-wide.
# Static Method: standard_performance_index(score): Returns a normalized performance score.
# Subclass - Manager:
# Additional Attributes: subordinates (a list of Employees under this manager).
# Additional Methods: add_subordinate(emp), remove_subordinate(emp_id).
# Usage of Inheritance and Encapsulation:
# Data about salaries and subordinates should be protected to prevent unauthorized access.
# Example usage
# mgr = Manager("Jane Doe", "001", 90000)
# emp = Employee("John Smith", "002", 50000)
# mgr.add_subordinate(emp)
# Applying changes and displaying information
# mgr.give_raise()
# print(mgr._salary)  # Output: 92700.0
# Changes made by me:
# every time print function is called there is couple of seconds delay to make it more realistic
# added __str__ method to both classes to make it easier to print objects
# added time module to make it possible to use time.sleep() function

import time

class Employee:
    raise_amt = 1.05

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self._salary = salary

    def give_raise(self, percentage):
        self._salary = self._salary * (1 + percentage)
        print("Raising salary by", percentage * 100, "%")
        time.sleep(2)

    @classmethod
    def set_raise_amt(cls, percentage):
        cls.raise_amt = percentage
        print("Setting raise amount to", percentage * 100, "%")
        time.sleep(2)

    @staticmethod
    def standard_performance_index(score):
        print("Calculating performance index for score", score)
        time.sleep(2)
        return score / 100
    
    def __str__(self):
        return f"Employee: {self.name}, ID: {self.id}, Salary: {self._salary}"
    
class Manager(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)
        self.subordinates = []

    def add_subordinate(self, emp):
        self.subordinates.append(emp)
        print("Adding subordinate", emp.name)
        time.sleep(2)

    def remove_subordinate(self, emp_id):
        for emp in self.subordinates:
            if emp.id == emp_id:
                self.subordinates.remove(emp)
                print("Removing subordinate", emp.name)
                time.sleep(2)
                return
        print("Subordinate not found")
        time.sleep(2)

    def give_raise(self):
        self._salary = self._salary * self.raise_amt
        print("Raising salary by", self.raise_amt * 100, "%")
        time.sleep(2)

    def __str__(self):
        return f"Manager: {self.name}, ID: {self.id}, Salary: {self._salary} \nSubordinates: {', '.join([emp.name for emp in self.subordinates])}"
    

def main():
    mgr = Manager("Jane Doe", "001", 90000)
    emp = Employee("John Smith", "002", 50000)
    Employee.set_raise_amt(1.1)
    mgr.add_subordinate(emp)
    mgr.give_raise()
    mgr.give_raise()
    mgr.remove_subordinate("002")
    print(mgr)
    print(emp)

main()


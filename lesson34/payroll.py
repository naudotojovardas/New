# Create a class called Employee with a static method called calculate_payroll that takes a list of
#  Employee instances and returns the total amount to be paid to all employees. Each Employee instance has two attributes: name and salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_payroll(employees):
        return sum([emp.salary for emp in employees])   
    
emp1 = Employee("John", 1000)
emp2 = Employee("Alice", 1500)
emp3 = Employee("Bob", 1200)
employees = [emp1, emp2, emp3]
print(Employee.calculate_payroll(employees)) 


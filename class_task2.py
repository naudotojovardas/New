class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = f"{first_name} {last_name}"
        self.email = f"{first_name}.{last_name}@company.com".lower()

emp1 = Employee('kaziukas', 'kazaitis')
print(emp1.fullname) 
print(emp1.email) 

emp2 = Employee('grazioji', 'mergaite')
print(emp2.fullname) 
print(emp2.email)
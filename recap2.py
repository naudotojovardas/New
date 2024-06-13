employees = [
    {'name': 'Ben', 'age': 25, 'salary': 80000},
    {'name': 'Guy', 'age': 50, 'salary': 100000},
    {'name': 'Is', 'age': 35, 'salary': 60000},
    {'name': 'Nuts', 'age': 44, 'salary':90000}
]

sorted_by_salary = sorted(employees, key=lambda x: x['salary'])
print(sorted_by_salary)
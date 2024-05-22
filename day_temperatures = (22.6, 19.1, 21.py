students = set()
while True :
    student = input('Please state your name(or type done):')
    if student.lower() == 'done':
        break
    students.add(student)
    print(f'{student} was added to the list')
print('students listed:' ,  students)
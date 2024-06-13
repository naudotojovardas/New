class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []  

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Added grade: {grade}")
        else:
            print("Grade must be between 0 and 100.")

    def get_average_grade(self):
        if self.__grades:
            average = sum(self.__grades) / len(self.__grades)
            return average
        return 0

    def get_grades(self):
        return self.__grades

# Example usage
student = Student("morgan freeman", "A12345")
student.add_grade(69) 
student.add_grade(42) 
student.add_grade(91)
print(student.get_grades())   
print(student.get_average_grade())

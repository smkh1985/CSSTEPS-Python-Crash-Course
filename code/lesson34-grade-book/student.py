class Student:
    def __init__(self, name, age):
        self.grades = {}
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    def add_grade(self, course, grade):
        if grade < 0 or grade > 100:
            print(f"{grade} is not a valid grade")
            return
        self.grades[course] = grade
        
    def print_grades(self):
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
        
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

student1 = Student("Emma", 20)
student1.print_info()

student2 = Student("Sam", 22)
student2.print_info()

student1.age = 21
student1.print_info()

student1.add_grade("Math", 90)
student1.add_grade("Science", 85)
student2.add_grade("Math", 75)
student1.add_grade("Math", 95)
student2.add_grade("Science", 150)
student1.print_grades()
student2.print_grades()
print(student1.average(), student2.average())

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Student(User):
    def __init__(self, first_name, last_name, student_id, grades=None):
        super().__init__(first_name, last_name)
        self.student_id = student_id
        if grades is None:
            grades = []
        self.grades = grades
        
    def __str__(self):
        text = super().__str__()
        return f"{text}, student {self.student_id}, grades: {len(self.grades)}"
        
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
        
user1 = User("Emma", "Clark")
print(user1)
student1 = Student("Sam", "Lee", 1001)
print(student1)
student2 = Student("Mia", "Wong", 1002, [90, 80])
print(student2)
print(student2.average())
student3 = Student("Leo", "Park", 1003)
student1.grades.append(95)
print(student1)
print(student3)

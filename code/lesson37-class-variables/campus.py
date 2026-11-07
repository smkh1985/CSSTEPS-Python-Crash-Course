class Student:
    university = "UBC"

    def __init__(self, name):
        self.name = name
        
s1 = Student("Emma")
s2 = Student("Sam")
print(s1.university, s2.university)
Student.university = "SFU"
print(s1.university, s2.university)
s1.university = "UVic"
print(s1.university, s2.university)
print(Student.university)

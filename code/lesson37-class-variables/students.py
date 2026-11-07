class Student:
    count = 0
    next_id = 1000

    def __init__(self, name):
        self.name = name
        Student.count += 1
        self.id = Student.next_id
        Student.next_id += 1
        
s1 = Student("Emma")
s2 = Student("Sam")
s3 = Student("Mia")

print(Student.count)
print(s1.id, s2.id, s3.id)

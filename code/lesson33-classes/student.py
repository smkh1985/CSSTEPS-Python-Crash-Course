class Student:
    def __init__(self, name, age):
        print("A new student is created")
        self.name = name
        self.age = age
        
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
student1 = Student("Emma", 20)
student1.print_info()

student2 = Student("Sam", 22)
student2.print_info()

print(type(student1))
print(type(student2))

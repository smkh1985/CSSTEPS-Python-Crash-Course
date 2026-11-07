import json


class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "courses": self.courses,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
        

emma = Student("Emma", 20, ["Python", "Math"])

with open("student.json", "w") as f:
    json.dump(emma.to_dict(), f, indent=4)

with open("student.json") as f:
    data = json.load(f)

student = Student.from_dict(data)
print(student.name, student.age, student.courses)
print(type(student))

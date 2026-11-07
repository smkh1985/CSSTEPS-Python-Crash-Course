from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    percent: float = 0.0
        
s1 = Student("Emma", 20, 90.0)
s2 = Student("Emma", 20, 90.0)
s3 = Student("Sam", 22)

print(s1)
print(s1 == s2)
print(s3)

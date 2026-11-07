from dataclasses import dataclass, field

@dataclass
class Course:
    name: str
    students: list[str] = field(default_factory=list)
    
math = Course("Math")
science = Course("Science")
math.students.append("Emma")
print(math)
print(science)

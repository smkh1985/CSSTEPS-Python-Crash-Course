import json

with open("students.json") as f:
    students = json.load(f)
    
sam = {"name": "Sam", "age": 22, "courses": ["Math"], "is_active": True}
students.append(sam)

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)
    
print(len(students), "students saved")

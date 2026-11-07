import json

with open("student.json") as f:
    student = json.load(f)
    
print(student)
print(type(student))
print(student["name"])
print(student["courses"][0])
print(student["address"]["city"])

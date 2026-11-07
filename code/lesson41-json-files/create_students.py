import json

emma = {
    "name": "Emma",
    "age": 20,
    "courses": ["Python", "Math"],
    "address": {"city": "Victoria", "country": "Canada"},
    "is_active": True,
    "middle_name": None,
}
students = [emma]

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

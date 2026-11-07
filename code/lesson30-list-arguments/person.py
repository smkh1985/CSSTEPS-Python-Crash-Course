def title_values(person):
    for key, value in person.items():
        person[key] = value.title()
        
person = {"name": "emma clark", "city": "victoria", "job": "data analyst"}
title_values(person)
print(person)

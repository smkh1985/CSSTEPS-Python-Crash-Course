countries = [
    {"name": "Canada", "capital": "Ottawa", "population": 41},
    {"name": "Japan", "capital": "Tokyo", "population": 124},
    {"name": "Brazil", "capital": "Brasilia", "population": 212},
]

for country in countries:
    for key, value in country.items():
        print(f"{key}: {value}")

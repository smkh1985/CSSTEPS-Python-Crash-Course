cities = ["Victoria", "Vancouver", "Seattle"]
travel_times = [0, 3, 7]

for city, hours in zip(cities, travel_times):
    print(f"{city} | {hours} hours from the start")
    
for stop_number, city in enumerate(cities, start=1):
    print(f"{stop_number}. {city}")

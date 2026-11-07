names = ["Leo", "Ruth", "Ben"]
ages = [10, 70, 30]

for name, age in zip(names, ages):
    if age < 12 or age >= 65:
        print(f"{name}, {age}: Admission is free.")
    else:
        print(f"{name}, {age}: A ticket is required.")

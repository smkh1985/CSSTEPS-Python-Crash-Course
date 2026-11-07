def show_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be a whole number")
    if age < 0:
        raise ValueError("Age can't be negative")
    print(f"You are {age} years old.")

show_age(10)
show_age("ten")

def print_profile(name, **details):
    print(f"Profile for {name}")

    for field, value in details.items():
        print(f"  {field}: {value}")
    
print_profile("Maya", city="Victoria", email="maya@example.com")
print_profile("Leo", age=30, job="teacher")

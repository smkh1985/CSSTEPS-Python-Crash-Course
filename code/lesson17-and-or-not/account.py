names = ["Emma", "Sam"]
active = [False, True]

for name, isActive in zip(names, active):
    if not isActive:
        print(f"{name}: Please activate your account.")
    print(f"{name}: Account check complete.")

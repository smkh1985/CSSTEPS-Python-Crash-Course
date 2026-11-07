def print_guest_list(*names, numbered=True):
    for position, name in enumerate(names, start=1):
        if numbered:
            print(f"{position}. {name}")
        else:
            print(name)
    
print_guest_list("Ava", "Ben", "Chloe")
print_guest_list("Dan", "Eve", numbered=False)

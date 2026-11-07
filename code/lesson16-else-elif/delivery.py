weights = [0.5, 3, 8]

for weight in weights:
    if weight <= 1:
        print(f"{weight} kg: Delivery costs $5.")
    elif weight <= 5:
        print(f"{weight} kg: Delivery costs $10.")
    else:
        print(f"{weight} kg: Delivery costs $20.")

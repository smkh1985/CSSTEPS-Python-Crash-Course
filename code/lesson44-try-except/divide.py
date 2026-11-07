try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    result = dividend / divisor
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError as e:
    print("Error: Invalid input:", e)
else:
    print(f"Result of division: {result}")

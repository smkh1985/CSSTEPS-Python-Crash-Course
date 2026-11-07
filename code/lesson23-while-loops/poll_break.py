poll_results = {}

while True:
    name = input("\nWhat is your name? ")
    if name.strip() == "":
        print("Please type a name.")
        continue
    language = input("What is your favorite programming language? ")

    poll_results[name] = language

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.strip().lower() == 'no':
        break

print("\n--- Poll Results ---")
for name, language in poll_results.items():
    print(f"{name.title()} loves {language.title()}.")

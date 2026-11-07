poll_results = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    language = input("What is your favorite programming language? ")
    
    poll_results[name] = language
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.strip().lower() == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, language in poll_results.items():
    print(f"{name.title()} loves {language.title()}.")

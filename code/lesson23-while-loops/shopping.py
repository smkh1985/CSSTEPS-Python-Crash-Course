shopping_list = []

item = input("Add an item, or press Enter to finish: ").strip()

while item != "":
    shopping_list.append(item)
    item = input("Add an item, or press Enter to finish: ").strip()
    
print("Your shopping list:")
for item in shopping_list:
    print(f"- {item}")

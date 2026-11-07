def modify_and_redefine(my_list):
    my_list.append("Appended Inside")
    print("Inside (after append):   ", my_list)
    my_list = ["New List", "Completely", "Redefined"]
    print("Inside (after redefine): ", my_list)
    
original_list = ["Initial Item"]
print("Outside (before function):", original_list)
print("-" * 40)
modify_and_redefine(original_list)
print("-" * 40)
print("Outside (after function): ", original_list)

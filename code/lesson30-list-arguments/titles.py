def title_in_place(items):
    for i in range(len(items)):
        items[i] = items[i].title()
        
def title_copy(items):
    return [item.title() for item in items]
        
names = ["emma clark", "sam lee", "ava jones"]
result = title_in_place(names)
print(names)
print(result)
guests = ["ben ross", "chloe king"]
titled = title_copy(guests)
print(guests)
print(titled)

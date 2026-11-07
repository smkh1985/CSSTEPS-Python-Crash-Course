from contacts import add_contact, show_contacts, find_contact as find

book = {}
add_contact(book, "Emma", "555-0101")
add_contact(book, "Sam", "555-0199")
show_contacts(book)
print(find(book, "Sam"))

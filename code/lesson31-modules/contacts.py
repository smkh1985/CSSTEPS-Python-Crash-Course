def add_contact(contacts, name, phone):
    contacts[name] = phone


def find_contact(contacts, name):
    return contacts.get(name)


def show_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

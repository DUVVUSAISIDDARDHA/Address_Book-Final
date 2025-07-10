from contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("\nContact added successfully!\n")
        print("Saved Contact:")
        print("----------------------------")
        print(contact.display())
        print("----------------------------")

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print("----------------------------")
                print(contact.display())
                print("----------------------------")

    
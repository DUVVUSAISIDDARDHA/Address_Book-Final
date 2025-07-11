from contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []

    # UC2: Add a new contact with duplicate check
    def add_contact(self, contact):
        for existing in self.contacts:
            if (existing.first_name.lower() == contact.first_name.lower() and
                existing.last_name.lower() == contact.last_name.lower()):
                print("\nDuplicate contact! Person already exists in this address book.\n")
                return

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

    
    def edit_contact(self, first_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                print("Contact found. Enter new details:")
                contact.last_name = input("New Last Name: ") or contact.last_name
                contact.address = input("New Address: ") or contact.address
                contact.city = input("New City: ") or contact.city
                contact.state = input("New State: ") or contact.state
                contact.zip_code = input("New Zip Code: ") or contact.zip_code
                contact.phone = input("New Phone: ") or contact.phone
                contact.email = input("New Email: ") or contact.email
                print("\nContact updated successfully:")
                print("----------------------------")
                print(contact.display())
                print("----------------------------")
                return
        print("Contact not found.")

    
    def delete_contact(self, first_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{first_name}' deleted successfully!\n")
                return
        print(f"\nContact with name '{first_name}' not found.\n")

    # Optional: Add multiple contacts at once
    def add_multiple_contacts(self, contacts):
        for contact in contacts:
            self.add_contact(contact)

    #  UC11: Sort contacts alphabetically by First Name + Last Name (no __str__)
    def sort_contacts_by_name(self):
        if not self.contacts:
            print("No contacts to sort.")
            return

        # Sort contacts by first and then last name (both in lowercase)
        sorted_contacts = sorted(self.contacts, key=lambda c: (c.first_name.lower(), c.last_name.lower()))

        print("\nSorted Contacts by Name:")
        for contact in sorted_contacts:
            print(contact.display())
            print("-" * 30)

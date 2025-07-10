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
                return contact.display()
        print("Contact not found.")

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
                return contact.display()
        print("Contact not found.")
    
    def delete_contact(self, first_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{first_name}' deleted successfully!\n")
                return
        print(f"\nContact with name '{first_name}' not found.\n")    
    
    
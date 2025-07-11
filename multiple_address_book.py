from address_book import AddressBook

class MultipleAddressBookSystem:
    def __init__(self):
        self.books = {}

    # UC6: Create a new Address Book
    def create_address_book(self, book_name):
        if book_name in self.books:
            print(f"\nAddress Book '{book_name}' already exists.\n")
        else:
            self.books[book_name] = AddressBook()
            print(f"\nAddress Book '{book_name}' created successfully.\n")

    # UC6: Get an existing Address Book by name
    def get_address_book(self, book_name):
        return self.books.get(book_name)

    # UC6: Display all Address Books and their Contacts
    def display_all_books(self):
        if not self.books:
            print("No Address Books available.")
        else:
            print("\nAvailable Address Books and Contacts:")
            for name, book in self.books.items():
                print(f"\n===== {name.upper()} Address Book =====")
                book.display_all_contacts()

    # UC8: Search persons by city or state
    def search_person_by_city_or_state(self, location_type, value):
        value = value.strip().lower()
        found = False
        print(f"\nSearch results for {location_type.title()} '{value.title()}':")
        for name, book in self.books.items():
            for contact in book.contacts:
                city_match = contact.city.strip().lower() == value
                state_match = contact.state.strip().lower() == value
                if location_type == "city" and city_match:
                    print(f"\n[From {name} Address Book]")
                    print(contact.display())
                    found = True
                elif location_type == "state" and state_match:
                    print(f"\n[From {name} Address Book]")
                    print(contact.display())
                    found = True
        if not found:
            print("No contacts found.")

    # UC9: View grouped persons by city or state
    def view_persons_by_location(self, location_type):
        location_dict = {}
        for book in self.books.values():
            for contact in book.contacts:
                key = contact.city.lower() if location_type == "city" else contact.state.lower()
                if key not in location_dict:
                    location_dict[key] = []
                location_dict[key].append(contact)
        if not location_dict:
            print(f"No contacts found in any {location_type}.")
            return
        print(f"\nPeople grouped by {location_type.title()}:")
        for location, people in location_dict.items():
            print(f"\n{location_type.title()}: {location.title()}")
            for contact in people:
                print(contact.display())
                print("-" * 30)

    
    # UC10: Count persons and show phones by specific city or state
    def count_contacts_by_specific_location(self, location_type, location_value):
        location_value = location_value.strip().lower()
        phones = []
        for book in self.books.values():
            for contact in book.contacts:
                key = contact.city.lower() if location_type == "city" else contact.state.lower()
                if key == location_value:
                    phones.append(contact.phone)

        if not phones:
            print(f"\nNo contacts found for {location_type.title()} '{location_value.title()}'.")
            return

        print(f"\n{location_type.title()}: {location_value.title()} → {len(phones)} person(s)")
        for i, phone in enumerate(phones, 1):
            print(f"  {i}. Phone: {phone}")
            print("-" * 40)

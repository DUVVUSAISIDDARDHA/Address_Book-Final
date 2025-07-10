from address_book import AddressBook

class MultipleAddressBookSystem:
    def __init__(self):
        self.books = {}

    def create_address_book(self, book_name):
        if book_name in self.books:
            print(f"\nAddress Book '{book_name}' already exists.\n")
        else:
            self.books[book_name] = AddressBook()
            print(f"\nAddress Book '{book_name}' created successfully.\n")

    def get_address_book(self, book_name):
        return self.books.get(book_name)

    def display_all_books(self):
        if not self.books:
            print("No Address Books available.")
        else:
            print("\nAvailable Address Books and Contacts:")
            for name, book in self.books.items():
                print(f"\n===== {name.upper()} Address Book =====")
                book.display_all_contacts()

    def search_person_by_city_or_state(self, location_type, value):
        found = False
        print(f"\nSearch results for {location_type.title()} '{value}':")
        for name, book in self.books.items():
            for contact in book.contacts:
                if location_type == "city" and contact.city.lower() == value.lower():
                    print(f"\n[From {name} Address Book]")
                    print(contact.display())
                    found = True
                elif location_type == "state" and contact.state.lower() == value.lower():
                    print(f"\n[From {name} Address Book]")
                    print(contact.display())
                    found = True
        if not found:
            print("No contacts found.")

    
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

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

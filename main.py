from multiple_address_book import MultipleAddressBookSystem
from contact import Contact

system = MultipleAddressBookSystem()

# UC1 - Create Address Book
while True:
    book_name = input("\nEnter Address Book Name: ")
    system.create_address_book(book_name)
    book = system.get_address_book(book_name)

    # UC2 & UC5 - Add Contact / Add Multiple Contacts
    while True:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone: ")
        email = input("Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        book.add_contact(contact)  # UC7 - Duplicate check happens here

        cont = input("Add another contact to this address book? (y/n): ").lower()
        if cont != "y":
            break

    # UC3 - Edit Contact (optional, uncomment to use)
    # edit_name = input("Enter name to edit: ")
    # book.edit_contact(edit_name)

    # UC4 - Delete Contact (optional, uncomment to use)
    # delete_name = input("Enter name to delete: ")
    # book.delete_contact(delete_name)

    more_books = input("Do you want to add another address book? (y/n): ").lower()
    if more_books != "y":
        break

# UC6 - Display All Address Books and Contacts (optional, uncomment to use)
# system.display_all_books()

# UC8 - Search Person by City or State (optional, uncomment to use)
# search_type = input("\nSearch by 'city' or 'state'?: ").strip().lower()
# if search_type in ['city', 'state']:
#     search_value = input(f"Enter {search_type} name to search: ")
#     system.search_person_by_city_or_state(search_type, search_value)
# else:
#     print("Invalid search type.")

# UC9 - View Persons grouped by City or State (optional, uncomment to use)
location_type = input("\nView persons grouped by 'city' or 'state'?: ").strip().lower()
if location_type in ['city', 'state']:
    system.view_persons_by_location(location_type)
else:
    print("Invalid location type.")

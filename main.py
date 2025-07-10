from multiple_address_book import MultipleAddressBookSystem
from contact import Contact

system = MultipleAddressBookSystem()

while True:
    book_name = input("\nEnter Address Book Name: ")
    system.create_address_book(book_name)
    book = system.get_address_book(book_name)

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
        book.add_contact(contact)

        cont = input("Add another contact to this address book? (y/n): ").lower()
        if cont != "y":
            break

    
    # edit_name = input("Enter first name of the contact to edit: ")
    # book.edit_contact(edit_name)

    
    # delete_name = input("Enter first name of the contact to delete: ")
    # book.delete_contact(delete_name)

    more_books = input("Do you want to add another address book? (y/n): ").lower()
    if more_books != "y":
        break

# UC 8 - Search Across Books by City or State
search_type = input("\nSearch by 'city' or 'state'?: ").lower()
search_value = input(f"Enter {search_type} name to search: ")
system.search_person_by_city_or_state(search_type, search_value)

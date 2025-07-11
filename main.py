from multiple_address_book import MultipleAddressBookSystem
from contact import Contact

# UC6: Initialize the system that can manage multiple address books
system = MultipleAddressBookSystem()

while True:
    # UC6: Add a new Address Book
    book_name = input("\nEnter Address Book Name: ")
    system.create_address_book(book_name)
    book = system.get_address_book(book_name)

    while True:
        # UC1: Take input from user
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone: ")
        email = input("Email: ")

        # UC2–UC7: Create and add contact (duplicate check is inside add_contact)
        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        book.add_contact(contact)

        # UC3: Option to add more contacts in same address book
        cont = input("Add another contact to this address book? (y/n): ").lower()
        if cont != "y":
            break

    # UC4: Edit contact (Optional)
    # edit_name = input("Enter name to edit: ")
    # book.edit_contact(edit_name)

    # UC5: Delete contact (Optional)
    # delete_name = input("Enter name to delete: ")
    # book.delete_contact(delete_name)

    # UC6: Ask if user wants to add another address book
    more_books = input("Do you want to add another address book? (y/n): ").lower()
    if more_books != "y":
        break

# UC8: Search person across address books by city/state
location_type = input("\nSearch by 'city' or 'state'?: ").lower()
location_value = input(f"Enter {location_type} name to search: ")
system.search_person_by_city_or_state(location_type, location_value)

# UC9: View grouped persons by city/state (Optional)
# system.view_persons_by_location(location_type)

# UC10: Count persons by city/state with phone numbers
# UC10: Count persons by city/state with phone numbers
system.count_contacts_by_specific_location(location_type, location_value)


#  Optional UC10 (Extra): Count for specific city/state only
# system.count_contacts_by_specific_location(location_type, location_value)

# UC6: Final display of all address books (Optional)
# system.display_all_books()

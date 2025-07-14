from multiple_address_book import MultipleAddressBookSystem
from contact import Contact

# UC6 - Initialize system to handle multiple address books
system = MultipleAddressBookSystem()

# UC6 - Create and manage multiple address books
while True:
    book_name = input("\nEnter Address Book Name: ")
    system.create_address_book(book_name)
    book = system.get_address_book(book_name)

    # UC5 - Add multiple contacts to address book
    while True:
        # UC1 - Create contact
        print("\nEnter Contact Details:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone: ")
        email = input("Email: ")

        # UC2 - Add contact to address book
        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)

        # UC7 - Prevent duplicate entry
        book.add_contact(contact)

        more_contacts = input("Add another contact to this address book? (y/n): ").lower()
        if more_contacts != "y":
            break

    # UC3 - Edit contact (Optional)
    # edit_name = input("Enter First Name to Edit Contact (or press Enter to skip): ")
    # if edit_name:
    #     book.edit_contact(edit_name)

    # UC4 - Delete contact (Optional)
    # delete_name = input("Enter First Name to Delete Contact (or press Enter to skip): ")
    # if delete_name:
    #     book.delete_contact(delete_name)

    more_books = input("Do you want to add another address book? (y/n): ").lower()
    if more_books != "y":
        break

# UC8 - Search person by city or state across all address books
search_type = input("\nSearch by 'city' or 'state'?: ").strip().lower()
if search_type in ['city', 'state']:
    search_value = input(f"Enter {search_type} name to search: ")
    system.search_person_by_city_or_state(search_type, search_value)

    # UC10 - Count persons by city/state
    system.count_contacts_by_specific_location(search_type, search_value)

    # UC9 - (Optional) View grouped persons by city/state
    # system.view_persons_by_location(search_type)
else:
    print("Invalid search type.")

# UC11 - Sort contacts alphabetically in selected address book
sort_book_name = input("\nEnter Address Book name to sort contacts alphabetically: ")
book_to_sort = system.get_address_book(sort_book_name)
if book_to_sort:
    book_to_sort.sort_contacts_by_name()
else:
    print(f"Address Book '{sort_book_name}' not found.")

#  UC12 - Sort contacts by City, State, or Zip Code
sort_by = input("\nDo you want to sort contacts by 'city', 'state' or 'zip_code'? (or press Enter to skip): ").strip().lower()
if sort_by in ['city', 'state', 'zip_code']:
    sort_book = system.get_address_book(sort_book_name)
    if sort_book:
        sort_book.sort_contacts_by(sort_by)
    else:
        print(f"Address Book '{sort_book_name}' not found.")
# else: Skipped if input is blank or invalid

# Optional: Final display of all address books and contacts
# system.display_all_books()

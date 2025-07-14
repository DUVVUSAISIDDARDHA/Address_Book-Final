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

        # UC2 - Add contact to address book (with duplicate check)
        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        book.add_contact(contact)

        more_contacts = input("Add another contact to this address book? (y/n): ").lower()
        if more_contacts != "y":
            break

    more_books = input("Do you want to add another address book? (y/n): ").lower()
    if more_books != "y":
        break

# UC3 - Edit a contact
edit_choice = input("\nDo you want to edit a contact? (y/n): ").strip().lower()
if edit_choice == "y":
    book_name = input("Enter Address Book Name: ")
    book = system.get_address_book(book_name)
    if book:
        name_to_edit = input("Enter First Name of contact to edit: ")
        book.edit_contact(name_to_edit)
    else:
        print("Address book not found.")

# UC4 - Delete a contact
delete_choice = input("\nDo you want to delete a contact? (y/n): ").strip().lower()
if delete_choice == "y":
    book_name = input("Enter Address Book Name: ")
    book = system.get_address_book(book_name)
    if book:
        name_to_delete = input("Enter First Name of contact to delete: ")
        book.delete_contact(name_to_delete)
    else:
        print("Address book not found.")

# UC8 - Search person by city or state across all address books
search_type = input("\nUC8 - Search by 'city' or 'state'?: ").strip().lower()
if search_type in ['city', 'state']:
    search_value = input(f"Enter {search_type} name to search: ")
    system.search_person_by_city_or_state(search_type, search_value)

    # UC10 - Count persons by city/state
    system.count_contacts_by_specific_location(search_type, search_value)

    # UC9 - Optional: View grouped persons by city/state
    # system.view_persons_by_location(search_type)
else:
    print("Invalid search type. Skipping search.")

# UC11 - Sort contacts alphabetically in selected address book
sort_book_name = input("\nUC11 - Enter Address Book name to sort contacts by name: ")
book_to_sort = system.get_address_book(sort_book_name)
if book_to_sort:
    book_to_sort.sort_contacts_by_name()

    # UC12 - Sort contacts by city/state/zip
    sort_by = input("UC12 - Sort by 'city', 'state' or 'zip_code' (or press Enter to skip): ").strip().lower()
    if sort_by in ['city', 'state', 'zip_code']:
        book_to_sort.sort_contacts_by(sort_by)
else:
    print(f"Address Book '{sort_book_name}' not found.")

# UC13 - Save/Load from text file
file_action = input("\nUC13 - Do you want to 'save' or 'load' contacts from text file? (or press Enter to skip): ").strip().lower()
if file_action in ['save', 'load']:
    file_name = input("Enter filename (e.g., contacts.txt): ")
    if book_to_sort:
        book_to_sort.save_or_load_file(file_name, file_action)
    else:
        print("No valid address book found for file operation.")

# UC14 - Save/Load from CSV file
csv_action = input("\nUC14 - Do you want to 'save' or 'load' contacts from CSV file? (or press Enter to skip): ").strip().lower()
if csv_action in ['save', 'load']:
    csv_file = input("Enter CSV filename (e.g., contacts.csv): ")
    if book_to_sort:
        book_to_sort.save_or_load_csv(csv_file, csv_action)
    else:
        print("No valid address book found for CSV operation.")

# Optional: Final display of all address books (UC15 if required)
# system.display_all_books()

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

    # Optional: You can use this if you're adding contacts from a list
    # book.add_multiple_contacts([...])

    # Optional: Uncomment to allow editing a contact
    # edit_name = input("Enter name to edit: ")
    # book.edit_contact(edit_name)

    # Optional: Uncomment to allow deleting a contact
    # delete_name = input("Enter name to delete: ")
    # book.delete_contact(delete_name)

    more_books = input("Do you want to add another address book? (y/n): ").lower()
    if more_books != "y":
        break

system.display_all_books()

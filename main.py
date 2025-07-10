from contact import Contact
from address_book import AddressBook

address_book = AddressBook()

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
    address_book.add_contact(contact)  

    cont = input("Add another contact? (y/n): ").lower()
    if cont != "y":
        break


# edit_name = input("Enter name to edit: ")
# address_book.edit_contact(edit_name)


# delete_name = input("Enter name to delete: ")
# address_book.delete_contact(delete_name)


# address_book.display_all_contacts()

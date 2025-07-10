from contact import Contact
from address_book import AddressBook



contact1 = Contact(
    first_name="Sai",
    last_name="Siddu",
    address="123 MG Road",
    city="Hyderabad",
    state="Telangana",
    zip_code="500001",
    phone="9876543210",
    email="sai@example.com"
)


contact2 = Contact(
    first_name="Anu",
    last_name="Kumar",
    address="456 Banjara Hills",
    city="Hyderabad",
    state="Telangana",
    zip_code="500034",
    phone="9123456780",
    email="anu@example.com"
)

address_book = AddressBook()
address_book.add_contact(contact1)
address_book.add_contact(contact2)

address_book.edit_contact("Anu")
address_book.display_all_contacts() 
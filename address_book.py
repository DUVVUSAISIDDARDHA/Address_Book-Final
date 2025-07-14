import os
import csv
import json
from contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        for existing in self.contacts:
            if (existing.first_name.lower() == contact.first_name.lower() and
                existing.last_name.lower() == contact.last_name.lower()):
                print("\nDuplicate contact! Person already exists in this address book.\n")
                return
        self.contacts.append(contact)
        print("\nContact added successfully!\n")
        print("Saved Contact:")
        print("----------------------------")
        print(contact.display())
        print("----------------------------")

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print("----------------------------")
                print(contact.display())
                print("----------------------------")

    def edit_contact(self, first_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                print("Contact found. Enter new details:")
                contact.last_name = input("New Last Name: ") or contact.last_name
                contact.address = input("New Address: ") or contact.address
                contact.city = input("New City: ") or contact.city
                contact.state = input("New State: ") or contact.state
                contact.zip_code = input("New Zip Code: ") or contact.zip_code
                contact.phone = input("New Phone: ") or contact.phone
                contact.email = input("New Email: ") or contact.email
                print("\nContact updated successfully:")
                print("----------------------------")
                print(contact.display())
                print("----------------------------")
                return
        print("Contact not found.")

    def delete_contact(self, first_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{first_name}' deleted successfully!\n")
                return
        print(f"\nContact with name '{first_name}' not found.\n")

    def sort_contacts_by_name(self):
        if not self.contacts:
            print("No contacts to sort.")
            return
        sorted_contacts = sorted(self.contacts, key=lambda c: (c.first_name.lower(), c.last_name.lower()))
        print("\nSorted Contacts by Name:")
        for contact in sorted_contacts:
            print(contact.display())
            print("-" * 30)

    def sort_contacts_by(self, field):
        if not self.contacts:
            print("No contacts to sort.")
            return
        valid_fields = ['city', 'state', 'zip_code']
        if field not in valid_fields:
            print(f"Invalid sort field. Choose from: {', '.join(valid_fields)}")
            return
        sorted_contacts = sorted(
            self.contacts,
            key=lambda c: getattr(c, field).lower() if isinstance(getattr(c, field), str) else getattr(c, field)
        )
        print(f"\nSorted Contacts by {field.capitalize()}:")
        for contact in sorted_contacts:
            print(contact.display())
            print("-" * 30)

    def save_or_load_file(self, filename, mode):
        if mode == "save":
            with open(filename, "w") as file:
                for contact in self.contacts:
                    file.write(f"{contact.first_name},{contact.last_name},{contact.address},{contact.city},"
                               f"{contact.state},{contact.zip_code},{contact.phone},{contact.email}\n")
            print(f"\nAll contacts saved to file '{filename}' successfully.")
        elif mode == "load":
            if not os.path.exists(filename):
                print(f"\nFile '{filename}' does not exist.")
                return
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 8:
                        contact = Contact(*data)
                        self.add_contact(contact)
            print(f"\nContacts loaded from file '{filename}' successfully.")
        else:
            print("Invalid mode! Use 'save' or 'load'.")

    def save_or_load_csv(self, filename, mode):
        if mode == "save":
            with open(filename, mode='w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['First Name', 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'Phone', 'Email'])
                for contact in self.contacts:
                    writer.writerow([
                        contact.first_name, contact.last_name, contact.address,
                        contact.city, contact.state, contact.zip_code,
                        contact.phone, contact.email
                    ])
            print(f"\nAll contacts saved to CSV file '{filename}' successfully.")
        elif mode == "load":
            if not os.path.exists(filename):
                print(f"\nCSV file '{filename}' does not exist.")
                return
            with open(filename, mode='r') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)
                for row in reader:
                    if len(row) == 8:
                        contact = Contact(*row)
                        self.add_contact(contact)
            print(f"\nContacts loaded from CSV file '{filename}' successfully.")
        else:
            print("Invalid mode! Use 'save' or 'load'.")

    def save_or_load_json(self, filename, mode):
        if mode == "save":
            data = []
            for contact in self.contacts:
                data.append({
                    "first_name": contact.first_name,
                    "last_name": contact.last_name,
                    "address": contact.address,
                    "city": contact.city,
                    "state": contact.state,
                    "zip_code": contact.zip_code,
                    "phone": contact.phone,
                    "email": contact.email
                })
            with open(filename, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print(f"\nAll contacts saved to JSON file '{filename}' successfully.")

        elif mode == "load":
            try:
                with open(filename, "r") as json_file:
                    data = json.load(json_file)
                    for entry in data:
                        if all(k in entry for k in ["first_name", "last_name", "address", "city", "state", "zip_code", "phone", "email"]):
                            contact = Contact(
                                entry["first_name"], entry["last_name"], entry["address"],
                                entry["city"], entry["state"], entry["zip_code"],
                                entry["phone"], entry["email"]
                            )
                            self.add_contact(contact)
                print(f"\nContacts loaded from JSON file '{filename}' successfully.")
            except FileNotFoundError:
                print(f"\nJSON file '{filename}' does not exist.")
        else:
            print("Invalid mode! Use 'save' or 'load'.")

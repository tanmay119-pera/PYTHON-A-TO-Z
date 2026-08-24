'''                              PROJECT 7 - Object Oriented Contact Book
           Concepts used: Classes, Objects, Encapsulation, __init__, methods, file handling (JSON).                           '''

''' what is a json file?

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write,
and easy for machines to parse and generate. In Python, we can use the built-in json module to work with JSON data. In this 
project, we will use a JSON file to store our contacts permanently, so that even after the program is closed, the contacts remain 
saved. Each contact will be stored as a dictionary in a list, and the entire list will be saved to a JSON file. When the program starts,
 it will load the contacts from this file back into memory, allowing the user to view, search, update, or delete them.
 
 for example, a contact might be stored in the JSON file like this:
[
    {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "john.doe@example.com"
    }
]

for multiple contacts, the JSON file would look like this:
[
    {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "john.doe@example.com"
    },
    {
        "name": "Jane Smith",
        "phone": "098-765-4321",
        "email": "jane.smith@example.com"
    }
]
 for beginners, think of a JSON file as a simple text file that stores data in a structured way, making it easy to read and write. In this project, we will use it to save our contacts so that they are not lost when the program is closed.
 and they take help of any AI for the getting help for how to use json file in python, they can refer to the official documentation: https://docs.python.org/3/library/json.html however, the code below is self-explanatory and should be easy to understand for beginners.'''

import json   # used to save/load contacts in a .json file
import os     # used to check if the save file already exists

FILE_NAME = "contacts.json"  # file where all contacts will be stored permanently


class Contact:
    """
    This class represents ONE contact.
    Think of it as a blueprint for a single person's details.
    """

    def __init__(self, name, phone, email):
        # self.name, self.phone, self.email are called attributes.
        # They store data that belongs to this specific object.
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        # Converts the Contact object into a dictionary.
        # This is needed because JSON files can only store
        # dictionaries/lists, not Python objects directly.
        return {"name": self.name, "phone": self.phone, "email": self.email}

    def __str__(self):
        # This special method controls what gets printed
        # when we do print(contact_object).
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"


class ContactBook:
    """
    This class manages MANY Contact objects.
    It stores them in a list and provides methods to
    add, view, search, update, and delete contacts.
    """

    def __init__(self):
        # self.contacts is a list that will hold Contact objects.
        self.contacts = []
        # As soon as the ContactBook is created, load any
        # previously saved contacts from the file.
        self.load_contacts()

    def add_contact(self, name, phone, email):
        # Step 1: Create a new Contact object using the Contact class.
        new_contact = Contact(name, phone, email)
        # Step 2: Add that object to our contacts list.
        self.contacts.append(new_contact)
        # Step 3: Save the updated list to the file so it's not lost.
        self.save_contacts()
        print("Contact added successfully.\n")

    def view_contacts(self):
        # If the list is empty, there is nothing to show.
        if not self.contacts:
            print("No contacts found.\n")
            return

        print("\n--- CONTACT LIST ---")
        # enumerate() gives us both the index (i) and the contact object.
        # start=1 makes numbering begin from 1 instead of 0.
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")  # this uses __str__ from Contact class
        print()

    def search_contact(self, name):
        # This creates a new list containing only contacts
        # whose name matches (case-insensitive) the search term.
        found = [c for c in self.contacts if c.name.lower() == name.lower()]

        if found:
            print("\n--- SEARCH RESULT ---")
            for c in found:
                print(c)
            print()
        else:
            print("Contact not found.\n")

    def update_contact(self, name, new_phone, new_email):
        # Loop through every contact to find a matching name.
        for c in self.contacts:
            if c.name.lower() == name.lower():
                # Update the attributes of that specific object.
                c.phone = new_phone
                c.email = new_email
                self.save_contacts()
                print("Contact updated successfully.\n")
                return  # stop searching once found and updated
        print("Contact not found.\n")

    def delete_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)  # remove object from the list
                self.save_contacts()
                print("Contact deleted successfully.\n")
                return
        print("Contact not found.\n")

    def save_contacts(self):
        # Convert every Contact object in the list into a dictionary,
        # because json.dump() cannot save custom objects directly.
        data = [c.to_dict() for c in self.contacts]
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)  # indent=4 makes the file readable

    def load_contacts(self):
        # Only try to load if the file actually exists.
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                data = json.load(f)
                # Convert each dictionary back into a Contact object.
                self.contacts = [Contact(d["name"], d["phone"], d["email"]) for d in data]


def main():
    # Create one ContactBook object. This is the "manager"
    # we will keep using throughout the program.
    book = ContactBook()

    while True:  # keep showing the menu until the user chooses to exit
        print("===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            book.search_contact(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            book.update_contact(name, phone, email)

        elif choice == "5":
            name = input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == "6":
            print("Goodbye!")
            break  # exits the while loop, ending the program

        else:
            print("Invalid choice. Try again.\n")


# This ensures main() only runs when this file is executed directly,
# not when it's imported into another file.
if __name__ == "__main__":
    main()
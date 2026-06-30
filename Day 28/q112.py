contacts = {}
choice = 0

while choice != 4:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Contact Name: ")
        if name in contacts:
            print("Contact name already exists.")
        else:
            phone = input("Enter Phone Number: ")
            email = input("Enter Email Address: ")
            contacts[name] = {"phone": phone, "email": email}
            print(f"Contact '{name}' saved.")
    elif choice == 2:
        if not contacts:
            print("No contacts saved.")
        else:
            print("\nSaved Contact List:")
            for name, details in contacts.items():
                print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")
    elif choice == 3:
        name = input("Enter Contact Name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Contact not found.")
    elif choice == 4:
        print("Exiting Contact System.")
    else:
        print("Invalid choice.")
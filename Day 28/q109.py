books = {}
choice = 0

while choice != 4:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        isbn = input("Enter ISBN: ")
        if isbn in books:
            print("Book with this ISBN already exists.")
        else:
            title = input("Enter Book Title: ")
            books[isbn] = {"title": title, "status": "Available"}
            print(f"'{title}' added successfully.")
    elif choice == 2:
        isbn = input("Enter ISBN to issue: ")
        if isbn in books:
            if books[isbn]["status"] == "Available":
                books[isbn]["status"] = "Issued"
                print(f"'{books[isbn]['title']}' has been issued.")
            else:
                print("Book is already issued.")
        else:
            print("Book not found.")
    elif choice == 3:
        isbn = input("Enter ISBN to return: ")
        if isbn in books:
            if books[isbn]["status"] == "Issued":
                books[isbn]["status"] = "Available"
                print(f"'{books[isbn]['title']}' returned successfully.")
            else:
                print("Book was not issued.")
        else:
            print("Book not found.")
    elif choice == 4:
        print("Exiting Library System.")
    else:
        print("Invalid choice.")
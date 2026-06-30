titles = []
authors = []
issued_status = []
choice = 0

while choice != 4:
    print("\n--- Mini Library Menu ---")
    print("1. Add New Book")
    print("2. Issue a Book")
    print("3. Return a Book")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        titles.append(title)
        authors.append(author)
        issued_status.append(False)
        print(f"Book '{title}' added.")
    elif choice == 2:
        search_title = input("Enter Book Title to issue: ")
        found_idx = -1
        for i in range(len(titles)):
            if titles[i] == search_title:
                found_idx = i
                break
        if found_idx != -1:
            if not issued_status[found_idx]:
                issued_status[found_idx] = True
                print("Book successfully issued.")
            else:
                print("Book is already issued to someone else.")
        else:
            print("Book not available in the library library database.")
    elif choice == 3:
        search_title = input("Enter Book Title to return: ")
        found_idx = -1
        for i in range(len(titles)):
            if titles[i] == search_title:
                found_idx = i
                break
        if found_idx != -1:
            if issued_status[found_idx]:
                issued_status[found_idx] = False
                print("Book successfully returned.")
            else:
                print("This book is not currently marked as issued.")
        else:
            print("Book record not found.")
    elif choice == 4:
        print("Exiting Library System.")
    else:
        print("Invalid choice choice.")
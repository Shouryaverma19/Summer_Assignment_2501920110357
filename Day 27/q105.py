students = {}
choice = 0

while choice != 4:
    print("\n--- Student Record Menu ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll No")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        roll_no = input("Enter Roll Number: ")
        if roll_no in students:
            print("Roll number already exists.")
        else:
            name = input("Enter Student Name: ")
            course = input("Enter Course: ")
            students[roll_no] = {"name": name, "course": course}
            print("Student added successfully.")
    elif choice == 2:
        if not students:
            print("No records found.")
        else:
            for roll_no, details in students.items():
                print(f"Roll No: {roll_no} | Name: {details['name']} | Course: {details['course']}")
    elif choice == 3:
        roll_no = input("Enter Roll Number to search: ")
        if roll_no in students:
            print(f"Found Details -> Name: {students[roll_no]['name']}, Course: {students[roll_no]['course']}")
        else:
            print("Student not found.")
    elif choice == 4:
        print("Exiting System.")
    else:
        print("Invalid choice.")
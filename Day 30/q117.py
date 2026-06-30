names = []
rolls = []
courses = []
choice = 0

while choice != 4:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Enter Roll No: ")
        if roll in rolls:
            print("Roll number already exists.")
        else:
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            names.append(name)
            rolls.append(roll)
            courses.append(course)
            print("Student added successfully.")
    elif choice == 2:
        num_students = len(rolls)
        if num_students == 0:
            print("No student records available.")
        else:
            for i in range(num_students):
                print(f"Roll No: {rolls[i]} | Name: {names[i]} | Course: {courses[i]}")
    elif choice == 3:
        search_roll = input("Enter Roll No to search: ")
        found_idx = -1
        for i in range(len(rolls)):
            if rolls[i] == search_roll:
                found_idx = i
                break
        if found_idx != -1:
            print(f"Student Found -> Name: {names[found_idx]}, Course: {courses[found_idx]}")
        else:
            print("Student record not found.")
    elif choice == 4:
        print("Exiting Student System.")
    else:
        print("Invalid choice choice selected.")
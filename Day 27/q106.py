employees = {}
choice = 0

while choice != 4:
    print("\n--- Employee Management Menu ---")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Department")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print("Employee ID already exists.")
        else:
            name = input("Enter Employee Name: ")
            dept = input("Enter Department: ")
            employees[emp_id] = {"name": name, "dept": dept}
            print("Employee record added.")
    elif choice == 2:
        if not employees:
            print("No employee records found.")
        else:
            for emp_id, info in employees.items():
                print(f"ID: {emp_id} | Name: {info['name']} | Department: {info['dept']}")
    elif choice == 3:
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in employees:
            new_dept = input("Enter New Department: ")
            employees[emp_id]["dept"] = new_dept
            print("Department updated successfully.")
        else:
            print("Employee not found.")
    elif choice == 4:
        print("Exiting System.")
    else:
        print("Invalid choice.")
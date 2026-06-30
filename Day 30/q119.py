emp_ids = []
emp_names = []
salaries = []
choice = 0

while choice != 4:
    print("\n--- Mini Employee Dashboard ---")
    print("1. Add Employee Record")
    print("2. Display All Employees")
    print("3. Display Highest Paid Employee")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        eid = input("Enter Employee ID: ")
        if eid in emp_ids:
            print("Employee ID already exists.")
        else:
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Base Salary: "))
            emp_ids.append(eid)
            emp_names.append(name)
            salaries.append(salary)
            print("Employee record saved successfully.")
    elif choice == 2:
        total = len(emp_ids)
        if total == 0:
            print("No employee records found.")
        else:
            for i in range(total):
                print(f"ID: {emp_ids[i]} | Name: {emp_names[i]} | Salary: Rs.{salaries[i]:.2f}")
    elif choice == 3:
        total = len(emp_ids)
        if total == 0:
            print("No records to calculate.")
        else:
            max_idx = 0
            for i in range(1, total):
                if salaries[i] > salaries[max_idx]:
                    max_idx = i
            print(f"Highest Paid -> Name: {emp_names[max_idx]} | ID: {emp_ids[max_idx]} | Salary: Rs.{salaries[max_idx]:.2f}")
    elif choice == 4:
        print("Exiting Employee System.")
    else:
        print("Invalid option selected.")
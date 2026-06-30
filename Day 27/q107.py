salaries = {}
choice = 0

while choice != 4:
    print("\n--- Salary Management Menu ---")
    print("1. Add/Update Salary")
    print("2. Display Salary Sheet")
    print("3. Calculate Total Expenditure")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Base Salary Amount: "))
        salaries[name] = salary
        print(f"Salary data saved for {name}.")
    elif choice == 2:
        if not salaries:
            print("No salary records found.")
        else:
            for name, amount in salaries.items():
                print(f"Employee: {name} | Salary: Rs. {amount}")
    elif choice == 3:
        total_payroll = 0.0
        for amount in salaries.values():
            total_payroll += amount
        print(f"Total Company Salary Expenditure: Rs. {total_payroll}")
    elif choice == 4:
        print("Exiting System.")
    else:
        print("Invalid choice.")
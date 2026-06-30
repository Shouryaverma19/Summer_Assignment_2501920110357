choice = 0

while choice != 5:
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice in (1, 2, 3, 4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            print(f"Result: {num1 + num2}")
        elif choice == 2:
            print(f"Result: {num1 - num2}")
        elif choice == 3:
            print(f"Result: {num1 * num2}")
        elif choice == 4:
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    elif choice == 5:
        print("Exiting Calculator.")
    else:
        print("Invalid choice.")
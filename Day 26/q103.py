balance = 5000.0
choice = 0

while choice != 4:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f"Your current balance is: Rs. {balance}")
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Rs. {amount} deposited successfully.")
        else:
            print("Invalid amount.")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            print("Invalid amount.")
    elif choice == 4:
        print("Thank you for using the ATM.")
    else:
        print("Invalid choice. Please select a valid option.")
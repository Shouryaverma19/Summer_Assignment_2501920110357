accounts = {}
choice = 0

while choice != 4:
    print("\n--- Bank Account System ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc_no = input("Enter unique Account Number: ")
        if acc_no in accounts:
            print("Account number already exists.")
        else:
            holder = input("Enter Account Holder Name: ")
            initial_balance = float(input("Enter initial deposit amount: "))
            accounts[acc_no] = {"name": holder, "balance": initial_balance}
            print(f"Account successfully created for {holder}.")
    elif choice == 2:
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                accounts[acc_no]["balance"] += amount
                print(f"Deposit successful. New Balance: Rs. {accounts[acc_no]['balance']}")
            else:
                print("Invalid deposit amount.")
        else:
            print("Account not found.")
    elif choice == 3:
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter withdrawal amount: "))
            if 0 < amount <= accounts[acc_no]["balance"]:
                accounts[acc_no]["balance"] -= amount
                print(f"Withdrawal successful. Remaining Balance: Rs. {accounts[acc_no]['balance']}")
            elif amount > accounts[acc_no]["balance"]:
                print("Insufficient balance.")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("Account not found.")
    elif choice == 4:
        print("Exiting Banking System.")
    else:
        print("Invalid choice.")
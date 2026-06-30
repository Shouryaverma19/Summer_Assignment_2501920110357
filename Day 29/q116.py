inventory = {}
choice = 0

while choice != 5:
    print("\n--- Inventory Management System ---")
    print("1. Add/Update Item")
    print("2. View Inventory Status")
    print("3. Check Item Stock level")
    print("4. Delete Item Record")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_id = input("Enter unique Item ID: ")
        item_name = input("Enter Item Name: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price per unit: "))
        inventory[item_id] = {"name": item_name, "qty": qty, "price": price}
        print(f"Record for '{item_name}' saved.")
    elif choice == 2:
        if not inventory:
            print("Inventory is completely empty.")
        else:
            print("\nCurrent Inventory Stock:")
            for item_id, details in inventory.items():
                print(f"ID: {item_id} | Name: {details['name']:<15} | Qty: {details['qty']:<5} | Price: Rs.{details['price']:.2f}")
    elif choice == 3:
        item_id = input("Enter Item ID to check: ")
        if item_id in inventory:
            print(f"Item: {inventory[item_id]['name']} | Available Stock Level: {inventory[item_id]['qty']} units.")
        else:
            print("Item ID not recognized.")
    elif choice == 4:
        item_id = input("Enter Item ID to delete: ")
        if item_id in inventory:
            deleted_name = inventory[item_id]['name']
            del inventory[item_id]
            print(f"Product '{deleted_name}' removed from database successfully.")
        else:
            print("Item ID not found.")
    elif choice == 5:
        print("Exiting Inventory Dashboard System.")
    else:
        print("Invalid choice choice selected.")
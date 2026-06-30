def add_product(ids, names, stocks):
    pid = input("Enter unique Product ID: ")
    if pid in ids:
        print("Product ID already exists.")
        return
    name = input("Enter Product Name: ")
    stock = int(input("Enter Initial Stock Quantity: "))
    ids.append(pid)
    names.append(name)
    stocks.append(stock)
    print("Product catalog updated successfully.")

def display_inventory(ids, names, stocks):
    total = len(ids)
    if total == 0:
        print("Inventory is currently empty.")
        return
    print("\n--- Current Inventory Status ---")
    for i in range(total):
        print(f"Product ID: {ids[i]} | Name: {names[i]:<15} | Stock Level: {stocks[i]} units")

def update_stock(ids, stocks):
    pid = input("Enter Product ID to update: ")
    found_idx = -1
    for i in range(len(ids)):
        if ids[i] == pid:
            found_idx = i
            break
    if found_idx != -1:
        adjustment = int(input("Enter quantity adjustment (positive for add, negative for remove): "))
        if stocks[found_idx] + adjustment < 0:
            print("Operation failed: Cannot reduce stock levels below 0 units.")
        else:
            stocks[found_idx] += adjustment
            print(f"Stock quantity adjusted successfully. New total: {stocks[found_idx]}")
    else:
        print("Product ID not found.")

def main_dashboard():
    p_ids = []
    p_names = []
    p_stocks = []
    choice = 0
    
    while choice != 4:
        print("\n==================================")
        print("   INVENTORY MANAGEMENT PROJECT   ")
        print("==================================")
        print("1. Register New Product Row")
        print("2. Display Product Stock Sheets")
        print("3. Modify Existing Inventory Quantities")
        print("4. Terminate Project Application")
        choice = int(input("Select system operation: "))
        
        if choice == 1:
            add_product(p_ids, p_names, p_stocks)
        elif choice == 2:
            display_inventory(p_ids, p_names, p_stocks)
        elif choice == 3:
            update_stock(p_ids, p_stocks)
        elif choice == 4:
            print("Project terminated successfully. Congratulations on completing Day 30!")
        else:
            print("Invalid structural system choice code.")

main_dashboard()
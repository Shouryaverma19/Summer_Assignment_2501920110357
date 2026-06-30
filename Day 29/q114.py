size = int(input("Enter the initial size of the array: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(size)]
choice = 0

while choice != 5:
    print("\n--- Array Operations Menu ---")
    print("1. Traverse/Display Array")
    print("2. Insert Element at End")
    print("3. Delete Element by Value")
    print("4. Search Element")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Array:", arr)
    elif choice == 2:
        val = int(input("Enter value to insert: "))
        arr.append(val)
        print(f"{val} inserted successfully.")
    elif choice == 3:
        val = int(input("Enter value to delete: "))
        if val in arr:
            arr.remove(val)
            print(f"First occurrence of {val} deleted.")
        else:
            print("Value not found in array.")
    elif choice == 4:
        val = int(input("Enter target value to search: "))
        found_idx = -1
        for i in range(len(arr)):
            if arr[i] == val:
                found_idx = i
                break
        if found_idx != -1:
            print(f"Element found at index: {found_idx}")
        else:
            print("Element not found in array.")
    elif choice == 5:
        print("Exiting Array System.")
    else:
        print("Invalid choice.")
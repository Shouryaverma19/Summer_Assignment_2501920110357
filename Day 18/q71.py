n = int(input("Enter size of array: "))
print("Note: For Binary Search to work, enter elements in SORTED ascending order!")
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

target = int(input("Enter element to search for: "))

low = 0
high = n - 1
found_idx = -1

while low <= high:
    mid = (low + high) // 2
    
    if arr[mid] == target:
        found_idx = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found_idx != -1:
    print(f"Element found at index: {found_idx}")
else:
    print("Element not found in the array.")
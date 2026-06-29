n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i}: ")))

target = int(input("Enter the element to search for: "))
found = False
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element found at index: {i}")
        found = True
        break

if not found:
    print("Element not found in the array.")
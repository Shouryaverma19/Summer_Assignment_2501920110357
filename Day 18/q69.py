n = int(input("Enter size of array: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array (Bubble Sort):", arr)
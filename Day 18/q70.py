n = int(input("Enter size of array: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Sorted array (Selection Sort):", arr)
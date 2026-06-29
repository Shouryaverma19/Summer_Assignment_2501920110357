n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i}: ")))

if n > 1:
    first = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = first

print("Array after left rotation:", arr)
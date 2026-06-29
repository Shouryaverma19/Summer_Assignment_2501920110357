n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))
largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"Largest element: {largest}")
print(f"Smallest element: {smallest}")
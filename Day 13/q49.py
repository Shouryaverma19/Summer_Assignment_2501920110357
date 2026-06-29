n = int(input("Enter the number of elements you want in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)
print("The array elements are:", arr)
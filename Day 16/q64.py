size = int(input("Enter size of array: "))
arr = []
for i in range(size):
    arr.append(int(input(f"Enter element {i}: ")))
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)

print("Array after removing duplicates:", unique_arr)
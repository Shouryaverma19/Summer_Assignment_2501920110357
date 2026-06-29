n1 = int(input("Enter size of first array: "))
arr1 = [int(input(f"Enter element {i+1}: ")) for i in range(n1)]
n2 = int(input("Enter size of second array: "))
arr2 = [int(input(f"Enter element {i+1}: ")) for i in range(n2)]
merged_arr = []

for num in arr1:
    merged_arr.append(num)
for num in arr2:
    merged_arr.append(num)

print("Merged array:", merged_arr)
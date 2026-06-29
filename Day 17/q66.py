n1 = int(input("Enter size of first array: "))
arr1 = [int(input(f"Enter element {i+1}: ")) for i in range(n1)]
n2 = int(input("Enter size of second array: "))
arr2 = [int(input(f"Enter element {i+1}: ")) for i in range(n2)]
union_arr = []

for num in arr1:
    if num not in union_arr:
        union_arr.append(num)

for num in arr2:
    if num not in union_arr:
        union_arr.append(num)

print("Union of arrays:", union_arr)
n1 = int(input("Enter size of first array: "))
arr1 = [int(input(f"Enter element {i+1}: ")) for i in range(n1)]

n2 = int(input("Enter size of second array: "))
arr2 = [int(input(f"Enter element {i+1}: ")) for i in range(n2)]

temp_arr2 = list(arr2)
common_elements = []

for num in arr1:
    if num in temp_arr2:
        common_elements.append(num)
        temp_arr2.remove(num)

print("Common elements found:", common_elements)
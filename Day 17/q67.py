n1 = int(input("Enter size of first array: "))
arr1 = [int(input(f"Enter element {i+1}: ")) for i in range(n1)]

n2 = int(input("Enter size of second array: "))
arr2 = [int(input(f"Enter element {i+1}: ")) for i in range(n2)]

intersection_arr = []

for num in arr1:
    if num in arr2 and num not in intersection_arr:
        intersection_arr.append(num)

print("Intersection of arrays:", intersection_arr)
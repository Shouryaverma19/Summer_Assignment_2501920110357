n1 = int(input("Enter size of first sorted array: "))
arr1 = [int(input(f"Enter element {i+1}: ")) for i in range(n1)]

n2 = int(input("Enter size of second sorted array: "))
arr2 = [int(input(f"Enter element {i+1}: ")) for i in range(n2)]

merged = []
i = 0
j = 0

while i < n1 and j < n2:
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < n1:
    merged.append(arr1[i])
    i += 1

while j < n2:
    merged.append(arr2[j])
    j += 1

print("Merged sorted array:", merged)
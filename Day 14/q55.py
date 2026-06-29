n = int(input("Enter size of array (must be >= 2): "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i}: ")))
largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("There is no unique second largest element.")
else:
    print(f"The second largest element is: {second_largest}")
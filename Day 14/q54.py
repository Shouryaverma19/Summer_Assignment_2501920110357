n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i}: ")))

target = int(input("Enter target element to find its frequency: "))
count = 0
for num in arr:
    if num == target:
        count += 1

print(f"Frequency of {target} is: {count}")
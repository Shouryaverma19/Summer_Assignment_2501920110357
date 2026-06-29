size = int(input("Enter size of array: "))
arr = []
for i in range(size):
    arr.append(int(input(f"Enter element {i}: ")))
frequencies = {}
for num in arr:
    if num in frequencies:
        frequencies[num] += 1
    else:
        frequencies[num] = 1

max_element = arr[0]
max_count = 0

for num, count in frequencies.items():
    if count > max_count:
        max_count = count
        max_element = num

print(f"Element with maximum frequency is {max_element} (appears {max_count} times).")
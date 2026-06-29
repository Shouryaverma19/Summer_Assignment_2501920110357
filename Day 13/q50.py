n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))
total_sum = 0
for num in arr:
    total_sum += num
average = total_sum / n
print(f"Sum of array: {total_sum}")
print(f"Average of array: {average}")
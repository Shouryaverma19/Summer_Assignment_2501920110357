n = int(input("Enter the value of n (total expected range size): "))
arr = []
print(f"Enter {n - 1} elements from 1 to {n} with one missing:")
for i in range(n - 1):
    arr.append(int(input(f"Element {i + 1}: ")))
expected_sum = (n * (n + 1)) // 2
actual_sum = sum(arr)

missing_number = expected_sum - actual_sum
print(f"The missing number is: {missing_number}")
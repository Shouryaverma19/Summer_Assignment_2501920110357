n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i}: ")))
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)
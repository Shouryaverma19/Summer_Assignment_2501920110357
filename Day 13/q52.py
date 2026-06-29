n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))
even_count = 0
odd_count = 0

for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of Even elements: {even_count}")
print(f"Number of Odd elements: {odd_count}")
x = int(input("Enter a number: "))
n = int(input("Enter a power: "))
result = 1
for i in range(n):
    result *= x
print(f"{x} raised to the power of {n} is: {result}")
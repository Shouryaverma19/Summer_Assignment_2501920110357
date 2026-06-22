n = int(input("Enter a number: "))
binary = " "
count = 0
while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2
    if remainder == 1:
     count += 1
print("Binary representation:", binary)
print("Number of bits:", count)
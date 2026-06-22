n = int(input("Enter a number: "))
decimal = 0
power = 0
while n > 0:
    remainder = n % 10
    decimal += remainder * (2 ** power)
    n = n // 10
    power += 1
print("Decimal representation:", decimal)
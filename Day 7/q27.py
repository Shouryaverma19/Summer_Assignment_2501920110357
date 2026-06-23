def sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum(n // 10)
n = int(input("Enter a number : "))
print("Sum of digits of", n, "is", sum(n))
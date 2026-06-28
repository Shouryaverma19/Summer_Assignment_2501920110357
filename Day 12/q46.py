def armstrong(n):
    original = n
    sum = 0
    digits = len(str(n))
    while n > 0:
        digit = n % 10
        sum += digit ** digits
        n //= 10
    return original == sum
n = int(input("Enter a number: "))
if armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
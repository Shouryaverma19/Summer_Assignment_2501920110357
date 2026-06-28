def is_pallindrone(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    return original == reverse

n = int(input("Enter a number: "))
if is_pallindrone(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
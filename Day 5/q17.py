n = int(input("Enter a number: "))
factor_sum = 0
for i in range (1, n):
    if n % i == 0:
        factor_sum += i
if factor_sum == n:
    print(f"{n} is a perfect number.")
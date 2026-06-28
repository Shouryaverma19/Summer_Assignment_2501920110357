def perfect_number(n):
    if n<1:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n
n = int(input("Enter a number: "))
if perfect_number(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
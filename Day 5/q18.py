n = int(input("Enter a number: "))
temp = n
sum = 0
while temp > 0:
     digit = temp % 10
     fact = 1
     for i in range(1, digit + 1):
        fact *= i
     sum += fact
     temp //= 10
if sum == n:
    print(f"{n} is an strong number.")
else:
    print(f"{n} is not an strong number.")
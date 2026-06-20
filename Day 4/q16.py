upper = int(input("Enter the upper number : "))
lower = int(input("Enter the lower number : "))
for num in range (lower, upper + 1):
    temp = num
    power = len(str(num))
    sum = 0
    while temp > 0:
     digit = temp % 10
     sum += digit ** power
     temp //= 10
    if sum == num:
        print(num)
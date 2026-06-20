num = int(input("Enter the number : "))
temp = num
power = len(str(num))
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
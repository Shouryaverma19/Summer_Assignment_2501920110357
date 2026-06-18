n = int(input('Enter the number : '))
count = 0
while n > 0:
    count += n % 10
    n = n // 10
print(count)
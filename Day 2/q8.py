n = int(input('Enter the number : '))
temp = n
count = 0
while n > 0:
    dig = n % 10
    count = (count*10) + dig
    n = n // 10
if temp == count:
    print("Palindronme")
else:
    print('Not')
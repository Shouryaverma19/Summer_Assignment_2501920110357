a = int(input('Enter the number : '))
b = int(input('Enter the number : '))
num1, num2 = a, b
while b>0:
    remainder = a % b
    a = b
    b = remainder
print('GCD of', num1, 'and', num2, 'is :', a)
a = int(input('Enter the number : '))
b = int(input('Enter the number : '))
num1, num2 = a, b
while b>0:
    remainder = a % b
    a = b
    b = remainder
lcm = (num1 * num2) // a
print('LCM of', num1, 'and', num2, 'is :', lcm)
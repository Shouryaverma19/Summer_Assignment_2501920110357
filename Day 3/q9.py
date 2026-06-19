n = int(input('Enter the number : '))
if n <= 1:
    print('No prime number')
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print('Prime number')
    else:
        print('No prime number')
n = int(input("Enter a number: "))
original = n
i = 2
while n>1 :
    if n%i == 0 :
        print(i)
        n //= i
    else :
        i += 1
print(f"{i} is the largest prime factor of the number {original}.")
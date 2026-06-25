n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(i + 65), end=' ')
    print()
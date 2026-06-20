n = int(input("Enter the number of terms: "))

a = 0
b = 1
if n == 1:
    print(a)
else:
    for i in range(2, n-1):
        term = a + b
        a = b
        b = term
        ans = a
print(ans)
term = int(input("Enter the number of terms: "))

a = 0
b = 1
print(a, b, end=" ")

for i in range(2, term):
    term = a + b
    print(term, end=" ")
    a = b
    b = term
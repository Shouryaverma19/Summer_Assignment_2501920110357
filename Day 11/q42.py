def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

max_val = find_maximum(num1, num2)
print(f"The maximum number is: {max_val}")
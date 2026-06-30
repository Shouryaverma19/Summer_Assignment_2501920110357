s = input("Enter a string: ")

seen = []
found = False

for char in s:
    if char in seen:
        print("The first repeating character is:", char)
        found = True
        break
    seen.append(char)

if not found:
    print("No repeating characters found.")
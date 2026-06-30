s = input("Enter a string: ")

frequencies = {}
for char in s:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

found = False
for char in s:
    if frequencies[char] == 1:
        print("The first non-repeating character is:", char)
        found = True
        break

if not found:
    print("All characters repeat or string is empty.")
s = input("Enter a string: ")

frequencies = {}
for char in s:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

for char, count in frequencies.items():
    print(f"'{char}': {count}")
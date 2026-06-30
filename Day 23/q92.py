s = input("Enter a string: ")

if s == "":
    print("The string is empty.")
else:
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    max_char = ""
    max_count = 0

    for char, count in frequencies.items():
        if count > max_count:
            max_count = count
            max_char = char

    print(f"The maximum occurring character is '{max_char}' with a count of {max_count}.")
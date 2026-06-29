s = input("Enter a lowercase string: ")

uppercase_str = ""
for char in s:
    if "a" <= char <= "z":
        uppercase_str += chr(ord(char) - 32)
    else:
        uppercase_str += char

print("String in Uppercase:", uppercase_str)
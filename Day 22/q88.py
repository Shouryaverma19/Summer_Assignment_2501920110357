s = input("Enter a string with spaces: ")

clean_str = ""
for char in s:
    if char != " ":
        clean_str += char

print("String after removing spaces:", clean_str)
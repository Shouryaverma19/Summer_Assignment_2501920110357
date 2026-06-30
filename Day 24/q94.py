s = input("Enter a string to compress: ")

length = 0
for char in s:
    length += 1

if length == 0:
    print("Compressed string: ")
else:
    compressed = ""
    current_char = s[0]
    count = 1
    
    for i in range(1, length):
        if s[i] == current_char:
            count += 1
        else:
            compressed += current_char + str(count)
            current_char = s[i]
            count = 1
            
    compressed += current_char + str(count)
    print("Compressed string:", compressed)
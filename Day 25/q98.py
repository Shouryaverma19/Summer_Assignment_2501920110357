s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

freq2 = {}
for char in s2:
    if char in freq2:
        freq2[char] += 1
    else:
        freq2[char] = 1

common_chars = []
for char in s1:
    if char in freq2 and freq2[char] > 0:
        common_chars.append(char)
        freq2[char] -= 1

print("Common characters:", common_chars)
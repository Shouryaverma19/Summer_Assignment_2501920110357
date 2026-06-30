s1 = input("Enter original string: ")
s2 = input("Enter string to check for rotation: ")

is_rotation = False

len1 = 0
for char in s1:
    len1 += 1

len2 = 0
for char in s2:
    len2 += 1

if len1 == len2 and len1 > 0:
    temp = s1 + s1
    if s2 in temp:
        is_rotation = True

if is_rotation:
    print("The string is a valid rotation.")
else:
    print("The string is not a valid rotation.")
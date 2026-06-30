s = input("Enter a string: ")

is_palindrome = True
length = 0
for char in s:
    length += 1

for i in range(length // 2):
    if s[i] != s[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
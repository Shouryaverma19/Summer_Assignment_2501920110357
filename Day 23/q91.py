s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

is_anagram = True

length1 = 0
for char in s1:
    length1 += 1

length2 = 0
for char in s2:
    length2 += 1

if length1 != length2:
    is_anagram = False
else:
    freq1 = {}
    freq2 = {}
    
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
            
    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
            
    if freq1 != freq2:
        is_anagram = False

if is_anagram:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
sentence = input("Enter a sentence: ")

longest_word = ""
current_word = ""

for char in sentence:
    if char != " " and char != "\t" and char != "\n":
        current_word += char
    else:
        len_longest = 0
        for c in longest_word:
            len_longest += 1
            
        len_current = 0
        for c in current_word:
            len_current += 1
            
        if len_current > len_longest:
            longest_word = current_word
        current_word = ""

len_longest = 0
for c in longest_word:
    len_longest += 1
    
len_current = 0
for c in current_word:
    len_current += 1

if len_current > len_longest:
    longest_word = current_word

print("The longest word is:", longest_word)
sentence = input("Enter a sentence: ")

words = []
current_word = ""
for char in sentence:
    if char != " " and char != "\t" and char != "\n":
        current_word += char
    else:
        if current_word != "":
            words.append(current_word)
            current_word = ""
if current_word != "":
    words.append(current_word)

num_words = 0
for w in words:
    num_words += 1

for i in range(num_words):
    for j in range(0, num_words - i - 1):
        len_j = 0
        for c in words[j]:
            len_j += 1
            
        len_next = 0
        for c in words[j + 1]:
            len_next += 1
            
        if len_j > len_next:
            words[j], words[j + 1] = words[j + 1], words[j]

print("Words sorted by length:", words)
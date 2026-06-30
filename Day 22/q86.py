sentence = input("Enter a sentence: ")

word_count = 0
in_word = False

for char in sentence:
    if char != " " and char != "\t" and char != "\n":
        if not in_word:
            word_count += 1
            in_word = True
    else:
        in_word = False

print("Total number of words:", word_count)
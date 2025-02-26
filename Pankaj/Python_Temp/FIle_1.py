sentence = "let's learn python today"
words = sentence.split()  # Split the sentence into words

# Use a for loop to iterate over the words and replace "today" with "python"
for i in range(len(words)):
    if words[i] == "today":
        words[i] = "tomorow"

# Join the words back together to form the updated sentence
updated_sentence = " ".join(words)
print(updated_sentence)


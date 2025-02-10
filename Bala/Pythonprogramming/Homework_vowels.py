#
# ####### TO get count of Vowels #######
# string = "Hello Good Moooorning"
# vowels = "aeiouAEIOU"
#
# count1 = sum(string.count(vowel) for vowel in vowels)
# print(count1)

str1 = "lick Open Zoom Workplace app on the dialog shown by your browser"
small_word = ''
small_len = 4

# get word list with split method
word_list = str1.split()
# get each word using loop
for word in word_list:
    word_len = len(word)  # get length of each word
    print(word, word_len)
    # compare word_len with long_len:
    if word_len < small_len:  # |  4 > 4 | 9 > 4 | 3 > 9
        small_len = word_len  # 4 ,9
        small_word = word  # lick, Workplace
    else:
        continue

print("Smallest word :", small_word, small_len)



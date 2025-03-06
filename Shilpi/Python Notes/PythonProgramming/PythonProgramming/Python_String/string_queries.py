# str1 = "Good Morning"
# str_len = len(str1)
#
# for i in range(str_len):
#     print(i,":", str1[i])
#
#
# str1= "  Hello Good Morning  "
# print(str1.lstrip().rstrip().lower().upper().replace(" ", "_").split("_"))
# # ['HELLO', 'GOOD', 'MORNING']
#

file = open("read_data.txt", "r")
data = file.read()
print(data)
word_list = data.split(" ")
for word in word_list:
    if word.isdigit():
        print(word)


dict1 = {'Name': 'Virat', 'Age': 35}
for val in dict1.items():
    print(val[0], val[1])

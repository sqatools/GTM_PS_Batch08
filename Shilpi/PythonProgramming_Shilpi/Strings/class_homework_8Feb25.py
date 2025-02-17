str3="Pramod Hema Kartik Bala Pramod Manoj Hema Kartik"
str4=str3.split()

# set1=set(str4)
# print(set1)
str5=""
for word in str4:
    if word not in str5:
        str5=str5+word+" "
    else:
        continue
print(str5)
print("_"*100)

str2="Click open zoom Workplace app on the dialog shown by your browser"
str6=str2.split(" ")
l1=len(str6[0])
smallest_word=str6[0]

for word in str6:
    if len(word)<l1:
        smallest_word=word
        l1=len(word)
    else:
        continue
print("The smallest word in the string is :",smallest_word)
print("Length of",smallest_word,"=",l1)
print("_"*100)

# Q2 :  write a python program to get count all vowels from given string
str_a = "Hello GoOd MOrnIong"
# output = 7
vowels=0
list1=["a","e","i","o","u","A","E","I","O","U"]
for i in str_a:
    if i in list1:
        vowels+=1
    else:
        continue
print("The number of vowels is",vowels)
print("_"*100)

# Q3 :  Write a python program to Convert all Vowels from upper to lower and lower to upper.
str_b = "We Are LEarnIng Python PrOgrammIng"
# output = "WE arE LeArning PythOn ProgrAmming"
list2=["a","e","i","o","u","A","E","I","O","U"]
str_output=""
for i in str_b:
    if i not in list2:
        str_output=str_output+i
    else:
        str_output=str_output+i.swapcase()
print(str_output)
print("_"*100)






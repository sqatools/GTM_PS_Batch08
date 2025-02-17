"""
print("1). Write a Python program to get a string made of the first and the last 2 chars from a given string.")
print("If the string length is less than 2, return True instead of the empty string")

str1=input("Your String: ")
if len(str1)<2:
    print(True)
else:
    s1=str1[:2]+str1[-2:]
    print(s1)
print("_"*100)

print("2). Python string program that takes a list of strings and returns the length of the longest string.")
list1=["Python","is","an", "interesting","language"]
b=len(list1[0])
for i in list1:
    l=len(i)
    if l>b:
        b=l
    else:
        continue
print(b)
print("_"*100)

print("3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)")
str3="Rama"
print(str3[-2:]*4)
print("_"*100)

print("4). Python string program to reverse a string if it’s length is a multiple of 4.")
str4="Learning is life"
l1=len(str4)
print(l1)
if l1%4==0:
    print(str4[-1:-l1-1:-1])

else:
    print(f"{l1} is not a multiple of 4")
print("_"*100)

print("5). Python string program to count occurrences of a substring in a string.")
str5="She sells sea shells for she likes to sell the sea shells at the sea shore"
s5="sea"
c=str5.count(s5)
print(f"The count of {s5} in the given string is {c}")


print("6). Python string program to test whether a passed letter is a vowel or consonant.")
str6="Python"
list1=["a","e","i","o","u","A","E","I","O","U"]
for i in str6:
    if i in list1:
        print(i,"- vowel")
    else:
        print(i, "- consonant")
print("_"*100)

print("7). Find the longest and smallest word in the input string.")
str7="We are off to see the wizard, the wonderful wizard of oz."
str_split=str7.split()
word1=0
longword=str_split[1]
smallword=str_split[1]
for i in str_split:
    print(i)
    if len(i)>len(longword):
        longword=i
    elif len(i)<len(smallword):
        smallword=i
    else:
        continue
print("The Longest word is",longword)
print("The smallest word is",smallword)
print("_"*100)
"""
print("8). Print most simultaneously repeated characters in the input string.")
str1="grrrrrr said the lionnn to the mousseeeeeeee"
# str1="Hello how arrrrrrre youuuu"
max_count=0
max_char=""
for i in range(0,len(str1)-1):
    # if i==len(str1)-1:
    #     break
    # else:
        if str1[i]!=str1[i+1]:
            temp=1
            continue
        else:
            temp=temp+1
            if temp>max_count:
                max_count=temp
                max_char=str1[i]

print("The most simultaneously repeated character is",max_char)
print("The count of most simultaneously repeated character is",max_count)
print("_"*100)


"""
print("9). Write a Python program to calculate the length of a string with loop logic.")

str9="And miles to go before I sleep"
l=0
for i in str9:
    l=l+1
print(f"The length of the string using loop logic is {l}")
print("The length of the string using len is", len(str9))
print("_"*100)

# 10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”

str10="Programming"
output=""
for i in str10:
    if i not in output:
        output=output+i
    else:
        output=output+"$"
print(output)
print("_"*100)

# 11). Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
# Output = “lqaTooS”

str11="Sqatool"
output=""
for i in range(0,len(str11)):
    if i==0:
        output=output+str11[-1]
    elif i==len(str11)-1:
        output=output+str11[0]
    else:
        output=output+str11[i]
print(output)
print("_"*100)
"""
# 12). Write a python program to exchange the first and last character of each word from the given string.
# Input = “Its Online Learning”
# Output = “stI enlino gearninL”

str12="Its Online Learning"
str_a=str12.split(" ")
for i in str_a:
    output=""
    for j in range(-1,-len(i)-1,-1):
        print(i[j], end="")
    print(end=" ")
print()
print("_"*100)

print("13). Write a python to count vowels from each word in the given string show as dictionary output.")
# Input = “We are Learning Python Codding”
# output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}")
str12="We are Learning Python Coding"
dictA={}
str123=str12.split(" ")
for x in str123:
    c=0
    for y in x:
        if y=="a" or y=="e" or y=="i" or y=="o" or y=="u" or y=="A" or y=="E" or y=="I" or y=="O" or y=="U":
            c=c+1
    dictA[x]=c
print(dictA)
print("_"*100)

print("14). Write a python to repeat vowels 3 times and consonants 2 times.")
# Input = “Sqa Tools Learning”
# Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”")
str14="Sqa Tools Learning"
for i in str14:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        print(i*3,end="")
    elif i.isspace():
            print(i*1, end="")
    else:
        print(i*2,end="")
print()
print("_"*100)

print("15). Write a python program to re-arrange the string.")
# Input = “Cricket Plays Virat”
# Output = “Virat Plays Cricket”
str15="Cricket Plays Virat"
str15_1=str15.split(" ")
output=""
for x in range(-1,-len(str15_1)-1,-1):
    output=output+str15_1[x]+" "
print(output)
print("_"*100)

print("16). Write a python program to get all the digits from the given string.")
# Input = “””
# Sinak’s 1112 aim is to 1773 create a new generation of people who
# understand 444 that an organization’s 5324 success or failure is
# based on 555 leadership excellence and not managerial
# acumen
# “””
# Output = [1112, 5324, 1773, 5324, 555]
str16="""
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
str16_1=str16.split(" ")
output_list=list()
for x in str16_1:
    if x.isdigit():
        y=int(x)
        output_list.append(y)
    else:
        continue
print(output_list)
print("_"*100)

print("17). Write a python program to replace the words “Java” with “Python” in the given string.")
# Input = “JAVA is the Best Programming Language in the Market”
# Output = “Python is the Best Programming Language in the Market”")
str17="Java is the Best Programming Language in the Market"
print(str17)
output=str17.replace("Java","Python")
print(output)
print("_"*100)

print("18). Write a Python program to get all the palindrome words from the string.")
# Input = “Python efe language aakaa hellolleh”
# output = [“efe”, “aakaa”, “hellolleh”]")
str18="Python efe language aakaa hellolleh"
str18_1=str18.split(" ")
listpal=[]
for x in str18_1:
    if x==x[-1:-len(x)-1:-1]:
        listpal.append(x)
    else:
        continue
print(listpal)
print("_"*100)

print("19). Write a Python program to create a string with a given list of words.")
# Input = [“There”, “are”, “Many”, “Programming”, “Language”]
# Output = There are many programming languages.

str19=["There", "are", "Many", "Programming", "Language"]
str19_1= " ".join(str19) #converting list into string using join
print(str19_1, type(str19_1))
print("_"*100)

print("20). Write a Python program to remove duplicate words from the string.")
# Input = “John jany sabi row john sabi”
# output = “John jany sabi row"
str20="John jany sabi row John sabi"
str20_1=str20.split(" ")
output=""
for x in str20_1:
    if x not in output:
        output=output+x+" "
    else:
        continue
print(output)
print("_"*100)

































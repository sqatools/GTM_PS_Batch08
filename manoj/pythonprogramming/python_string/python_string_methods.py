print(dir(str))

# lower() and upper() :
#       -> lower method convert character in small case.
#       -> upper method convert characters in capital case.

str1 = "hello good morning"
print(str1.lower())  # hello good morning
print(str1.upper())  # HELLO GOOD MORNING

print(("_"*50))
##############
# is _lower() and is_upper():
# is_lower(): this method return True if all the character in string are small case else return fail
# is_upper(): this method return true id all the character in string are in capital case

str_a = "Hello"
str_b = "GOOD"
str_c = "morNING"

print("str_a is lower :", str_a.islower())  # False
print("str_a is upper :", str_a.isupper())  # False

print("str_b is upper :", str_b.isupper())
print("str_c is lower :", str_c.islower())

print("_"*50)
###################
# capitalize method : this method convert only first character of string in capital case
#                     and convert  remaining in small case

str_d = "India won today's match"  # India won today's match
print(str_d.capitalize())

print("_"*50)
#######################
# title method : This method cconvert first character each word into capital case.
str_e = "pYthoN ,IS vERy TO; LEarn"  # Python ,Is Very To; Learn
print(str_e.title())

str_f = "i,invited ma,no,oj"
print(str_f.title())  # I,Invited Ma,No,Oj

# istitle() : This method check the given string in following the rule of
#              title string or not, e.g. first character of each word in string should be capital case

str_g = " Hello Python"
str_h = "python Programming"
print("str_g.is title case :", str_g.istitle())  # true
print("str_h.is title case:", str_h.istitle())  # false

#######################
# swapcase() method :  This method convert upper case to lower case and lower case to upper case in one single string.

str_j = "Hello GOOD MORNing"
print(str_j.swapcase())  # hELLO good mornING

output = ""
for char in str_j:
    print(char)
    if char.isupper():
        output = output + char.lower()
    elif char.islower():
        output = output + char.upper()
    else:
        output = output + char

print("output :", output)


print("_"*50)
#######################
# strip method : This method remove trailing method from given string. all the spaces in the beginning
#                end of string

str_l = " Python Programing  "
print(str_l)
print(str_l.strip())

# lstrip method : This method only remove start spaces from given string
print(str_l.lstrip())

# rstrip method: This method only remove end of string spaces from given string.
print(str_l.rstrip())

str_m = " Hello Good morning  "
var1 = str_m.lstrip()
var2 = var1.rstrip()
print(var2)

print("_"*50)
########################
# count()method : This method return number of occurrences of any character/substring/special characters

str_n = " Hello Good Morning, We are Learning Python"

print("count of e:", str_n.count('e'))  # count of e: 4
print("count of in", str_n.count('in'))  # count of in 2
print("count of spaces:", str_n.count(' '))  # count of spaces: 7

print("_"*50)
###############
# index() method : Index method return index position of any substring or character
str_q = "India is best country"
print(str_q.index("b"))  # 9
# If character is repeated, then it will return first occurrence of the character


# -> if character or substring is not available then it will return error

print("_"*50)
#####################
# find() method : This method return index position of character/substring/number/special character
#                 if it is available in the target string
#                 -> If rhe given substring/character is not available, then it will return -1

str_w = "Learning id Fun"
print("find ing :", str_w.find("ing"))
print("find TO:", str_w.find("TQ"))
print("_"*50)

#########################
# split method : This method split string from any char/substring/delimitr and return list of words

str_A = " Hello Good Morning, How A re You?"
result1 = str_A.split(" ")
print(result1)  # Hello', 'Good', 'Morning,', 'How', 'A', 're', 'You?']

str_B = "Python#Programming#is#very#Easy#to#learn"
result2 = str_B.split("#")
print(result2)  # ['Python', 'Programming', 'is', 'very', 'Easy', 'to', 'learn']

str_C = "Python Programing ios Fun"
print(str_C.split("o"))   # ['Pyth', 'n Pr', 'graming i', 's Fun']

print("_"*50)
#################
# replace method : replace method help to replace any word/character/substring from target values

str_E = "Sky is Best Player"
result = str_E.replace("Sky", "Salt")
print(result)  # Salt is Best Player

result2 = str_E.replace("Sky", "Roy").replace("player", "captain")
print("result2 :", result2)  # Roy is Best Player

print("_"*50)
################################################
# is digit(): This method check given string only contains number
s1 = "helo123"
print("s1 is contains only digit :", s1.isdigit())  # false
s2 = "2343222"
print("s2 is contains only digit:", s2.isdigit())  # true

s3 = "234 345"
print("s3 is contains only digit :", s3.istitle())  # false

print("_"*50)

####################
# isalpha() " This method check if string only contains alphabets

p1 = "Hello"
print("p1 is contains only alphabets :", p1.isalpha())  # tue

p2 = "Hello Good"
print("p2 is contains only alphabets :", p2.isalpha())  # false

# isalnum() : This method check if given string contains only number and character

q1 = "hello143"
print("q1 is contains only characters and numbers :", q1.isalnum())  # true

q2 = "Hello 123"
print("q2 is contains only characters and numbers :", q2.isalnum())  # false

q3 = "Hellopython"
print("q3 is contains only characters and numbers :", q3.isalnum())  # true

print("_"*50)

####################
# isspace() : This method return True of given string contains only spaces
r1 = " "
print("r1 contains only space :", r1.isspace())  # true

# count the spaces without using count method.
str11 = "Hello good evening, how are you"
space_count = 0

for char in str11:
    if char.isspace():
        space_count += 1
    else:
        continue

print("total spaces :", space_count)
# total spaces : 5

print("_"*50)
###############################
# write a python program to replace the word Today with Tomorrow without using replace method
str_t = "Eat something new dish Today"
result = ""  # Eat something new dish Tomorrow
word_list = str_t.split()  # ['Eat', 'something', 'new', 'dish', 'Today']
print(word_list)
for word in word_list:
    print(word)
    if word == 'Today':
        result = result + 'Tomorrow' + " "
    else:
        result = result + word + " "

print(result)

print("_"*40)
#####################
word_list = ['Eat', 'Something', 'new', 'dish', 'today']
word_list.insert(2, '2025')
print(word_list)  # ['Eat', 'Something', '2025', 'new', 'dish', 'today']


# Join method : This method help to join string or list of string with special char/substring/delimiter
result = " ".join(word_list)
print(result)  # Eat Something 2025 new dish today

str_y = "hmm"
print("-".join(str_y))  # h-m-m

str1 = "listening class"
result2 = "^".join(str1)
print("Result :", result2)  # bl^i^s^t^e^n^i^n^g^ ^c^l^a^s^s


##############
str2 = "speaking 123 language 2"
result = str2 == ""
print(result)  # False

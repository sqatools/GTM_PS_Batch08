print(dir(str))

# lower() and upper() :
#       -> lower method convert character in small case.
#       -> upper method convert characters in capital case.

str1 = "hello good morning"
print(str1.lower()) # hello good morning
print(str1.upper()) # HELLO GOOD MORNING

print(("_"*50))
##############
# is _lower() and is_upper():
# is_lower(): this method return True if all the character in string are small case else return fail
# is_upper(): this method return true id all the character in string are in capital case

str_a = "Hello"
str_b = "GOOD"
str_c = "mORNING"

print("str_a is lower :", str_a.islower()) # False
print("str_a is upper :", str_a.isupper()) # False

print("str_b is upper :", str_b.isupper())
print("str_c is lower :", str_c.islower())

print("_"*50)
###################
# capitalize method : thiis mrthod convert only first character of string in capital case and convert  remaaining in small case

str_d = "India won today's match" # India won today's match
print(str_d.capitalize())

print("_"*50)
#######################
# title method : This method cconvert first characcter each word into capital case.
str_e = "pYthoN ,IS vERy TO; LEarn" # Python ,Is Very To; Learn
print(str_e.title())

str_f = "i,invited ma,no,oj"
print(str_f.title()) # I,Invited Ma,No,Oj

# istitle() : This method check the given string in following the rule of
#              title string or not, e.g. first character of eacch word in string should be capital case

str_g = " Hello Python"
str_h = "python Programming"
print("str_g.is title case :", str_g.istitle()) # true
print("str_h.is title case:", str_h.istitle()) # false

#######################]
# swapcase() method :  This method convert upper case to lower case and lower caase to upper case in one single string.

str_j = "Hello GOOD MORNing"
print(str_j.swapcase()) # hELLO good mornING

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
# strip method : This method remove trailing method from given dtring. all the spaces in the begining
#                end of string

str_l = " Python Programing  "
print(str_l)
print(str_l.strip())

# lstrip method : This method only remove start sspcees from given string
print(str_l.lstrip())

# rstrip method: This method only remove end of string spaacces from given string.
print(str_l.rstrip())

str_m = " Hello Good morning  "
var1 = str_m.lstrip()
var2 = var1.rstrip()
print(var2)

print("_"*50)
########################
# count()method : This method return number of occurenceces of any characcter/substring/special characters

str_n = " Hello Good Morning, We are Learning Python"

print("count of e:", str_n.count('e')) # count of e: 4
print("count of in", str_n.count('in')) # count of in 2
print("count of spaces:", str_n.count(' ')) # count of spaces: 7

print("_"*50)
###############
# index() method : Index method return index position of any substring or character
str_q = "India is best country"
print(str_q.index("b"))  # 9
# If charcter is repeated, then it will return first occurence of the character

# get index position of character which is not available
print(str_q.index("T"))
# ValueError: substring not found
# -> if character or substring is not available then it will return error

print("_"*50)
#####################
# find() method : This method return index position of character/substring/number/special character
#                 if it is available in the target string
#                 -> If rhe given substring/character is not available, then it will return -1

str_w = "Learning id Fun"
print("find ing :", str_w.find("ing"))
print("find TO:", str_w.find("TQ"))
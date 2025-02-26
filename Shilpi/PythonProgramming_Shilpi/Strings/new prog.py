# str1="Hello we are learning Python"
# str2=""
# vowels="aeiou"
# for x in range(len(str1)):
#     for y in range(x+1,len(str1)):
#         if str1[x] in vowels and str[x] not in str2:

# write a python program to remove all duplicate vowels from given string.
str1 = "Hello we are learning Python"
vowels="aeiou"
str2=""
for x in str1:
    if x in vowels and x not in str2:
        str2+=x
    elif x not in vowels:
        str2+=x
    else:
        continue
print(str2)
print("_"*100)

l1=[4,76,9,22,55,77,8]
l2=[4,22,5,66,7,22,76,8]
s1=set(l1)
s2=set(l2)
print(s1)
print(s2)
s3=s1.symmetric_difference(s2)
s4=s1.intersection(s2)
l3=list(s3)
l4=list(s4)
print("different value",l3)
print("common value",l4)
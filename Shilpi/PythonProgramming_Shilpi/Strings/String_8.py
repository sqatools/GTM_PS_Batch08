# 8). Print most simultaneously repeated characters in the input string.
str1="Hello how arrrrrrre youuuu"
max_count=0
max_char=""
for i in range(0,len(str1)-1):
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






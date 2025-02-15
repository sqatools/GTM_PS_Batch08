str1="India is my country"
print(str1)
print(str1[4:19:1])
print(str1[2:13:2])

#**string concatination**
str1="India"
str2="is best"
concat= str1+" "+str2
print(concat)
print("-"*50)

#**slicing**
str1="Hello Friends"
slice= str1[7:]
print(slice)
print("-"*50)

#***searching the string***
str1= "i like python."
w="python"
str_len= len(str1)
print(str_len)
if w in str1:
    print("Present")
else:
    print("Not present")
print("-"*50)

#**replace the string**
str1= "i like python."
replaced_string = str1.replace("like","love")
print(replaced_string)
print("-"*50)

#*** string reverse***
str1= "India is great"
print(len(str1))
print(str1[-1:-15:-1])

#****program to  make a string pyramid***
str1="apple"
n= len(str1)
for i in range(n):
    for j in range(n-i- 1):
        print(" ",end="")
    for j in range(2*i+1):
        print(str1[j%n],end="")
    print()
print("-"*50)

#**program for string formatting***
str1="Anupama"
str2="Indian"
new_string="My name is {} and I am an {}.".format(str1,str2)
print("formatted string:"+new_string)
print()
print("-"*50)

#**program to count number of spaces***
str2="I love my India"
print("The string is "+ str2)
c= " "
pos= str2.count(c)
print("The number of spaces are: ",pos)


#**problems given in class***
str4="learning Python"
""" 
1 read learning
2 read only first and last character
3 read all characters except first and last and repeat 2wice
4 get this output "LLLearning Pythonnn"""


print(str4[:8:])
print(str4[:15:14])
print(str4[:15:14],str4[:15:14])
print("ll"+str4[::]+"nn")

#get average
l1 = [2, 4, 6, 8, 10]
sum=0
for val in l1:
    sum +=  val
avg= sum/len(l1)
print(avg)

# check if list values are divisible by 3and 7
l2=[44,76,97,55,3,7,42,21]
for val in l2:
    if val % 3==0 and val%7==0:
        print(val)
print("-"*50)

#**Change the case of vovels in the given string**
s = input("enter the string: ")
v = "aeiouAEIOU"
t = ''
var = 0
for i in s:
    if i in v:
        if i.isupper():
            t = t+i.lower()
        else:
            t = t+i.upper()
    else:
        t = t+i
print(t)






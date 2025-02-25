"""
# Home work for string slicing
#str4 = "Learning Python"
'''
1. read only "Learning"
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
'''

str4 = 'Learning Python'
print(str4[0:8])
print(str4[0]+str4[-1])
print(str4[1:-1]*2)
print(str4[0]*3+str4[1:-1]+str4[-1]*3)

print("="*50)
'''
1). Write a Python program to get a string made of the first and the last 2 chars from a given string. 
If the string length is less than 2, return instead of the empty string
'''
str1 = input("Enter string : ")

if len(str1)<2:
    print(True)
else:
    str2 = str1[:2] + str1[-2:]

print("Substring = ",str2)


print("="*50)
'''
2). Python string program that takes a list of strings and returns the length of the longest string.
'''
str2 = input("Enter the sentence :")
list1=str2.split()
temp=''
for word in list1:
    if len(word)>len(temp):
        temp=word
    else:
        continue
print("Longest word is :",temp)


print("="*50)
'''
3). Python string program to get a string made of 4 copies of the last two characters 
of a specified string (length must be at least 2).
'''
str3= input("Enter string 3: ")
if len(str3)>=2:
    print("Substring 3 = ", str3[-2:]*4)
else:
    print("Entered string is invalid")



print("="*50)
'''
4). Python string program to reverse a string if it’s length is a multiple of 4.
'''
str4= input("Enter string 4: ")
if len(str4)%4==0:
    print("Substring 4 = ", str4[::-1])




print("="*50)
''' 
5). Python string program to count occurrences of a substring in a string.
'''
str5=input("Enter string 5 : ")
sub1='at'
counter1=str5.count(sub1)

print("Occurrences of substring = ",counter1)


print("="*50)
'''
6). Python string program to test whether a passed letter is a vowel or consonant.
'''
str6=input("Enter letter 6 : ")
str6=str6.lower()
if str6 in ['a','e','i','o','u']:
    print("letter is vowel ")
else:
    print("letter is consonant")



print("="*50)
'''
7). Find the longest and smallest word in the input string.  
'''
str7=input("Enter the string : ")
list7=str7.split(' ')
short1=list7[0]
long1=''
for word in list7:
    if len(short1)>len(word):
        short1=word
    if len(long1)<len(word):
        long1=word

print("Shortest word =",short1)
print("Longest word =", long1)



print("="*50)
'''
9). Write a Python program to calculate the length of a string with loop logic. 
'''
str9 = input("Enter the string 9")
count1=0
for i in str9:
    count1+=1

print("Entered string length =", count1)




print("="*50)
'
8). Write a program to get a list of all the mobile numbers from the given string using python.
Input str = “”” We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 
we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.”””
'''
str8 = ''' We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we
want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.'''
list8=str8.split()
list81=[]
for word in list8:
    if word.isdigit() and len(word)==10:
        list81.append(word)

print("List of phone numbers : ",list81)





print("="*50)
'''
10). Write a program to get all the email id’s from given string using python.
Input str = “”” We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com 
we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string.”””
Output = [‘john@gmail.com’, ‘ jay@lic.com’, ‘hari@facebook.com’, ‘mery@hotmail.com’ ]
'''
str10 = ''' We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com
we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string.'''

list10=str10.split()
email_list=[]
for word in list10:
    if word.endswith('.com') and '@' in word:
        email_list.append(word)

print("List of email ids : ",email_list)





print("="*50)
'''
11). WWrite a program to print each character on a new line using python.
Input = ‘python’
'''
str11 = 'python'
for i in str11:
    print(i)



print("="*50)
'''
12). Write a program to print a string 3 times using python.
Input = ‘sqatools’
Output = ‘sqatoolssqatoolssqatools’
'''
str12 = 'sqatools'
print(str12*3)




print("="*50)
'''
13). Write a program to remove repeated characters in a string and replace it with a single letter using python.
Input = ‘aabbccdd’
Output = ‘cabd’
'''
str13='aabbccdd'
str131=''
for i in str13:
    if i not in str131:
        str131+=i
print(str131)




print("="*50)
'''
14). Write a program to swap cases of a given string using python.
Input = ‘Learning Python’
Output = ‘lEARNING pYTHON’
'''
str14= "Learning Python"
print(str14.swapcase())




print("="*50)
'''
15). Write a program to find the first repeated character in a string and its index.
Input = ‘sqatools’
Output = (s,0)
'''
str15= 'sqatools'
for i in range (len(str15)):
    if str15.count(str15[i])>1:
        print((str15[i],i))
        break




print("="*50)
'''
16). Write a program to print the index of each character in a string.
Input =  ‘sqatools’
Output :
Index of s is 0
Index of q is 1
Index of a is 2
Index of t is 3
Index of o is 4
Index of o is 5
Index of l is 6
Index of s is 7
'''
str16 = "sqatools"
for i in range(len(str16)):
    print(f"Index of {str16[i]} is {i}")




print("="*50)
'''
17). Write a program to reverse words in a string using python.
Input = ‘string problems here’
Output = ‘here problems string’
'''
str17= "string problems here"
rev_str17=''
list17=str17.split()
list17_rev = list17[::-1]
for i in range(len(list17_rev)):
    rev_str17= rev_str17 + " " + list17_rev[i]

print("reversed word string : ",rev_str17)




print("="*50)
'''
18). Write a program to add ly at the end of the string if the given string ends with ing.
Input = ‘winning’
Output = ‘winningly’
'''
str18 = "Winning"
str18 = str18.lower()
if str18[-3::1] == 'ing':
    str18 = str18 + 'ly'
print(str18)



print("="*50)
'''
19). Write a program to check if a given string is binary or not.
Hint: Binary numbers only contain 0 or 1.

Input = ‘01011100’
Output = yes

Input = ‘sqatools 100’
Output = ‘No’
'''
str19 = input("enter string")
set19= {'0','1'}
binary = True
for i in str19:
    if i in set19:
        continue
        binary=True
    else:
        binary=False
        break

if binary == True:
    print("string is binary", str19)
else:
    print("string is not binary", str19)



"""

print("="*50)
'''
20). Write a program to remove the kth element from the string
K=2
Input = ‘sqatools’
Output = ‘sqtools’
'''
str20 = input("Enter string 20 : ")
k= int(input("Enter the index position which element needs to be removed : "))
result=''
if k > len(str20):
    print("Index out of bound, Enter correct Index")
else:
    for i in range(len(str20)):
        if i != k:
            result = result + str20[i]

print("Resulted string = ", result)

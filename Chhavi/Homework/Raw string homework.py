"""
# Home work for string slicing
str4 = "Learning Python"

1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"


print("Answer 1: ", str4[0:8])

# Extracting first and last character
char1 = str4[0]
char2= str4[-1]

# Displaying the result
print("Answer 2: ")
print("First character: ", char1)
print("Last character: ", char2)

#read all characters except first and last and repeat 2 times the output. "earning Pythoearning Pytho"

# getting all characters except first and last and repeating twice
all_chars = str4[1:-1] * 2

# Displaying the result
print("Answer 3: ", all_chars)

#get given output  : "LLLearning Pythonnn"

# Modifying the string to match the desired output
Output = str4[0] * 2 + str4 + str4[-1] * 2

# Displaying the result
print("Answer 4: ", Output)

#4). Get a string made of the first and the last 2 chars from a given string. If the string
# length is less than 2, return instead of the empty string

#Str2 = "PythonSyntex"
Str2= str(input("Enter any string of your choice :"))

#print(Str2[0:3])


if len(Str2) < 2:
    print(Str2[:2] + Str2[-3:])
else:
   print("The original string is: ", Str2)


#5 Python string program to get a string made of 4 copies of the
# last two characters of a specified string (length must be at least 2).

Str3= str(input("Enter a string of your choice :"))

print(Str3[-2:] * 4)


#6 Python string program to reverse a string if it’s length is a multiple of 4.

#Str4 = "StringLength"

Str4= str(input("Enter a string :"))

if len(Str4) % 4 == 0:
    print(Str4[::-1])
else:
    print(Str4[::-1])


#7Python string program to count occurrences of a substring in a string.

Str5 = "PythonPythonPythonPython"
print(Str5.count("hon"))

Str6 = "Icing Melting Swetting Ranting Chanting"
print("Count if ing in the string is :", Str6.count("ing"))



#8Python string program to test whether a passed letter is even or odd.

Str7 = str(input("Enter any word : "))

if len(Str7) % 2 == 0:
    print("The string contains even characters")
else:
    print("The string contains odd characters")


#9Python string program to test whether a passed letter is a vowel or consonant.

Str8 = str(input("Enter any single alphabet :"))

if Str8 in ("a","e","i","o","u"):
    print("It is a Vowel")
else:
    print("It is a consonent")

#10Find the longest and smallest word in the input string.

String = str(input("Enter any string : "))
result = String.split(" ")
print(result)

print("Longest word", max(result, key = len))
print("Shortest Word", min(result, key = len))
print("Capitalize : ", String.capitalize())
print("Change the title cases : ", String.title())


#11Print most simultaneously repeated characters in the input string
StringNew = str(input("Enter any string : "))


#12Write a Python program to calculate the length of a string with loop logic

Str_A = "I am learning a new language"
count = 0
for char in Str_A:
    count += 1
print("length of the string without loop: ", count)
print("length of the string with len function :", len(Str_A))




#13 Write a Python program to replace the second occurrence of any char with the special character $.
#Input = “Programming”
#Output = “Prog$am$in$”

Str_B = "Programming"
result = Str_B.replace("r","#")
print(result)

result = Str_B.replace()

#14 Write a python program to get to swap the last character of a given string.
#Input = “SqaTool”
#Output = “IqaTooS”

input_string = "SqaTool"
output_string = input_string.replace([0:1],[-1:0])
print(output_string)



#15 Write a python program to exchange the first and last character of each word from the given string.
#Input = “Its Online Learning”
#Output = “stI enlino gearninL”

input_string = "Its Online Learning"

list1 = input_string.split(" ")

for word in list1:
    new_word = word[-1]+word[1:-1]+word[0]
    print(new_word, end = " ")


"""

#16 Write a python program to count vowels from each word in the given string show as dictionary output.

#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

input_string = "We are Learning Python Coding"
List = input_string.split(" ")
print(List)
vowels = "aeiou"    # Creating vowels list
output_string = ""

for word in List:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
            output_string(word) = count
print(output_string)







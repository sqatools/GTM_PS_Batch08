"""
1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string
"""
from itertools import repeat

from Hema.PythonProgramming.Python_String.Python_string_programms_2 import max_count

string_input = "Helo World"
len_string = len(string_input)
first_2_chars = string_input[:2]
last_2_chars = string_input[-2:]

if len_string <= 2:
    print(f"String length below 2 chars, {string_input}" )
else:
    print(f"first characters are in string is {first_2_chars}, and last characters are {last_2_chars}")

print("-"*50)
"""
2). Python string program that takes a list of strings and returns the length of the longest string.

"""
list_alpha = [chr(i) for i in range(65, 91)]
new_string = ""
for i in list_alpha:
    new_string += i

print(f"longest string using list of characters is {new_string}")
print("-"*50)
"""

3). Python string program to get a string made of 4 copies of the last two characters of a specified string 
(length must be at least 2).
"""
copies_of_string = string_input * 4
print(f"string copies : {copies_of_string}")

print("-"*50)
"""
4). Python string program to reverse a string if it’s length is a multiple of 4.
"""
string_input = "darlingm"
len_of_string = len(string_input)
if len_of_string % 4 == 0:
    print(f"Reverse string is {string_input[::-1]}")
else:
    pass


print("-"*50)
"""
5). Python string program to count occurrences of a substring in a string.
"""
word = "Hello world!"
sub_string = "Hello"

if word.__contains__(sub_string):
    print(True)
else:
    print(False)
print("-"*50)
"""
6). Python string program to test whether a passed letter is a vowel or consonant.
"""
vowels = ["a", "e", "i", "o", "u" "A", "E", "I", "O","U"]

letter = "x"
if vowels.__contains__(letter):
    print(f"Given letter is a vowel: {letter}")
else:
    print(f"Given letter is a consonant: {letter}")

print("-"*50)
"""
7). Find the longest and smallest word in the input string.
"""
string = "My home location is Anantapur"
convert_to_list = string.split()
longest_word = max(convert_to_list, key=len)
shortest_word = min(convert_to_list, key=len)

print(f"Longest word: {longest_word} ({len(longest_word)} characters)")
print(f"Smallest word: {shortest_word} ({len(shortest_word)} characters)")

print("-"*50)
"""
8). Print most simultaneously repeated characters in the input string.

"""
def most_repeated_char(s):
    max_char = ''
    max_count = 0
    current_char = ''
    current_count = 0

    for char in s:
        if current_char == char:
            current_count +=1
        else:
            current_char = char
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            max_char = current_char
    return max_char, max_count


sentence = "abcdefabcdefabca"
char, count = most_repeated_char(sentence)
print(f"most repeated chars {char} and count {count} times")

"""
9). Write a Python program to calculate the length of a string with loop logic.

Solution
10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”

Solution
11). Write a python program to get to swap the last character of a given string.
Input = “SqaTool”
Output = “IqaTooS”

Solution
12). Write a python program to exchange the first and last character of each word from the given string.
Input = “Its Online Learning”
Output = “stI enlino gearninL”

Solution
13). Write a python to count vowels from each word in the given string show as dictionary output.
Input = “We are Learning Python Codding”
output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

Solution
14). Write a python to repeat vowels 3 times and consonants 2 times.
Input = “Sqa Tools Learning”
Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

Solution
15). Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”

Solution
16). Write a python program to get all the digits from the given string.
Input = “””
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
“””
Output = [1112, 5324, 1773, 5324, 555]

Solution
17). Write a python program to replace the words “Java” with “Python” in the given string.
Input = “JAVA is the Best Programming Language in the Market”
Output = “Python is the Best Programming Language in the Market”

Solution
18). Write a Python program to get all the palindrome words from the string.
Input = “Python efe language aakaa hellolleh”
output = [“efe”, “aakaa”, “hellolleh”]

Solution
19). Write a Python program to create a string with a given list of words.
Input = [“There”, “are”, “Many”, “Programming”, “Language”]
Output = There are many programming languages.

Solution
20). Write a Python program to remove duplicate words from the string.
Input = “John jany sabi row john sabi”
output = “John jany sabi row”

Solution
21). Write a Python to remove unwanted characters from the given string.
Input = “Prog^ra*m#ming”
Output = “Programming”

Input = “Py(th)#@&on Pro$*#gram”
Output = “PythonProgram”

Solution
22). Write a Python program to find the longest capital letter word from the string.
Input = “Learning PYTHON programming is FUN”
Output = “PYTHON”

Solution
23). Write a Python program to get common words from strings.
Input String1 = “Very Good Morning, How are You”
Input String1 = “You are a Good student, keep it up”
Output = “You Good are”
"""
print("-" * 50)
"""
Input:

3
5 6
0 0 0 0 0 0
1 1 0 0 0 0
0 0 0 0 1 1
0 0 0 0 0 0
0 0 0 0 0 0

output = 16

def count_adjacent_seats(N, rows, cols, seating):
    total_count = 0
    
    for row in seating:
        empty_streak = 0
        
        for seat in row:
            if seat == 0:
                empty_streak += 1
            else:
                if empty_streak >= N:
                    total_count += (empty_streak - N + 1)
                empty_streak = 0  # Reset for the next streak

        # If the row ends with a streak of zeros, process it
        if empty_streak >= N:
            total_count += (empty_streak - N + 1)

    return total_count

# Reading input
N = int(input())  # Minimum adjacent empty seats required
rows, cols = map(int, input().split())  # Matrix dimensions

# Reading the seating matrix
seating = []
for _ in range(rows):
    row = list(map(int, input().split()))
    seating.append(row)

# Computing the result
result = count_adjacent_seats(N, rows, cols, seating)
print(result)

"""

N = 3 #int(input("no of friends coming for cricket stadium is:"))

rows, cols = map(int, input().split())
seating = []
for _ in range(rows):
    row = list(map(int, input().split()))
    print(row)

print("*" * 50)
"""
def get_enemy_and_kidnaped_person_shirt_number(shirt_numbers):
    kidnaped_person = None
    enemy = None
    for shirt_number in range(1, len(shirt_numbers)+1):
        if shirt_numbers.count(shirt_number) == 2:
            enemy = shirt_number
        elif shirt_number not in shirt_numbers:
            kidnaped_person = shirt_number
    return enemy, kidnaped_person

shirt_numbers = list(map(int, input().split()))
enemy, kidnaped_person = get_enemy_and_kidnaped_person_shirt_number(shirt_numbers)
print(str(enemy) +  " " + str(kidnaped_person))

"""

# Home work for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""

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
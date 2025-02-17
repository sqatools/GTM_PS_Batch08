# Home work for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""

#1)read only "Learning"
str4 = "Learning Python"
print(str4[0:8])
print(str4[-15:-7])

#2) read only First and last character :  Ln
str4 = "Learning Python"
print(str4[0] + str4[-1])

#3)read all characters except first and last and repeat 2 times the output.
str4 = "Learning Python"
print((str4[1:14])*2, end="")

"""

#4)get given output  : "LLLearning Pythonnn"
str4 = "Learning Python"
result = f"LL{str4}nn"
print(result)

"""



# Homework for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""

print("_"*50)
# 1. read only "Learning"
print(str4[0:8])

print("_"*40)

# 2. read only First and last character :  Ln
##################
print(str4[0] + str4[-1])

print("_"*40)

# 3. read all characters except first and last and repeat 2 times the output.
# "earning Pythoearning Pytho"
print(str4[1:15]*2)

print("_"*40)

# 4. get given output  : "LLLearning Pythonnn"
print(str4[0]*3 + str4[1:15]+str4[-1]*3)

print("_"*40)
print(str4[-1:-len(str4)-1:-1])

print("_"*40)

print(str4[::-1])

print(chr(125))
print(ord("a"))
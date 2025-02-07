# Home work for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""

print("1. read only Learning")
print(str4[0:8])        # Learning
print()
print("_"*50)

print("2. read only First and last character :  Ln")
slen = len(str4)
print(str4[0],str4[slen-1])
print("_"*50)

"""
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
"""
print("3. print the pattern 'earning Pythoearning Pytho'")
slen = len(str4)
str5 = str4[1:slen-1]
print(str5*2)
print("_"*50)

"""
4. get given output  : "LLLearning Pythonnn" 0,14
"""
print("4. get given output  : 'LLLearning Pythonnn'")
s1 = str4[0]*2
s2 = str4[14]*2
s3 = s1+str4+s2
print(s3)
print("_"*50)
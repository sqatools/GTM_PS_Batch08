# Home work for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""

str4 = "Learning Python"

print('1. read only "Learning"')
print(str4[0:8])
print(str4[:8])
print("_"*100)

print('2. read only First and last character :  Ln')
print(str4[0]+str4[14])
print("{}{}".format(str4[0],str4[14]))
print(f"{str4[0]}{str4[14]}")
print("_"*100)

print('3. read all characters except first and last and repeat 2 times the output.\n "earning Pythoearning Pytho"\n')

print(str4[1:-1]*2)
print(str4[1:14]*2)
print(str4[-14:-1]*2)
print(str4[-14:14]*2)
print("_"*100)

print('4. get given output  : "LLLearning Pythonnn"')
print(str4[0]*2+str4+str4[-1]*2)
print("{}{}{}".format(str4[0]*2,str4,str4[-1]*2))
print(f"{str4[0]*2}{str4}{str4[-1]*2}")
print("_"*100)
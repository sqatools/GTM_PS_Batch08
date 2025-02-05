'''
strin1="python"
print(strin1, type(strin1))

#1) String concatination
name="Pramod MR"
companyname="tvam"
experiance ="4 years"

result="My self "+name+" working in "+companyname+" and I have "+experiance
print(result)

#2) String formating
result1="I am {} is working in {} and have experiance {}".format(name,companyname,experiance)
print(result1)

#3) f string formatting
result2=f"my self {name} currently working in {companyname} and I have {experiance} of experiance,"
print(result2)

print("_"*100)
Good Evening
01234567891011


'''


stra="Good Evening"
#print(stra[0:13])
#print(stra[0:1])
#print(stra[-13:11])
#print(stra[-13:-1]) #Good Evenin
#print(stra[2:-2])

# Home work for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""
#print(str4[0:8])
result=str4[1]+str4[-1]
print(result)







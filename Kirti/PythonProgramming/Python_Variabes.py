#========= Variables===========

# assignment operator (=)
a=10
print("a is : ",a)
print(id(a))

a=20
print("a is : ",a)
print(id(a))

#assign multiple values to multiple variables----------
p,q,r=10,20,30
print("p is : ",p)
print(id(p))
print("q is : ",q)
print(id(q))
print("r is : ",r)
print(id(r))

#---- assigning single value to multiple variables------
A=B=C=100
print("A is : ",A)
print(id(A))
print("B is : ",B)
print(id(B))
print("C is : ",C)
print(id(C))


#====Rules to define variables=====
'''
1. Variable name can not start with number   # 123kirti - invalid
2. variable name can have number digits     # kirti123
3. variable name can not have space in name  # kirti_test
4. there is no specific length for variable length   # no length limit
5. python is case sensitive        # kirti, Kirti, KIRTI, kIRti all treated as different variables
6. No special characters except '_'(underscore) are used in vaiable name
7. inbuit keywords as a variable names
'''

#==== Keywords in Python========
import keyword

print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''

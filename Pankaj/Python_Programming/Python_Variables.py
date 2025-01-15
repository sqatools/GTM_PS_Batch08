import keyword

a = 30
print(a)
# Here a: is variable
# Here =: is assignment variable
# Here 30: is value which is assigned to a

# way to find address of container where value of a is assigned
print(id(a))  # 140734940579656

b = 25
print(b, id(b))
# o/p 25 140734940579496
# in python , is used to separate different function

# When two variable have same values
c = 33
d = 33
print("c:", c, "Address of c:", id(c))
# c: 33 Address of c: 140734940579752
print("d:", d, "Address of c:", id(d))
# d: 33 Address of c: 140734940579752
# note* both have same address if value is same,
# so in this case both variables are referred to same address or container which have same value.
# note* if variable have different value address will be different for all variable.

# we can assign multiple variable together
A = B = C = 100
print("Value of A:", A, "Address of A:", id(A))
print("Value of B:", B, "Address of A:", id(B))
print("Value of C:", C, "Address of A:", id(C))
'''Value of A: 100 Address of A: 140734937763848
Value of B: 100 Address of A: 140734937763848
Value of C: 100 Address of A: 140734937763848'''
# Note* triple inverted comma open and close is used for multiline comment.

L = 200
# print(l)
# Error: NameError: name 'l' is not defined

######### Rules for assigning variable##########
# 1. Variable name can not start with number.
# 2. Variable name can not have space in between names for variable.
# 3. There is no specific length for variable.
# 4. Python is case-sensitive, variable names will treat differently with different case.
# 5. Special character cant be used for variable except underscore. "_".
# 6. In-build variables can't be used for variable name.

# How to print all keywords in python ?.
print(keyword.kwlist)
# o/p: ['False', 'None', 'True', 'and',
# 'as', 'assert', 'async', 'await', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
# 'raise', 'return', 'try', 'while', 'with', 'yield']


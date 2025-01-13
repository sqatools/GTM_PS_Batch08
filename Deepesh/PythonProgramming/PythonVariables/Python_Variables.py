a = 10
# a : variable
# = : assignment operator
# 10 : value assign to the variable

print(a)  # 10
print(id(a))  # 140720823159512

b = 20
print(b, id(b))  # 20 140720823159832

# Note: every different variable holding different value will have different addresses.

########### two variable have same value ##########
# if two variable have same value, thn their address will same
x = 40
y = 40

print("x :", x, "address:", id(x))
# x : 40 address: 140720823160472
print("y :", y, "address:", id(y))
# y : 40 address: 140720823160472

################### Assign multiple value to multiple value at a time ############

p, q, r = 50, 60, 70
print("value p:", p)  # value p: 50
print("value q:", q)  # value q: 60
print("value r:", r)  # value r: 70
print("value of p, q, r :", p, q, r)
# value of p, q, r : 50 60 70

########### Assign same value to multiple variables ###########

A = B = C = 100
print("Value A :", A, id(A))  # Value A : 100 140720823162392
print("Value B :", B, id(B))  # Value B : 100 140720823162392
print("Value C :", C, id(C))  # Value C : 100 140720823162392
#############
L = 200
# print(l)
# NameError: name 'l' is not defined. Did you mean: 'L'?

############# Rules to declare variables #############
# 1. Variable name can not start with number
var123 = 500  # correct
# 2var = 500   # wrong

# 2. Variable name can not have space in the name
var_name_email = 'rahul jain'  # correct
# var name = 'john' # wrong name

# 3. There is no specific length for variable
var_name_has_no_limit_wrtrewereer = 50
print(var_name_has_no_limit_wrtrewereer)

# 4. Python is case-sensitive, variable names will treat differently with different case.

Name = 'Jai'
NAME = 'Rahul'
name = 'Mohit'
namE = 'Pramod'

print(Name, NAME, name, namE)

print(Name, "\n", NAME, "\n", name, "\n", namE)

# 5. Can not use special character in variable name except underscore('_')
# var_$_123 = 500 # wrong
# var-to-home = 600

# 6. Can not inbuilt keyword as variables
# True = 600 # wrong # SyntaxError: cannot assign to True
true = 700  # wrong
# class = 600 # wrong

###################################
import keyword

print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 
'async', 'await', 'break', 'class', 'continue', 'def', 
'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""

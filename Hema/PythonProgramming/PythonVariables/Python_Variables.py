#Variable is holding the different type as values

a = 10

#where,
# a = variable name
# = is assignment operator
# 10 = value assign to the variable

print(a)
print(id(a))

#NOTE: every different variable holding different values will have different address

b = 20

print(b)
print(id(b))

###### two variables having same values #############

#if two variables have same value, then their address will also be same

x = 40
y = 40

print("x: ", x, "address: ", id(x))
#x:  40 address:  140705348721648

print("y: ", y, "address: ", id(y))
#y:  40 address:  140705348721648

#Assign multiple values to multiple variable at a same time

p,q,r = 50,60,70

print("value of p: ", p) #value of p:  50

print("value of q: ", q) #value of q:  60

print("value of r: ", r) #value of r:  70

print("value of p,q,r: ", p,q,r) #value of p,q,r:  50 60 70

############## Assign same value to multiple variable ##########

A = B = C = 100

print("value of A: ", A, "address: ", id(A)) # value of A:  100 address:  140705347347312
print("value of B: ", B, "address: ", id(B)) # value of B:  100 address:  140705347347312
print("value of C: ", C, "address: ", id(C)) # value of C:  100 address:  140705347347312
print("value of A, B, C: ", A,B,C) # value of A, B, C:  100 100 100

L = 200
# print(l)
#NameError: name 'l' is not defined

#### Rules to declare the variable ##########

#1. Variable name cannot start with number
var123 = 123 # correct

#12var = 456 # incorrect
#SyntaxError: invalid syntax

#2. Variable name cannot have space
var_name = "welcome" # correct

#var name = "john" # incorrect
#SyntaxError: invalid syntax

#3. There is no specific length in the variable name

var_name_has_no_limit = 50
print(var_name_has_no_limit)

#4. Python is case sensitive, variable will be trested differently in different cases

Name = 'Jai'
NAME = 'Rahul'
name = 'Mohit'
namE = 'Pramod'

print(Name, NAME, name, namE)

print(Name, "\n", NAME, "\n", name, "\n", namE)

#5. Variable name cannot have special characters except underscore (_)

# var_$_123 = 500 # wrong
# var-to-home = 600

#6. Cannot have inbuiltin keyword as variables

# True = 600 # wrong # SyntaxError: cannot assign to True
true = 700  # wrong
# class = 600 # wrong

import keyword

print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 
'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 
'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 
'while', 'with', 'yield']
'''
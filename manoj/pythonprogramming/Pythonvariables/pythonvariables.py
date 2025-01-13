a = 10
# a : variable
# = : assignment operator
# 10 : value assign to the variable

print(a)  # 10
print(id(a))  # 10 140729429984456

b = 30
print(b, id(b))  # 30 140729429985096

# Note: every different variable hold different value will have different addresses

######3 two variable have same value ###########
# if two variable have same value,then their address will be same
x = 50
y = 50

print("x :", x, "address:", id(x))
# x : 50 address: 140729121573320
print("y :", y, "address:", id(y))
# y : 50 address: 140729121573320

################assign multiple value to multiple value at a time########

p, q, r = 50, 60, 70
print("value p:", p) # value p: 50
print("value q:", q) # value q: 60
print("value r:", r) # value r: 70
print("value of p, q, r :", p, q, r)
# value of p, q, r : 50 60 70


########assign same value to multiple variables#########

A = B = C = 100
print("value A :", A, id(A)) # value A : 100 140729128062984
print("value B :", B, id(B)) # value B : 100 140729128062984
print("value C :", C, id(C)) # value C : 100 140729128062984

################# Rules to declare variables ##########
# 1. Variable name can not start with number
var123 = 500 # correct
# 2var = 500 # wrong

# 2. Variable name can not have space in the name
var_name_email = 'manoj jain' # correct
# var name = 'jain' wrong name

# 3 . There is no specific length fot varaible name
var_name_has_no_limit_wrtewereer =  50
print(var_name_has_no_limit_wrtewereer)

# 4. python is case-sensitive, variable names will treat  differently  with different case

Name = 'Jai'
NAME = 'Manoj'
name = 'Kumar'
namE = 'Deep'

print(Name, NAME, name ,namE)

print(Name,"\n" , NAME, "\n" , name, "\n" , namE, "\n")
# 5 . can not use special character in  variable name except underscore
#var_$_123 = 500 # wrong
#var-to-home = 600

# 6. can not inbuilt keyword as variables
#True = 600 # wrong #syntaxError : cannot assign to true
true = 700 # wrong
#class = 600 # wrong

############
import keyword
print(keyword.kwlist)

"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
 """


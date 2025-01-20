"""

types of python data types
1.Number
 a) Integer : Immutable
 b)Float : Immutable
 c)complex number : Immutable

2.Sequential
 a) string : Immutable
 b) list : mutable
 c)Tuple : Immutable

3.Dictionary : mutable
4.set : mutable
5.Boolean : Immutable
"""
########## Integer data type ######
n1 = 30
print(n1, type(n1))
# 30 <class 'int'>
"""
Properties of Integer
-> Integer is a immutable data type , once it is defined we can not change.
-> There is no limit for integer data type
-> Integer always consider a whole number (positve and negative both) .
"""

n2 = 8938299332020
print(n2, type(n2))
# 8938299332020 <class 'int'>

n3 = 0
print(n3, type(n3))
# 0 <class 'int'>

n4 = -73882
print(n4, type(n4))
# -73882 <class 'int'>

# when we add 2 integer value then output will be integer only
v1 = 230
v2 = 345
v3 = v1 + v2
print("v3:", v3, type(v3))
# v3 :575 <class 'int'>

print("_"*40)
############ Float ###########
p1 = 50.57
print(p1, type(p1))
# 50.57 <class 'float'>

"""
# properties of float
-> Float is immutable data type
-> There is no specific limit for float dataa type
-> All the pointer values will be consider as float(both positive and negative)

"""

v2 = 50 + 50.57
print(v2, type(v2))

p2 = 0.0
print("p2 :", p2, type(p2))  # p2 : 0.0 <class 'float'>
p3 = 0.000456
print("p3 :", p3, type(p3))  # p3 : 0.000456 <class 'float'>
p4 = 12.342234
print("p4 :", p4, type(p4))  # p4 : 12.342234 <class 'float'>
p5 = 34444444445.33
print("p5 :", p5, type(p5))   # p5 : 34444444445.33 <class 'float'>

print("_"*50)
############## complex number ########
# complex number represent with x+yj
# x = real number
# y = imaginary number

q1 = 10 + 20j
print(q1, type(q1))
# (10+20j) <class 'complex'>

q2 = 3.4 + 44.4j
print(q2, type(q2))
# (3.4+44.4j) <class 'complex'>

result = q1 + q2
print(result, type(result))
# (13.4+64.4j) <class 'complex'>

# complex number
q4 = q1*2
print("multiplication :", q4, type(q4))
# (20+40j) <class 'complex'>

q5 = 55+60j
print("real number :", q5.real)  # 55.0
print("imaginary number :", q5.imag)  # 60.0

q6 = int()

print(q6)


# p7 = 10 + 20i
# print(p7)
print("_"*50)
############## string data type ###########3

s1 = "Hello"
print(s1, type(s1))
# Hello  <class 'str'>

s = str()
s0 = ''
s2 = ""
s3 = 'A'
s4 = 'B'
s5 = 'Python'
s6 = "Hello we are learning python @@@@@"
s7 = 'python programming is 3453'
s8 = "good evening 'how' are you **"
s9 = 'very good "morning" , good @#$%^&*'
s10 = """ hello we are learning python programming, and learning is fun.
its very "easy" understand        
"""
s11 = '''
hello we are learning
python programming, 'and' 'learning is fun. 
Its very "easy" understand
'''

var1 = "nice"
s12 = " Have a "+var1+" day "
v1 = 40
v2 = 60
v3 = 70
print(v1, "hello",v2,"python",v3)

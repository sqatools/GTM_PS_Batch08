"""
Types of Python data types.
1. Numbers
   i). Integer :  Immutable
   ii). Float : Immutable
   iii). Complex number  : Immutable

2. Sequential
   i). String : Immutable
   ii). List :  mutable
   iii). Tuple : Immutable

3. Dictionary : mutable
4. Set : mutable
5. Boolean : Immutable
"""

print("_" * 50)
print("######## Integer Data Type #########")
n1 = 40
print(n1, type(n1))  # 40 <class 'int'>

""""
 Properties of Integer:
                        -->Integer is a immutable data type, once it is defined we can not change.
                        -->there is no limit integer Data type
                        -->Integer always consider a whole number( Positive and negative both)
"""
print("_" * 50)
print("??????????????????")
'''
 a1 = 121231545415454
 print(a1,type(a1)) #    a=121231545415454 IndentationError: unexpected indent
 '''
print("??????????????????")

n1 = 4564782341545245
print(n1, type(n1))  # 4564782341545245 <class 'int'>

n2 = 0
print(n2, type(n2))  # 0 <class 'int'>

n3 = -545643546465
print(n3, type(n3))  # -545643546465 <class 'int'>

'''
Note: when we add 2 integer value then output will be integer only
'''
A1 = 10
A2 = 30
A3 = A1 + A2
print("A3 :", A3, type(A3))  # A3 : 40 <class 'int'>

print("_" * 50)
print("######## Float Data Type #########")

p = 568.35
print(p, type(p))  # 568.35 <class 'float'>
""""
 Properties of Float:
                        -->Float is immutable data type.
                        -->There is no specific limit for float data type
                        -->All the pointer values will be consider as float( Positive and negative both)
"""
p1 = 100 + 5.36
print(p1, type(p1))

p2 = 0.0
print("p2 :", p2, type(p2))  # p2 : 0.0 <class 'float'>
p3 = 0.000891
print("p3 :", p3, type(p3))  # p3 : 0.000891 <class 'float'>
p4 = 11.000565555
print("p4 :", p4, type(p4))  # p4 : 11.000565555 <class 'float'>
p5 = 655464565654.12365478
print("p5 :", p5, type(p5))  # p5 : 655464565654.1237 <class 'float'>

print("_" * 50)
print("######## Complex  Number Data Type #########")
'''
    complex number represent with x+yj
    x = real number
    y = imaginary number
'''

q1 = 10 + 20j
print(q1, type(q1))  # (10+20j) <class 'complex'>

q2 = 3.6 + 65.3j
print(q2, type(q2))  # (3.6+65.3j) <class 'complex'>

result = q1 + q2
print(result, type(result))  # (13.6+85.3j) <class 'complex'>

######################### complex number
q4 = q1 * 2
print("multiplication :", q4, type(q4))  # multiplication : (20+40j) <class 'complex'>

q5 = 55 + 75j
print("real number :", q5.real)  # 55.0
print("imaginary number :", q5.imag)  # 75.0

q6 = int()

print(q6)
p7 = 10 + 20j
print(p7, type(p7))  # (10+20j) <class 'complex'>

# p7 = 10 + 20i
# print(p7) # SyntaxError: invalid decimal literal

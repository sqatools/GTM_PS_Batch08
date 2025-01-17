"""
Types of Python Data Types:
1. Numbers
    i. Integer : Immutable
    ii. Float : Immutable
    iii. Complex Numbers : Immutable

2. Sequential
    i. String : Immutable
    ii. List : Mutable
    iii. Tuple : Immutable

3. Dictionary : Mutable
4. Set : Mutable
5. Boolean : Immutable

"""

#################  Integer Numbers ##############
print("Different examples of Integers")
n1 = 25
print(n1,type(n1))   # 25 <class 'int'>

"""
Properties of Integer
->  Integer is an immutable data type, once it is defined we can not change.
->  There is no limit for integer data type
->  Integer is always considered as a whole numbers (+ve and -ve both)
"""

n2 = 743563847534990934728489930
print(n2, type(n2))   # 743563847534990934728489930 <class 'int'>

n3 = 0
print(n3, type(n3))   # 0 <class 'int'>

n4 = -65364367
print(n4, type(n4))   # -65364367 <class 'int'>

# When we add 2 integers then sum will be also Integer
v1 = 34
v2 = 578
v3 = v1 + v2
print("Sum of numbers is: ",v3)    #Sum of numbers is:  612

print("_"*100)

####################### Float Numbers ############################

print("Different examples of Float numbers")

p1 = 23.988
print(p1, type(p1))   # 23.988 <class 'float'>

"""
# Properties of Float :
->  Float is an immutable data type
->  There is no specific limit for float data type
->  All the pointer values will be considered as float (Both positive and negative)

"""

p2 = 0.000
print("p2 :", p2, type(p2))  # p2 : 0.0 <class 'float'>
p3 = 0.000345000
print("p3 :", p3, type(p3))  # p3 : 0.000345 <class 'float'>
p4 = 11.343434334543
print("p4 :", p4, type(p4))  # p4 : 11.343434334543 <class 'float'>
p5 = 655464565654.1234
print("p5 :", p5, type(p5))  # p5 : 655464565654.1234 <class 'float'>

print("_"*100)

#################### Complex Numbers #########################
# complex number represent with x+yj
# x = real number
# y = imaginary number

print("Different examples of Complex Numbers")

c1 = 20 + 30j
print(c1, type(c1))   # (20+30j) <class 'complex'>

c2 = 34.34 + 46.28j
print(c2, type(c2))  # (34.34+46.28j) <class 'complex'>

c3 = c1 + c2
print(c3, type(c3))   # (54.34+76.28j) <class 'complex'>

c4 = c2*3              # Multiplying a complex number
print(c4, type(c4))    # (103.02000000000001+138.84j) <class 'complex'>

c5 = 55 + 38j
print("Real Number is: ",c5.real)
print("Imaginary number is: ",c5.imag)
# Real Number is:  55.0
# Imaginary number is:  38.0

c6 = int()
print(c6)   # 0

# p7 = 10 + 20i
# print(c7) # SyntaxError: invalid decimal literal

#     p7 = 10 + 20i
# IndentationError: unexpected indent

print("_"*100)


########################### String Data Type ##########################
print("String Datatype related Examples")

s1 = "Hello"
print(s1, type(s1))    # Hello <class 'str'>

s = str()
s0 = ""
s2 = ''
s3 = 'A'
s4 = "B"
s5 = 'Python'
s6 = "Hello we are learning Selenium with Python $$$$"
s7 = 'Python programming is easy 2324'
s8 = "Good morning 'Hope' you are good"
s9 = 'Very good "evening". Enjoy your party &&^&^  \nThere is gonna be a party tomorrow as well \n I will attend a party tomorrow'
s10 = """We are leaning Python programming.
'and' learning is fun. It's
very easy to understand this concept
"""
s11 = '''
Hello we are learning
Python Programming, 'and' 'learning is fun.
Its very "easy" understand
'''

var1 = "great"
s12 = "Have a"+var1+" day"

print("_"*40)
print("s :",s)
print("_"*40)
print("s0 :",s0)
print("_"*40)
print("s1: ",s1)
print("_"*40)
print("s2: ",s2)
print("_"*40)
print("s3:", s3)
print("_"*40)
print("s4:", s4)
print("_"*40)
print("s5:", s5)
print("_"*40)
print("s6:", s6)
print("_"*40)
print("s7:", s7)
print("_"*40)
print("s8:", s8)
print("_"*40)
print("s9:", s9)
print("_"*40)
print("s10:", s10)
print("_"*40)
print("s11:", s11)
print("_"*40)
print("s12:", s12)

v1 = 40
v2 = 60
v3 = 70
print(v1,"Hello",v2,"python",v3)
print("_"*40)




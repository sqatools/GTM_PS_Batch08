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
print("############### Boolean Data Type #########")

# boolean data type only contains 2 values True and False

var1 = True
print(var1, type(var1))  #True <class 'bool'>

var2 = False
print(var2, type(var2))

print(dir(bool))
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']




n1 = 500
n2 = 600
print(n1+n2)
print(n1.__add__(n2))
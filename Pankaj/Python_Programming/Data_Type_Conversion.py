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

#################### Int #######################
print("_"*50)
# int--> float
n1 = 10
f1 = float(n1)
print(f1, type(f1))
print("_"*50)
# int--> string
n2 = 30
str2 = str(n2)
print(str2, type(str2))

print("_"*50)
# int--> list
# n3 = 50
# list3 = list(n3)
# print(list3, type(list3))
# TypeError: 'int' object is not iterable
"""
# TypeError: 'int' object is not iterable
print("_"*50)
### Int -> tuple ### Conversion is not possible
### Int -> dict ### Conversion is not possible
### Int -> set ### Conversion is not possible
"""





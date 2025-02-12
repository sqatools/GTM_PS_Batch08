"""TYPES OF PYTHON DATA TYPES
1.Number
2.Sequential
3.Dictionary
4.Set
5.Boolean

1.NUMBER
(i) int-immutable
(ii)float-immutable
(iii)complex number-immutable

2.SEQUENTIAL
(i)string-immutable
(ii)List-mutable
(iii)Tuple-immutable

3.DICTIONARY-mutable
4.SET-mutable
5.BOOLEAN"""

#1.NUMBER
#(i) int datatype
num1=10
print(num1,type(num1))

#(ii)float datatype
num2=20.88
print(num2,type(num2))

#(iii) complex number
num3=66.99+9j
print(num3,type(num3))

#Sequential
#(i) string-str
s1="Hello"
print(s1,type(s1))
s2=""
print(s2,type(s1))
s3='A'
print(s3,type(s3))
s4="B"
print(s4,type(s4))
s5='Python'
print(s5,type(s5))
s6="Hello we are learning Python"
print(s6,type(s6))
s7='Python Programming'
print(s7,type(s7))
s8=str()
print(s8,type(s8))
s0=''
print(s0,type(s0))
s8="Good Morning 'Hope you are doing well'"
print(s8,type(s8))
s9='Very "Good Evening", Enjoy your party'
print(s9,type(s9))
s10=""" For oft when on my couch I lie
in vacant or in pensive mood
they flash upon that inward eye
which is a bliss of solitude
and then my heart with pleasure fills
and dances with the daffodils
"""
print(s10,type(s10))
s11='''Born in the indian soil 
the tale of a zero's uprise
from valueless to infinity
boundless while bound in a vicious circle'''
print(s11,type(s11))

s12="Morning"
print(s12[3])
print(s12[-6])
print(len(s12))
print(s12.index('o'))
print(s12[2:4])

#List datatype-mutable
list1=[5,9,8,6,8,9,90,5]
print(list1)
list2=[88,2,3,4,55,[9,8,5],"Hello",'Python',(5,9,8),list1,{'name':'Shilpi'}]
print(list2)
list2.append("SJ")
print(list2)
print(dir(list))
print(list2[1])
print(list2[-6])

#Tuple- immutable-cannot be modified
tup1=()
print(tup1,type(tup1))
tup2=(2,5,7,8,2,4,5,6,2)
print(tup2,type(tup2))
print(dir(tuple))
print(tup2.count(2))# count gives how many times the particular item is repeated in the tuple
print(tup2.index(7))#similar to index of in java

#Dictionary-stores data in a key value pair
dict1={
    "Name":"Sita",
    "Age":25,
    "City":"Ayodhya"
}
print(dict1)
print(dict1["Name"])
dict1["phone"]=283900788
print(dict1)
print(dir(dict))

#Set-stores unique data. defined in curly {} braces. prints the set in random order. removes duplicates.
set1={3,9.9,3,8,9,67,56,45,9,56}
print(set1)
print(dir(set))
#set2={4,5,6,7,[89,90,67],89} # gives error when list is added
#print(set2)

#Boolean-True or False
var1=True
print(var1,type(var1))
var2=False
print(var2,type(var2))

#Magic methods-that python internally uses __add__ internally
n1=100
n2=200
print(n1+n2)
print(n1.__add__(n2))






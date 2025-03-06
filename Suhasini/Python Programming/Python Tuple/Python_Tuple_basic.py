"""
Tuple Properties:

1. Tuple is immutable data type, we can modify it.
2. Tuple can contain all types of data : int, float, string, list, tuple, bool, set, dict
3. Tuple follows +ve and -ve indexing like string and list
4. Tuple is defined with round braces ()
5. Tuple data type is used when data is not going to need changes
    Ex: days of week, months of year

"""

tup1 = (3, 3.5, 'Hello', [3, 5, 7], (4, 1, 5), {'a' : 123, 'b' : 45}, True, {3, 6, 8})

print(tup1, type(tup1))
# (3, 3.5, 'Hello', [3, 5, 7], (4, 1, 5), {'a': 123, 'b': 45}, True, {8, 3, 6}) <class 'tuple'>

# get value from tuple using index
print(tup1[4])  # (4, 1, 5)

print(tup1[4][2]) # 5

print(tup1[-3]) # {'a': 123, 'b': 45}
print("_"*70)

var1 = "2PIR"
var2 = "a^2+b^2+2ab"
var3 = [5, 7, 8]
tup3 = (var1, var2, var3)

print(tup3) # {'a': 123, 'b': 45}
var3.append(100)
print(tup3) # ('2PIR', 'a^2+b^2+2ab', [5, 7, 8, 100])
print("_"*70)

############################################
tup4 = ('a', 'b', 'c', 'd')

# without indexing
for val in tup4:
    print(val)

print("_"*40)
# with indexing
for i in range(len(tup4)):
    print(i, tup4[i])
"""
0 a
1 b
2 c
3 d
"""
print("_"*70)

###################################

name = "Suhasini"
tup5 = ("Hello", f"My name is {name}", "I am a good student")
print(tup5)
# ('Hello', 'My Name is Nitin', 'I am a good student')

print("_"*50)

##################################

tup6 = (4, 6, 8, 12, 13, 15, 16, 11, 22, 66)

print(tup6[6:-2:1]) # (16, 11)
print(tup6[3:8])  # (12, 13, 15, 16, 11)
print(tup6[-3:-8:-1]) # (11, 16, 15, 13, 12)
print(tup6[1:len(tup6):2]) # (6, 12, 15, 11, 66)
print(tup6[1:-1:1]) # (6, 8, 12, 13, 15, 16, 11, 22)
print(tup6[1:-1]) # (6, 8, 12, 13, 15, 16, 11, 22)

print("_"*70)

###############################
# print(dir(tuple))
# 'count', 'index'

tup7 = (5, 7, 8, 7, 2, 7, 3, 7)
print("Number of times 7 is repeated is: ",tup7.count(7))
# Number of times 7 is repeated is:  4

print("index of 3 :", tup7.index(3))
# index of 3 : 6

# print(tup7.index(100))
# ValueError: tuple.index(x): x not in tuple
print("_"*70)

######################################
# max min and sum from tuple
tup8 = (33, 66, 77, 102, 40, 50, 20)

print("max value :", max(tup8))
# max value : 102
print("Min value :", min(tup8))
# Min value : 20
print("sum of values :", sum(tup8))
# sum of values : 388

print("_"*70)

#######################################
# get index position of any specific repeated value from given tuple.

tup8 = (5, 7, 8, 7, 2, 7, 8,  3, 7, 8)
#second_7_index

num = 8
count_of_num = 2
count = 0
for i in range(len(tup8)):
    if tup8[i] == num:
        count += 1
        if count_of_num == count:
            print(i)
            break
    else:
        continue

print("_"*70)

####################################
tup_a = (4, 7, 1, 8, 22, 6, 17)

# get sorted value from tuple
result1 = tuple(sorted(tup_a))
print("sorted result :", result1)  # (1, 4, 6, 7, 8, 17, 22)

# get reversed from tuple
result2 = tuple(reversed(tup_a))
print("reversed value :", result2) # (17, 6, 22, 8, 1, 7, 4)
print("_"*70)

###################### Tuple Comprehension #########################

tup_b = (5, 7, 9, 2, 5, 7)
res1 = (x**2 for x in tup_b)
print(tuple(res1))
# (25, 49, 81, 4, 25, 49)

tup_c = (11, 55, 88, 22, 66, 99)
res2 = tuple(['even', x] if x%2 ==0 else ['odd', x] for x in tup_c )
print(res2)
print("_"*70)



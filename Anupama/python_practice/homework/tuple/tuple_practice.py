"""
tuple properties :
->  tuple is immutable data type, we can not modify it
->  tuple can contain all types of data, int, float, string, list, tuple, dict, set, bool.
->  tuple follows +ve and -ve indexing as like list and string
->  tuple defined with round brackets.
->  Generally we use tuple data type, when the data is going to fix no changes are required.
    e.g. days in a week, months in year. etc
"""

tup1 = (3, 3.5, 'Hello', [3, 5, 7], (4, 1, 5), {'a' : 123, 'b' : 45}, True, {3, 6, 8})

print(tup1, type(tup1))
# (3, 3.5, 'Hello', [3, 5, 7], (4, 1, 5), {'a': 123, 'b': 45}, True, {8, 3, 6}) <class 'tuple'>

# get value from tuple using index
print(tup1[4])  # (4, 1, 5)

print(tup1[4][2]) # 5

print(tup1[-3]) # {'a': 123, 'b': 45}

var1 = "2PIR"
var2 = "a^2+b^2+2ab"
var3 = [5, 7, 8]
tup3 = (var1, var2, var3)

print(tup3) # {'a': 123, 'b': 45}
var3.append(100)
print(tup3) # ('2PIR', 'a^2+b^2+2ab', [5, 7, 8, 100])


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

print("_"*50)
name= "Nitin"
tup5 = ("Hello", f"My Name is {name}", "I am a good student")
print(tup5)
# ('Hello', 'My Name is Nitin', 'I am a good student')

print("_"*50)
#################### slicing in tuple ##################

tup6 = (4, 6, 8, 12, 13, 15, 16, 11, 22, 66)

print(tup6[6:-2:1]) # (16, 11)
print(tup6[3:8])  # (12, 13, 15, 16, 11)
print(tup6[-3:-8:-1]) # (11, 16, 15, 13, 12)
print(tup6[1:len(tup6):2]) # (6, 12, 15, 11, 66)
print(tup6[1:-1:1]) # (6, 8, 12, 13, 15, 16, 11, 22)
print(tup6[1:-1]) # (6, 8, 12, 13, 15, 16, 11, 22)

print("_"*50)
###############################
print(dir(tuple))
# 'count', 'index'

tup7 = (5, 7, 8, 7, 2, 7, 3, 7)
print("count of 7 :", tup7.count(7))
# count of 7 : 4

print("index of 3 :", tup7.index(3))
# index of 3 : 6

# print(tup7.index(100))
# ValueError: tuple.index(x): x not in tuple

#
######################################
# max min and sum from tuple
tup8 = (33, 66, 77, 102, 40, 50, 20)

print("max value :", max(tup8))
# max value : 102
print("Min value :", min(tup8))
# Min value : 20
print("sum of values :", sum(tup8))
# sum of values : 388


print("_"*50)
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


print("_"*50)
####################################
tup_a = (4, 7, 1, 8, 22, 6, 17)

# get sorted value from tuple
result1 = tuple(sorted(tup_a))
print("sorted result :", result1)  # (1, 4, 6, 7, 8, 17, 22)

# get reversed from tuple
result2 = tuple(reversed(tup_a))
print("reversed value :", result2) # (17, 6, 22, 8, 1, 7, 4)

######################## Tuple Comprehension ################
print("_"*40)

tup_b = (5, 7, 9, 2, 5, 7)
result1 = (x**2 for x in tup_b)
print("result1 :", tuple(result1))


tup_c = (11, 55, 88, 22, 66, 99)
result2 = tuple(['even', x] if x%2 == 0 else ['odd', x] for x in tup_c)
print(result2) # (['odd', 11], ['odd', 55], ['even', 88], ['even', 22], ['even', 66], ['odd', 99])

"""
# Q1 : write tuple program to get max from tuple without using max function.
t1 = (55, 77, 203, 5, 1, 7)
output = 203

# Q2 : write a python program to get list of combination of two values whose sum is 20
t2 = (3, 6, 9, 10, 11, 12, 8, 14, 6)
(9, 11)
(12, 8)
(14, 6)

#Q3 : write a python remove value which is repeated more two times and store in list.
t3 = (1, 3, 1, 4, 1, 5, 3, 6, 3, 7, 3, 4, 6 ,4)
output = [5, 6, 7]
"""

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

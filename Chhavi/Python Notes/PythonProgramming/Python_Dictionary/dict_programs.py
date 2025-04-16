dict1 = {'name':'john','city':'Landon','country':'UK'}
dict2 = {}
temp = dict1.copy()

for val in temp:
    v1 = dict1.pop(val)
    dict2[val] = v1

print("dictionary 2 :", dict2)
print("dictionary 1 :", dict1)



list7=[4, 5, 6, 2, 1, 7, 11]
dict9={x:x**2 if x%2==0 else x**3 for x in list7}
print("dict9 :", dict9)


dict1 = {'d':14,'b':52,'a':13,'c': 1}

dict_items = dict1.items()
print(dict_items)

result = sorted(dict_items, key=lambda item: item[1])
print(result)
print(dict(result))


# [('d', 14), ('b', 52), ('a', 13), ('c', 1)]

result = lambda x,y : x+y
print(result(50, 60))


# [('d', 14), ('b', 52), ('a', 13), ('c', 1)]
# [('a', 13), ('b', 52), ('d', 14), ('c', 1)]
# [('c', 1), ('b', 52), ('d', 14), ('a', 13)]

# [('c', 1),('d', 14), ('b', 52), ('a', 13)]
# [('c', 1),('a', 13), ('b', 52), ('d', 14)]


input_list = [4, 5, 6, 2, 1, 7, 11]
dict_result={x:x**2 if x%2==0 else x**3 for x in input_list}
print("output dictionary :", dict_result)


input_key = "city"


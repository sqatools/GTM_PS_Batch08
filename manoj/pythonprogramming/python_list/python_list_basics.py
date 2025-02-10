"""
-> List is mutable data type, we update, add, remove value from list
-> List can contain all the typr of data,int,float,string,list,tuple ,dict,bool etc
-> List follows +ve and -be indexing as like string
-> we defined list with square brackets [].
"""

list1 =[4,4.5, 'hello', [2, 4, 5],(2, 7, 2), {'a': 123, 'b': 567},
        True , {4, 6, 8 ,1}]

print(list1, type(list))
# [4, 4.5, 'hello', [2, 4, 5], (2, 7, 2), {'a': 123, 'b': 567}, True, {8, 1, 4, 6}] <class 'type'>




print("_"*50)
#################### apply loop on the list ######
list3 = [5, 7, 2, 8, 11, 44, 77]

for val in list3:
    print(val)
# loop with indexing

for i in range(len(list3)):
    print(i, list3[i])

"""


"""

print("_"*50)
############### slicing in the list ##################

list_a = [5, 7, 2, 8, 11, 7, 22, 88, 3]
print(list_a[3:7])  # [8, 11, 7, 22]
print(list_a[1:6])  # [7, 2, 8, 11, 7]
print(list_a[-5:-1])  # [11, 7, 22 ,88]
print(list_a[-1:-5])  # []
print(list_a[1:8:2])  # [7, 8 , 7 ,88]
print(list_a[-2:-9:-2])  # [88, 7, 8, 7]
print(list_a[-8:-1:1])  # [7, 2, 8, 11, 7, 22, 88]
print(list_a[::-1]) # [3, 88, 22, 7, 11, 8, 2, 7, 5]
# list_a[]-1:-len(list)-1: -1]


print(list_a[::1])  # [5, 7, 2, 8, 11, 7, 22, 88, 3]

list_b = ['a', 'b', 'c', 'd', 'e']
print(list_b[-5:-1:])  # ['a', 'b', 'c', 'd']
print(list_b[-1:-5])  # []

print("_"*50)
########## list methods ########
print(dir(list))

###### add content to the list ########3
print("_"*50)
#########
# append method() : This method add valur to the list at last index
list_c = [54, 7, 2, 5, 7]
list_c.append(400)
list_c.append('hello')
print("list_c:", list_c)
# list_c: [54, 7, 2, 5, 7, 400, 'hello']
print("_"*50)
#############
# insert method() : This method add value to specified index position
list_d = [6, 8, 22, 55, 99, 9]
list_d.insert(2, 900)
print("list_d:", list_d)
# list_d: [6, 8, 900, 22, 55, 99, 9]

list_d.insert(3, 'python')
print("list_d:", list_d)
# list_d: [6, 8, 900, 'python', 22, 55, 99, 9]

list_d.insert(-1, [4, 6, 8])
print("list_d :", list_d)
# list_d : [6, 8, 900, 'python', 22, 55, 99, [4, 6, 8], 9]

print("_"*50)
############
# extend method() : This method help to add one list data to  another list  at end of another
list_p = ['a', 'b', 'c']
list_q = [3, 6, 8, 2]
list_q.extend(list_p)
print("list_q :", list_q)
# list_q : [3, 6, 8, 2, 'a', 'b', 'c']
list_r = [4, 6, 7]
list_r.append(list_p)
print("list_r :", list_r)
# list_r : [4, 6, 7, ['a', 'b', 'c']

list_t = [4, 6, 7, ['a', 'b', 'c', [17, 18, 19]]]
print(list_t[3][1]) # b
print(list_t[3][3][2]) # 19

print("_"*50)

########### replace data in current ########
# we can replace data in the list with help of index position
list_Y = [5, 7, 9, 22, 55]
list_Y[3] = 100

print("list_y :", list_Y)
# list_y : [5, 7, 9, 100, 55]


# replace with help of slicing

list_z = [4, 6, 7, 8, 1, 5]

list_z[1:4] = [100, 200, 300]
print("list_z:", list_z)
# list_z: [4, 100, 200, 300, 1, 5]

list_z[2:3] = [500, 600]
print("list_z:", list_z)
# list_z: [4, 100, 500, 600, 300, 1, 5]

# replace one value with multiple value
list_w = [4, 6, 7, 8, 1, 5]
list_w[2:3] = [500, 600]
print("list_w :", list_w)
# list_w : [4, 6, 500, 600, 8, 1, 5]

# replace multiple value with one value
list_q = [4, 6, 7, 8, 1, 5]
list_q[1:4] =[500]
print("list_q :", list_q)
# list_q : [4, 500, 1, 5]



print("_"*50)



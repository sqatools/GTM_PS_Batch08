#Q3 write a python program to remove all the duplicate value from given dictionary values
dict1 = {'a' : [3, 5, 7, 3, 7, 8],
         'b' : 'Programming',
         'c' : (4, 7, 9, 11, 5, 7, 11, 77, 88, 11),
         'd' : [True, False, True, False]}
dict2={}
for k,v in dict1.items():
    dict2[k]=list(set(v))
print(dict2)



# write a python program to remove all duplicate vowels from given string.
str1 = "Hello we are learning Python"
print(set(str1)) # {'g', ' ', 'o', 'n', 'P', 'H', 't', 'e', 'h', 'a', 'r', 'y', 'w', 'l', 'i'}
vowels = 'aeiou'


output = ''
for char in str1:
    if (char in vowels ) and (char not in output):
        output += char
    elif char not in vowels:
        output += char
    else:
        continue

print("output :", output)
# Hello w ar lrning Pythn

print ("#"*50)
################################################################
#Q2 write a python program to find out the diff, common value between lists
#
l1 = [4, 76, 9, 22, 55, 77, 8]
l2 = [4, 22, 5, 66, 7, 22, 76, 8]

tup_l1 = set(l1)
tup_l2 = set(l2)

diff_output = tup_l1.difference(tup_l2)
print(diff_output) #{9, 77, 55}


comman_val = tup_l1.intersection(tup_l2)
print(comman_val) # {8, 4, 22, 76}


print ("#"*50)
#Q3 write a python program to remove all the duplicate value from given dictionary values

dict1 = {'a' : [3, 5, 7, 3, 7, 8],
         'b' : 'Programming',
         'c' : (4, 7, 9, 11, 5, 7, 11, 77, 88, 11),
         'd' : [True, False, True, False]}

output = {}
for key , value in dict1.items():
    dict1[key] = remove.duplicates(values)
        output = output + dict1[key]
print(output)




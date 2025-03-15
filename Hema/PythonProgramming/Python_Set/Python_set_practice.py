
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

################################################################
#Q2 write a python program to find out the diff, common value between lists
#
l1 = [4, 76, 9, 22, 55, 77, 8]
l2 = [4, 22, 5, 66, 7, 22, 76, 8]

#Q3 write a python program to remove all the duplicate value from given dictionary values

dict1 = {'a' : [3, 5, 7, 3, 7, 8],
         'b' : 'Programming',
         'c' : (4, 7, 9, 11, 5, 7, 11, 77, 88, 11),
         'd' : [True, False, True, False]}
out_var_3 =[]
out_3 =[]
out_var = {}

# for v in dict1.values():
#     out_var_3.append(v)
#     for i in range(len(out_var_3)):
#         for j in range(i+1, len(out_var_3)):
#             #print(out_var_3[i])
#             #print(out_var_3[j])
#             if out_var_3[i][0] not in out_3 :
#                 out_3.append(out_var_3[i])
#             else:
#                 continue

for k,v in dict1.items():
    # for value in v:
        #print(value)
    if type(v) == list:
        for value in range(len(v)):
            #print(value)
            if v[value] not in out_var_3:
                out_var_3.append(v[value])
        out_var[k] = out_var_3

    elif type(v) == str:
        for ch in range(len(v)):
            #print(ch)
            if v[ch] not in out_var_3:
                out_var_3.append(v[ch])
                #print(out_var_3)
        out_var[k]=''.join(out_var_3)


    else:
        out_var_3[k]=v
#print(out_var_3)
#print(out_3)
print(out_var)
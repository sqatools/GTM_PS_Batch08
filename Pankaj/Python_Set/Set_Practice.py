# Write a python program to remove all duplicate vowels from given string
str1 = "Hello we are learning python"
vowels = 'aeiou'
print(set(str1)) # {'t', 'r', 'h', 'H', 'o', 'l', 'g', 'a', 'n', 'p', 'i', 'w', ' ', 'y', 'e'}
output = ''
for char in str1:
    if (char in vowels) and (char not in output):
        output += char
    elif char not in vowels:
        output += char
    else:
        continue
print(output)

# 2. write python program to find out the diff, common value between lists

l1 = [4, 76, 9, 22, 55, 77, 8]
l2 = [4, 22, 5, 66, 7, 22, 76, 8]

# 3. write a python program to remove all the duplicate value from given dictionary values

dict1 = {'a' : [3, 5, 7, 3, 7, 8],
         'b' : 'Programming',
         'c' : (4, 7, 9, 11, 5, 7, 11, 77, 88, 11),
         'd' : [True, False, True, False]}

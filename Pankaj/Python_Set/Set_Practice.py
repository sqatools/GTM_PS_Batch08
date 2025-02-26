# Write a python program to remove all duplicate vowels from given string
str1 = "Hello we are learning python"
vowels = 'aeiou'
print(set(str1))#{'t', 'r', 'h', 'H', 'o', 'l', 'g', 'a', 'n', 'p', 'i', 'w', ' ', 'y', 'e'}
output = ''
for char in str1:
    if (char in vowels) and (char not in output):
        output += char
    elif char not in vowels:
        output += char
    else:
        continue
print(output)

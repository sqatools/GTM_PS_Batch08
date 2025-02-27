str_1 = "Hello we are learning python"
vowels = "aeiouAEIOU"
res = []
for char in str_1:
    if char in vowels:
        res += res
    else:
        res.append(char)

print(res)
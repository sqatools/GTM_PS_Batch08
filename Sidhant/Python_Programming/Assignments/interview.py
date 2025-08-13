# def reverse_str(s):
#     print( s[::-1] )


# inp1 = "Sidhant"
# print(inp1[::-1])

# def even_odd(num):
#     if num % 2 ==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(8))

inp1 = str(input("Enter the string:"))
vowel = "aeiouAEIOU"
count =0
for val in inp1:
    if val  in vowel:
        count +=1
print(count)









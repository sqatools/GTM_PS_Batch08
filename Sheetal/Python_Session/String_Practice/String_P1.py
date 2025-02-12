# Types of Python data types.
# 1. Numbers
#    i). Integer :  Immutable
#    ii). Float : Immutable
#    iii). Complex number  : Immutable
#
# 2. Sequential
#    i). String : Immutable
#    ii). List :  mutable
#    iii). Tuple : Immutable
#
# 3. Dictionary : mutable
# 4. Set : mutable
# 5. Boolean : Immutable
# """
#

### list -> int ### conversion is not possible
### list -> float ### conversion is not possible
### list -> complex ### conversion is not possible
########################### Tuple Data Type Conversion ###################
# tuple -> int # conversion is not possible
# tuple -> float # conversion is not possible
# tuple -> complex # conversion is not possible

import keyword

#Trim left space and right space

w=" Learn Python "
print(w.find("ea"))
print(w.index("ea"))

print(w.lstrip().rstrip())

# Remove duplicates
str3 = "Pramod Hema Kartik Bala Pramod Manoj Hema Kartik"

str3_split = str3.split()
list1 = []

for i in str3_split:
    if i not in list1:
        list1.append(i)
final_list = " ".join(list1)



# Convert list back to string
# result = " ".join(list1)
print(list1)
print(final_list)

print(keyword.kwlist)

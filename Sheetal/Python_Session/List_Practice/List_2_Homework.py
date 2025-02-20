# Program 1:
print("WAP to find the average of the number in the list")
LIST3 = [3,4,6,7,8,9]
sum_val = 0
for val in LIST3:
    sum_val = sum_val + val

print("The average is: ", sum_val/len((LIST3)))

print("_"*40)
# Program 2
print("WAP to find the number from the list which are divisible by 3 and 7")
list_d = [9,42,33,21,28,25,9]
list_new =[]

for val in list_d:
    if val%3 == 0 and val%7 == 0:
        list_new.append(val)

print(list_new)

print("_"*40)
#Program 3:
print("WAP to Remove duplicates from the list  using set method")
list_d = [9,42,33,21,28,25,9]
set_pair = set(list_d)
print(list(set_pair))

#Program 4:
print("WAP to remove duplicates from the string using set method")
str3 = "Pramod Hema Kartik Bala Pramod Manoj Hema Kartik"
set_spair =set(str3.split())
print(" ".join(set_spair))

#Program 5:
print("WAP to move all the +ve number towards left side and all the -ve numbers towards right side in reverse order")
list_b = [4,-6,8,-22,77,-99,22,-13,56]

list_r =[]
list_l = []
for i in list_b:
    if i> 0:
        list_l.append(i)
    else:
        list_r.append(i)

print(sorted((list_l), reverse=True) + sorted((list_r), reverse=True))



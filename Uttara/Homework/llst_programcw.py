
#WAP check values can be divded by 3 and 7
list_d = [9,42,33,21,28,25]
list1 = []
for val in list_d:
    if val % 7 == 0 and val % 3 == 0:
        list1.append(val)
        print("values which is divsble by 3 and 7 :", list1)
# values which is divsble by 3 and 7 : [42, 21]

# 2 .WAP to get avg of all list values without using functon and method
list_c = [55,66,33,22,12]
sum1 = 0
totalnum =0
for number in list_c:
    sum1 =+ number
    totalnum += 1
avg = sum1/totalnum
print("average of numbers:",avg)
# average: 2.4"""


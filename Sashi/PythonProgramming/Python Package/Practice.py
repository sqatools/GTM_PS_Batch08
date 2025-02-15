list_C = [55,63,32,22,12]

print("sum of all values :", sum(list_C)/ len(list_C))


list_1 = [9,42,33,21,28,25]

list_2 = []
for i in list_1:
    if (i % 3 == 0) and (i % 7 == 0):
        list_2.append(i)
    else:
        continue

print(list_2)

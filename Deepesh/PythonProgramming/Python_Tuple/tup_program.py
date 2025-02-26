"""
tup =  (6,7,3)
#tup2 = (a, b, c)
(a,b,c) = tup

print("a: ",a)
print("b: ",b)
print("c: ",c)


p, q, r = (8, 9, 10)
print(p, q, r)


(x, y, z) = [10, 30, 40]
# print(x, y, z)

tup2 = (x, y, z)
print(tup2)
"""
"""
# Q14 : from sqa tools:

tupA = [[('sqa', 4)], [('tools', 8)], [('Python', 9)], [('Python', 11)]]
tupB = (3, 6, 10)
print("Input A : ", tupA)
print("Input B : ", tupB)

output = []
for i in range(len(tupA)):

    l1 = list(tupA[i][0])
    if i < len(tupB):
        l1.append(tupB[i])
    output.append([tuple(l1)])

print(output)
"""

# Q17 : tuple programs from sqa tools:
"""
17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
Input:
[(3,6,7),(7,8,4),(7,3),(3,0,5)]
Output:
[(3,6,7,0,5),(7,8,4,3)]
"""

l1 = [(3, 6, 7), (7, 8, 4), (7, 3), (3, 0, 5)]
output = []

for i in range(len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i][0] == l1[j][0]:
            output.append(tuple(list(l1[i]) + list(l1[j][1:])))
        else:
            continue

print(output)

result = [tuple(list(l1[i]) + list(l1[j][1:])) for i in range(len(l1)) for j in range(i+1, len(l1)) if l1[i][0] == l1[j][0]]

print("result :", result)

########################################
# program to check data type each value
print("_"*50)
list1 = [3, 3.5, 'Hello', [5, 6, 7], (1, 3, 5)]
for val in list1:
    if isinstance(val, int):
        print("data type :int, ", val)
    elif isinstance(val, str):
        print("data type :string, ", val)
    elif isinstance(val, float):
        print("data type :float, ", val)
    elif isinstance(val, list):
        print("data type :list, ", val)
    elif isinstance(val, tuple):
        print("data type :tuple, ", val)


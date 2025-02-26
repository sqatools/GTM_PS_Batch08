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

tupA=[[('sqa',4)],[('tools',8)], [('Python',9)],  [('Python',11)]]
tupB=(3, 6, 10)
print("Input A : ",tupA)
print("Input B : ",tupB)

output = []
for i in range(len(tupA)):

    l1 = list(tupA[i][0])
    if i < len(tupB):
        l1.append(tupB[i])
    output.append([tuple(l1)])

print(output)


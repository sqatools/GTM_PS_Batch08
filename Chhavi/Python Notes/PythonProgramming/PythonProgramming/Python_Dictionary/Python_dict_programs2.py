dict12 = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
dict12_2={}
s2=sorted(dict12.values())
for y in range(len(s2)):
    for x in dict12:
        if dict12[x]==s2[y]:
            dict12_2[x]=dict12[x]

print(dict12_2)
print("_"*100)

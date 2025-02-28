print("15). Python Dictionary program to swap the values of the keys in the dictionary.")
#The solution in website is to switch key and value not below. which is the correct question.
#website output {'yash': 'name', 'pune': 'city'}
# Input = {name:’yash’, city: "pune’}
# Output = {name:’pune’, city: "yash’}

dict15_3={'name':'yash','city':'pune'}
dict16={}
dict16['name']=dict15_3['city']
dict16['city']=dict15_3['name']
print(dict16)

print("12). Python Dictionary program to sort a dictionary in python using values.")
#Website solution not clear. Uses lambada. Please explain

# Input = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
# Output= (c, 1) (a,13) (d, 14) (b, 52)

dict12= {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
l1=[]
for k,v in dict12.items():
    l1.append(v)
l1.sort()
dict12_1={}
for x in l1:
        for k,v in dict12.items():
            if v==x:
                dict12_1.update({k:v})
print(dict12_1)

print("12). Python Dictionary program to sort a dictionary in python using values.")
dict12= {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
l2=[]
dict12_1={}
for k,v in dict12.items():
    l2.append((k,v))
print(dict12)
print(l2)
for x in range(len(l2)):
    for y in range(x+1,len(l2)):
        if l2[y][1]<l2[x][1]:
            a,b=l2.index(l2[x]),l2.index(l2[y])
            l2[a],l2[b]=l2[b],l2[a]
        else:
            continue

dict12_3=dict(l2)
print(dict12_3)






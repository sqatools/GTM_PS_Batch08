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








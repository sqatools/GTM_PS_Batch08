
k=10
list1=[2,8,2,3,1,6,4]
for x in range(0,len(list1)):
    c=0
    l1=[]
    print("x index position:",x,"value:",list1[x])
    for y in range(x,len(list1)):
        print("y index position:", y, "value:", list1[y])
        c=c+list1[y]
        print("counter value:",c)
        if c==k:
            for n in range(x,y+1):
                l1.append(list1[n])
                print(l1)
            if sum(l1)==k and len(l1)!=1:
                print(l1)
            else:
                c=0
                l1=[]
        elif c>k:
            break
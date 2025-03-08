# # k=6
# # list2=[2,3,1,5]
# def consecutive_sum(k,list1):
#     c=0
#     list3=[]
#     for x in range(len(list1)):
#         if c<k:
#             c=c+list1[x]
#             list3.append(list1[x])
#             continue
#         elif c==k:
#             print(list3)
#             list3=[]
#             c=0
#             continue
#         else:
#             list3=[]
#             c=0
#         continue
#
# consecutive_sum(6,[2,3,1,5,1,6,2])

k=6
list1=[2,3,1,2,4,6,7]                #[2,8,2,3,1,6,4]
for x in range(0,len(list1)):
    c=0
    l1=[]
    for y in range(x,len(list1)):
        c=c+list1[y]
        if c==k:
            for n in range(x,y+1):
                l1.append(list1[n])
            if sum(l1)==k and len(l1)!=1:
                print(l1)
            else:
                c=0
                l1=[]

        #      for n in range(x,y):
        #          l1.append(list1[n])
        #      print(l1)
        #      break
        #
        # elif c<k:
        #     c+=list1[y]
        #
        # elif c>k:
        #     c=0
        #     l1=[]
        #     break
        #
        #
        #
        #
        #
        #
        #












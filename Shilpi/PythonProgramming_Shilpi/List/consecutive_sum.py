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

k=10
#list1=[2,3,1,2,4,6,7]                #
list1 = [2,8,2,3,1,6,4]
for x in range(0,len(list1)): #0, 1
    c=0
    l1=[]
    for y in range(x,len(list1)):# 0, 1,2, 3
        c=c+list1[y] #  2, 5, 6, 8
        if c==k: # 2 ==6 | 5 == 6 | 6 == 6 | 8 == 6 |
            #             (x=0, y=2+1)
            for n in range(x,y+1):
                l1.append(list1[n])
            if len(l1)!=1:
                print(l1)  # [2, 3, 1]
            # else:
            #     c=0
            #     l1=[]
        else:
            continue

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












"""
num = 345
#num = 7
reverse = 0

while num > 0: # 34 > 0 | 3 > 0 | 0> 0
    temp = num%10 # 5, 4, 3
    reverse = reverse*10 + temp #| 10*0 + 5 = 5 | 5*10 + 4 = 54| 54*10 = 3 = 543
    num = num//10 # 34 | 3 | 0


print("Reverse :", reverse)

print(-345%10)
"""


num = -345
reverse = 0

# while num < 0:
#     temp = num%10 # 5
#     reverse = reverse*10 + temp # 5
#     num = num//10 #

#print(-345//10)

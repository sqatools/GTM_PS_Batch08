#creating a class
'''


class car:
    def car_name(self):
        return "Tata Nexon"
    def car_colour(self):
        return "grey"
obj = car()
print(obj.car_name())
obj.car_colour()

from Uttara.Homework.SQA_PracticePrograms import password

round1 = input('enter pass or fail')
round2= input('enter pass or fail')
round3= input('enter pass or fail')

if round1 == "pass":
    print("round 1 clear")
    if round2 == "pass":
        print("round 2 cleared")
        if round3 == "pass":
            print("round 3 cleared")
        else:
            print(" 3rnd round not clear")
    else :
        print("round 2 not clered")

else:
    print("round 1 not clear")


A= int(input("enter number"))

if A%2 == 0 :
    print ( " number is even")
    if A <1 :
        print("number greatee than 1 ")
    elif A > 50:
        print('number grater')
else:
    print(" number odd")


fact = 1
num = 3
for i in range(1,4):
    fact = fact* i
print (fact)
'''

char = "o"
letter = 'aissh'

if char in letter:
    print("present ")
else :
    print(" no ")

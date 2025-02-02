#Write a python program to check for the greatest number among 3 numbers
a=90
b=30
c=100
if a>b and a>c:
    print("a is the greatest of all numbers")
elif b>a and b>c:
    print("b is the greatest of all numbers")
elif c>a and c>b:
    print("c is the greatest of all numbers")
else:
    print("None of the numbers is the greatest")
print("_"*100)

#Write a python program to provide the grade to the students as per marks obtained

marks=39

if marks>100 or marks<0:
    print("Invalid Entry")
elif 90<=marks<=100:
    print("A")
elif 80<=marks<90:
    print("B+")
elif 70<=marks<80:
    print("B-")
elif 60<=marks<70:
    print("C+")
elif 50<=marks<60:
    print("C-")
elif 40<=marks<50:
    print("D")
elif 0<=marks<40:
    print("F")
print("_"*100)




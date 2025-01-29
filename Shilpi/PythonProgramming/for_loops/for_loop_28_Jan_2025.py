
#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50
#Q2 write a python print square of even number and cube of odd from 1 to 20

print("Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50")

for i in range(1,51):
    if i%5==0 and i%7==0:
        print(i)
print("_"*100)

print("Q2 write a python print square of even number and cube of odd from 1 to 20")

for i in range(1,21):
    if i%2==0:
        print(i,"^ 2 =",i**2)
    else:
        print(i,"^ 3 =",i**3)

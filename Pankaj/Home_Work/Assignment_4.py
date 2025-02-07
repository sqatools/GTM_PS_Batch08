#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50

print("Values from range which is divisible by 5 :")

for i in range(1, 51, 1):
    if i % 5 == 0:
        print(i, end=" ")

print("_"*70)

#Q2 write a python program to print square of even number and cube of odd from 1 to 20
for i in range(1, 21, 1):
    if i % 2 == 0:
        print("Even Number: ", i, "Square of Even Number :", i**2)
    else:
        print("Odd Number: ", i, "Qube of Even Number :", i**3)
    print()

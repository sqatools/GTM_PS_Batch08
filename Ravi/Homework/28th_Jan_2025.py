#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50

for i in range(1, 51):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
    else:
        continue

print("-"*50)
#Q2 write a python print square of even number and cube of odd from 1 to 20

for j in range(1, 21):
    if j % 2 == 0:
        print("Even_number:"+str(j)+"\t"+"Square"+str(j**2))
    else:
        print("Odd_number:"+str(j)+"\t"+"Cube"+str(j**2))
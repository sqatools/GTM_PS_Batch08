

#1.write a python program to print value which are divisible 5 and 7 from 1 to 50

for i in range(1, 51,1):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")

print("This Value which is divisible by 5 and 7 both")

# output:35 This Value which is divisible by 5 and 7 both
print("_"*150)

#Q2 write a python print square of even number and cube of odd from 1 to 20
#numb = int(input("Enter a Number"))
for numb in range(1,21):
    if numb % 2 == 0:
        print("Number is Even Print Square",numb ** 2)
    else:
        print("Number is Odd Print Cube", numb ** 3)


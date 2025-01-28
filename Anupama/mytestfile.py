print ("*"*10,"Program to print O","*"*10)
for row in range(0, 7):
        for column in range(0, 7):
            if (row == 0 or row == 6) and (1 < column < 5) :
                print("*", end=' ')
            elif (0 < row <= 5) and (column ==1 or column ==5):
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()


#write a program to calculatr the bill amount on basis of units consumed

unit = 155
total_bill=0
if unit<=100:
    total_bill= total_bill+ unit*20
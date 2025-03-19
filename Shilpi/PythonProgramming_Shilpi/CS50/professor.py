import random
rightanswer=0
score=0
num1=0
num2=0
def main():
    level1=get_level()
    generate_integer(level1)


def get_level():
    while True:
        try:
            l1=int(input("Level: "))
            if 1<=l1<=3:
                break
            else:
                continue

        except ValueError:
            continue
    return l1

def generate_integer(level):
    global rightanswer,score,num1,num2
    for x in range(10):
        if level==1:
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            print(num1, "+", num2, "=", end="")
            answer1 = input()
            if answer1.isdigit():
                a=int(answer1)
                if a==num1+num2:
                    score+=1
                    continue
                elif a!=num1+num2:
                    for x in range(2):
                        print("EEE")
                        print(f"{num1} + {num2} = ",end="")
                        answer=input()
                        if answer.isdigit():
                            a=int(answer)
                            if a!=num1+num2 and x!=1:
                                continue
                            elif a!=num1+num2 and x==1:
                                print("EEE")
                                print(f"{num1} + {num2} = {num1+num2}")
                            elif a==num1+num2:
                                break
                        elif answer.isdigit()==False and x!=1:
                            continue
                        elif answer.isdigit()==False and x==1:
                            print("EEE")
                            print(f"{num1} + {num2} = {num1 + num2}")
                            continue

            elif answer1.isdigit()==False:
                for x in range(2):
                    print("EEE")
                    print(f"{num1} + {num2} = ", end="")
                    answer = input()
                    if answer.isdigit():
                        a = int(answer)
                        if a != num1 + num2 and x != 1:
                            continue
                        elif a != num1 + num2 and x == 1:
                            print("EEE")
                            print(f"{num1} + {num2} = {num1 + num2}")
                            continue
                        elif a == num1 + num2:
                            break
                    elif answer.isdigit()==False and x!=1:
                        continue
                    elif answer.isdigit()==False and x==1:
                        print("EEE")
                        print(f"{num1} + {num2} = {num1 + num2}")
                        continue














    print(f"Score: {score}")







                        # else:
                        #     for y in range(3):
                        #         print("EEE")
                        #         print(num1, "+", num2, "=", end="")
                        #         answer1 = input()
                        #         if answer1.isdigit() == True:
                        #             answer1 = int(answer1)
                        #             if answer1 != num1 + num2 and y != 3:
                        #                 continue
                        #             elif answer1 == num1 + num2:
                        #                 break
                        #             elif answer1 != num1 + num2 and y == 3:
                        #                 print(num1, "+", num2, "=", num1 + num2, end="")
                        #         else:
                        #             if y == 3:
                        #                 print("EEE")
                        #                 print(num1, "+", num2, "=", num1 + num2, end="")
                        #                 break


            # else:
            #     for y in range(3):
            #         try:
            #             if answer1 != rightanswer and y == 2:
            #                 print("EEE")
            #                 print(num1, "+", num2, "=", num1 + num2)
            #             if answer1 == rightanswer:
            #                 print(score)
            #                 break
            #             if answer1 != rightanswer and y != 2:
            #                 print("EEE")
            #                 print(num1, "+", num2, "=", end="")
            #                 answer1 = int(input())
            #         except ValueError:
            #             continue




if __name__=="__main__":
    main()






import random
score=0
num1=0
num2=0
def main():
    level1=get_level()
    print(level1)
    generate_integer1(level1)


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

def generate_integer1(level):
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
        elif level==2:
            num1=random.randint(10,99)
            num2=random.randint(10,99)
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

        elif level==3:
            num1=random.randint(100,999)
            num2=random.randint(100,999)
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
        else:
            raise ValueError

    print("Score: ",score)


if __name__=="__main__":
    main()






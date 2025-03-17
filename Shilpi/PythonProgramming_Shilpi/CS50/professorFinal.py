import random
score=0
num1=0
num2=0
def main():
    level1=get_level()
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

def generate_integer(level):
    dict1={1:0,2:10,3:100}
    if 1<=level<=3:
        num3=random.randint(dict1[level],(10**level)-1)
        return num3
    else:
        raise ValueError


def generate_integer1(level):
    global rightanswer,score,num1,num2
    dict1={1:0,2:10,3:100}
    for x in range(10):
        if 1<=level<=3:
            num1=random.randint(dict1[level],(10**level)-1)
            num2=random.randint(dict1[level],(10**level)-1)
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
                                score+=1
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
                            score+=1
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






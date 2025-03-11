import random
answer1,rightanswer,score=0,0,0
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
    global answer1,score
    for x in range(10):
        if level==1:
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            print(num1, "+", num2, "=", end="")
            try:
                answer1 = int(input())
                rightanswer = num1 + num2
            except ValueError:
                print("EEE")
                print(num1, "+", num2, "=", end="")
                answer1 = int(input())
                for y in range(2):
                    try:
                        rightanswer = num1 + num2
                        if answer1 != rightanswer and y == 1:
                            print("EEE")
                            print(num1, "+", num2, "=", num1 + num2)
                        if answer1 == rightanswer:
                            print(score)
                            break
                        if answer1 != rightanswer and y != 1:
                            print("EEE")
                            print(num1, "+", num2, "=", end="")
                            answer1 = int(input())
                    except ValueError:
                        continue

            else:
                for y in range(3):
                    try:
                        if answer1 != rightanswer and y == 2:
                            print("EEE")
                            print(num1, "+", num2, "=", num1 + num2)
                        if answer1 == rightanswer:
                            print(score)
                            break
                        if answer1 != rightanswer and y != 2:
                            print("EEE")
                            print(num1, "+", num2, "=", end="")
                            answer1 = int(input())
                    except ValueError:
                        continue




if __name__=="__main__":
    main()






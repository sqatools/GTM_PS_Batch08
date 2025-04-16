"""print ("*"*10,"Program to print O","*"*10)
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


def num():

    a = 20
    a = a + 10
    print(a)


a = 10
num()
print(a)"""


def find_word(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            longest_word = max(words, key=len)
            return longest_word
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
file_path = 'myfile.txt'
longest_word = find_word(file_path)
print(f"The longest word in the file is: {longest_word}")
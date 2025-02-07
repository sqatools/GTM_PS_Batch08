start_pt = ord('a')

for i in range(1, 8):
    print(" " * (7 - i), end="")  # Print leading spaces

    temp = start_pt + (i - 1)  # Start from the correct letter

    # Print first half (descending order)
    for j in range(i):
        print(chr(temp), end="")
        temp -= 1

    # Print middle character again for mirroring effect
    temp += 1
    print(chr(temp), end="")  # Middle character repeated

    # Print second half (ascending order)
    for j in range(i - 1):
        temp += 1
        print(chr(temp), end="")

    print()  # Move to the next line
    start_pt += 2  # Move starting letter forward

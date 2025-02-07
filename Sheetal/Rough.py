start_pt = ord('a')
end_pt = ord('y')

for i in range(1, 9):
    print(" " * (9 - i) + chr(start_pt) * i)  # Convert ASCII back to character
    start_pt += 1
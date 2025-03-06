
def find_max(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    max_num = numbers[0]  # Assume the first number is the maximum
    for num in numbers:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    return max_num

# Example usage
numbers = [3, 5, 7, 2, 8, -1, 4, 10, 12]
max_number = find_max(numbers)
print(f"The maximum number is: {max_number}")

l1= [1,4,6,10,]
res=1
for val in l1:
    res=res*val
print(res)

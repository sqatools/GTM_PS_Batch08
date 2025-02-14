"""
Python program to find the largest number among three numbers.
"""

test_cases = {
    "all_positive_different": [5, 10, 3],
    "all_negative_different": [-5, -10, -3],
    "mix_positive_negative": [-5, 10, 3],
    "first_largest": [10, 5, 3],
    "second_largest": [5, 10, 3],
    "third_largest": [5, 3, 10],
    "all_equal": [5, 5, 5],
    "first_two_equal_largest": [10, 10, 5],
    "last_two_equal_largest": [5, 10, 10],
    "first_and_last_equal_largest": [10, 5, 10],
    "zero_and_positives": [0, 5, 10],
    "zero_and_negatives": [0, -5, -10],
    "zero_and_mixed": [0, 10, -5],
    "first_zero": [0, 10, 3],
    "second_zero": [5, 0, 3],
    "third_zero": [5, 10, 0],
    "large_numbers": [100000, 99999, 88888],
    "small_numbers": [-100000, -99999, -88888],
    "first_two_equal_smaller": [5, 5, 10],
    "last_two_equal_smaller": [3, 10, 10],
    "first_and_last_equal_smaller": [7, 10, 7],
}

for i in test_cases:
    print("considered test case: "+i+" Values:"+str(test_cases[i]))

    if test_cases[i][0] > test_cases[i][1]:
        if test_cases[i][0] > test_cases[i][2]:
            print("1st number is the greatest of the three numbers")
        elif test_cases[i][0] == test_cases[i][2]:
            print("The 1st and 3rd numbers are equal and greater than 2nd number")
        else:
            print("The 3rd number is greatest")
    elif test_cases[i][0] == test_cases[i][1]:
        if test_cases[i][0] == test_cases[i][2]:
            print("All the three number are equal")
        elif test_cases[i][0] > test_cases[i][2]:
            print("The 1st and 2nd numbers are equal and are greater than 3rd number")
        else:
            print("The 3rd number is the greatest")
    else:
        if test_cases[i][1] > test_cases[i][2]:
            print("The 2nd number is the greatest")
        elif test_cases[i][1] == test_cases[i][2]:
            print("2nd and 3rd numbers are equal and are greater than 1st number")
        else:
            print("The 3rd number is greatest")
    print("-"*50)

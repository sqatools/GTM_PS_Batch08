#### Python Program to find the max value in the list using function #####

def max_value(lst):

    return max(lst)

# Example usage
numbers = [10, 45, 67, 23, 89, 90, 100, 56]
max_value = max_value(numbers)
print("The maximum value in the list is:", max_value)

##### Python Program to return factorial value of number ########

#####python program to calculate the number of consonants in given string using function#

def count_consonants(string):
    vowels = "aeiouAEIOU"
    consonant_count = 0

    for char in string:
        if char.isalpha() and char not in vowels:  # Check if it's a letter and not a vowel
            consonant_count += 1

    return consonant_count

# Example usage
text = input("Enter a string: ")
print(f"Number of consonants in the given string: {count_consonants(text)}")
#string concatination
#\t for adding tab and \n for adding a newline
# add 'r' before the string and double quote, then string converts to raw string



# string slicing
"""rules 1 str[start index:end index}
 in above rule string includes start index value nd exclude end index value
 output will always consider string value from left ro right
 it contains both positive and negative index values""
 """
str_a ="programming"
print(str_a[2:7])#ogram
print(str_a[0:9]) #programmi

print(str_a[2:-2])
print(str_a[1:-1])

str3= "good morning"
print(str3[-8: 12])
print(str3[-12: -8])

str4="learning Python"
""" 
1 read learning
2 read only first and last character
3 read all characters except first and last and repeat 2wice
4 get this output "LLLearning Pythonnn"""

#****program to  make a string pyramid***
s = "apple"
n = len(s)
print(len(s))
    for i in range(n):
        # Print leading spaces
        for j in range(n- i- 1):
            print(" ", end="")
        # Print the string characters
        for j in range(2 * i + 1):
            print(s[j % n], end="")
        # Move to the next line
        print()


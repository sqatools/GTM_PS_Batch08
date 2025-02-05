#4th Feb 2025

# Home work for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""
'''
 0   1   2   3   4   5   6   7  8   9  10  11  12  13  14 
 L   e   a   r   n   i   n   g      p  y   t    h   o   n
-15 -14 -13 -12 -11 -10 -9  -8 -7  -6 -5  -4   -3  -2  -1
'''
print("#"*50)
print("Given string: ", str4)
print("1. read only 'Learning'")
print("Output using string concatenation")
positive_positive_read = str4[0:8]
print("Output read only 'Learning' with +ve to +ve slicing: " + positive_positive_read)
positive_negative_read = str4[0:-7]
print("Output read only 'Learning' with +ve to -ve slicing: " + positive_negative_read)
negative_positive_read = str4[-15:8]
print("Output read only 'Learning' with -ve to +ve slicing: " + negative_positive_read)
negative_negative_read = str4[-15:-7]
print("Output read only 'Learning' with -ve to -ve slicing: " + negative_negative_read)

print("#"*50)
print("Output using f-string formating")
print(f"Output read only 'Learning' with +ve to +ve slicing: {positive_positive_read}")
print(f"Output read only 'Learning' with +ve to -ve slicing: {positive_negative_read} ")
print(f"Output read only 'Learning' with -ve to +ve slicing: {negative_positive_read}" )
print(f"Output read only 'Learning' with -ve to -ve slicing: {negative_negative_read}")

print("#"*50)
print("Output using string format method")
print("Output read only {} with +ve to +ve slicing: {}".format('Learning',positive_positive_read))
print("Output read only {} with +ve to -ve slicing: {} ".format('Learning',positive_negative_read))
print("Output read only 'Learning' with -ve to +ve slicing: {}".format('Learning',negative_positive_read) )
print("Output read only 'Learning' with -ve to -ve slicing: {}".format('Learning',negative_negative_read))

print("#"*50)
print("2. read only First and last character :  Ln")
print("Output using String Concatenation")
positive_first_positive_last = str4[0]+str4[14]
print("Output  with +ve to +ve slicing: " + positive_first_positive_last)
positive_first_negative_last = str4[0]+str4[-1]
print("Output with +ve to -ve slicing: " + positive_first_negative_last)
negative_first_positive_last = str4[-15]+str4[14]
print("Output  with -ve to +ve slicing: " + negative_first_positive_last)
negative_first_negative_last = str4[-15]+str4[-1]
print("Output  with -ve to -ve slicing: " + negative_first_negative_last)
print("#"*50)
print("Output using  f-string Formatting")
positive = str4[0]
positive2 = str4[14]
print(f"Output  with +ve {positive} to +ve {positive2} slicing: {positive+positive2}")
print(f"Output with +ve {str4[0]} to -ve {str4[-1]} slicing: {positive_first_negative_last}")
print(f"Output  with -ve to +ve slicing: {negative_first_positive_last}")
print(f"Output  with -ve to -ve slicing: {negative_first_negative_last}")

print("#"*50)
print("3. read all characters except first and last and repeat 2 times the output.'earning Pythoearning Pytho'")
print("Output using string concatenatiom")
positive_positive_multi = 2*(str4[1:14])
print("Output with +ve to +ve slicing: " + positive_positive_multi)
positive_negative_multi = 2*(str4[1:-1])
print("Output with +ve to -ve slicing: " + positive_negative_multi)
negative_positive_multi = 2*(str4[-14:14])
print("Output  with -ve to +ve slicing: " + negative_positive_multi)
negative_negative_multi = 2*(str4[-14:-1])
print("Output  with -ve to -ve slicing: " + negative_negative_multi)
print("#"*50)
print("Output using  f-string Formatting")
positive_except_first_postive_last = (str4[1:14]+str4[1:14])
print(f"Output  with +ve to +ve slicing: {positive_except_first_postive_last}")
positive_except_first_negative_last = (str4[1:-1]+str4[1:-1])
print(f"Output with +ve to -ve slicing: {positive_except_first_negative_last}")
negative_except_first_positive_last = (str4[-14:14]+str4[-14:14])
print(f"Output  with -ve to +ve slicing: {negative_except_first_positive_last}")
negative_except_first_negative_last = (str4[-14:-1]+str4[-14:-1])
print(f"Output  with -ve to -ve slicing: {negative_except_first_negative_last}")

print("#"*50)
print("4. get given output  : 'LLLearning Pythonnn'")
print("Output using string concatenation")
positive_positive_output = 2*(str4[0])+str4[0:15]+2*(str4[14])
print("Output with +ve to +ve slicing: " + positive_positive_output)
positive_negative_output = 2*(str4[0])+str4[0:]+2*(str4[-1])
print("Output with +ve to -ve slicing: " + positive_negative_output)
negative_positive_output = 2*(str4[-15])+str4[-15:14]+2*(str4[14])
print("Output  with -ve to +ve slicing: " + negative_positive_output)
negative_negative_output = 2*(str4[-15])+str4[-15:-1]+2*(str4[-1])
print("Output  with -ve to -ve slicing: " + negative_negative_output)
print("#"*50)
print("Output using  f-string Formatting")

print(f"Output  with +ve to +ve slicing: {positive_positive_output}")
print(f"Output with +ve to -ve slicing: {positive_negative_output}")
print(f"Output  with -ve to +ve slicing: {negative_positive_output}")
print(f"Output  with -ve to -ve slicing: {negative_negative_output}")

print("#"*50)
print("Output using  format string method")

print("Output  with +ve to +ve slicing: {}".format(positive_positive_output))
print("Output with +ve to -ve slicing: {}".format(positive_negative_output))
print("Output  with -ve to +ve slicing: {}".format(negative_positive_output))
print("Output  with -ve to -ve slicing: {}".format(negative_negative_output))

print("#"*50)
print("Output using  raw string ")

print(rf"Output  with +ve to +ve slicing: {positive_positive_output}")
print(r"Output with +ve to -ve slicing: {}".format(positive_negative_output))
print(rf"Output  with -ve to +ve slicing: {negative_positive_output}")
print(r"Output  with -ve to -ve slicing: {}".format(negative_negative_output))
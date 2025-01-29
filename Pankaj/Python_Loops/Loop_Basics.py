"""
for cond:
    code

"""

# range (start,stop,difference)
# when we run loop with range, then it include the start value and exclude stop value
print("_*60")
for i in range(1, 10, 2):  # range is class
    print(i)
print("_*60")
# range with two parameter (start,stop), default value will be 1 if not defined
for j in range(2, 7):
    print(j)

print("_*60")
# Reverse order
for x in range(-20, -10):
    print(x, end=" ")  # for printing in horizontal line

print("_*60")
# range with single value (by default it will start from 0 till range with difference 1)

for y in range(10):
    print(y)
for q in (1, 20, 2):
    print(q, q*q*q)
# Note: range (start, stop, step)
# Note: range() can not generate sequence of float
"""
range class rules
-> range accepts three parameters range(start,stop,step)
-> range o/p include start value and exclude value
-> if we don't define the initial value and step value the, 
   default initial value will be zero(0)
   default step value will be 1
->range (30)-> range (0,30,1)
-> range accept only int
-> if we define twp parameter then it will consider start and stop, default step will be 1
-> range (2, 10)-> start=2, stop=10, step=1
"""
###########
# apply if condition in the loop
print("_"*60)
# write a pro to get all the number which are divisible by 7 from 1 to 50
for i in range(1, 50):
    if i % 7 == 0:
        print(i, end=" ")



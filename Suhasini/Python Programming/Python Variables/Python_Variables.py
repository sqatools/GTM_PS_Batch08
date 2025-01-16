a=10
# a is a variable, = is assignment operator and 10 is value

print("Value of a =", a)   #Output : Value of a = 10
print("Address of a =",id(a))   #Address of a = 4320078720

b = 20
print(b, id(b))   #20 4333137088

# Note: every different variable holding different value will have different addresses

#### Two variables with same value ####

x = 40
y = 40
print("Value of x = ",x , " and address of x is: ",id(x))
# Value of x =  40  and address of x is:  4333973312
print("Value of y = ",y , " and address of x is: ",id(y))
# Value of y =  40  and address of y is:  4333973312



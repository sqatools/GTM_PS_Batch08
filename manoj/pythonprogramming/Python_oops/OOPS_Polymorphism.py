"""
Polymorphism : In this concept when we defined any single method can perform the multiple parameters
then it is called polymorphism
1. Method overriding : when we have 2 classes and set the inheritance between them,if both the class
                       have some method name with different params, then the child class method will overide
                       the parent class method and child class method  will get priority
2. method overloading : when one class have two methods with same name but different parameters, then it
                        is called method overloading, and python doesn't support method overloading
                        if we define two method with same name, then latest define method will get
                        a priority
3. operator over loading : when one operator [erform multiple task then it is called operator over loading
                          e.g : -> plus(+) operator can add 2 int value, 2 string as well
                                -> star(*)
"""
#parent class
class ABC:
    def greeting(self, n1):
        print(n1)
        print(" Good morning from ABC")


    def get_square(self, num):
        print("square of value :", num**2)

# child class
class XYZ(ABC):

    def greeting(self, n1, n2):
        print(n1, n2)
        print(" good evening from XYZ")


    def get_cube(self, num):
        print("cube of value :", num ** 3)

    # this method will be ignored
    def addition(self, v1, v2):
        print("addition :", v1+v2)


    # This method will be considered
    def addition(self, p1, p2, p3):
        print("addition :", p1+p2+p3)

obj = XYZ()
obj.greeting(20, 40)
obj.get_square(20)

obj.addition(40, 50, 60)



######## operator overloading #####
num1 = 100
num2 = 500

print(" add numbers :", num1 + num2)  # 600
print(" add numbers :", num1.__add__(num2))  # 600
print(dir(int))

s1 = "Help"
s2 = "me"

print(" add words :", s1+s2)  # # Helpme
print(" add words :", s1.__add__(s2))   # Helpme
print(dir(str))

l1 = [3, 5, 7]
l2 = ['a', 'b', 'c']
print(" add list values :", l1+l2) # [3, 5, 7, 'a', 'b', 'c']
print("add list values :", l1.__add__(l2))  # [3, 5, 7, 'a', 'b', 'c']

p1 = 60
p2 = 50
print("multiplication :", p1*p2)
print("multiplication :", p1.__mul__(p2))  # 3000

q1 = 10
q2 = 90
print("compare value :", q1 == q2)
print("compare value :", q1.__eq__(q2))
print(q1.__sub__(q2))  # -80
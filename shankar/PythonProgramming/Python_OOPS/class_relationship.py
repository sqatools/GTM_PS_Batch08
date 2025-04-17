class A:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


    def show_v1_value(self):
        print("value of v1 :", self.v1)
        self.v2.greeting_from_B()


class B:

    def greeting_from_B(self):
        print("Good Morning from B")



obj_b = B()
a_obj = A(100, obj_b)
a_obj.show_v1_value()

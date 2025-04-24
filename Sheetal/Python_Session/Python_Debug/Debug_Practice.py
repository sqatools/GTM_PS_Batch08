import pdb

class Addition:
    def add_two_num(self,num1,num2):
        pdb.set_trace()
        self.n01 = num1
        self.n02 = num2

        sum = num1 + num2

        return sum

Add = Addition()
Add.add_two_num(23,"String")

from abc import abstractmethod

# abstraction : when we show the overview information about the method in parent class and implement that
#               method in child  class, then it is called abstract method.
#

str1 = "Hello"
str1.upper()

class Animal:
    def name(self):
        """This method will return the name of the animal"""
        pass

    @abstractmethod
    def voice(self):
        """This method will return the voice of the animal"""
        pass

    @abstractmethod
    def breed(self):
        """This method will return the breed of the animal"""
        pass



class Dog(Animal):

    def name(self):
        print("This is Pet Dog and name is Tommy")


    def voice(self):
        print("Barking")


    def breed(self):
        print("German")


class Lion(Animal):
    def name(self):
        print("African LION")


    def voice(self):
        print("Roar")


    def breed(self):
        print("White LION")


obj= Dog()
obj.name() # This is Pet Dog and name is Tommy

obj2 = Lion()
obj2.voice() # Roar


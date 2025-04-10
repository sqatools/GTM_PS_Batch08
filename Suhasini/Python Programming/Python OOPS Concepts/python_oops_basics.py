"""
1. Class : class is nothing but the blueprint of the object where we defined all the feature and
        attribute/methods for the object.

2. Object : Object is an entity through which we can access all the property/attribute defined in the class.
         ->  We can create n number of objects for one class.
         ->  We can access all method/variable with any of the object of the class.

3. Method : When we define any function inside the class it becomes method with self as its first parameter
            1. Instance Method : When we define any with self as first parameter, then
                                    it is called Instance Method
            2. Class Method
            3. Static Method

4.Variables : 1. Instance variable: instance variable is that we declare with self keyword inside
                constructor, we can access the instance variable anywhere in the class.
                ->  we can call instance variable inside any method as well, but to initiate
                    that variable we have to call method.

                ->  Instance variable value can be changed while creating the variable.
                ->  Instance variable value can be changed outside the class with the help of
                    setter(__setattr__) and getter (__getattribute__)

              2. class variable: The variable that we declare on class level and has to be assigned initial value.

                ->  Can not change the value of class variable while creating the object.
                ->  can not change the class variable value with the help of class object
                ->  We can change the class variable value with the class name only
                    className.variable_name = new_value

5.Constructor : Constructor which initialize the memory for the object of the class being created.
              we define the constructor with __init__ name
              ->  Constructor initialize automatically whenever will create a object of the class
                  no need to call the constructor.

              There are 2 types of constructor
              1.  Default constructor/: Default constructor being called internally whenever we create an object of the class.
              2.  Parametrize constructor : parametrize constructor accept the parameter and we can provide
                  values to the parameters during while creating the object of the class


"""
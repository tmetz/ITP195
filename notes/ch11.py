class Student(object):  # What goes in the parens is all the classes your class inherits (e.g. Python's object) [parent objects]
    def __init__(self, first='', last='', id=0):
        self.first_name_str = "test"

# Usually class names start with a capital letter
# All Python data types are classes

# polymorphism allows one message to be sent to any object and it responds
# appropriately based on the type of object it is
# polymorphism -> + sign is used to add integers but also to concatenate strings

# Each class has 1. Fields and 2. Methods.  Both are attributes.

# The dir() function lists all the attributes of a class, including all that it inherits

class MyClass(object):
    def __init__(self, last, first):
        self.last_name = last
        self.first_name = first
    def pretty_print(self):
        print("My name is {} {}".format(self.first_name, self.last_name))

my_obj = MyClass("Metz", "Tammy")  # <-- constructor is MyClass("Metz", "Tammy")
MyClass.my_attrib = "Hello"  #  You can do this too!!!
print(dir(my_obj))

my_obj.pretty_print()
print(my_obj.__class__) # my_obj is an instance-of the MyClass class
print(my_obj.__dict__) # the namespace
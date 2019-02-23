# updated description 2-22-19
# instance-of (for instances of a class)
# is-a (for inheritance from a parent class) -> class hierachy
# superclass > subclass


# class MyClass(object):
#     pass
#
# class MyChildClass(MyClass):
#     pass
#
# my_child_instance = MyChildClass()
# my_class_instance = MyClass()
#
# print(MyChildClass.__bases__)
# print(MyClass.__bases__)
# print(object.__bases__)
#
# print(my_child_instance.__class__)
# print(type(my_child_instance))

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)  # You have to call the init method of the superclass
        self.staffnumber = staffnum

    def get_employee(self):
        return self.name() + ", " + self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")
z = Employee(x.firstname, x.lastname, "666")

print(x.name())
print(y.get_employee())
print(z.get_employee())

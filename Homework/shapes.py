"""
Tammy Metz
Homework due 4-18-18

Create a Shape superclass, a Rectangle class that inherits Shape, and
a Square class that inherits Rectangle
"""


class Shape (object):
    def __init__(self, shape_name):
        self.name = shape_name

    def __str__(self):
        return "Shape: {}".format(self.name)


class Rectangle(Shape):
    def __init__(self, shape_name, length, width):
        Shape.__init__(self, shape_name)
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2* self.length + 2 * self.width

    def get_area(self):
        return self.length * self.width

    def __str__(self):
        return_str = "Shape: {}\n".format(self.name)
        return_str += "{} (height = {}, width = {})\n".format(self.name, self.length, self.width)
        return_str += "Perimeter: {}\n".format(self.get_perimeter())
        return_str += "Area: {}\n\n".format(self.get_area())
        return return_str


class Square(Rectangle):
    def __init__(self, shape_name, side):
        Rectangle.__init__(self, shape_name, side, side)
        self.side = side

    def get_perimeter(self):
        return 4 * self.side

    def get_area(self):
        return self.side * self.side

    def __str__(self):
        return_str = "Shape: {}\n".format(self.name)
        return_str += "{} (side = {})\n".format(self.name, self.side)
        return_str += "Perimeter: {}\n".format(self.get_perimeter())
        return_str += "Area: {}".format(self.get_area())
        return return_str


def main():
    rect1 = Rectangle("Rectangle", 6, 8)
    print(rect1)
    sq1 = Square("Square", 5)
    print(sq1)
    print("Superclass of Shape is {}".format(Shape.__bases__))
    print("Superclass of Rectangle is {}".format(Rectangle.__bases__))
    print("The class for rectangle object (rect1) is {}".format(rect1.__class__))
    print("The type for rectangle object (rect1) is {}".format(type(rect1)))

if __name__ == "__main__":
    main()
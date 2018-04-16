

class Shape (object):
    def __init__(self, shape_name):
        self.name = shape_name

    def __str__(self):
        return "Shape: {}".format(self.name)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_perimeter(self):
        pass
    def get_area(self):
        pass
    def __str__(self):
        return_str = "Shape: {}\n".format(self.name)
        return_str += "{} (height = {}, width = {})\n".format(self.name, self.height, self.width)
        return_str += "Perimeter: {}".format(self.get_perimeter())
        return_str += "Area: {}".format(self.get_area())
        return return_str

def main ():
    rect1 = Rectangle(6, 8)
    print(rect1)

if __name__ == "__main__":
    main()
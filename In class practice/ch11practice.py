import math

class Point(object):
    def __init__(self, x_param = 0.0, y_param = 0.0):
        self.x = x_param
        self.y = y_param

    def distance(self, param_pt):
        x_diff = self.x - param_pt.x
        y_diff = self.y - param_pt.y
        return math.sqrt(x_diff**2 + y_diff**2)

    def sum(self, param_pt):
        return Point(self.x + param_pt.x, self.y + param_pt.y)

    def __str__(self):
        return("({:.2f}, {:.2f})".format(self.x, self.y))

def main():
    pt1_inst = Point(5.0, 9.0)
    pt2_inst = Point(3.0, 3.0)
    print(pt1_inst)
    print(pt2_inst)

    print("Sum: ", pt1_inst.sum(pt2_inst))
    print("Distance: {:.4f}".format(pt1_inst.distance(pt2_inst)))

if __name__ == "__main__":
    main()
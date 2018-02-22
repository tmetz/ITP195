"""
Tammy Metz
2-21-18

This program contains 6 math functions for various geometry calculations involving area, perimeter, and volume.

Requirements for the functions:
	Each function should accept input parameter(s) from the calling code.
	Each function should return the answer.
	The functions should not contain any print or input statements.

"""

import math # Need this to use pi

def rectangle_perimeter(height, width): # returns the perimeter of a rectangle
    return 2*(height+width)

def circle_perimeter(radius): # returns the circumference of a circle
    return 2*math.pi*radius

def rectangle_area(height, width): # returns the area of a rectangle
    return height*width

def circle_area(radius): # returns the area of a circle
    return math.pi*radius**2

def cube_volume(side): # returns the volume of a cube
    return side**3

def cylinder_volume(radius, height): # returns the volume of a cylinder
    return math.pi*height*radius**2

print("Welcome to the math functions program!")

print("\nNow computing rectangle perimeter")
height = int(input("Enter height: "))
width = int(input("Enter width: "))
print ("The rectangle perimeter is", format(rectangle_perimeter(height, width),'.2f'))

print("\nNow computing circumference [circle perimeter]")
radius = int(input("Enter radius: "))
print ("The circumference [circle perimeter] is", format(circle_perimeter(radius),'.2f'))

print("\nNow computing rectangle area")
height = int(input("Enter height: "))
width = int(input("Enter width: "))
print ("The rectangle area is", format(rectangle_area(height, width),'.2f'))

print("\nNow computing circle area")
radius = int(input("Enter radius: "))
print ("The circle area is", format(circle_area(radius),'.2f'))

print("\nNow computing cube volume")
height = int(input("Enter side length: "))
print ("The cube volume is", format(cube_volume(height),'.2f'))

print("\nNow computing cylinder volume")
radius = int(input("Enter radius: "))
height = int(input("Enter height: "))
print ("The cylinder volume] is", format(cylinder_volume(radius, height),'.2f'))
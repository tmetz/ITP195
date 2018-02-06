# print("Hello, World")
#
# for x in range(20):
#     print(x)

# Statements - has a consequence/modifies something.  Commands, don't return any value.
#
# Expressions return a value (by performing an operation)
#
# Expressions can act as statements, but not the reverse
#
# namespace -> For variables: the table that contains the association of a name with a value


import math
import os

os.system('cls')

radius_str = input ("Enter radius: ")
radius_int = int(radius_str)

circumference = 2*math.pi*radius_int
area = math.pi*radius_int**2

print ("The circumference:", circumference, "\nThe area:", area)

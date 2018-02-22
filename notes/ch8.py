"""


def testfn (x,y):
    print(id(x))
    x = 5
    print(id(x)) # different b/c int is immutable, so assignment creates whole new object

a = 7
b = 8
print(id(a))
testfn(a,b)
print(a,b)


def testfn2 (i):
    print(i)
    i[1] = 999 # lists are mutable, so will also change argument my_list!!!!!
    print(i)

my_list = [6, 8, 2]
print(my_list)
testfn2(my_list)
print (my_list) # Has been changed!
# Assignment is not a change; will create a new obj.  Must use a list method or individual element assign.

"""

"""
def my_func():
    print(my_str)

my_str = "This works!"
my_func()
"""

"""
def my_func():
    my_str = "Something else"
    print(my_str)

my_str = "This works!"
my_func()
"""

"""
# This will throw an error about referencing variable before assignment!
def my_func():
    print(my_str)
    my_str = "Something else"
    print(my_str)

my_str = "This works!"
my_func()
"""

"""
def my_func():
    global my_str
    print(my_str)
    my_str = "Something else"
    print(my_str)

my_str = "This works!"
my_func()
print(my_str)
"""

"""
def foo(x,y):
    global a
    a = 42
    x,y=y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)

a,b,x,y = 1,15,3,4
foo(17,4)
print(a,b,x,y)
"""

# You can have default parameters so if the caller does not provide a value,
# the default is the parameter assigned value

"""
def box(height=10,width=10,depth=10,color="blue"):
    print (height*width*depth)
    print(color)

glob_h = 5
box() # uses all default arguments
box(glob_h) # glob_h will be mapped to height, and defaults used for all other arguments
box(color="red", width=30, height=25) # if you name the parameters you don't have to match the order!!!

def my_fun(a,b):
    print("a is {} and b is {}".format(a,b))

my_fun(b=1, a=2) #named parameters
"""

"""
def fn1 (arg1=[], arg2=27):
    arg1.append(arg2)
    return arg1

# Crazy things happen when you use mutables as arguments, or at least named parameters
my_list = [1, 2, 3]
print(fn1(my_list,4)) # prints [1, 2, 3, 4]
print(fn1(my_list)) # prints [1, 2, 3, 4, 27]
print(fn1()) #prints [27]
print(fn1()) #prints [27, 27]
"""

def my_func (param1 : int, param2 : float) -> None :
    """Sample docstring.  This should provide information
    about what this function does"""
    print("Result is ",param1, param2)
my_func(1, 2.0)

print(dir(my_func)) # shows all info you can get, including docstring, annotations, etc.
print(my_func.__annotations__) # what we did in the function declaration above
print(my_func.__doc__)


def arb_arg_func(fixed_param, *my_tup): # tuples use one *, dictionaries use two **
    print(fixed_param)
    print(my_tup)

arb_arg_func(1, 2, 3, 4)
arb_arg_func(1, 2, 3, 4, 5, 6)
arb_arg_func(1)
arb_arg_func(fixed_param=4)

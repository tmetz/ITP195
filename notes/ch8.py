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
"""
ITP 195 - Lab Assignment 7 - Lists

This program does several manipulations to a list
"""

my_list = []
num_elements = int(input("How many numbers do you want to enter? "))

# Populate the list from user input:
for i in range(num_elements):
    next_num = int(input("Enter a number: "))
    my_list.append(next_num)

print(my_list)
print(type(my_list))

# Print each list item and its type:
for elem in my_list:
    print(elem)
    print(type(elem))

search_for = int(input("Enter a number to search for: "))

if search_for in my_list:
    print("Your number {} was found".format(search_for))
else:
    print("Your number {} was not found".format(search_for))

print("Now updating element 0 to be the value of 100 . . .")
my_list[0] = 100
print(my_list)

print("Now appending value of 200 . . .")
my_list.append(200)
print(my_list)

print("Now inserting 5 before index 0 . . .")
my_list.insert(0,5)
print(my_list)

print("Now deleting element 0 . . .")
my_list.pop(0)
print(my_list)

print("The sum is ", sum(my_list))
print("The length is ", len(my_list))
print("The min is ", min(my_list))
print("The max is ", max(my_list))
import math
import string

#my_utf = ord("h") # Returns integer (ordinal) UTF-8 value of char
#my_utf_ch = chr(121) # Returns UTF-8 char
#print(my_utf, my_utf_ch)
my_str = "This is a test of a string"
#print(my_str[:8]) # Print from beginning to 7th char.  Does not print the 8th character!!!

# Extended slicing:
# [start:finish:countBy]

#print(my_str[0:11:2]) # prints every other letter (count by 2)

# reversing a string:

reverse_my_str = my_str[::-1]
#print(reverse_my_str)

#print(my_str*5)

#print(my_str.upper().find('S')) # chaining

#my_str = my_str.upper()
#print(my_str)
# print("TEST" in my_str)
# print(len(my_str))
# print(my_str.find('T')) # Assume start looking from 0
# print(my_str.find('T',11)) # Start looking from character 11
#
# # Nested methods:
# print(my_str.find('T', my_str.find('T')+1)) # Find the second 'T'
#print("This is a {:_>15} test of {}".format("not", "something cool."))
# for i in range(5):
#     print("{:10d} --> {:4d}".format(i,i**2))
#
# print("Pi is {:.10f}".format(math.pi)) # pi to 10 decimal places

# river = "Mississippi"
# target = input("Input a character to find: ")
# for index in range(len(river)):
#     if river[index].lower() == target.lower():
#         print("Letter \"{}\" found at index: {}".format(target, index))
#         break
# else:
#     print("Letter \"{}\" not found in \"{}\"".format(target, river))


# river = "Mississippi"
# target = input("Input a character to find: ")
# for index,letter in enumerate(river):
#     if letter.lower() == target.lower():
#         print("Letter \"{}\" found at index: {}".format(target, index))
#         break
# else:
#     print("Letter \"{}\" not found in \"{}\"".format(target, river))

new_str = "This is a test string to split"
new_list = new_str.split(" ")
print(new_list)

name_str = "Tamara Leah Metz"
first_name, middle_name, last_name = name_str.split(" ")
print(middle_name)

pal_str = "Madam, I'm Adam"
modified_str = pal_str.lower()

bad_chars = string.whitespace + string.punctuation

for char in modified_str:
    if char in bad_chars:
        modified_str = modified_str.replace(char,"")

if modified_str == modified_str[::-1]:
    print(\
        "The original string is {}\n")

# Need to finish copying this!!!!!

"""
This lab is to try out various string operations and methods.
"""

#2 - ask for string, then iterate through each character using a []
# to access each character, printing all
my_str = input("Please enter a string: \n")
for i in range(len(my_str)):
    print(my_str[i], end=" ")

#3 - ask for string, replicate it, print length of new string,
# change to all upper case
my_str2 = input("\nPlease enter another stirng: \n")
repl_str =  my_str2*4
print(repl_str)
print("The length of the new string is", len(repl_str))
repl_str_upper = repl_str.upper()
print(repl_str_upper)

#4 - split string by spaces and assign to variables
my_str3 = input("\nPlease enter another string that is 3 words separated by spaces (e.g. Tamara Leah Metz)\n")
str_list = my_str3.split()
first, middle, last = str_list[0], str_list[1], str_list[2]
print ("First: ", first)
print ("Middle: ", middle)
print ("Last: ", last)
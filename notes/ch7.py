# list_1 = [4, 7, 2, -9, 6]
# list_2 = [1, 2, 3, 4, 5, 6]
# big_list = list_1 + list_2
# print(big_list)
# print(len(big_list))

# Methods come with the object.  It is a function called in a special way, the dot call.
# e.g. my_str.replace() is a method.  my_list.append() is a method.

# my_str = "Tammy is cool"
# new_str = my_str.replace('m','z')
# print (my_str, "\n", new_str)

# List methods: .reverse(), .sort(), .append(), .pop(), .insert(), .extend()
# .remove() <--- .remove(x) would remove the first element whose value is x
# .insert(5, "a") would insert "a" before element 5

# Lists have a built-in .sort() method, but not strings -- so split string to list first

# name_list = new_str.split() #split into list
# print(name_list)
# name_list.insert(2,"yo")
# print(name_list)
# final_str = ' '.join(name_list) #join back to string
# print(final_str)
#
#
# sort_list = sorted("I like to put things in alphabetical order")
# print(sort_list)
#
#
#
# def are_anagrams(word1, word2):
#     """Return true if words are anagrams"""
#     print("Word 1: ",word1)
#     print("Word 2: ",word2)
#     print("Anagrams? ", end="")
#     word1_sorted = sorted(word1) # returns sorted list from the string
#     word2_sorted = sorted(word2)
#     if word1_sorted == word2_sorted:
#         return True
#     else:
#         return False
#
# print(are_anagrams("Tammy", "Rachel"))
# print(are_anagrams("Tammy", "ymTam"))


list_a = [1, 5, 7]
list_b = list_a # list_b is a pointer to list_a and changes when list_a changes
list_c = list_a[:] # list_c is a copy and will change if there was a pointer that changes
# using [:] makes a copy, which is different from assignment!!!!!!!
list_a.append(56)
print(list_a, list_b, list_c)

# SHALLOW COPY - copies references instead of the physical numbers/chars:
a_list = [1,2,3]
b_list = [5,6,7]
a_list.append(b_list)
# a_list is [1,2,3,[5,6,7]]
c_list = b_list
c_list[2] = 88
# now a_list is [1,2,3,[5,6,88]]
# c_list is [5, 6, 88]


# DEEP COPY - copy of the physical numbers/chars - no pointers:
a_list = [1,2,3]
b_list = [5,6,7]
a_list.append(b_list)
# a_list is [1,2,3,[5,6,7]]
import copy
c_list = copy.deepcopy(b_list)
# c_list is [5, 6, 7]
b_list[0] = 1000
# now a_list is [1, 2, 3, [1000, 6, 7]]
# c_list is [5, 6, 7]


# tuples are lists that are immutable
# Use them if you don't want the program modifying things
# Or if you want the size to stay the same, e.g. RGB colors
my_tup = (6, 7, 8)
# you can even forget the parentheses and just do my_tup = 6, 7, 8


# List comprehension

cool_list = [n**2 for n in range(1,6)]
print(cool_list)


# Multiple collects

more_cool = [x+y for x in range(1,4) for y in range(1,4)]
print(more_cool)
# We just did a nested for loop in 1 line


# Modifying what gets collected in list comprehension

cool_if_list = [my_char for my_char in "Hi There Mom" if my_char.isupper()]
print(cool_if_list)

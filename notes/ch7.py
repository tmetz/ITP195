# list_1 = [4, 7, 2, -9, 6]
# list_2 = [1, 2, 3, 4, 5, 6]
# big_list = list_1 + list_2
# print(big_list)
# print(len(big_list))

# Methods come with the object.  It is a function called in a special way, the dot call.
# e.g. my_str.replace() is a method.  my_list.append() is a method.

my_str = "Tammy is cool"
new_str = my_str.replace('m','z')
print (my_str, "\n", new_str)

# List methods: .reverse(), .sort(), .append(), .pop(), .insert(), .extend()
# .remove() <--- .remove(x) would remove the first element whose value is x
# .insert(5, "a") would insert "a" before element 5

# Lists have a built-in .sort() method, but not strings -- so split string to list first

name_list = new_str.split() #split into list
print(name_list)
name_list.insert(2,"yo")
print(name_list)
final_str = ' '.join(name_list) #join back to string
print(final_str)


sort_list = sorted("I like to put things in alphabetical order")
print(sort_list)



def are_anagrams(word1, word2):
    """Return true if words are anagrams"""
    print("Word 1: ",word1)
    print("Word 2: ",word2)
    print("Anagrams? ", end="")
    word1_sorted = sorted(word1) # returns sorted list from the string
    word2_sorted = sorted(word2)
    if word1_sorted == word2_sorted:
        return True
    else:
        return False

print(are_anagrams("Tammy", "Rachel"))
print(are_anagrams("Tammy", "ymTam"))
"""
Dictionaries, aka associative arrays, associative lists, maps

Dictionaries are stored in a namespace...Python doesn't loop through each value --
it grabs the value it needs from the namespace

key in my_dict

my_dict.clear()

my_dict.update(yourDict) - for each key in yourDict, updates my_dict with
that key/value pair.  Like extend does for lists.

my_dict.copy - shallow copy.  Copies the reference.

my_dict.pop(key)

my_dict.items() - all the key/value pairs
my_dict.keys()
my_dict.values()

"""

"""
contacts = {'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}

print(contacts)
print(contacts['jane'])

contacts['Tammy'] = "555-555-5555"
print(contacts)

contacts.pop("Tammy")
print(contacts)

print("jane" in contacts) # must be the key, not the value
print("352-1234" in contacts)

for key in contacts:
    print (contacts[key])

print("-----")

for i in contacts.values():
    print(i)

"""

"""
#csv.reader takes opened file object and reads one line at a time

import csv
periodic_file = open("PeriodicTable.csv", "r", encoding="windows-1252")
reader = csv.reader(periodic_file)
for row in reader:
    print row

"""

# list is ordered, set is not ordered.  So my_set[5] won't work.
# Set is mutable.  Set is a collection.
# Sets cannot contain duplicate values.

my_set = {'a', 'b', 'c'}
my_set = set('abc') # put any iterable in the parens
print(my_set)
#my_set = set() # empty set

a_set=set("abcd")
b_set = set("cdef")

# Intersection (2 ways):
print(a_set & b_set)
print(b_set.intersection(a_set))


#Difference (2 ways) - NOT commutative!!!:
print(a_set - b_set)
print(a_set.difference(b_set))

print(b_set - a_set)
print(b_set.difference(a_set))


# Union (2 ways):
print(a_set | b_set)
print(b_set.union(a_set))


#symmetric difference - IS COMMUTATIVE
# opposite of intersection - what elements are not in both sets

print(a_set ^ b_set)
print(a_set.symmetric_difference(b_set))

print(b_set ^ a_set)
print(b_set.symmetric_difference(a_set))


# issubset and issuperset
small_set=set("abc")
big_set=set("abcdef")
print(small_set <= big_set)  # True
print(big_set >= small_set)  # True

a_set.add("Tammy") # like .append for lists

# my_set.clear()
# my_set.remove("g")
# my_set.discard("g") If item is not in there, remove throws an error but discard does not

# my_set.copy() # shallow copy
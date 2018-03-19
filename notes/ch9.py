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
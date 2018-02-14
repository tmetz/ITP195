river = "Mississippi"
target = input("Input a character to find: ")

# 1 - Code Listing 4.1:
print("\n----------------------------------------------\n")
print("~~~ Using an index: ~~~")
for index in range(len(river)):
    if river[index] == target:
        print("Letter found at index: ", index)
        break
else:
    print("Letter",target,"not found in",river)


# 2 - use 'for char in':
print("\n----------------------------------------------\n")
print("~~~ Using 'for char in': ~~~")
for char in river:
    if char == target:
        print("Letter found.")
        break
else:
    print("Letter",target,"not found in",river)

# NOTE:
# I followed the exact instructions, but to make the program
# have exactly the same output as the Code Listing 4.1,
# you would need to do the following:
#
# for index,char in enumerate(river):
#     if char == target:
#         print("Letter found at index: ", index)
#         break
# else:
#     print("Letter",target,"not found in",river)

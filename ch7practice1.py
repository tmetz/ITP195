valid_ints = (10, 15, 20, 25)
int_list = []

print("Welcome to my program!")
print("The valid integers to enter are: 10 15 20 25")

continue_loop = "y"

while continue_loop == "y":
    my_int = int(input("Enter an integer: "))
    if my_int in valid_ints:
        int_list.append(my_int)
        print("Valid!  {} has been added to the list.".format(my_int))
    else:
        print("Not Valid!  {} has not been added to the list.".format(my_int))
    continue_loop = input("Do you want to loop again?  y/n: ").lower()

int_list = sorted(int_list)
print("Here is the sorted list:")
print(int_list)
print("The sum of the elements is {}".format(sum(int_list)))
print("The min is {} and the max is {}".format(min(int_list), max(int_list)))

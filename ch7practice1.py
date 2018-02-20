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
print("\nLoop Complete.")
print("The sorted list is: {} ".format(int_list))
print("The sum of the list is: {}".format(sum(int_list)))
print("The min in the list is: {}".format(min(int_list)))
print("The max in the list is: {}".format(max(int_list)))

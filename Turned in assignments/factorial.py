"""
Tammy Metz
ITP 195 - Topics In Python
4-25-18

Non-recursive factorial

Calls the factorial function with user input, then also
loops through the numbers 0 through 5 and calls the
factorial for each of those as well.
"""


def factorial(num):
    my_ans = 1
    for i in range(2, num+1):
        my_ans *= i
    return my_ans


def main():
    try:
        what_int = int(input("What number would you like to calculate the factorial of? "))
        print("The factorial of {} is {}".format(what_int, factorial(what_int)))
    except ValueError:
        print("Sorry, we don't recognize that value.")
    print("Now sending some test data: ")
    for int_to_pass in range(6):
        print("The factorial of {} is {}.".format(int_to_pass, factorial(int_to_pass)))


if __name__ == "__main__":
    main()
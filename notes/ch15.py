"""
Recursion needs:

1. a base case (how it stops or becomes false)
2. a recursive step
"""


def take_step(n):
    if n == 1:
        return "Easy"
    else:
        this_step = "step(" + str(n) + ")"
        previous_steps = take_step(n-1)
        return this_step + " + " + previous_steps

def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def factorial(num): # recursion
    if num == 1:
        return num
    else:
        return num*factorial(num-1)

def factorial_loop(num):
    my_ans = 1
    for i in range(2, num+1):
        my_ans *= i
    return my_ans

def reverser(my_str):
    if len(my_str) == 1:
        return my_str
    else:
        new_str = reverser(my_str[1:]) + my_str[0]
        print("{} + {} is {}".format(my_str[0], my_str[1:], new_str))
        return new_str

#what_number = int(input("enter #: "))
#print(take_step(what_number))
#print(factorial(what_number))
#print(factorial_loop(what_number))
#print(fibo(what_number))

what_string = input("Enter string to reverse: ")
result = reverser(what_string)
print("The reverse of {} is {}".format(what_string, result))
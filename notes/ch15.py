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

def fibonacci(n):
    if n not in fibo_dict:
        fibo_dict[n] = fibonacci(n-1) + fibonacci(n-2)
        print(fibo_dict[n])
    return fibo_dict[n]

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

def factorial2(num):
    indent = 4*(6-num)*" "
    print (indent + "Enter factorial n = ", num)
    if num == 1:
        print(indent + "Base case.")
        return 1
    else:
        print(indent + "Before recursive call factorial(" + str(num-1) + ")")
        rest = factorial2(num-1)
        print(indent + "After recursive call factorial(" + str(num-1) + ") = ", rest)
        return num*rest

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

# what_string = input("Enter string to reverse: ")
# result = reverser(what_string)
# print("The reverse of {} is {}".format(what_string, result))
#x = factorial2(8)


fibo_dict = {}
fibo_dict[0] = 1
fibo_dict[1] = 1

fibo_val = input("Calculate what fibonacci value? ")
print(fibo_dict[0], "\n", fibo_dict[1])
print("Fibonnaci value of ",fibo_val, " is ", fibonacci(int(fibo_val)))
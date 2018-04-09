"""
Tammy Metz
ITP 195 - Topics In Python
HW 4 - due April 9, 2018

Create a python module called "stack" that has methods for popping, pushing, and returning
the top of the stack
"""


class Stack(object):

    def __init__(self, stack_as_list):
        self.stack = stack_as_list

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def top(self):
        return self.stack[-1]

    def push(self, item_to_add):
        self.stack.append(item_to_add)

    def pop(self):
        popped_item = self.stack.pop()
        return (popped_item)

    def __str__(self):
        return_string = ""
        self.stack.reverse() # Reversing order so we can print FILO order
        for item in self.stack:
            return_string = return_string + str(item) + "\n"
        self.stack.reverse() # Put it back in order
        return(return_string)


def main():
    list1 = [9, "Bob", 5.8]
    stack1 = Stack(list1)
    for i in range(10):
        stack1.push("Extra item "+str(i))
    print("")
    print("The top of the stack is {} \n".format(stack1.top()))
    print("Printing the stack object: ")
    print(stack1)
    print("Popping items....")
    while not stack1.is_empty():
        print("Popping {}".format(stack1.pop()))

if __name__ == "__main__":
    main()
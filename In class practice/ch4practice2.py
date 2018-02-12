my_sentinel = 'Y'

print("Loop Variation 1:")
while(my_sentinel == 'Y'):
    fruit = input("Enter 'A' for apple, 'B' for banana, and 'C' for coconut:")
    fruit = fruit.upper()

    if fruit == 'A':
        print("Apple")
    elif fruit == 'B':
        print("Banana")
    elif fruit == 'C':
        print("Coconut")
    else:
        print("No fruit for you")
    my_sentinel = input("Do you want to loop again?  Enter Y or N: ")

print("Loop Variation 2:")
num_times = int(input("How many times would you like to loop?"))
for x in range(num_times):
    fruit = input("Enter 'A' for apple, 'B' for banana, and 'C' for coconut:")
    fruit = fruit.upper()

    if fruit == 'A':
        print("Apple")
    elif fruit == 'B':
        print("Banana")
    elif fruit == 'C':
        print("Coconut")
    else:
        print("No fruit for you")

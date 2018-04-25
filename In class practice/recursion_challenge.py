"""
Tammy Metz
4-25-18
Challenge question: using a recursive function, add the digits of a number.
"""
def sumOfDigits(num):
    if num < 0:
        num = num * -1
    if 0 <= num <= 9:
        return num
    else:
        return (num % 10) + sumOfDigits(int(num/10))


def main():
    try:
        what_num = int(input("What is your number? "))
        print(sumOfDigits(what_num))
    except ValueError:
        print("Sorry, I need an integer.")

if __name__ == "__main__":
    main()
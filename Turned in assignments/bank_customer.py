"""
Tammy Metz
ITP 195 - Python

Bank customer module that has class methods to withdraw, deposit, and determine
how many times a customer has overdrawn their account
"""

class Customer(object):

    def __init__(self, cus_name, cus_balance=0.0, times_overdrawn=0):
        self.name = cus_name
        self.balance = cus_balance
        self.overdrawn = times_overdrawn

    def withdraw(self, with_amt):
        if with_amt > self.balance:
            self.overdrawn += 1
            self.balance -= with_amt
            return self.balance
        else:
            self.balance -= with_amt
            return self.balance

    def deposit(self, dep_amt):
        self.balance += dep_amt
        return self.balance

    def get_overdrawn(self):
        return self.overdrawn

    def __str__(self):
        return "Welcome {}.  Your current balance is {}.  You have overdrawn your account {} times.".format(self.name, self.balance, self.overdrawn)

"""
# Commenting out the main() function I used for testing.
def main():
    cust1 = Customer("Tammy", 105.75, 0)
    print(cust1)
    print("Current balance: {}".format(cust1.withdraw(107.00)))
    print(cust1)
    print("Current balance: {}".format(cust1.deposit(500.00)))
    print(cust1)
    

if __name__ == "__main__":
    main()
"""
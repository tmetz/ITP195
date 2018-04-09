"""
We are going to make a class for rational numbers
"""

def gcd(bigger, smaller):
    print("in gcd")
    if not bigger > smaller:
        bigger, smaller = smaller, bigger
    while smaller != 0:
        remainder = bigger % smaller
        bigger, smaller = smaller, remainder
    return bigger

def lcm(a,b):
    print("in lcm")
    return (a*b) // gcd(a,b)

class Rational(object):
    def __init__(self, numer, denom = 1):
        print("In constructor")
        self.numer = numer
        self.denom = denom

    def __str__(self):
        print ("In str")
        return str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        print("In repr")
        return self.__str__()

    def __add__(self, param_Rational):
        print("In add")
        the_lcm = lcm(self.denom, param_Rational.denom)
        numerator_sum = (the_lcm * self.numer / self.denom) + (the_lcm * param_Rational.numer / param_Rational.denom)
        return Rational(int(numerator_sum), the_lcm)

    def __sub__(self, param_Rational):
        print("In subtract")
        the_lcm = lcm(self.denom, param_Rational.denom)
        numerator_diff = (the_lcm * self.numer / self.denom) - (the_lcm * param_Rational.numer / param_Rational.denom)
        return Rational(int(numerator_diff), the_lcm)

    def reduce_rational(self):
        the_gcd = gcd(self.numer, self.denom)
        return Rational(self.numer // the_gcd, self.denom // the_gcd)

    def __eq__(self, paramRational):
        reduced_self = self.reduce_rational()
        reduced_param = paramRational.reduce_rational()
        return reduced_self.numer == reduced_param.numer and reduced_self.denom == reduced_param.denom

r1 = Rational(5,9)
r2 = Rational(7, 27)
r_sum = r1 + r2
print(r_sum)
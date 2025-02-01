class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        elif isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = denominator
        elif isinstance(numerator, str):
            separated = numerator.split("/")
            if len(separated) != 2 or separated[0].isalpha():
                self.numerator = 0
                self.denominator = 0
            else:
                self.numerator = int(separated[0])
                self.denominator = int(separated[1])
        else:
            self.numerator = 0
            self.denominator = 0

    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        else:
            smaller = 0
            if abs(a) > abs(b):
                smaller = abs(b)
            else:
                smaller = abs(a)
            commonFactors = []
            for number in range(1, smaller+1):
                if a % number == 0 and b % number == 0:
                    commonFactors.append(number)
            commonFactors.sort(reverse=True)
            return commonFactors[0]

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
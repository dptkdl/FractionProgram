class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        elif isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = denominator
        elif isinstance(numerator, str):
            separated = numerator.split("/")
            self.numerator = int(separated[0])
            self.denominator = int(separated[1])

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
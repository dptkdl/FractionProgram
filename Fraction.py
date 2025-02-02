class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        if isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = denominator
        #checks if input is a string
        elif isinstance(numerator, str):
            separated = numerator.split("/")
            #after splitting, string should be a number and list
            #should have length 2
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
        '''
        @fn gcd
        @brief gets the greatest common divisor of two given integers
        '''
        # If any of the parameters is 0, returns 0
        if a == 0 or b == 0:
            return 0
        # If both parameters are valid, identifies which parameter is bigger and which is smaller
        smaller = 0
        if abs(a) > abs(b):
            smaller = abs(b)
        else:
            smaller = abs(a)
        # Creates a list for the common factors of the parameters
        common_factors = []
        # Checks which integers from 1 to the smaller number is a common factor
        # of both parameters and adds that integer to the list
        for number in range(1, smaller+1):
            if a % number == 0 and b % number == 0:
                common_factors.append(number)
        # Returns the biggest element
        return max(common_factors)

    def get_numerator(self):
        return self.numerator//Fraction.gcd(self.numerator, self.denominator)

    def get_denominator(self):
        return self.denominator//Fraction.gcd(self.numerator, self.denominator)

    def get_fraction(self):
        if Fraction.gcd(self.numerator, self.denominator) == 0:
            return "0"
        if Fraction.get_denominator(self) < 0:
            if Fraction.get_numerator(self) > 0:
                return f"-{self.get_numerator()}/{abs(self.get_denominator())}"
            if Fraction.get_numerator(self) < 0:
                return f"{abs(self.get_numerator())}/{abs(self.get_denominator())}"
        return f"{self.get_numerator()}/{self.get_denominator()}"

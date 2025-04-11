def main():
    class Fraction:
        def __init__(self, numerator=0, denominator=1):
            self.numerator = numerator
            self.denominator = denominator
        def __str__(self):
            self.simplify()
            return f"{self.numerator} / {self.denominator}"
        def __call__(self):
            return self.numerator / self.denominator
        def set_value(self, number):
            if isinstance(number, int):
                self.numerator = number
                self.denominator = 1
            elif isinstance(number, float):
                counter = 0
                while number-int(number) > 0:
                    number *= 10
                    counter += 1
                self.numerator = int(number)
                self.denominator = 10**counter
                self.simplify()
        def simplify(self):
            divisor = 2
            while divisor <= self.denominator:
                if self.denominator % divisor == 0 and self.numerator % divisor == 0:
                    self.denominator //= divisor
                    self.numerator //= divisor
                else:
                    divisor += 1
        def __add__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            numerator = (self.numerator * other.denominator) + (self.denominator * other.numerator)
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        def __sub__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            numerator = (self.numerator * other.denominator) - (self.denominator * other.numerator)
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        def __mul__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        def __truediv__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)
        def __gt__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            return self.numerator * other.denominator > self.denominator * other.numerator
        def __lt__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            return self.numerator * other.denominator < self.denominator * other.numerator
        def __eq__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            return self.numerator * other.denominator == self.denominator * other.numerator
        def __ge__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            return self.numerator * other.denominator >= self.denominator * other.numerator
        def __le__(self, other):
            if isinstance(other, (int, float)):
                other = Fraction(other)
            return self.numerator * other.denominator <= self.denominator * other.numerator
        def __ne__(self, other):
            return not self == other

if __name__ == "__main__":
    main()

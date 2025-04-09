from math import gcd

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            return ValueError
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        divisor = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= divisor
        self.denominator //= divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @staticmethod
    def from_float(value):
        factor = 10 ** len(str(value).split(".")[1])
        numerator = int(value * factor)
        denominator = factor
        return Fraction(numerator, denominator)

    def set_value(self, value):
        if isinstance(value, int):
            self.numerator = value
            self.denominator = 1
        elif isinstance(value, float):
            fraction = Fraction.from_float(value)
            self.numerator = fraction.numerator
            self.denominator = fraction.denominator
        else:
            return ValueError
        self.simplify()

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator + self.denominator * other.denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,self.denominator * other.denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        if other.numerator == 0:
            return ZeroDivisionError
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return abs(float(self) - other) < 1e-9
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return float(self) < other
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __call__(self):
        return self.numerator / self.denominator

    def __float__(self):
        return self.numerator / self.denominator


f1 = Fraction()
f2 = Fraction(12)
f3 = Fraction(12, 9)

print(f1)
print(f2)
print(f3)

f1.set_value(9)
print(f1)

f1.set_value(2.34)
print(f1)

print(f1 + f3)
print(f1 - f3)
print(f1 * f3)
print(f1 / f3)
print(f1 + 1)
print(f1 - 2)
print(f1 * 3)
print(f1 / 3)

print(f1)
print(f1())

print(f1 > f3, f1 == f3, f1 < f3, f1 >= f3, f1 <= f3, f1 != f3)
print(f1 > 2.34, f1 == 2.34, f1 < 2.34, f1 >= 2.34, f1 <= 2.34, f1 != 2.34)

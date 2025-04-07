from math import gcd


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, float):
            self.set_value(numerator)
            return
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        d = gcd(self.numerator, self.denominator)
        self.numerator //= d
        self.denominator //= d
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def set_value(self, value):
        if isinstance(value, int):
            self.numerator = value
            self.denominator = 1
        elif isinstance(value, float):
            factor = 10 ** len(str(value).split('.')[1])
            self.numerator = int(value * factor)
            self.denominator = factor
        self.simplify()

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __call__(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)

        left = self.numerator * other.denominator
        right = self.denominator * other.numerator

        if left == right:
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)

        left = self.numerator * other.denominator
        right = self.denominator * other.numerator

        if left < right:
            return True
        else:
            return False

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other


f1 = Fraction()
f2 = Fraction(12)
f3 = Fraction(12, 9)
print(f1)
print(f2)
print(f3)

f2.set_value(9)
f1.set_value(2.34)

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

from math import gcd

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, float):
            self.set_value(numerator)
        else:
            self.numerator = numerator
            self.denominator = denominator
            self._simplify()

    def _simplify(self):
        if self.denominator == 0:
            raise ValueError("makhraj sefr nemishe!")
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def set_value(self, value):

        if isinstance(value, int):
            self.numerator = value
            self.denominator = 1

        elif isinstance(value, float):
            self.numerator = int(round(value * 10**10))
            self.denominator = 10**10
            self._simplify()

        else:
            raise ValueError("enter integer or float.")

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __call__(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            return self + Fraction(other)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            return self - Fraction(other)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            return self * Fraction(other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero fraction.")
            return self * Fraction(other.denominator, other.numerator)
        else:
            return self / Fraction(other)

    def __gt__(self, other):
        if isinstance(other, (Fraction, int, float)):
            other_fraction = Fraction(other) if not isinstance(other, Fraction) else other
            return self.numerator * other_fraction.denominator > other_fraction.numerator * self.denominator
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (Fraction, int, float)):
            other_fraction = Fraction(other) if not isinstance(other, Fraction) else other
            return self.numerator * other_fraction.denominator < other_fraction.numerator * self.denominator
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, (Fraction, int, float)):
            other_fraction = Fraction(other) if not isinstance(other, Fraction) else other
            return self.numerator * other_fraction.denominator == other_fraction.numerator * self.denominator
        return NotImplemented

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __ne__(self, other):
        return not self == other


f1 = Fraction()
f2 = Fraction(12)
f3 = Fraction(12, 9)

print(f1)
print(f2)
print(f3)

f1.set_value(2.34)
f2.set_value(9)

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

print(f1 > f3 , f1 == f3 , f1 < f3 , f1 >= f3, f1 <= f3, f1 != f3)

print(f1 > 2.34 , f1 == 2.34 , f1 < 2.34 , f1 >= 2.34, f1 <= 2.34, f1 != 2.34)
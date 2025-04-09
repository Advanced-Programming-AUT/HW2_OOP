from math import gcd

class Rational:
    def __init__(self, numerator=0, denominator=1):
        self.num = numerator
        self.den = denominator if denominator != 0 else 1
        self._reduce()

    def _reduce(self):
        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common
        if self.den < 0:
            self.num *= -1
            self.den *= -1

    def __str__(self):
        return f"{self.num} / {self.den}"

    def __call__(self):
        return self.num / self.den

    def update(self, decimal_value):
        while not decimal_value.is_integer():
            decimal_value *= 10
            self.den *= 10
        self.num = int(decimal_value)
        self._reduce()

    def __add__(self, other):
        if isinstance(other, int):
            return Rational(self.num + self.den * other, self.den)
        return Rational(self.num * other.den + other.num * self.den, self.den * other.den)

    def __sub__(self, other):
        if isinstance(other, int):
            return Rational(self.num - self.den * other, self.den)
        return Rational(self.num * other.den - other.num * self.den, self.den * other.den)

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.num * other, self.den)
        return Rational(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Rational(self.num, self.den * other)
        return Rational(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        return float(self) == float(other)

    def __ne__(self, other):
        return float(self) != float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)


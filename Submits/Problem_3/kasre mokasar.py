from math import gcd


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        if type(self.numerator) == int:
            numerator = self.numerator
            denominator = self.denominator
            self.numerator //= gcd(numerator, self.denominator)
            self.denominator //= gcd(numerator, denominator)
        else:
            while self.numerator - int(self.numerator) != 0:
                self.numerator *= 10
                self.denominator *= 10
            self.numerator = int(self.numerator)
            self.simplify()

    def set_value(self, numerator):
        self.numerator = numerator
        self.denominator = 1
        self.simplify()

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __call__(self):
        return self.numerator / self.denominator
    def __add__(self, other):  # -
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        temp = Fraction(numerator, denominator)
        return temp


    def __sub__(self, other):  # +
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        temp = Fraction(numerator, denominator)
        return temp

    def __mul__(self, other):  # *
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        temp = Fraction(numerator, denominator)
        return temp


    def __truediv__(self, other):  # /
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator // other.denominator
        denominator = other.numerator // self.denominator
        temp = Fraction(numerator, denominator)
        return temp


    def __gt__(self, other):  # >
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.numerator * other.denominator > self.denominator * other.numerator:
            return True
        return False

    def __lt__(self, other):  # <
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.numerator * other.denominator < self.denominator * other.numerator:
            return True
        return False


    def __ge__(self, other):  # >=
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.numerator * other.denominator >= self.denominator * other.numerator:
            return True
        return False

    def __le__(self, other):  # <=
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.numerator * other.denominator <= self.denominator * other.numerator:
            return True
        return False

    def __eq__(self, other):  # ==
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True
        return False

    def __ne__(self, other):  # !=
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.numerator * other.denominator != self.denominator * other.numerator:
            return True
        return False


f1 = Fraction()  # Default value: 0 / 1
f2 = Fraction(12)  # Value: 12 / 1
f3 = Fraction(12, 9)  # Simplified to: 4 / 3
print(f1)  # Output: "0 / 1"
print(f2)  # Output: "12 / 1"
print(f3)  # Output: "4 / 3"

f2.set_value(9)  # Set value to 9 / 1
f1.set_value(2.34)  # Set value to 117 / 50

print(f1)  # Output: "117 / 50"
print(f2)  # Output: "9 / 1"

print(f1()) # Output: "2.34"

print(f1 + f3)  # Output: "551 / 150"
print(f1 - f3)  # Output: "151 / 150"
print(f1 * f3)  # Output: "78 / 25"
print(f1 / f3)  # Output: "351 / 200"
print(f1 + 1)  # Output: "167 / 50"
print(f1 - 2)  # Output: "51 / 50"
print(f1 * 3)  # Output: "351 / 50"
print(f1 / 3)  # Output: "39 / 50"

print(f1 > f3, f1 == f3, f1 < f3, f1 >= f3, f1 <= f3, f1 != f3)
# Output: True, False, False, True, False, True

print(f1 > 2.34, f1 == 2.34, f1 < 2.34, f1 >= 2.34, f1 <= 2.34, f1 != 2.34)
# Output: False, True, False, True, True, False

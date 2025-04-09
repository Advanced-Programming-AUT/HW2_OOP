#     __call__
#     __rmul__
#     __rsub__
#     __radd__
#     __rtruediv__
#     __truediv__
#     __gt__
#     __lt__
#     __eq__
#     __le__
#     __ne__
#     __ge__

from math import gcd

class Fraction:

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

        common = gcd(self.numerator, self.denominator)
        if common != 0:
            self.numerator //= common
            self.denominator //= common

    def set_value(self, value):
        if isinstance(value, int):
            self.numerator = value
            self.denominator = 1
        elif isinstance(value, float):
            s = str(value)
            if '.' in s:
                decimal_places = len(s.split('.')[1])
            else:
                decimal_places = 0
            factor = 10 ** decimal_places
            self.numerator = int(round(value * factor))
            self.denominator = factor
        else:
            raise TypeError("set_value must be int or float")
        self._simplify()

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __call__(self):
        return self.numerator / self.denominator

    def _to_fraction(self, other):
        if isinstance(other, Fraction):
            return other
        elif isinstance(other, int):
            return Fraction(other, 1)
        elif isinstance(other, float):
            temp = Fraction()
            temp.set_value(other)
            return temp
        else:
            raise TypeError("Unsupported type for arithmetic operation")

    # Arithmetic operations
    def __add__(self, other):
        other = self._to_fraction(other)
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = self._to_fraction(other)
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __rsub__(self, other):
        other = self._to_fraction(other)
        return other.__sub__(self)

    def __mul__(self, other):
        other = self._to_fraction(other)
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = self._to_fraction(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is undefined")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def __rtruediv__(self, other):
        other = self._to_fraction(other)
        return other.__truediv__(self)

    def __eq__(self, other):
        try:
            other = self._to_fraction(other)
        except TypeError:
            return False
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        other = self._to_fraction(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        other = self._to_fraction(other)
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        other = self._to_fraction(other)
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        other = self._to_fraction(other)
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

#teste sample ha ye pdf...
def main():

    f1 = Fraction()
    f2 = Fraction(12)
    f3 = Fraction(12, 9)

    print("Initial Fractions:")
    print("f1:", f1)
    print("f2:", f2)
    print("f3:", f3)

    f2.set_value(9)
    f1.set_value(2.34)

    print("\nAfter set_value:")
    print("f1:", f1)
    print("f2:", f2)
    print("f1() as float:", f1())

    add_result = f1 + f3
    sub_result = f1 - f3
    mul_result = f1 * f3
    div_result = f1 / f3

    print("\nArithmetic Operations:")
    print("f1 + f3 =", add_result)
    print("f1 - f3 =", sub_result)
    print("f1 * f3 =", mul_result)
    print("f1 / f3 =", div_result)

    print("\nArithmetic with int/float:")
    print("f1 + 1 =", f1 + 1)
    print("f1 - 2 =", f1 - 2)
    print("f1 * 3 =", f1 * 3)
    print("f1 / 3 =", f1 / 3)

    comp1 = (f1 > f3, f1 == f3, f1 < f3, f1 >= f3, f1 <= f3, f1 != f3)
    print("\nFraction Comparisons (f1 vs f3):", comp1)

    comp2 = (f1 > 2.34, f1 == 2.34, f1 < 2.34, f1 >= 2.34, f1 <= 2.34, f1 != 2.34)
    print("Fraction Comparisons (f1 vs 2.34):", comp2)


if __name__ == "__main__":
    main()

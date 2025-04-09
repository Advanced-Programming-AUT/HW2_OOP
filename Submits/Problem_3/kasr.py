import math

class Fraction:
    def __init__(self, numerator=None, denominator=None):
        self.set_value(numerator, denominator)



    def convert_float_to_fraction(self, number):
        decimal_str = str(number).split(".")[1]
        decimal_places = len(decimal_str)
        numerator = int(number * (10 ** decimal_places))
        denominator = 10 ** decimal_places
        return numerator, denominator



    def set_value(self, numerator=None, denominator=None):
        if numerator is None:
            self.numerator = 0
            self.denominator = 1
        elif isinstance(numerator, float):
            self.numerator, self.denominator = self.convert_float_to_fraction(numerator)
        else:
            self.numerator = numerator
            self.denominator = denominator if denominator is not None else 1
        self.simplify()
        return self.get_value()



    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd



    def get_value(self):
        return f"{self.numerator} / {self.denominator}"



    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)



    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)



    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)



    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        if other.numerator != 0:
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)



    def __call__(self):
        return float(self.numerator / self.denominator)

    def __eq__(self, other):
        if isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        if isinstance(other, Fraction):
            return (self.numerator == other.numerator) and (self.denominator == other.denominator)
        raise TypeError("Unsupported comparison with type: " + str(type(other)))



    def __ne__(self, other):
        if isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        if isinstance(other, Fraction):
            return not self.__eq__(other)
        raise TypeError("Unsupported comparison with type: " + str(type(other)))



    def __gt__(self, other):
        if isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) > (self.denominator * other.numerator)
        raise TypeError("Unsupported comparison with type: " + str(type(other)))



    def __lt__(self, other):
        if isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) < (self.denominator * other.numerator)
        raise TypeError("Unsupported comparison with type: " + str(type(other)))



    def __ge__(self, other):
        if isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) >= (self.denominator * other.numerator)
        raise TypeError("Unsupported comparison with type: " + str(type(other)))



    def __le__(self, other):
        if isinstance(other, float):
            other = Fraction(*self.convert_float_to_fraction(other))
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) <= (self.denominator * other.numerator)
        raise TypeError("Unsupported comparison with type: " + str(type(other)))



    def __str__(self):
        return f"{self.numerator} / {self.denominator}"


f1 = Fraction()
print(f1)
f2 = Fraction(12)
f3 = Fraction(12, 9)

print(f1.set_value(2.34))
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

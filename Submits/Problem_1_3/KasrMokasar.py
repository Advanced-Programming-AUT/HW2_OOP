import  math

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("the denominator can't be zero!")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @classmethod
    def numerator(cls, numerator):
        return cls(numerator, 1)

    @classmethod
    def default(cls):
        return cls()

    @classmethod
    def integer(cls, integer):
        return cls(integer, 1)

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def set_value(self, value):
        if isinstance(value, int):
            self.numerator = value
            self.denominator = 1
        elif isinstance(value, float):
            self.numerator = int(value * 10**10)
            self.denominator = 10**10
            self.simplify()

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        self.simplify()
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __call__(self):
        return self.numerator / self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __eq__(self, other):
        return  self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return  self.numerator * other.denominator != other.numerator * self.denominator

    def to_decimal(self):
        return self.numerator / self.denominator

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.to_decimal() > other
        elif isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.to_decimal() < other
        elif isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.to_decimal() >= other
        elif isinstance(other, Fraction):
            return self.numerator * other.denominator >= other.numerator * self.denominator

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.to_decimal() <= other
        elif isinstance(other, Fraction):
            return self.numerator * other.denominator <= other.numerator * self.denominator

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.to_decimal() == other
        elif isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        if isinstance(other, (int, float)):
            return self.to_decimal() != other
        elif isinstance(other, Fraction):
            return self.numerator * other.denominator != other.numerator * self.denominator

if __name__ == "__main__":
    f1 = Fraction()
    f2 = Fraction(12)
    f3 = Fraction(12, 9)
    print(f1)
    print(f2)
    print(f3)
    f2.set_value(9)
    print(f2)
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
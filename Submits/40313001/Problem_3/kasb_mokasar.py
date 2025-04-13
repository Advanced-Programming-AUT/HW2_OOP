from math import gcd


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, float):
            self.set_value(numerator)
        else:
            if denominator == 0:
                raise ValueError("Denominator cannot be zero.")
            self.numerator = numerator
            self.denominator = denominator
            self.simplify()

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def set_value(self, value):
        if isinstance(value, int):
            self.numerator = value
            self.denominator = 1
        elif isinstance(value, float):
            factor = 10 ** len(str(value).split(".")[1])  # تعیین تعداد ارقام اعشار
            self.numerator = int(value * factor)
            self.denominator = factor
        self.simplify()

    def __call__(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

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
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __ne__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return self.numerator * other.denominator != self.denominator * other.numerator


#test case
f1=Fraction()
f2=Fraction(12)
f3=Fraction(12,9)
print(f1)
print(f2)
print(f3)
f2.set_value(9)
f1.set_value(2.34)
print(f1+f3)
print(f1-f3)
print(f1*f3)
print(f1/f3)
print(f1+1)
print(f1-2)
print(f1*3)
print(f1/3)
print(f1)
print(f1())
print(f1>f3,f1==f3,f1<f3,f1>=f3,f1<=f3,f1!=f3)
print(f1>2.34,f1==2.34,f1<2.34,f1>=2.34,f1<=2.34,f1!=2.34)

import sys, os
from math import gcd, lcm

original_stdout = sys.stdout

os.remove('output.txt')

file1 = open('input.txt', 'r')
file2 = open('output.txt', 'a')

sys.stdout = file2

# ---------- Main Code ----------

class Fraction:
    def __simplify(self):
        while self.__numerator % 1 or self.__denominator % 1:
            self.__numerator *= 10
            self.__denominator *= 10

        self.__numerator = int(self.__numerator)
        self.__denominator = int(self.__denominator)

        g = gcd(self.__numerator, self.__denominator)
        self.__numerator //= g
        self.__denominator //= g

    def __init__(self, numerator = 0, denominator = 1):
        self.__numerator = numerator
        self.__denominator = denominator

        self.__simplify()

    def set_value(self, numerator = 0, denominator = 1):
        self.__numerator = numerator
        self.__denominator = denominator

        self.__simplify()

    def reverse(self):
        self.__numerator, self.__denominator = self.__denominator, self.__numerator

    def __str__(self):
        self.__simplify()
        return f'{self.__numerator} / {self.__denominator}'

    def __float__(self):
        self.__simplify()
        return self.__numerator / self.__denominator

    def __call__(self):
        return float(self)

    def __add__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        l = lcm(self.__denominator, other.__denominator)
        l1 = l / self.__denominator
        l2 = l / other.__denominator

        return Fraction(self.__numerator * l1 + other.__numerator * l2, l)

    def __sub__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        l = lcm(self.__denominator, other.__denominator)
        l1 = l / self.__denominator
        l2 = l / other.__denominator

        return Fraction(self.__numerator * l1 - other.__numerator * l2, l)

    def __mul__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __truediv__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __gt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        return self.__numerator * other.__denominator > self.__denominator * other.__numerator

    def __lt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        return self.__numerator * other.__denominator < self.__denominator * other.__numerator

    def __eq__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        return self.__numerator * other.__denominator == self.__denominator * other.__numerator

    def __ge__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        return self.__numerator * other.__denominator >= self.__denominator * other.__numerator

    def __le__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        return self.__numerator * other.__denominator <= self.__denominator * other.__numerator

    def __ne__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)

        return self.__numerator * other.__denominator != self.__denominator * other.__numerator

if __name__ == '__main__':
    f1 = Fraction()
    f2 = Fraction(12)
    f3 = Fraction(12, 9)
    print(f1)
    print(f2)
    print(f3)
    print()

    f2.set_value(9)
    f1.set_value(2.34)
    print()

    print(f1 + f3)
    print(f1 - f3)
    print(f1 * f3)
    print(f1 / f3)
    print(f1 + 1)
    print(f1 - 2)
    print(f1 * 3)
    print(f1 / 3)
    print()

    print(f1)
    print()

    print(f1())
    print()

    print(f1 > f3, f1 == f3, f1 < f3, f1 >= f3, f1 <= f3, f1 != f3)
    print()

    print(f1 > 2.34, f1 == 2.34, f1 < 2.34, f1 >= 2.34, f1 <= 2.34, f1 != 2.34)
    print()

# ---------- End of Main Code ----------

sys.stdout = original_stdout

file1.close()
file2.close()

from math import gcd


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError(" zero is not acceptable...  .")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __call__(self):
        return self.numerator / self.denominator

    def reciprocal(self):
        if self.numerator == 0:
            raise ValueError("  reciprocal of zero is  irregular...")
        return Fraction(self.denominator, self.numerator)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return self * other.reciprocal()

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def to_mixed_number(self):
        whole_part = self.numerator // self.denominator
        remainder = self.numerator % self.denominator
        if remainder == 0:
            return str(whole_part)
        return f"{whole_part} {remainder}/{self.denominator}" if whole_part != 0 else f"{remainder}/{self.denominator}"


while True:
    try:
        num1 = int(input(" please Enter the numerator: "))
        den1 = int(input(" please Enter the denominator: "))
        fraction = Fraction(num1, den1)
        print("Your fraction:", fraction)
        print("Decimal value:", fraction())
        print("Reciprocal:", fraction.reciprocal())
        print("Mixed Number:", fraction.to_mixed_number())

        num2 = int(input(" please Enter the numerator for the second fraction: "))
        den2 = int(input(" please Enter the denominator for  the second fraction: "))
        fraction2 = Fraction(num2, den2)

        print("Addition:", fraction + fraction2)
        print("Subtraction:", fraction - fraction2)
        print("Multiplication:", fraction * fraction2)
        print("Division:", fraction / fraction2)
        print("Comparison (==):", fraction == fraction2)
        print("Comparison (<):", fraction < fraction2)
        print("Comparison (>):", fraction > fraction2)

        another = input(" enter another fraction? (y/n): ")
        if another.lower() != 'y':
            break
    except ValueError as e:
        print("Error:", e)
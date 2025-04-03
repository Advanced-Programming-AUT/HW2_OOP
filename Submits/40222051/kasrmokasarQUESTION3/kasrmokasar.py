class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        return max([i for i in range(1, max(a, b) + 1) if a % i == 0 and b % i == 0])

    def return_value(self):
        if self.numerator == 0:
            return '0/1'
        elif self.denominator == 1:
            return f"{self.numerator}/1"
        else:
            gcm = self.gcd(abs(self.numerator), abs(self.denominator))
            return f"{self.numerator//gcm}/{self.denominator//gcm}"

    def set_value(self, num):
        if isinstance(num, int):
            self.numerator = num
            self.denominator = 1
        else:
            power = len(str(num).split('.')[1]) if '.' in str(num) else 0
            self.denominator = 10 ** power
            self.numerator = int(num * self.denominator)

    def add(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = other.denominator * self.denominator
        return Fraction(numerator, denominator).return_value()

    def sub(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = other.denominator * self.denominator
        return Fraction(numerator, denominator).return_value()

    def mul(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        denominator = other.denominator * self.denominator
        numerator = other.numerator * self.numerator
        return Fraction(numerator, denominator).return_value()

    def truediv(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        denominator = other.numerator * self.denominator
        numerator = other.denominator * self.numerator
        return Fraction(numerator, denominator).return_value()

    def __gt__(self, other):  # Fixed comparison methods
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return (self.numerator * other.denominator) > (other.numerator * self.denominator)

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return (self.numerator * other.denominator) >= (other.numerator * self.denominator)

    def __le__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return (self.numerator * other.denominator) <= (other.numerator * self.denominator)

    def __ne__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return (self.numerator * other.denominator) != (other.numerator * self.denominator)

    def __str__(self):
        return self.return_value()

# Testing
f1 = Fraction()         # 0/1
f2 = Fraction(12)       # 12/1
f3 = Fraction(12, 9)    # 4/3
print(f1)               # "0/1"
print(f2)               # "12/1"
print(f3)               # "4/3"

f2.set_value(9)         # 9/1
f1.set_value(2.34)      # 117/50
print(f2)               # "9/1"
print(f1)               # "117/50"

print(f1.add(f3))       # "551/150"
print(f1 > f3)          # True
print(f1 == f3)         # False

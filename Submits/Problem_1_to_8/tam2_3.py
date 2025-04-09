import math
class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.num = numerator
        self.den = denominator
        gcd = math.gcd(self.num , self.den)
        self.num = self.num // gcd
        self.den = self.den // gcd

    def set_value(self, number):
        if isinstance(number, int):
            self.num = number
        elif isinstance(number, float):
            str_number = str(number)
            str_number = str_number.split('.')
            len_float = len(str_number[1])
            num = int(number * (10**len_float))
            den = 10**len_float
            gcd = math.gcd(num, den)
            self.num = num // gcd
            self.den = den // gcd

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            str_other = str(other)
            str_other = str_other.split('.')
            len_float = len(str_other[1])
            num = int(other * (10 ** len_float))
            den = 10 ** len_float
            other = Fraction(num, den)
        num = (self.num * other.den) + (self.den * other.num)
        den = self.den * other.den
        gcd = math.gcd(num, den)
        num = num // gcd
        den = den // gcd
        return f'{num} / {den}'

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            str_other = str(other)
            str_other = str_other.split('.')
            len_float = len(str_other[1])
            num = int(other * (10 ** len_float))
            den = 10 ** len_float
            other = Fraction(num, den)
        num = (self.num * other.den) - (self.den * other.num)
        den = self.den * other.den
        gcd = math.gcd(num, den)
        num = num // gcd
        den = den // gcd
        return f'{num} / {den}'

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            str_other = str(other)
            str_other = str_other.split('.')
            len_float = len(str_other[1])
            num = int(other * (10 ** len_float))
            den = 10 ** len_float
            other = Fraction(num, den)
        num = self.num * other.num
        den = self.den * other.den
        gcd = math.gcd(num, den)
        num = num // gcd
        den = den // gcd
        return f'{num} / {den}'

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            str_other = str(other)
            str_other = str_other.split('.')
            len_float = len(str_other[1])
            num = int(other * (10 ** len_float))
            den = 10 ** len_float
            other = Fraction(num, den)
        num = self.num * other.den
        den = self.den * other.num
        gcd = math.gcd(num, den)
        num = num // gcd
        den = den // gcd
        return f'{num} / {den}'

    def __str__(self):
        return f'{self.num} / {self.den}'

    def __call__(self, *args, **kwargs):
        return self.num / self.den

    def __gt__(self, other):
        if isinstance(other, Fraction):
            if self.num / self.den > other.num / other.den:
                return True
            else:
                return False
        else:
            if self.num / self.den > other / 1:
                return True
            else:
                return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            if self.num / self.den < other.num / other.den:
                return True
            else:
                return False
        else:
            if self.num / self.den < other / 1:
                return True
            else:
                return False

    def __eq__(self, other):
        if isinstance(other, Fraction):
            if self.num / self.den == other.num / other.den:
                return True
            else:
                return False
        else:
            if self.num / self.den == other / 1:
                return True
            else:
                return False

    def __ge__(self, other):
        if isinstance(other, Fraction):
            if self.num / self.den >= other.num / other.den:
                return True
            else:
                return False
        else:
            if self.num / self.den >= other / 1:
                return True
            else:
                return False

    def __le__(self, other):
        if isinstance(other, Fraction):
            if self.num / self.den <= other.num / other.den:
                return True
            else:
                return False
        else:
            if self.num / self.den <= other / 1:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, Fraction):
            if self.num / self.den != other.num / other.den:
                return True
            else:
                return False
        else:
            if self.num / self.den != other / 1:
                return True
            else:
                return False


f1 = Fraction() # Default value: 0 / 1
f2 = Fraction(12) # Value: 12 / 1
f3 = Fraction(12, 9) # Simplified to: 4 / 3
print(f1) # Output: "0 / 1"
print(f2) # Output: "12 / 1"
print(f3) # Output: "4 / 3"
f2.set_value(9) # 9 / 1
f1.set_value(2.34) # 117 / 50
print(f1) # Output: 117 / 50
print(f2) # Output: 9 / 1
print(f1 + f3) # Output: "551 / 150"
print(f1 - f3) # Output: "151 / 150"
print(f1 * f3) # Output: "78 / 25"
print(f1 / f3) # Output: "351 / 200"
print(f1 + 1) # Output: "167 / 50"
print(f1 - 2) # Output: "51 / 50"
print(f1 * 3) # Output: "351 / 50"
print(f1 / 3) # Output: "39 / 50"
print(f1) # Output: 117 / 50
print(f1()) # Output: 2.34
print(f1 > f3, f1 == f3, f1 < f3, f1 >= f3, f1 <= f3, f1 != f3) # Output: True, False, False, True, False, True
print(f1 > 2.34, f1 == 2.34, f1 < 2.34, f1 >= 2.34, f1 <= 2.34) # Output: False, True, False, True, True
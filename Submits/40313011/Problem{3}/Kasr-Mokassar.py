# Completed

def lcm(a, b):
    for i in range(2, a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


def bcd(a, b):
    find_bcd = 1
    for i in range(1, max(int(a), int(b)) + 1):
        if a % i == 0 and b % i == 0:
            find_bcd = i
    return find_bcd


class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            self.numerator, self.denominator = args
        if len(args) == 1:
            self.numerator = args[0]
            self.denominator = 1
        if len(args) == 0:
            self.denominator = 1
            self.numerator = 1

    def set_value(self, value):
        # still not completed!!!
        denominator = 1
        while value * denominator != int(value * denominator):
            denominator += 1
        numerator = 1
        while numerator / denominator != value:
            numerator += 1
        self.numerator = numerator
        self.denominator = denominator

    def simplification(self):
        fraction_bcd = bcd(self.numerator, self.denominator)
        if fraction_bcd == 1:
            return Fraction(self.numerator, self.denominator)
        else:
            return Fraction(self.numerator // fraction_bcd, self.denominator // fraction_bcd)

    def fraction_to_value(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            denominator = lcm(self.denominator, other.denominator)
            numerator = (((denominator//self.denominator)*self.numerator) +
                         ((denominator//other.denominator)*other.numerator))
            return Fraction(numerator, denominator)

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            denominator = lcm(self.denominator, other.denominator)
            numerator = (((denominator//self.denominator)*self.numerator) -
                         ((denominator//other.denominator)*other.numerator))
            return Fraction(numerator, denominator)

    def __mul__(self, other):
        answer = Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
        answer = answer.simplification()
        return answer

    def __truediv__(self, other):
        tmp_fraction = Fraction(other.denominator, other.numerator)
        answer = tmp_fraction * Fraction(self.numerator, self.denominator)
        answer = answer.simplification()
        return answer

    def __eq__(self, other):
        self.simplification()
        if isinstance(other, Fraction):
            other = other.simplification()
            if self.numerator == other.numerator:
                if self.denominator == other.denominator:
                    return True
                else:
                    return False
            return False
        else:
            _self = self.fraction_to_value()
            if _self == other:
                return True
            else:
                return False

    def __ne__(self, other):
        self.simplification()
        if isinstance(other, Fraction):
            other = other.simplification()
            if self.numerator == other.numerator:
                if self.denominator == other.denominator:
                    return False
                else:
                    return True
            return True
        else:
            _self = self.fraction_to_value()
            if _self == other:
                return False
            else:
                return True

    def __lt__(self, other):
        if isinstance(other, Fraction):
            _self = self.fraction_to_value()
            _other = other.fraction_to_value()
            if _self < _other:
                return True
            else:
                return False
        else:
            _self = self.fraction_to_value()
            if _self < other:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            _self = self.fraction_to_value()
            _other = other.fraction_to_value()
            if _self > _other:
                return True
            else:
                return False
        else:
            _self = self.fraction_to_value()
            if _self > other:
                return True
            else:
                return False

    def __le__(self, other):
        if isinstance(other, Fraction):
            _self = self.fraction_to_value()
            _other = other.fraction_to_value()
            if _self <= _other:
                return True
            else:
                return False
        else:
            _self = self.fraction_to_value()
            if _self <= other:
                return True
            else:
                return False

    def __ge__(self, other):
        if isinstance(other, Fraction):
            _self = self.fraction_to_value()
            _other = other.fraction_to_value()
            if _self >= _other:
                return True
            else:
                return False
        else:
            _self = self.fraction_to_value()
            if _self >= other:
                return True
            else:
                return False

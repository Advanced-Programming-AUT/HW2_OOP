from math import gcd

def float_as_integer_ratio(num: float) -> tuple[int]:
    denom = 1
    while num % 1:
        denom *= 10
        num *= 10

    return normalize(int(num), denom)

def normalize(num: int, denom: int) -> tuple[int]:
    common = gcd(num, denom)
    return num // common, denom // common

class Fraction:
    def __init__(self, num: int = 0, denom: int = 1) -> None:
        if not denom:
            raise ZeroDivisionError
        self.num, self.denom = normalize(num, denom)

    def __add__(self, other):
        res = Fraction(self.num, self.denom)

        if isinstance(other, int):
            res.num += other * res.denom
            return res
        if isinstance(other, float):
            num, denom = float_as_integer_ratio(other)
            res.num = res.num * denom + num * res.denom
            res.denom *= denom

            res.num, res.denom = normalize(res.num, res.denom)
            return res
        if isinstance(other, Fraction):
            res.num = res.num * other.denom + other.num * res.denom
            res.denom *= other.denom

            res.num, res.denom = normalize(res.num, res.denom)
            return res
        raise TypeError

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        res = Fraction(self.num, self.denom)

        if isinstance(other, int):
            res.num *= other

            res.num, res.denom = normalize(res.num, res.denom)
            return res
        if isinstance(other, float):
            num, denom = float_as_integer_ratio(other)
            res.num *= num
            res.denom *= denom

            res.num, res.denom = normalize(res.num, res.denom)
            return res
        if isinstance(other, Fraction):
            res.num *= other.num
            res.denom *= other.denom

            res.num, res.denom = normalize(res.num, res.denom)
            return res
        raise TypeError

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not other:
            raise ZeroDivisionError

        res = Fraction(self.num, self.denom)

        if isinstance(other, int):
            res.denom *= other

            res.num, res.denom = normalize(res.num, res.denom)
            return res
        if isinstance(other, float):
            num, denom = float_as_integer_ratio(other)
            res.num *= denom
            res.denom *= num

            res.num, res.denom = normalize(res.num, res.denom)
            return res
        if isinstance(other, Fraction):
            res.num *= other.denom
            res.denom *= other.num

            res.num, res.denom = normalize(res.num, res.denom)
            return res
        raise TypeError

    def __rtruediv__(self, other):
        if not self:
            raise ZeroDivisionError

        res = Fraction(self.denom, self.num)
        return res * other

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.denom == 1 and self.num == other
        if isinstance(other, float):
            num, denom = float_as_integer_ratio(other)
            return self.num == num and self.denom == denom
        if isinstance(other, Fraction):
            return self.num == other.num and self.denom == other.denom
        raise TypeError

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __lt__(self, other) -> bool:
        if isinstance(other, int):
            return self.num < other * self.denom
        if isinstance(other, float):
            num, denom = float_as_integer_ratio(other)
            return self.num * denom < self.denom * num
        if isinstance(other, Fraction):
            return self.num * other.denom < self.denom * other.num
        raise TypeError

    def __gt__(self, other) -> bool:
        if isinstance(other, int):
            return self.num > other * self.denom
        if isinstance(other, float):
            num, denom = float_as_integer_ratio(other)
            return self.num * denom > self.denom * num
        if isinstance(other, Fraction):
            return self.num * other.denom > self.denom * other.num
        raise TypeError

    def __le__(self, other) -> bool:
        return not (self > other)

    def __ge__(self, other) -> bool:
        return not (self < other)

    def __neg__(self):
        self.num = -self.num
        return self

    def __bool__(self):
        return self.num != 0

    def __call__(self) -> float:
        return self.num / self.denom

    def __repr__(self) -> str:
        return f"{self.num} / {self.denom}"

    def set_value(self, value) -> None:
        if isinstance(value, int):
            self.num = value
            self.denom = 1
        elif isinstance(value, float):
            self.num, self.denom = float_as_integer_ratio(value)
        else:
            raise TypeError

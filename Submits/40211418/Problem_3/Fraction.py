from math import gcd, lcm


class Fraction:
    def __init__(self, num=0, denom=1):
        if denom == 0:
            raise ValueError('Denominator cannot be zero.')

        self.num = num
        self.denom = denom
        self.__simplify()

    def __simplify(self):
        g = gcd(self.num, self.denom)
        self.num //= g
        self.denom //= g

    def __str__(self):
        return f"{self.num} / {self.denom}"

    def set_value(self, value: int):
        if isinstance(value, int):
            self.num = value
            self.denom = 1

        elif isinstance(value, float):
            # calculate number of digits after decimal point
            number_of_digits = len(str(value).split(sep='.')[1])
            self.denom = 10 ** number_of_digits
            self.num = int(value * self.denom)
            self.__simplify()

        else:
            raise TypeError('Unsupported type')

    def __add__(self, other):
        if isinstance(other, Fraction):
            res_num = self.num * other.denom + self.denom * other.num
            res_denom = self.denom * other.denom
            return Fraction(res_num, res_denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self + f

        else:
            raise ValueError('Unsupported type')

    def __sub__(self, other):
        if isinstance(other, Fraction):
            res_num = self.num * other.denom - self.denom * other.num
            res_denom = self.denom * other.denom
            return Fraction(res_num, res_denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self - f

        else:
            raise ValueError('Unsupported type')

    def __mul__(self, other):
        if isinstance(other, Fraction):
            res_num = self.num * other.num
            res_denom = self.denom * other.denom
            return Fraction(res_num, res_denom)

        elif isinstance(other, int) or isinstance(other, float):
            f = Fraction()
            f.set_value(other)
            return self * f

        else:
            raise ValueError('Unsupported type')

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            res_num = self.num * other.denom
            res_denom = self.denom * other.num
            return Fraction(res_num, res_denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self / f

        else:
            raise ValueError('Unsupported type')

    def __eq__(self, other):
        if isinstance(other, Fraction):
            l = lcm(self.denom, other.denom)
            return self.num * (l / self.denom) == other.num * (l / other.denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self == f

        else:
            raise ValueError('Unsupported type')

    def __ne__(self, other):
        if isinstance(other, Fraction):
            l = lcm(self.denom, other.denom)
            return self.num * (l / self.denom) != other.num * (l / other.denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self != f

        else:
            raise ValueError('Unsupported type')

    def __lt__(self, other):
        if isinstance(other, Fraction):
            l = lcm(self.denom, other.denom)
            return self.num * (l / self.denom) < other.num * (l / other.denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self < f

        else:
            raise ValueError('Unsupported type')

    def __gt__(self, other):
        if isinstance(other, Fraction):
            l = lcm(self.denom, other.denom)
            return self.num * (l / self.denom) > other.num * (l / other.denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self > f

        else:
            raise ValueError('Unsupported type')

    def __le__(self, other):
        if isinstance(other, Fraction):
            l = lcm(self.denom, other.denom)
            return self.num * (l / self.denom) <= other.num * (l / other.denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self <= f

        else:
            raise ValueError('Unsupported type')

    def __ge__(self, other):
        if isinstance(other, Fraction):
            l = lcm(self.denom, other.denom)
            return self.num * (l / self.denom) >= other.num * (l / other.denom)

        elif isinstance(other, float) or isinstance(other, int):
            f = Fraction()
            f.set_value(other)
            return self >= f

        else:
            raise ValueError('Unsupported type')

    def __call__(self):
        return self.num / self.denom


# some examples
if __name__ == '__main__':
    f1 = Fraction()  # Default value: 0 / 1
    f2 = Fraction(12)  # Value: 12 / 1
    f3 = Fraction(12, 9)  # Simplified to: 4 / 3

    f2.set_value(9)  # Set value to 9 / 1
    f1.set_value(2.34)  # Set value to 117 / 50
    print(f1)
    print(f1())

    print(f1 + f3)  # Output: "551 / 150"
    print(f1 - f3)  # Output: "151 / 150"
    print(f1 * f3)  # Output: "78 / 25"
    print(f1 / f3)  # Output: "351 / 200"
    print(f1 + 1)  # Output: "167 / 50"
    print(f1 - 2)  # Output: "17 / 50"
    print(f1 * 3)  # Output: "351 / 50"
    print(f1 / 3)  # Output: "39 / 50"
    print(f1 > f3, f1 == f3, f1 < f3, f1 >= f3, f1 <= f3, f1 != f3)
    print(f1 > 2.34, f1 == 2.34, f1 < 2.34, f1 >= 2.34, f1 <= 2.34)
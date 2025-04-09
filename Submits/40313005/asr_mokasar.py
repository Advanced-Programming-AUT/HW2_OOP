import math


def check(case):
    if isinstance(case, int):
        case = Fraction(case)
    elif isinstance(case, float):
        case = Fraction(int(case * 1000000), 1000000)
    return case


class Fraction:
    def __init__(self, soorat=0, makhraj=1):
        self.soorat = soorat
        self.makhraj = makhraj
        self.simplify()

    def simplify(self):
        common_divisor = math.gcd(abs(self.soorat), abs(self.makhraj))
        self.soorat //= common_divisor
        self.makhraj //= common_divisor
        if self.makhraj < 0:  
            self.soorat *= -1
            self.makhraj *= -1

    def set_value(self, value):
        if isinstance(value, int):
            self.soorat = value
            self.makhraj = 1
        elif isinstance(value, float):
            self.makhraj = 1000000 
            self.soorat = int(value * self.makhraj)
            self.simplify()


    def __add__(self, other):
        other=check(other)
        new_soorat = self.soorat * other.makhraj + other.soorat * self.makhraj
        new_makhraj = self.makhraj * other.makhraj
        return Fraction(new_soorat, new_makhraj)

    def __sub__(self, other):
        other=check(other)
        new_soorat = self.soorat * other.makhraj - other.soorat * self.makhraj
        new_makhraj = self.makhraj * other.makhraj
        return Fraction(new_soorat, new_makhraj)

    def __mul__(self, other):
        other=check(other)
        new_soorat = self.soorat * other.soorat
        new_makhraj = self.makhraj * other.makhraj
        return Fraction(new_soorat, new_makhraj)

    def __truediv__(self, other):
        other=check(other)
        new_soorat = self.soorat * other.makhraj
        new_makhraj = self.makhraj * other.soorat
        return Fraction(new_soorat, new_makhraj)

    def __eq__(self, other):
        other=check(other)
        return self.soorat == other.soorat and self.makhraj == other.makhraj

    def __lt__(self, other):
        other=check(other)
        return self.soorat * other.makhraj < other.soorat * self.makhraj

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __call__(self):
        return self.soorat / self.makhraj

    def __str__(self):
        return f"{self.soorat} / {self.makhraj}"



f1 = Fraction() # Default value: 0 / 1
f2 = Fraction(12) # Value: 12 / 1
f3 = Fraction(12, 9) # Simplified to: 4 / 3
print(f1) # Output: "0 / 1"
print(f2) # Output: "12 / 1"
print(f3) # Output: "4 / 3"

f2.set_value(9) # Set value to 9 / 1
f1.set_value(2.34) # Set value to 117 / 50
print(f1) # Output: "0 / 1"
print(f2) # Output: "12 / 1"
print(f1 + f3) # Output: "551 / 150"
print(f1 - f3) # Output: "151 / 150"
print(f1 * f3) # Output: "78 / 25"
print(f1 / f3) # Output: "351 / 200"
print(f1 + 1) # Output: "167 / 50"
print(f1 - 2) # Output: "51 / 50"
print(f1 * 3) # Output: "351 / 50"
print(f1 / 3) # Output: "39 / 50"

print(f1()) 
print(f1 > f3, f1 == f3, f1 < f3, f1 >= f3, f1 <= f3, f1 != f3)
print(f1 > 2.34, f1 == 2.34, f1 < 2.34, f1 >= 2.34, f1 <= 2.34)
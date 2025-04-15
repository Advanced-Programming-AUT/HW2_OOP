import math
def k_m_m(x, y):
    return (x * y) // (math.gcd(x , y))

class Fraction:
    def __init__(self, *arg):
        self.sorat = 0
        self.makhraj = 1
        if len(arg) == 2:
            self.sorat = arg[0]
            self.makhraj = arg[1]
        if len(arg) == 1:
            self.sorat = arg[0]
            self.makhraj = 1
        b_m_m = math.gcd(self.sorat, self.makhraj)
        if self.sorat != 0:
            self.sorat = self.sorat // b_m_m
            self.makhraj = self.makhraj // b_m_m
        self.answer = f"{self.sorat} / {self.makhraj}"
    def set_value(self, digit):
        if type(digit) == int:
            self.sorat = digit
            self.makhraj = 1
        else:
            num_float = len(str(digit).split(".")[1])
            self.makhraj = int(pow(10, num_float))
            self.sorat = int(digit * self.makhraj)
        b_m_m = math.gcd(self.sorat, self.makhraj)
        if self.sorat != 0:
            self.sorat = self.sorat // b_m_m
            self.makhraj = self.makhraj // b_m_m
        self.answer = f"{self.sorat} / {self.makhraj}"
    def __call__(self):
        return self.sorat / self.makhraj
    def __str__(self):
        return f"{self.sorat} / {self.makhraj}"
    def __add__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        makhraj = k_m_m(self.makhraj, other.makhraj)
        sorat = self.sorat * (makhraj // self.makhraj) + other.sorat * (makhraj // other.makhraj)
        b_m_m = math.gcd(sorat, makhraj)
        if makhraj != 0:
            b_m_m = math.gcd(makhraj, sorat)
            sorat = sorat // b_m_m
            makhraj = makhraj // b_m_m
        return f"{sorat} / {makhraj}"
    def __sub__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)    
        makhraj = k_m_m(self.makhraj, other.makhraj)
        sorat = self.sorat * (makhraj // self.makhraj) - other.sorat * (makhraj // other.makhraj)
        b_m_m = math.gcd(sorat, makhraj)
        if makhraj != 0:
            b_m_m = math.gcd(makhraj, sorat)
            sorat = sorat // b_m_m
            makhraj = makhraj // b_m_m
        return f"{sorat} / {makhraj}"
    def __mul__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        makhraj = self.makhraj * other.makhraj
        sorat = self.sorat * other.sorat
        b_m_m = math.gcd(sorat, makhraj)
        if makhraj != 0:
            b_m_m = math.gcd(makhraj, sorat)
            sorat = sorat // b_m_m
            makhraj = makhraj // b_m_m
        return f"{sorat} / {makhraj}"
    def __truediv__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        if other.sorat == 0:
            raise ZeroDivisionError
        else:    
            makhraj = self.makhraj * other.sorat
            sorat = self.sorat * other.makhraj
            b_m_m = math.gcd(sorat, makhraj)
            if makhraj != 0:
                b_m_m = math.gcd(makhraj, sorat)
                sorat = sorat // b_m_m
                makhraj = makhraj // b_m_m
            return f"{sorat} / {makhraj}"
    def __eq__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        if (self.sorat / self.makhraj) == (other.sorat / other.makhraj):
            return True
        else:
            return False
    def __ne__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        if (self.sorat / self.makhraj) != (other.sorat / other.makhraj):
            return True
        else:
            return False
    def __lt__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        if (self.sorat / self.makhraj) < (other.sorat / other.makhraj):
            return True
        else:
            return False
    def __le__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        if (self.sorat / self.makhraj) <= (other.sorat / other.makhraj):
            return True
        else:
            return False
    def __gt__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        if (self.sorat / self.makhraj) > (other.sorat / other.makhraj):
            return True
        else:
            return False
    def __ge__(self, other):
        if type(other) == int:
            other = Fraction(other)
        if type(other) == float:
            number = other
            other = Fraction()
            other.set_value(number)
        if (self.sorat / self.makhraj) >= (other.sorat / other.makhraj):
            return True
        else:
            return False

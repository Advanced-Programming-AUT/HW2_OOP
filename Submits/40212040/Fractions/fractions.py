from math import gcd, lcm, floor

class Fraction:
    def __init__(self,numerator=0,denominator=1):
        self.numerator=numerator
        self.denominator=denominator
        if isinstance(numerator,int):
            self.simplify()
        else:
            self.turn_to_fraction()
        if self.numerator is None:
            self.numerator =0
            self.denominator=1
        elif self.denominator is None:
            self.denominator=1

    def __str__(self):
        return (f'{self.numerator} / {self.denominator}')
    def turn_to_fraction(self):
        x=self.numerator
        counter=0
        while(floor(x) != x):
            x *= 10
            counter += 1
        self.denominator=(10**counter)
        self.numerator=x
    def simplify(self):
        d=gcd(self.numerator, self.denominator)
        if d != 1:
            self.numerator//=d
            self.denominator //= d
    def set_value(self,number):
        if isinstance(number,int):
            self.numerator=number
            self.denominator=1
            return Fraction(self.numerator,self.denominator)
        else:
            x=number
            power=0
            while(not int(x) == x):
                x*=10
                power+=1
            return int(number*(10**power)),10**power
    def __add__(self,other):
        if not isinstance(other,Fraction):
            Other=Fraction(other)
        else:
            Other=other
        l=lcm(self.denominator,Other.denominator)
        r1=l//self.denominator
        r2=l//Other.denominator
        n=self.numerator*r1+Other.numerator*r2
        return Fraction(n,l)
    def __sub__(self, other):
        if not isinstance(other,Fraction):
            Other=Fraction(other)
        else:
            Other=other
        l = lcm(self.denominator, Other.denominator)
        r1 = l // self.denominator
        r2 = l //Other.denominator
        n = self.numerator * r1 - Other.numerator * r2
        return Fraction(n, l)
    def __mul__(self, other):
        if not isinstance(other,Fraction):
            Other=Fraction(other)
        else:
            Other=other
        n=self.numerator*Other.numerator
        m=self.denominator*Other.denominator
        return Fraction(n , m)
    def __divmod__(self, other):
        if not isinstance(other,Fraction):
            Other=Fraction(other)
        else:
            Other=other
        n=self.numerator*Other.denominator
        m=self.denominator*Other.numerator
        return Fraction(n,m)
    def __lt__(self,other):
        if not isinstance(other,Fraction):
            Other=Fraction(other)
        else:
            Other=other
        x=Other.denominator*self.numerator
        y=Other.numerator*self.denominator
        if x < y:
            return True
        else:
            return False
    def __gt__(self,other):
        if not isinstance(other,Fraction):
            Other=Fraction(other)
        else:
            Other=other
        x=Other.denominator*self.numerator
        y=Other.numerator*self.denominator
        if x > y:
            return True
        else:
            return False
    def __le__(self, other):
        if not isinstance(other, Fraction):
            Other = Fraction(other)
        else:
            Other = other
        x = Other.denominator * self.numerator
        y = Other.numerator * self.denominator
        if x <= y:
            return True
        else:
            return False
    def __ge__(self,other):
        if not isinstance(other, Fraction):
            Other = Fraction(other)
        else:
            Other = other
        x = Other.denominator * self.numerator
        y = Other.numerator * self.denominator
        if x >= y:
            return True
        else:
            return False
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            Other = Fraction(other)
        else:
            Other = other
        x = Other.denominator * self.numerator
        y = Other.numerator * self.denominator
        if x == y:
            return True
        else:
            return False
    def __ne__(self, other):
        if not isinstance(other, Fraction):
            Other = Fraction(other)
        else:
            Other = other
        x = Other.denominator * self.numerator
        y = Other.numerator * self.denominator
        if x != y:
            return True
        else:
            return False
    def decimal(self):
       return (self.numerator/self.denominator)
    def __call__(self):
        return self.decimal()

#Test:
f1=Fraction(1,3)
print(f1())

print(f1 > 1/3)
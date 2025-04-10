class Fraction:
    def __init__(self , S=0 , M=1):
        if M==0: raise ValueError('makhraj 0 taarif nashode ast!')
        self.S = S ; self.M = M

    def set_value(self , value):
        if isinstance(value,int):
            self.S = value ; self.M = 1
        elif isinstance(value , float):
            self.S = int(value * (10 **(str(value)[::-1].find('.'))))
            self.M = 10 **(str(value)[::-1].find('.'))
    
    def idk(self , value):
        if isinstance(value , int):
            return Fraction(value)
        elif isinstance(value , float):
            fr = Fraction() ; fr.set_value(value)
            return fr
        elif isinstance(value , Fraction):
            return value
    
    def __add__ (self , second):
        second = self.idk(second)
        a2 = self.M * self.M
        a1 = (self.S* second.M) + (second.S * self.M)
        return Fraction(a1,a2)
    
    def __sub__(self , second):
        second = self.idk(second)
        a1 = (self.S * second.M) - second.S * self.M
        a2 = self.M * second.M
        return Fraction(a1, a2)
    
    def __mul__(self , second):
        second = self.idk(second)
        a1 = self.S * second.S
        a2 = self.M * second.M
        return Fraction(a1, a2)

    def __truediv__(self , second):
        second = self.idk(second)
        if second.S ==0: raise ZeroDivisionError('!')

        a1 = self.S * second.M
        a2 = self.M * second.S
        return Fraction(a1, a2)



    def __eq__(self, second):
        second = self.idk(second)
        return (self.S * second.M == self.M * second.S)
    
    def __lt__(self , second):
        second = self.idk(second)
        return (self.S * second.M < self.M * second.S)
    def __le__(self , second):
        
        return (self <= second)
    
    def __gt__(self, other):
        return (self > other)

    def __ge__(self, other):
        return self >= other

    def __ne__(self, other):
        return self != other
     
    def __str__ (self):
        return f"{self.S}/{self.M}"
    
f1 = Fraction()
f2 = Fraction(12)
f3 = Fraction(12 , 9)
print(f1 , f2 , f3)
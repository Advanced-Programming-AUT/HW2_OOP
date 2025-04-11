
class Fraction:
    def __init__(self,sorat = 0,makhraj = 1)->None:
        self.sorat = sorat
        self.makhraj = makhraj
    def __str__(self):
        if int(self.sorat)>int(self.makhraj) :

            bmm = int(self.makhraj)
            if bmm == 0 :
                pass
            else :
                while bmm >0 :
                    if int(self.sorat)%bmm == 0 and int(self.makhraj)%bmm == 0 :
                        break
                    else :
                        bmm -= 1
                self.sorat =int( int(self.sorat)/bmm)
                self.makhraj = int(int(self.makhraj)/bmm)
        else :
            bmm = int(self.sorat)
            if bmm == 0 :
                pass
            else :
                while bmm >0 :
                    if int(self.sorat)%bmm == 0 and int(self.makhraj)%bmm == 0 :
                        break
                    else :
                        bmm -= 1
                self.sorat =int( int(self.sorat)/bmm)
                self.makhraj =int( int(self.makhraj)/bmm)
        return f"{self.sorat}/{self.makhraj}"




    def set_value(self,a):
        b = float(a)
        i= 1
        if int(a) == float(a) :
            self.sorat = a
            self.makhraj = 1
            return f"{int(a)}/{1}"
        else :
            while float(b) != int (b) :
                b = float(a)*i
                i += 1
                self.sorat = int(b)
                if i == 1 :
                    self.makhraj = 1
                else :
                    self.makhraj = int(i-1)

            return f"{int(b)}/{int(i-1)}"


    def __add__(self, other):
        if type(other) != Fraction :
            other = Fraction(other)
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        kmm = 0
        i= 1
        if m1 >m2 :
            kmm = m1
        else :
            kmm = m2
        while kmm <= (m1*m2) :
            if kmm % m1 == 0 and kmm %m2 == 0 :
                break
            kmm = kmm*i
            i += 1
        s3 =  (s1*int(kmm/m1)) + (s2*int(kmm/m2))
        m3 = int(kmm)
        another = Fraction(int(s3),int(m3))
        return another
    def __sub__(self, other):
        if type(other) != Fraction :
            other = Fraction(other)
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        kmm = 0
        i= 1
        if m1 >m2 :
            kmm = m1
        else :
            kmm = m2
        while kmm <= (m1*m2) :
            if kmm % m1 == 0 and kmm %m2 == 0 :
                break
            kmm = kmm*i
            i += 1
        s3 =  (s1*int(kmm/m1)) - (s2*int(kmm/m2))
        m3 = int(kmm)
        another = Fraction(int(s3),int(m3))
        return another

    def __mul__(self, other):
        if type(other) != Fraction :
            other = Fraction(other)
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        s3 = s1*s2
        m3 = m1*m2

        another = Fraction(int(s3),int(m3))
        return another

    def __truediv__(self, other):
        if type(other) != Fraction :
            other = Fraction(other)

        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        s3 = s1*m2
        m3 = m1*s2

        another = Fraction(int(s3),int(m3))
        return another
    def __gt__(self, other):
        if type(other) != Fraction :
            other = float(other)
            if self() > other:
                return f"True"
            else:
                return f"False"
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        kmm = 0
        i= 1
        if m1 >m2 :
            kmm = m1
        else :
            kmm = m2
        while kmm <= (m1*m2) :
            if kmm % m1 == 0 and kmm %m2 == 0 :
                break
            kmm = kmm*i
            i += 1

        s3 = int(s1*int(kmm/m1))
        s4 = int(s2*int(kmm/m2))
        if s3 > s4 :
            return f"True"
        else :
            return f"False"

    def __ge__(self, other):
        if type(other) != Fraction :
            other = float(other)
            if self() >= other:
                return f"True"
            else:
                return f"False"
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        kmm = 0
        i = 1
        if m1 > m2:
            kmm = m1
        else:
            kmm = m2
        while kmm <= (m1 * m2):
            if kmm % m1 == 0 and kmm % m2 == 0:
                break
            kmm = kmm * i
            i += 1

        s3 = int(s1 * int(kmm / m1))
        s4 = int(s2 * int(kmm / m2))
        if s3 >= s4:
            return f"True"
        else:
            return f"False"

    def __lt__(self, other):
        if type(other) != Fraction :
            other = float(other)
            if self() < other:
                return f"True"
            else:
                return f"False"
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        kmm = 0
        i = 1
        if m1 > m2:
            kmm = m1
        else:
            kmm = m2
        while kmm <= (m1 * m2):
            if kmm % m1 == 0 and kmm % m2 == 0:
                break
            kmm = kmm * i
            i += 1

        s3 = int(s1 * int(kmm / m1))
        s4 = int(s2 * int(kmm / m2))
        if s4 > s3:
            return f"True"
        else:
            return f"False"

    def __le__(self, other):
        if type(other) != Fraction :
            other = float(other)
            if self() <= other:
                return f"True"
            else:
                return f"False"
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        kmm = 0
        i = 1
        if m1 > m2:
            kmm = m1
        else:
            kmm = m2
        while kmm <= (m1 * m2):
            if kmm % m1 == 0 and kmm % m2 == 0:
                break
            kmm = kmm * i
            i += 1

        s3 = int(s1 * int(kmm / m1))
        s4 = int(s2 * int(kmm / m2))
        if s4 >= s3:
            return f"True"
        else:
            return f"False"

    def __eq__(self, other):
        if type(other) != Fraction :
            other = float(other)
            if self() == other:
                return f"True"
            else:
                return f"False"
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        kmm = 0
        i = 1
        if m1 > m2:
            kmm = m1
        else:
            kmm = m2
        while kmm <= (m1 * m2):
            if kmm % m1 == 0 and kmm % m2 == 0:
                break
            kmm = kmm * i
            i += 1

        s3 = int(s1 * int(kmm / m1))
        s4 = int(s2 * int(kmm / m2))
        if s3 == s4:
            return f"True"
        else:
            return f"False"

    def __ne__(self, other):
        if type(other) != Fraction :
            other = float(other)
            if self() != other:
                return f"True"
            else:
                return f"False"
        m1 = int(self.makhraj)
        m2 = int(other.makhraj)
        s1 = int(self.sorat)
        s2 = int(other.sorat)
        kmm = 0
        i = 1
        if m1 > m2:
            kmm = m1
        else:
            kmm = m2
        while kmm <= (m1 * m2):
            if kmm % m1 == 0 and kmm % m2 == 0:
                break
            kmm = kmm * i
            i += 1

        s3 = int(s1 * int(kmm / m1))
        s4 = int(s2 * int(kmm / m2))
        if s3 != s4:
            return f"True"
        else:
            return f"False"

    def __call__(self):
        return float(self.sorat/self.makhraj)



f1 = Fraction()
f2 = Fraction(12,)
f3 = Fraction(12,9)

print(f1)
print(f2)
print(f3)
f2.set_value(9)
f1.set_value(2.34)
print(f2)
print(f1)
print(f1 + f3)
print(f1 - f3)
print(f1 *f3)
print(f1/f3)
print(f1>f3,f1 == f3 , f1<f3 ,f1 >= f3 , f1 <= f3, f1 != f3)
print(f1())
print(f3+3)
print(f3*3)
print(f3/3)
print(f1())
print(f1>2.34,f1==2.34,f1<2.34,f1>=2.34,f1<=2.34)
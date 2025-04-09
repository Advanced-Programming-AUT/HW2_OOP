class Fraction:
    def __init__(self, up = 0, down = 1):
        self.up = up
        self.down = down
        self.simplify()

    def simplify(self):
        new_up = self.up
        for i in range(2, int(self.up**0.5)+2):
            if new_up%i == 0 and self.down%i == 0:
                new_up //= i
                self.down //= i
        self.up = new_up

    def __str__(self):
        return f"{self.up} / {self.down}"

    def __call__(self):
        return self.up/self.down

    def set_value(self, value):
        while int(value) != value:
            value *= 10
            self.down *= 10
        self.up = int(value)
        self.simplify()

    def __add__(self, other):
        if type(other) == type(0):
            return Fraction(self.up+self.down*other, self.down)
        else:
            return Fraction(other.down*self.up+self.down*other.up, self.down*other.down)

    def __sub__(self, other):
        if type(other) == type(0):
            return Fraction(self.up-self.down*other, self.down)
        else:
            return Fraction(other.down*self.up-self.down*other.up, self.down*other.down)

    def __mul__(self, other):
        if type(other) == type(0):
            return Fraction(self.up*other, self.down)
        else:
            return Fraction(self.up*other.up, self.down*other.down)

    def __truediv__(self, other):
        if type(other) == type(0):
            return Fraction(self.up, self.down*other)
        else:
            return Fraction(self.up*other.down, self.down*other.up)

    def __eq__(self, other):
        return self() == other()

    def __ne__(self, other):
        return self() != other()

    def __lt__(self, other):
        return self() < other()

    def __le__(self, other):
        return self() <= other()

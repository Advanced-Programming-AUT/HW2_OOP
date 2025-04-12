
import math

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def set_value(self, value):
        if isinstance(value, int):
            self.numerator = value
            self.denominator = 1
        elif isinstance(value, float):
            fractional = Fraction.from_float(value)
            self.numerator = fractional.numerator
            self.denominator = fractional.denominator
        else:
            raise TypeError("Value must be an integer or float.")

    @staticmethod
    def from_float(value):
        str_value = str(value)
        decimal_places = len(str_value.split(".")[1])
        numerator = int(value * (10 ** decimal_places))
        denominator = 10 ** decimal_places
        return Fraction(numerator, denominator)

    def __call__(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        elif isinstance(other, (int, float)):
            return self + Fraction.from_float(float(other))
        else:
            raise TypeError("Can only add a Fraction, int, or float.")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        elif isinstance(other, (int, float)):
            return self - Fraction.from_float(float(other))
        else:
            raise TypeError("Can only subtract a Fraction, int, or float.")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        elif isinstance(other, (int, float)):
            return self * Fraction.from_float(float(other))
        else:
            raise TypeError("Can only multiply by a Fraction, int, or float.")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)
        elif isinstance(other, (int, float)):
            return self / Fraction.from_float(float(other))
        else:
            raise TypeError("Can only divide by a Fraction, int, or float.")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        elif isinstance(other, (int, float)):
            return self.__call__() == float(other)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < self.denominator * other.numerator
        elif isinstance(other, (int, float)):
            return self.__call__() < float(other)
        else:
            return False

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other


def main_menu():
    print("Welcome to Fraction System!")

    while True:
        print("\n--- Fraction Management Menu ---")
        print("1. Create a new Fraction")
        print("2. Set value for Fraction")
        print("3. Perform mathematical operations")
        print("4. Compare Fractions")
        print("5. Display Fraction details")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            numerator = int(input("Enter numerator: "))
            denominator = int(input("Enter denominator (cannot be 0): "))
            try:
                fraction = Fraction(numerator, denominator)
                print(f"Fraction created: {fraction}")
            except ValueError as e:
                print(e)

        elif choice == "2":
            value = input("Enter an integer or float to set the Fraction value: ")
            try:
                if "." in value:
                    fraction.set_value(float(value))
                else:
                    fraction.set_value(int(value))
                print(f"Fraction updated: {fraction}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            operation = input("Enter operation (+, -, *, /): ")
            numerator = int(input("Enter numerator for the second Fraction: "))
            denominator = int(input("Enter denominator for the second Fraction (cannot be 0): "))
            try:
                second_fraction = Fraction(numerator, denominator)
                if operation == "+":
                    result = fraction + second_fraction
                elif operation == "-":
                    result = fraction - second_fraction
                elif operation == "*":
                    result = fraction * second_fraction
                elif operation == "/":
                    result = fraction / second_fraction
                else:
                    print("Invalid operation.")
                    continue
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            numerator = int(input("Enter numerator for the second Fraction: "))
            denominator = int(input("Enter denominator for the second Fraction (cannot be 0): "))
            try:
                second_fraction = Fraction(numerator, denominator)
                print(f"Comparisons:")
                print(f"{fraction} > {second_fraction}: {fraction > second_fraction}")
                print(f"{fraction} == {second_fraction}: {fraction == second_fraction}")
                print(f"{fraction} < {second_fraction}: {fraction < second_fraction}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            print(f"Fraction details: {fraction}")
            print(f"Decimal value: {fraction()}")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")





if __name__ == '__main__':
    main_menu()



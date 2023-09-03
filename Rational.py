class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def display(self):
        print(f"{self.numerator} / {self.denominator}")


# Sample usage
numerator1 = int(input("Enter numerator for the first rational number: "))
denominator1 = int(input("Enter denominator for the first rational number: "))
numerator2 = int(input("Enter numerator for the second rational number: "))
denominator2 = int(input("Enter denominator for the second rational number: "))

r1 = Rational(numerator1, denominator1)
r2 = Rational(numerator2, denominator2)

# Addition
result = r1 + r2
result.display()

# Subtraction
result = r1 - r2
result.display()

# Multiplication
result = r1 * r2
result.display()

# Division
result = r1 / r2
result.display()

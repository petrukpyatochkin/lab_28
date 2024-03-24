class Fraction:
    _instances = 0

    def __init__(self, numerator, denominator):
        from math import gcd
        if denominator == 0:
            raise ValueError("Знаменник не може бути 0.")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common
        Fraction._instances += 1

    @staticmethod
    def get_instance_count():
        return Fraction._instances

    def display(self):
        print(f"{self.numerator}/{self.denominator}")

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
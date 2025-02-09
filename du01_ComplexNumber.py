import math

class ComplexNumber:
    def __init__(self, real, imag):
        if not isinstance(real, (int, float)) or not isinstance(imag, (int, float)):
            raise TypeError("Real and imaginary parts must be numbers!")
        self._real = real
        self._imag = imag

    def __eq__(self, other):
        return (isinstance(other, ComplexNumber) and self.real == other.real
                and self.imag == other.imag)

    def __lt__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return self.absolute_value() < other.absolute_value()

    def __gt__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return self.absolute_value() > other.absolute_value()

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

    def __str__(self):
        return f"{self.real} {'+' if self.imag >= 0 else '-'} {abs(self.imag)}i"

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Real part must be a number!")
        self._real = value

    @property
    def imag(self):
        return self._imag

    @imag.setter
    def imag(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Imaginary part must be a number!")
        self._imag = value

    def add(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Operand must be a ComplexNumber!")
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Operand must be a ComplexNumber!")
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Operand must be a ComplexNumber")
        return ComplexNumber(self.real*other.real, self.imag *other.imag)

    def divide(self,other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Operand must be a ComplexNumber")
        denominator = other.real ** 2 + other.imag ** 2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real, imag)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def absolute_value(self):
        return math.sqrt(self.real **2 + self.imag**2)

if __name__ == "__main__":
    try:
        real1 = float(input("Enter the real part of the first complex number: "))
        imag1 = float(input("Enter the imaginary part of the first complex number: "))

        real2 = float(input("Enter the real part of the second complex number: "))
        imag2 = float(input("Enter the imaginary part of the second complex number: "))

        c1 = ComplexNumber(real1, imag1)
        c2 = ComplexNumber(real2, imag2)

        print(f"\nFirst complex number: {c1}")
        print(f"Second complex number: {c2}\n")

        print(f"Sum: {c1.add(c2)}")
        print(f"Diff: {c1.subtract(c2)}")
        print(f"Product: {c1.multiply(c2)}")

        try:
            print(f"Quotient: {c1.divide(c2)}")
        except ZeroDivisionError as e:
            print(f"Cannot divide by zero")

        print(f"Conjugate of the first complex number: {c1.conjugate()}")
        print(f"Absolute value of the first complex number: {c1.absolute_value()}")

    except ValueError:
        print("Invalid input! Please enter numerical values for real and imaginary parts.")








import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        return (isinstance(other, ComplexNumber) and self.real == other.real
                and self.imag == self.imag)

    def __lt__(self, other):
        return self.absolute_value() < other.absolute_value()

    def __gt__(self, other):
        return self.absolute_value() > other.absolute_value()

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = value

    @property
    def imag(self):
        return self._imag

    @imag.setter
    def imag(self, value):
        self._imag = value

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        return ComplexNumber(self.real * other.real, self.imag * other.imag)

    def divide(self,other):
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag)  / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real, imag)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def absolute_value(self):
        return math.sqrt(self.real **2 + self.imag**2)

if __name__ == "__main__":
    real1 = float(input("Enter the real part of the first complex number: "))
    imag1 = float(input("Enter the imaginary part of the first complex number: "))

    real2 = float(input("Enter the real part of the second complex number: "))
    imag2 = float(input("Enter the imaginary part of the second complex number: "))

    c1 = ComplexNumber(real1, imag1)
    c2 = ComplexNumber(real2, imag2)

    print(f"First complex number: {c1}")
    print(f"Second complex number: {c2}")

    print(f"The sum of the complex numbers is: {c1.add(c2)}")
    print(f"The difference of the complex numbers is: {c1.subtract(c2)}")
    print(f"The product of the complex numbers is: {c1.multiply(c2)}")

    try:
        print(f"The division of the complex numbers is: {c1.divide(c2)}")
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero")

    print(f"The conjugate of the first complex number is: {c1.conjugate()}")
    print(f"The absolute value of the first complex number is: {c1.absolute_value()}")








import pytest
from du01_ComplexNumber import ComplexNumber

def test_add():
    c1 = ComplexNumber(1,2)
    c2 = ComplexNumber(3,4)
    assert c1.add(c2) == ComplexNumber(4,6)

def test_subtract():
    c1 = ComplexNumber(5,6)
    c2 = ComplexNumber(2,3)
    assert c1.subtract(c2) == ComplexNumber(3,3)

def test_multiply():
    c1 = ComplexNumber(5, 6)
    c2 = ComplexNumber(2, 3)
    assert c1.multiply(c2) == ComplexNumber(10, 18)

def test_divide():
    c1 = ComplexNumber(4, 2)
    c2 = ComplexNumber(2, -2)
    assert c1.divide(c2) == ComplexNumber(0.5, 1.5)

def test_divide_by_zero():
    c1 = ComplexNumber(1, 1)
    c2 = ComplexNumber(0, 0)
    with pytest.raises(ZeroDivisionError):
        c1.divide(c2)

def test_conjugate():
    c = ComplexNumber(3,4)
    assert c.conjugate() == ComplexNumber(3, -4)

def test_absolute_value():
    c = ComplexNumber(3,4)
    assert c.absolute_value() == 5

def test_comparisons():
    c1 = ComplexNumber(3,4)
    c2 = ComplexNumber(1,1)
    assert c1 > c2
    assert c2 < c1

def test_repr_str():
    c = ComplexNumber(3,-4)
    assert repr(c) == "ComplexNumber(3, -4)"
    assert str(c) == "3 - 4i"
import pytest
from p01_BasicCalc import BasicCalc

def test_add():
    basic_calc = BasicCalc()
    result = basic_calc.add(3, 5)
    assert result == 8
    assert basic_calc.add(-6, -4) == -10
    assert basic_calc.add(-3, 4) == 1
    assert basic_calc.add(5, -6) == -1
    assert basic_calc.add(5, 0) == 5
    assert round(basic_calc.add(2.1, 3.2), 5) == 5.3
    assert round(basic_calc.add(10, 5.3), 5) == 15.3
    assert basic_calc.add("3", "5") is None
    assert basic_calc.add("Hello", "World") is None
    assert basic_calc.add(3, "5") is None
    assert basic_calc.add([3], 5) is None


def test_subtraction():
    basic_calc = BasicCalc()
    result = basic_calc.subtract(3, 5)
    assert result == -2
    assert basic_calc.subtract(-6, -4) == -2
    assert basic_calc.subtract(-3, 4) == -7
    assert basic_calc.subtract(5, -6) == 11
    assert basic_calc.subtract(5, 0) == 5
    assert round(basic_calc.subtract(2.1, 3.2), 5) == -1.1
    assert round(basic_calc.subtract(10, 5.3), 5) == 4.7
    assert basic_calc.subtract("3", "5") is None
    assert basic_calc.subtract("Hello", "World") is None
    assert basic_calc.subtract(3, "5") is None
    assert basic_calc.subtract([3], 5) is None


def test_multiply():
    basic_calc = BasicCalc()
    result = basic_calc.multiply(6, 3)
    assert result == 18
    assert basic_calc.multiply(-6, -2) == 12
    assert basic_calc.multiply(-3, 3) == -9
    assert basic_calc.multiply(6, -6) == -36
    assert basic_calc.multiply(5, 0) == 0
    assert round(basic_calc.multiply(2.1, 3.2), 5) == 6.72
    assert round(basic_calc.multiply(11.25, 2.25), 5) == 25.3125
    assert basic_calc.multiply("3", "5") is None
    assert basic_calc.multiply("Hello", "World") is None
    assert basic_calc.multiply(3, "5") is None
    assert basic_calc.multiply([3], 5) is None


def test_divide():
    basic_calc = BasicCalc()
    result = basic_calc.divide(6, 3)
    assert result == 2
    assert basic_calc.divide(-6, -2) == 3
    assert basic_calc.divide(-3, 3) == -1
    assert basic_calc.divide(6, -6) == -1
    assert round(basic_calc.divide(2.1, 3.2), 5) == 0.65625
    assert round(basic_calc.divide(11.25, 2.25), 5) == 5
    assert basic_calc.divide("3", "5") is None
    assert basic_calc.divide("Hello", "World") is None
    assert basic_calc.divide(3, "5") is None
    assert basic_calc.divide([3], 5) is None

    with pytest.raises(ZeroDivisionError):
        assert basic_calc.divide(5, 0)
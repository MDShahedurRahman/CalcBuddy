import math
from calculator import Calculator


def test_add():
    c = Calculator()
    assert c.add(2, 3).value == 5


def test_subtract():
    c = Calculator()
    assert c.subtract(10, 4).value == 6


def test_multiply():
    c = Calculator()
    assert c.multiply(3, 5).value == 15


def test_divide_ok():
    c = Calculator()
    assert c.divide(10, 2).value == 5


def test_divide_by_zero():
    c = Calculator()
    r = c.divide(10, 0)
    assert math.isnan(r.value)
    assert "Division by zero" in r.message


def test_power():
    c = Calculator()
    assert c.power(2, 3).value == 8


def test_modulo_ok():
    c = Calculator()
    assert c.modulo(10, 3).value == 1

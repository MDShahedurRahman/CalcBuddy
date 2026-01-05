import math
from calculator import Calculator


def test_add():
    c = Calculator()
    assert c.add(2, 3).value == 5


def test_subtract():
    c = Calculator()
    assert c.subtract(10, 4).value == 6

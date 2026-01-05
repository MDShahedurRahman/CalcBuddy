import math
from calculator import Calculator


def test_add():
    c = Calculator()
    assert c.add(2, 3).value == 5

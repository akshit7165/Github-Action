import pytest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

class CalculatorTest:

    def test_add(self):
        assert add(1, 2) == 3
        assert add(-3, 5) == 2
        assert add(0, 0) == 0

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(-2, 1) == -3
        assert subtract(0, 0) == 0

    def test_multiply(self):
        assert multiply(2, 3) == 6
        assert multiply(-4, -2) == 8
        assert multiply(1, 0) == 0

    def test_divide(self):
        assert divide(6, 2) == 3
        assert divide(-10, 5) == -2
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)

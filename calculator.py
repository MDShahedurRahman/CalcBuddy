from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CalcResult:
    value: float
    message: str = ""


class Calculator:
    def add(self, a: float, b: float) -> CalcResult:
        return CalcResult(a + b)

    def subtract(self, a: float, b: float) -> CalcResult:
        return CalcResult(a - b)

    def multiply(self, a: float, b: float) -> CalcResult:
        return CalcResult(a * b)

    def divide(self, a: float, b: float) -> CalcResult:
        if b == 0:
            return CalcResult(float("nan"), "Error: Division by zero")
        return CalcResult(a / b)

    def power(self, a: float, b: float) -> CalcResult:
        return CalcResult(a ** b)

    def modulo(self, a: float, b: float) -> CalcResult:
        if b == 0:
            return CalcResult(float("nan"), "Error: Modulo by zero")
        return CalcResult(a % b)


def parse_number(text: str) -> float:
    """
    Converts input string to float safely.
    Raises ValueError if invalid.
    """
    text = text.strip()
    # Allow comma-separated numbers like "1,000"
    text = text.replace(",", "")
    return float(text)

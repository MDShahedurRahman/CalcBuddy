from calculator import Calculator, parse_number


MENU = """
CalcBuddy - Simple Calculator
----------------------------
1) Add (+)
2) Subtract (-)
3) Multiply (*)
4) Divide (/)
5) Power (**)
6) Modulo (%)
7) Quit
"""


def get_choice() -> str:
    return input("Choose an option (1-7): ").strip()


def get_two_numbers():
    a = parse_number(input("Enter first number: "))
    b = parse_number(input("Enter second number: "))
    return a, b

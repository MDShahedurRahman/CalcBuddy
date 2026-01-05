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


def run():
    calc = Calculator()

    while True:
        print(MENU)
        choice = get_choice()

        if choice == "7":
            print("Bye!")
            break

        try:
            a, b = get_two_numbers()
        except ValueError:
            print("Invalid number. Try again.\n")
            continue

        if choice == "1":
            r = calc.add(a, b)
            print(f"Result: {r.value}\n")
        elif choice == "2":
            r = calc.subtract(a, b)
            print(f"Result: {r.value}\n")
        elif choice == "3":
            r = calc.multiply(a, b)
            print(f"Result: {r.value}\n")
        elif choice == "4":
            r = calc.divide(a, b)
            if r.message:
                print(f"{r.message}\n")
            else:
                print(f"Result: {r.value}\n")
        elif choice == "5":
            r = calc.power(a, b)
            print(f"Result: {r.value}\n")
        elif choice == "6":
            r = calc.modulo(a, b)
            if r.message:
                print(f"{r.message}\n")
            else:
                print(f"Result: {r.value}\n")
        else:
            print("Invalid option. Choose 1-7.\n")


if __name__ == "__main__":
    run()

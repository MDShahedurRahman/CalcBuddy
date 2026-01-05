# CalcBuddy

CalcBuddy is a simple command-line calculator built with Python.\
It demonstrates Python fundamentals, basic CLI interaction, and unit
testing with `pytest`.

This project is intentionally small and clean, suitable for beginners
and for showcasing proper GitHub workflow and testing practices.

------------------------------------------------------------------------

## Features

-   Add, subtract, multiply, divide
-   Power (`**`) and modulo (`%`)
-   Safe handling of division and modulo by zero
-   Interactive command-line menu
-   Unit tests using `pytest`

------------------------------------------------------------------------

## Requirements

-   Python 3.9 or higher

------------------------------------------------------------------------

## Setup

Clone the repository and move into the project directory:

``` bash
git clone https://github.com/MDShahedurRahman/CalcBuddy.git
cd CalcBuddy
```

Create and activate a virtual environment:

### macOS / Linux

``` bash
python -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

``` powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Upgrade pip and install dependencies:

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Run the Calculator

``` bash
python main.py
```

Follow the on-screen menu to perform calculations.

------------------------------------------------------------------------

## Run Tests

Always run tests using the active Python interpreter:

``` bash
python -m pytest -q
```

This ensures tests run inside the virtual environment.

------------------------------------------------------------------------

## Project Structure

    CalcBuddy/
    ├── calculator.py
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── tests/
    │   ├── conftest.py
    │   └── test_calculator.py

------------------------------------------------------------------------

## Notes

-   The project uses only Python standard library at runtime.
-   `requirements.txt` contains testing dependencies only.
-   Virtual environments (`.venv`) are not committed to the repository.

------------------------------------------------------------------------

## License

This project is open source and available under the MIT License.

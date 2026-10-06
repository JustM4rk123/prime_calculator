# Prime Number Calculator

Small Python project that uses the Sieve of Eratosthenes to calculate the percentage of prime numbers up to a user-provided maximum value.

## Requirements

- Python 3.10 or later
- `pip`

## Installation

From the project root, install the dependencies and the package in editable mode:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

The `requirements.txt` file contains:

- [`bitarray`](https://pypi.org/project/bitarray/), used to efficiently represent prime and non-prime values.
- `pytest`, used to run the automated tests.

## Usage

The program can be run either interactively or by passing the number directly as a CLI argument.

### Interactive mode

```bash
python -m prime_calculator
```

Example:

```text
Up to which number should prime numbers be calculated? 100
25.0% of the numbers are prime
```

### CLI argument mode

```bash
python -m prime_calculator -n 100
```

or:

```bash
python -m prime_calculator --number 100
```

Example output:

```text
25.0% of the numbers are prime
```

The provided value must be a non-negative integer. Passing a negative number raises a `ValueError`.

### Speed test

You can run the included benchmark script:

```bash
python -m prime_calculator.speedtest
```

This script runs multiple benchmarks from small values (for example `10`) up to very large ones (for example `10_000_000_000`), printing the prime percentage and the elapsed time for each run.

## Use as a library

The `sieve` function is available directly from the package:

```python
from prime_calculator import sieve

percentage = sieve(100)
print(percentage)  # 25.0
```

The function returns the percentage of prime numbers from `0` to `n`, inclusive. It returns `0` for values below `2`.

## Tests

Run the test suite with:

```bash
python -m pytest
```

The tests cover the main sieve calculations and edge cases.

## Project structure

```text
prime_calculator/
├── pyproject.toml
├── requirements.txt
├── README.md
├── src/
│   └── prime_calculator/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core.py
│       ├── speedtest.py
│       └── validation.py
└── tests/
    ├── test_cli.py
    ├── test_prime_calculator.py
    └── test_validation.py
```

- `core.py`: implements the Sieve of Eratosthenes logic.
- `validation.py`: validates the user-provided number.
- `__main__.py`: handles command-line execution.
- `speedtest.py`: runs performance benchmarks.
- `tests/`: contains the automated tests.

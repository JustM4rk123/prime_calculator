# Prime Number Calculator


Small Python project that uses the **Sieve of Eratosthenes** to calculate the percentage of prime numbers between `0` and a maximum value provided by the user.

## Requirements

- Python 3.10 or later
- `pip`

## Installation

From the project root, install the dependencies listed in `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
python -m pip install -e .
```

The `requirements.txt` file contains:

- [`bitarray`](https://pypi.org/project/bitarray/), used to efficiently represent prime and non-prime values.
- `pytest`, used to run the automated tests.

## Usage

The program can be run with or without a flag:

Senza flag:

```powershell
python -m prime_calculator
```

Enter the maximum number when prompted. For example:

```text
Up to which number should prime numbers be calculated? 100
25.0% of the numbers are prime
```

With flag:

```powershell
python -m prime_calculator -n [number]
```

Or:

```powershell
python -m prime_calculator --number [number]
```

Example:

```powershell
python -m prime_calculator -n 100
25.0% of the numbers are primes
```

The provided value must be a non-negative integer. A negative value raises a `ValueError`.

Also, you can run a speedtest script by executing this command in the terminal:
```poweshell
python -m primecalculator.speedtest
``` 

This script runs several benchmarks from low numbers (such as 50) all the way up to high ones (such as 10 bilions),
printing the percentage output and the elapsed time for each execution

## Use as a library

The `sieve` function is available directly from the package:

```python
from prime_calculator import sieve

percentage = sieve(100)
print(percentage)  # 25.0
```

The function returns the percentage of prime numbers between `0` and `n`, inclusive. It returns `0` for values below `2`.

## Tests

Run the test suite with:

```powershell
python -m pytest
```

The tests verify sieve results for different values and edge cases.

## Struttura del progetto

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
│       ├── validation.py
│	└── speedtest.py
└── tests/
	├── test_prime_calculator.py
	├── test_cli.py
	└── test_validation.py
```

- `core.py`: implements the Sieve of Eratosthenes.
- `validation.py`: validates the provided number.
- `__main__.py`: handles command-line execution.
- `tests/`: contains the automated tests.

import time

from prime_calculator.core import sieve

BENCHMARKS = [
    10,
    100,
    1_000,
    10_000,
    100_000,
    1_000_000,
    10_000_000,
    100_000_000,
    1_000_000_000,
    10_000_000_000,
]


def speedtest():
    for n in BENCHMARKS:
        start = time.perf_counter()
        result = sieve(n)
        elapsed = time.perf_counter() - start

        print(f"{n:>14,} -> {result:>9.6f} %, elapsed time: {elapsed:>11.6f} seconds")


if __name__ == "__main__":
    speedtest()

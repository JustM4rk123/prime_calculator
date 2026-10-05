from math import isqrt

from bitarray import bitarray


def sieve(n: int) -> float:
    if n < 2:
        return 0

    primes_until_sqrt_of_n = small_sieve(isqrt(n) + 1)

    CHUNK_SIZE = 10_000_000
    current_chunk = 3  # starts at 3 since 2 is already handled separately
    prime_sum = 1  # 2 is prime

    while current_chunk <= n:
        chunk_end = min(current_chunk + 2 * CHUNK_SIZE, n + 1)

        prime_flags = bitarray((chunk_end - current_chunk) // 2)
        prime_flags.setall(1)

        for prime in primes_until_sqrt_of_n:
            if prime == 2:
                continue

            if prime * prime >= chunk_end:
                break

            first_multiple = max(
                prime * prime,
                ((current_chunk + prime - 1) // prime) * prime,
            )

            if first_multiple % 2 == 0:
                first_multiple += prime

            if first_multiple < chunk_end:
                start = (first_multiple - current_chunk) // 2
                prime_flags[start::prime] = 0

        prime_sum += prime_flags.count(1)
        current_chunk = chunk_end

    return (prime_sum / n) * 100


def small_sieve(n: int) -> list[int]:
    if n < 2:
        return []

    prime_flags = bitarray((n - 1) // 2)
    prime_flags.setall(1)

    for i in range(isqrt(n) + 1):
        prime = 2 * i + 3  # aligns index with odd numbers starting from 3

        if prime * prime > n:
            break

        if prime_flags[i]:
            prime_flags[(prime * prime - 3) // 2 :: prime] = 0

    return [2] + [2 * i + 3 for i, is_prime in enumerate(prime_flags) if is_prime]

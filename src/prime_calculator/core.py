from math import isqrt

from bitarray import bitarray


def sieve(n: int) -> float:
    if n < 2:
        return 0

    # Only primes up to sqrt(n) are needed to mark composite values.
    primes_until_sqrt_of_n = small_sieve(isqrt(n) + 1)

    CHUNK_SIZE = 10_000_000
    odd_count = (n - 1) // 2
    current_chunk = 0
    prime_sum = 1  # The only even prime is 2.

    while current_chunk < odd_count:
        chunk_size = min(CHUNK_SIZE, odd_count - current_chunk)
        chunk_start = 3 + 2 * current_chunk
        chunk_end = chunk_start + 2 * chunk_size
        prime_flags = bitarray(chunk_size)
        prime_flags.setall(1)

        for prime in primes_until_sqrt_of_n:
            if prime == 2:
                continue
            # Larger primes cannot introduce a new composite in this chunk.
            if prime * prime >= chunk_end:
                break

            # Start at the first multiple inside the current chunk, but never
            # before p^2 so that the prime p itself remains marked as prime.
            first_multiple = max(
                prime * prime,
                ((chunk_start + prime - 1) // prime) * prime,
            )
            if first_multiple % 2 == 0:
                first_multiple += prime
            if first_multiple < chunk_end:
                first_index = (first_multiple - chunk_start) // 2
                prime_flags[first_index::prime] = 0

        prime_sum += prime_flags.count(1)
        current_chunk += chunk_size

    return (prime_sum / n) * 100


def small_sieve(n: int) -> list[int]:
    if n < 2:
        return []

    # Each bit represents an odd number starting at 3.
    prime_flags = bitarray((n - 1) // 2)
    prime_flags.setall(1)

    for i in range(isqrt(n) + 1):
        prime = 2 * i + 3
        if prime * prime > n:
            break
        if prime_flags[i]:
            prime_flags[(prime * prime - 3) // 2 :: prime] = 0

    return [2] + [2 * i + 3 for i, is_prime in enumerate(prime_flags) if is_prime]

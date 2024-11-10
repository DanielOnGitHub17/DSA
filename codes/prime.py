"""Module about prime number algorithms"""
import sys

FIRST_THREE_PRIMES = (2, 3, 5)


def n_primes(n=3):
    """Function to generate n primes efficiently 
      - my idea in spring semester 2024
    Instead of checking if each number, X, 'is_prime' by looping all numbers
     from 2 -> sqrt(X), just check it with the previously generated primes.
    """

    primes = list(FIRST_THREE_PRIMES)
    num = primes[-1]

    while len(primes) < n:
        num += 1
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)

    return primes if n > 2 else primes[:n]


if __name__ == "__main__":
    n_of_primes = int(sys.argv[1]) if len(sys.argv) == 2 else 0
    print(n_primes(n_of_primes))

"""Module about prime number algorithms"""
import sys
import time


FIRST_THREE_PRIMES = (2, 3, 5)


def n_primes_no_even(n: int) -> list:
    """Copy of 'n_primes_sqrt', will skip even numbers.
    Future: Skip even numbers, multiples of 3, 5, 7...
     - I believe that's already an algorithm :)
    What is in my mind of 'skipping' multiples is probably Erostosthenes' Sieve.
    It's not to skip, but to mark as composite.
    """

    primes = list(FIRST_THREE_PRIMES)
    num = primes[-1]

    while len(primes) < n:
        num += 2
        sqrt_num = int(num**0.5) + 1
        for _, p in enumerate(primes):
            if num % p == 0:
                break
            if p > sqrt_num:
                primes.append(num)
                break

    return primes if n > 2 else primes[:n]


def n_primes_sqrt(n: int) -> list:
    """Copy of 'n_primes_base'
     - optimized to stop at ceiling of square root
    There's no more prime factors of the number 
     after the squareoot.

    Might be more explainable if done without a for loop :)
    """

    primes = list(FIRST_THREE_PRIMES)
    num = primes[-1]

    while len(primes) < n:
        num += 1
        sqrt_num = int(num**0.5) + 1
        for _, p in enumerate(primes):
            if num % p == 0:
                break
            if p > sqrt_num:
                primes.append(num)
                break

    return primes if n > 2 else primes[:n]


def n_primes_base(n: int) -> list:
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
    n_of_primes = int(sys.argv[1]) if len(sys.argv) == 2 else int(input("Enter the number of primes: "))
    start_time = time.time()
    n_primes_base(n_of_primes)
    end_time = time.time()
    print(end_time-start_time)
    n_primes_sqrt(n_of_primes)
    print(time.time()-end_time)
    input("DONE")

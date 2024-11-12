"""Module about prime number algorithms"""
import sys
import time


FIRST_THREE_PRIMES = (2, 3, 5)


def n_primes_better(n=3):
    """
    :param n:
    :return list[int]:

    Copy of 'n_primes', will skip even numbers.
    Future: Skip even numbers, multiples of 3, 5, 7...
     - I believe that's already an algorithm :)
    """


def n_primes(n=3):
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
        prime_index = 0
        while primes[prime_index] <= sqrt_num:
            if num % primes[prime_index] == 0:
                break
            prime_index += 1
        else:
            primes.append(num)

    return primes if n > 2 else primes[:n]


def n_primes_base(n=3):
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
    n_primes(n_of_primes)
    print(time.time()-end_time)
    input("DONE")

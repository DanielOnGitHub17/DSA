"""Module on prime number algorithms
Try n=10000, and erostothenes starts doing well.
"""
import math
import sys
import time


FIRST_THREE_PRIMES = (2, 3, 5)


def n_primes_euler(n: int) -> list:
    """Optimized Erostosthenes' Sieve algorithm to generate n primes.
    - Marks a number composite only once.
    - Keeps a running product of primes and marks the multiples of that product
    - Issue: the product becomes large, fast. Adding large numbers might be time-consuming...
    """

    first_five_primes = [2, 3, 5, 7, 11]
    # Base cases. n=1, Log(log) will fail. n<6, formula fails.
    if n < 6:
        return first_five_primes[:n]

    nth_prime_approx = int(n * (math.log(n) + math.log(math.log(n))))
    numbers = [*range(2, nth_prime_approx+1)]
    n_numbers = len(numbers)
    marker = 1

    count = 0
    for maker_index in range(n_numbers):
        prime = numbers[maker_index]
        if not prime:
            continue
        marker *= prime
        print(prime)
        for composite_index in range(maker_index+marker, n_numbers, marker):
            numbers[composite_index] = 0
            count += 1
    print("euler", count)
    return [p for p in numbers if p][:n]  # offset might be much


def n_primes_erostosthenes(n: int) -> list:
    """Erostosthenes' Sieve algorithm to generate n primes.
    - Eliminate multiples of each prime number.
    I get the approximate nth prime number by using the formula: n(ln(n) + ln(ln(n)))
    Then I slice the result if it's too much
    """

    first_five_primes = [2, 3, 5, 7, 11]
    # Base cases. n=1, Log(log) will fail. n<6, formula fails.
    if n < 6:
        return first_five_primes[:n]

    nth_prime_approx = int(n * (math.log(n) + math.log(math.log(n))))
    numbers = [*range(2, nth_prime_approx+1)]
    n_numbers = len(numbers)
    count = 0
    for maker_index in range(n_numbers):
        prime = numbers[maker_index]
        if prime == 0:
            continue
        for composite_index in range(maker_index+prime, n_numbers, prime):
            numbers[composite_index] = 0
            count += 1
    print("euler", count)

    return [p for p in numbers if p][:n]  # offset might be much


def n_primes_by_six(n: int) -> list:
    """Better version of 'n_primes_no_even' by incrementing by 6.
    - 6k +/- 1 are the only numbers that are prime.
    Essentially, O(n/6) is still better than O(n/2) :)
    """

    primes = list(FIRST_THREE_PRIMES[:2])  # First two primes, 2 and 3
    counter = 6

    while len(primes) < n:
        sqrt_num = int(counter**0.5) + 1
        is_prime = True
        for num in (counter-1, counter+1):
            for _, p in enumerate(primes):
                if num % p == 0 or p > sqrt_num:
                    is_prime = p > sqrt_num  # It broke because no factors
                    break
            if is_prime:
                primes.append(num)
        counter += 6

    return primes[:n]


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


prime_functions = [
    n_primes_base,
    n_primes_sqrt,
    n_primes_no_even,
    n_primes_by_six,
    n_primes_erostosthenes,
    # n_primes_euler,
]


if __name__ == "__main__":
    n_of_primes = int(sys.argv[1]) if len(sys.argv) == 2 else\
          int(input("Enter the number of primes: "))
    for n_primes in prime_functions:
        start_time = time.time()
        primes_nos = n_primes(n_of_primes)
        end_time = time.time()
        print(f"{(n_primes.__name__+f'({n_of_primes}):').ljust(30)} {primes_nos}")
        print(f"{(n_primes.__name__+' finished in').ljust(30)} {end_time-start_time}")
    input("\nDONE")

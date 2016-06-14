# coding=utf-8
import math
from timing import timing


@timing
def get_primes_with_remember(max_number):
    primes = [2]
    for number in range(3, max_number):
        square_root = math.sqrt(number)
        for divider in primes:
            if divider > square_root:
                primes.append(number)
                break
            if number % divider == 0:
                break
    return primes


@timing
def get_primes_eratosthenes(max_number):
    primes = [False, False] + [True]*(max_number-1)
    square_root = math.sqrt(max_number)
    for number, is_prime in enumerate(primes):
        if number > square_root:
            break
        if is_prime:
            for index in range(number*number, max_number+1, number):
                primes[index] = False
    result = []
    for number, is_prime in enumerate(primes):
        if is_prime:
            result.append(number)
    return result


test_size = 1000000
print(len(get_primes_with_remember(test_size)))
print(len(get_primes_eratosthenes(test_size)))


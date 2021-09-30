#!/usr/bin/python3

"""Module containing two functions for RSA Challenge"""


def factorize(value):
    """Factorize helps to get p and q
    such that value = p * q

    Args:
    value: Number to get it factors

    """
    a = 2
    while True:
        if value % a == 0:
            value = value / a
            return (value, a)
        a += 1

def is_prime(value):
    """A function to check if a number is prime

    Args:
    value: Number to check if is prime

    """
    if value == 1 or value == 0 or (value % 2 == 0 and value > 2):
        return (False)
    else:
        for i in range(3, int(value **(1 / 2)) + 1, 2):
            if value % i == 0:
                return (False)
        return (True)
